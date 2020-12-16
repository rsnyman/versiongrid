import connexion

from versiongrid.db.base import session
from versiongrid.db.models import Version


def add_version(version=None):
    """Create a new version

    Create a new version

    :param version:
    :type version: dict | bytes

    :rtype: Version
    """
    if not connexion.request.is_json:
        return "Bad request, JSON required", 400
    version = Version(**connexion.request.get_json())
    session.add(version)
    return version.to_dict(), 201


def delete_version(version_id):
    """Delete a single version

    Delete a version

    :param version_id:
    :type version_id: str

    :rtype: None
    """
    version = Version.query.get(version_id)
    if version:
        session.delete(version)
        session.commit()
        return "Deleted", 200
    else:
        return "Version not found", 404


def get_version(version_id):
    """Get a single version

    Get a version by id

    :param version_id:
    :type version_id: str

    :rtype: Version
    """
    version = Version.query.get(version_id)
    if version:
        return version.to_dict()
    else:
        return "Version not found", 404


def get_version_list(
    commit=None,
    image_tag=None,
    template_ref=None,
    revision=None,
    version=None,
    page=1,
    page_size=25,
):
    """Get a list of versions

    A list of versions # noqa: E501

    :param commit:
    :type commit: str
    :param image_tag:
    :type image_tag: str
    :param template_ref:
    :type template_ref: str
    :param revision:
    :type revision: str
    :param version:
    :type version: str

    :rtype: VersionList
    """
    offset = (page * page_size) - page_size
    query = Version.query
    total_items = query.count()
    total_pages = (total_items // page_size) + (1 if total_items % page_size > 0 else 0)
    versions = query.limit(page_size).offset(offset).all()
    return {
        "versions": [version.to_dict() for version in versions],
        "pagination": {
            "page": page,
            "page_size": page_size,
            "total_items": total_items,
            "total_pages": total_pages,
        },
    }


def update_version(version_id, version=None):  # noqa: E501
    """Update a single version

    Update a particular version # noqa: E501

    :param version_id:
    :type version_id: str
    :param version:
    :type version: dict | bytes

    :rtype: Version
    """
    if not connexion.request.is_json:
        return "Bad request, JSON required", 400
    version = Version.query.get(version_id)
    if not version:
        return "Version not found", 404
    version.update(connexion.request.get_json())
    session.add(version)
    session.commit()
    return version.to_dict()
