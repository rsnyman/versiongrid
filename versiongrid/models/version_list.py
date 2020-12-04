# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from versiongrid.models.base_model_ import Model
from versiongrid.models.pagination import Pagination
from versiongrid.models.version import Version
from versiongrid import util

from versiongrid.models.pagination import Pagination  # noqa: E501
from versiongrid.models.version import Version  # noqa: E501

class VersionList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pagination=None, versions=None):  # noqa: E501
        """VersionList - a model defined in OpenAPI

        :param pagination: The pagination of this VersionList.  # noqa: E501
        :type pagination: Pagination
        :param versions: The versions of this VersionList.  # noqa: E501
        :type versions: List[Version]
        """
        self.openapi_types = {
            'pagination': Pagination,
            'versions': List[Version]
        }

        self.attribute_map = {
            'pagination': 'pagination',
            'versions': 'versions'
        }

        self._pagination = pagination
        self._versions = versions

    @classmethod
    def from_dict(cls, dikt) -> 'VersionList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VersionList of this VersionList.  # noqa: E501
        :rtype: VersionList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pagination(self):
        """Gets the pagination of this VersionList.


        :return: The pagination of this VersionList.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this VersionList.


        :param pagination: The pagination of this VersionList.
        :type pagination: Pagination
        """

        self._pagination = pagination

    @property
    def versions(self):
        """Gets the versions of this VersionList.


        :return: The versions of this VersionList.
        :rtype: List[Version]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this VersionList.


        :param versions: The versions of this VersionList.
        :type versions: List[Version]
        """

        self._versions = versions
