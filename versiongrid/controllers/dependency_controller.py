import connexion
import six

from versiongrid.models.any_of_dependency_dependency_grid import AnyOfDependencyDependencyGrid  # noqa: E501
from versiongrid.models.dependency import Dependency  # noqa: E501
from versiongrid.models.dependency_check import DependencyCheck  # noqa: E501
from versiongrid.models.dependency_list import DependencyList  # noqa: E501
from versiongrid.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from versiongrid import util


def add_dependency(unknown_base_type=None):  # noqa: E501
    """Create a new dependency

    Create a new dependency # noqa: E501

    :param unknown_base_type: 
    :type unknown_base_type: dict | bytes

    :rtype: Dependency
    """
    if connexion.request.is_json:
        unknown_base_type = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def check_dependency(component, version=None, dependency=None):  # noqa: E501
    """Check a component&#39;s dependencies

    Check a list of dependencies # noqa: E501

    :param component: 
    :type component: str
    :param version: 
    :type version: str
    :param dependency: 
    :type dependency: str

    :rtype: DependencyCheck
    """
    return 'do some magic!'


def delete_dependency(dependency_id):  # noqa: E501
    """Delete a single dependency

    Delete a dependency # noqa: E501

    :param dependency_id: 
    :type dependency_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_dependency(dependency_id):  # noqa: E501
    """Get a single dependency

    Get a dependency by id # noqa: E501

    :param dependency_id: 
    :type dependency_id: str

    :rtype: Dependency
    """
    return 'do some magic!'


def get_dependency_list(commit=None, image_tag=None, template_ref=None, revision=None, version=None):  # noqa: E501
    """Get a list of dependencies

    A list of dependencies # noqa: E501

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

    :rtype: DependencyList
    """
    return 'do some magic!'


def update_dependency(dependency_id, dependency=None):  # noqa: E501
    """Update a single dependency

    Update a particular dependency # noqa: E501

    :param dependency_id: 
    :type dependency_id: str
    :param dependency: 
    :type dependency: dict | bytes

    :rtype: Dependency
    """
    if connexion.request.is_json:
        dependency = Dependency.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
