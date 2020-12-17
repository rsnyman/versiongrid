import connexion

from versiongrid.db.base import session
from versiongrid.db.models import Dependency


def add_dependency(dependency=None):
    """Create a new dependency

    Create a new dependency

    :param dependency:
    :type dependency: dict | bytes

    :rtype: Dependency
    """
    if not connexion.request.is_json:
        return "Bad request, JSON required", 400
    dependency = Dependency(**connexion.request.get_json())
    session.add(dependency)
    return dependency.to_dict(), 201


def delete_dependency(dependency_id):
    """Delete a single dependency

    Delete a dependency

    :param dependency_id:
    :type dependency_id: str

    :rtype: None
    """
    dependency = Dependency.query.get(dependency_id)
    if dependency:
        session.delete(dependency)
        session.commit()
        return "Deleted", 200
    else:
        return "Dependency not found", 404


def get_dependency(dependency_id):
    """Get a single dependency

    Get a dependency by id

    :param dependency_id:
    :type dependency_id: str

    :rtype: Dependency
    """
    dependency = Dependency.query.get(dependency_id)
    if dependency:
        return dependency.to_dict()
    else:
        return "Dependency not found", 404


def get_dependency_list(component=None, page=1, page_size=25):
    """Get a list of dependencies

    A list of dependencies

    :param :
    :type version: str

    :rtype: DependencyList
    """
    offset = (page * page_size) - page_size
    query = Dependency.query
    total_items = query.count()
    total_pages = (total_items // page_size) + (1 if total_items % page_size > 0 else 0)
    dependencies = query.limit(page_size).offset(offset).all()
    return {
        "dependencies": [dependency.to_dict() for dependency in dependencies],
        "pagination": {
            "page": page,
            "page_size": page_size,
            "total_items": total_items,
            "total_pages": total_pages,
        },
    }


def update_dependency(dependency_id, dependency=None):
    """Update a single dependency

    Update a particular dependency

    :param dependency_id:
    :type dependency_id: str
    :param dependency:
    :type dependency: dict | bytes

    :rtype: Dependency
    """
    if not connexion.request.is_json:
        return "Bad request, JSON required", 400
    dependency = Dependency.query.get(dependency_id)
    if not dependency:
        return "Dependency not found", 404
    dependency.update(connexion.request.get_json())
    session.add(dependency)
    session.commit()
    return dependency.to_dict()
