import connexion
import six

from versiongrid.models.version import Version  # noqa: E501
from versiongrid.models.version_list import VersionList  # noqa: E501
from versiongrid import util


def add_version(version=None):  # noqa: E501
    """Create a new version

    Create a new version # noqa: E501

    :param version: 
    :type version: dict | bytes

    :rtype: Version
    """
    if connexion.request.is_json:
        version = Version.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_version(version_id):  # noqa: E501
    """Delete a single version

    Delete a version # noqa: E501

    :param version_id: 
    :type version_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_version(version_id):  # noqa: E501
    """Get a single version

    Get a version by id # noqa: E501

    :param version_id: 
    :type version_id: str

    :rtype: Version
    """
    return 'do some magic!'


def get_version_list(commit=None, image_tag=None, template_ref=None, revision=None, version=None):  # noqa: E501
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
    return 'do some magic!'


def update_version(version_id, version=None):  # noqa: E501
    """Update a single version

    Update a particular version # noqa: E501

    :param version_id: 
    :type version_id: str
    :param version: 
    :type version: dict | bytes

    :rtype: Version
    """
    if connexion.request.is_json:
        version = Version.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
