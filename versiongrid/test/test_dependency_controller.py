# coding: utf-8
from __future__ import absolute_import

import unittest

from flask import json

from versiongrid.test import BaseTestCase


class TestDependencyController(BaseTestCase):
    """DependencyController integration test stubs"""

    def test_add_dependency(self):
        """Test case for add_dependency

        Create a new dependency
        """
        dependency = {
            "dependency_version_id": "dependency_version_id",
            "created": "created",
            "id": "id",
            "component_version_id": "component_version_id",
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        response = self.client.open(
            "/dependency",
            method="POST",
            headers=headers,
            data=json.dumps(dependency),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_delete_dependency(self):
        """Test case for delete_dependency

        Delete a single dependency
        """
        headers = {}
        response = self.client.open(
            "/dependency/{dependency_id}".format(dependency_id="dependency_id_example"),
            method="DELETE",
            headers=headers,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_dependency(self):
        """Test case for get_dependency

        Get a single dependency
        """
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/dependency/{dependency_id}".format(dependency_id="dependency_id_example"),
            method="GET",
            headers=headers,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_dependency_list(self):
        """Test case for get_dependency_list

        Get a list of dependencies
        """
        query_string = [
            ("commit", "commit_example"),
            ("image_tag", "image_tag_example"),
            ("template_ref", "template_ref_example"),
            ("revision", "revision_example"),
            ("version", "version_example"),
        ]
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/dependency", method="GET", headers=headers, query_string=query_string
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_update_dependency(self):
        """Test case for update_dependency

        Update a single dependency
        """
        dependency = {
            "dependency_version_id": "dependency_version_id",
            "created": "created",
            "id": "id",
            "component_version_id": "component_version_id",
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        response = self.client.open(
            "/dependency/{dependency_id}".format(dependency_id="dependency_id_example"),
            method="PUT",
            headers=headers,
            data=json.dumps(dependency),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
