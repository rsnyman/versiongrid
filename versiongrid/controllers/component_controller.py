import connexion
import six

from versiongrid.models.component import Component  # noqa: E501
from versiongrid.models.component_list import ComponentList  # noqa: E501
from versiongrid import util


def add_component(component=None):  # noqa: E501
    """Create a new component

    Create a new component # noqa: E501

    :param component: 
    :type component: dict | bytes

    :rtype: Component
    """
    if connexion.request.is_json:
        component = Component.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_component(component_id):  # noqa: E501
    """Delete a single component

    Delete a component # noqa: E501

    :param component_id: 
    :type component_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_component(component_id):  # noqa: E501
    """Get a single component

    Get a component by id # noqa: E501

    :param component_id: 
    :type component_id: str

    :rtype: Component
    """
    return 'do some magic!'


def get_component_list(commit=None, image_tag=None, template_ref=None, revision=None, version=None):  # noqa: E501
    """Get a list of components

    A list of components # noqa: E501

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

    :rtype: ComponentList
    """
    return 'do some magic!'


def update_component(component_id, component=None):  # noqa: E501
    """Update a single component

    Update a particular component # noqa: E501

    :param component_id: 
    :type component_id: str
    :param component: 
    :type component: dict | bytes

    :rtype: Component
    """
    if connexion.request.is_json:
        component = Component.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
