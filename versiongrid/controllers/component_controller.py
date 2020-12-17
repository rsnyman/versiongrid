import connexion

from versiongrid.db.base import session
from versiongrid.db.models import Component


def add_component(component=None):
    """Create a new component

    Create a new component

    :param component:
    :type component: dict | bytes

    :rtype: Component
    """
    if not connexion.request.is_json:
        return "Bad request, JSON required", 400
    component = Component(**connexion.request.get_json())
    session.add(component)
    return component.to_dict(), 201


def delete_component(component_id):
    """Delete a single component

    Delete a component

    :param component_id:
    :type component_id: str

    :rtype: None
    """
    component = Component.query.get(component_id)
    if component:
        session.delete(component)
        session.commit()
        return "Deleted", 200
    else:
        return "Component not found", 404


def get_component(component_id):
    """Get a single component

    Get a component by id

    :param component_id:
    :type component_id: str

    :rtype: Component
    """
    component = Component.query.get(component_id)
    if component:
        return component.to_dict()
    else:
        return "Component not found", 404


def get_component_list(page=1, page_size=25):
    """Get a list of components

    A list of components

    :param page:
    :type page: int
    :param page_size:
    :type page_size: int

    :rtype: ComponentList
    """
    offset = (page * page_size) - page_size
    query = Component.query
    total_items = query.count()
    total_pages = (total_items // page_size) + (1 if total_items % page_size > 0 else 0)
    components = query.limit(page_size).offset(offset).all()
    return {
        "components": [component.to_dict() for component in components],
        "pagination": {
            "page": page,
            "page_size": page_size,
            "total_items": total_items,
            "total_pages": total_pages,
        },
    }


def update_component(component_id, component=None):
    """Update a single component

    Update a particular component

    :param component_id:
    :type component_id: str
    :param component:
    :type component: dict | bytes

    :rtype: Component
    """
    if not connexion.request.is_json:
        return "Bad request, JSON required", 400
    component = Component.query.get(component_id)
    if not component:
        return "Component not found", 404
    component.update(connexion.request.get_json())
    session.add(component)
    session.commit()
    return component.to_dict()
