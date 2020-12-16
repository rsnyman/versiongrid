# coding: utf-8
from __future__ import absolute_import

from typing import List

from versiongrid import util
from versiongrid.models.base_model_ import Model
from versiongrid.models.grid_dependencies import GridDependencies


class Grid(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, component=None, version=None, dependencies=None):  # noqa: E501
        """Grid - a model defined in OpenAPI

        :param component: The component of this Grid.  # noqa: E501
        :type component: str
        :param version: The version of this Grid.  # noqa: E501
        :type version: str
        :param dependencies: The dependencies of this Grid.  # noqa: E501
        :type dependencies: List[GridDependencies]
        """
        self.openapi_types = {
            "component": str,
            "version": str,
            "dependencies": List[GridDependencies],
        }

        self.attribute_map = {
            "component": "component",
            "version": "version",
            "dependencies": "dependencies",
        }

        self._component = component
        self._version = version
        self._dependencies = dependencies

    @classmethod
    def from_dict(cls, dikt) -> "Grid":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Grid of this Grid.  # noqa: E501
        :rtype: Grid
        """
        return util.deserialize_model(dikt, cls)

    @property
    def component(self):
        """Gets the component of this Grid.


        :return: The component of this Grid.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this Grid.


        :param component: The component of this Grid.
        :type component: str
        """

        self._component = component

    @property
    def version(self):
        """Gets the version of this Grid.


        :return: The version of this Grid.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Grid.


        :param version: The version of this Grid.
        :type version: str
        """

        self._version = version

    @property
    def dependencies(self):
        """Gets the dependencies of this Grid.


        :return: The dependencies of this Grid.
        :rtype: List[GridDependencies]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this Grid.


        :param dependencies: The dependencies of this Grid.
        :type dependencies: List[GridDependencies]
        """

        self._dependencies = dependencies
