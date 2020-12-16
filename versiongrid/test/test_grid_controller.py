# coding: utf-8
from __future__ import absolute_import

import unittest

from flask import json

from versiongrid.test import BaseTestCase


class TestGridController(BaseTestCase):
    """GridController integration test stubs"""

    def test_add_grid(self):
        """Test case for add_grid"""
        grid = {
            "component": "component",
            "version": "version",
            "dependencies": [
                {"component": "component", "version": "version"},
                {"component": "component", "version": "version"},
            ],
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        response = self.client.open(
            "/grid",
            method="POST",
            headers=headers,
            data=json.dumps(grid),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_grid(self):
        """Test case for get_grid

        Check a component's dependencies
        """
        query_string = [("version", "version_example")]
        headers = {
            "Accept": "application/json",
        }
        response = self.client.open(
            "/grid/{component}".format(component="component_example"),
            method="GET",
            headers=headers,
            query_string=query_string,
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    unittest.main()
