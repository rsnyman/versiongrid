# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from versiongrid.models.base_model_ import Model
from versiongrid import util


class Dependency(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, component_version_id=None, dependency_version_id=None, created=None):  # noqa: E501
        """Dependency - a model defined in OpenAPI

        :param id: The id of this Dependency.  # noqa: E501
        :type id: str
        :param component_version_id: The component_version_id of this Dependency.  # noqa: E501
        :type component_version_id: str
        :param dependency_version_id: The dependency_version_id of this Dependency.  # noqa: E501
        :type dependency_version_id: str
        :param created: The created of this Dependency.  # noqa: E501
        :type created: str
        """
        self.openapi_types = {
            'id': str,
            'component_version_id': str,
            'dependency_version_id': str,
            'created': str
        }

        self.attribute_map = {
            'id': 'id',
            'component_version_id': 'component_version_id',
            'dependency_version_id': 'dependency_version_id',
            'created': 'created'
        }

        self._id = id
        self._component_version_id = component_version_id
        self._dependency_version_id = dependency_version_id
        self._created = created

    @classmethod
    def from_dict(cls, dikt) -> 'Dependency':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Dependency of this Dependency.  # noqa: E501
        :rtype: Dependency
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Dependency.


        :return: The id of this Dependency.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Dependency.


        :param id: The id of this Dependency.
        :type id: str
        """

        self._id = id

    @property
    def component_version_id(self):
        """Gets the component_version_id of this Dependency.


        :return: The component_version_id of this Dependency.
        :rtype: str
        """
        return self._component_version_id

    @component_version_id.setter
    def component_version_id(self, component_version_id):
        """Sets the component_version_id of this Dependency.


        :param component_version_id: The component_version_id of this Dependency.
        :type component_version_id: str
        """

        self._component_version_id = component_version_id

    @property
    def dependency_version_id(self):
        """Gets the dependency_version_id of this Dependency.


        :return: The dependency_version_id of this Dependency.
        :rtype: str
        """
        return self._dependency_version_id

    @dependency_version_id.setter
    def dependency_version_id(self, dependency_version_id):
        """Sets the dependency_version_id of this Dependency.


        :param dependency_version_id: The dependency_version_id of this Dependency.
        :type dependency_version_id: str
        """

        self._dependency_version_id = dependency_version_id

    @property
    def created(self):
        """Gets the created of this Dependency.


        :return: The created of this Dependency.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Dependency.


        :param created: The created of this Dependency.
        :type created: str
        """

        self._created = created
