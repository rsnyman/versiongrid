# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from versiongrid.models.base_model_ import Model
from versiongrid import util


class Pagination(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, page=None, page_size=None, total_items=None, total_pages=None):  # noqa: E501
        """Pagination - a model defined in OpenAPI

        :param page: The page of this Pagination.  # noqa: E501
        :type page: int
        :param page_size: The page_size of this Pagination.  # noqa: E501
        :type page_size: int
        :param total_items: The total_items of this Pagination.  # noqa: E501
        :type total_items: int
        :param total_pages: The total_pages of this Pagination.  # noqa: E501
        :type total_pages: int
        """
        self.openapi_types = {
            'page': int,
            'page_size': int,
            'total_items': int,
            'total_pages': int
        }

        self.attribute_map = {
            'page': 'page',
            'page_size': 'page_size',
            'total_items': 'total_items',
            'total_pages': 'total_pages'
        }

        self._page = page
        self._page_size = page_size
        self._total_items = total_items
        self._total_pages = total_pages

    @classmethod
    def from_dict(cls, dikt) -> 'Pagination':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Pagination of this Pagination.  # noqa: E501
        :rtype: Pagination
        """
        return util.deserialize_model(dikt, cls)

    @property
    def page(self):
        """Gets the page of this Pagination.


        :return: The page of this Pagination.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this Pagination.


        :param page: The page of this Pagination.
        :type page: int
        """

        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this Pagination.


        :return: The page_size of this Pagination.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this Pagination.


        :param page_size: The page_size of this Pagination.
        :type page_size: int
        """

        self._page_size = page_size

    @property
    def total_items(self):
        """Gets the total_items of this Pagination.


        :return: The total_items of this Pagination.
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this Pagination.


        :param total_items: The total_items of this Pagination.
        :type total_items: int
        """

        self._total_items = total_items

    @property
    def total_pages(self):
        """Gets the total_pages of this Pagination.


        :return: The total_pages of this Pagination.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this Pagination.


        :param total_pages: The total_pages of this Pagination.
        :type total_pages: int
        """

        self._total_pages = total_pages