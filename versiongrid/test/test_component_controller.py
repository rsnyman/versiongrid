# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from versiongrid.models.component import Component  # noqa: E501
from versiongrid.models.component_list import ComponentList  # noqa: E501
from versiongrid.test import BaseTestCase


class TestComponentController(BaseTestCase):
    """ComponentController integration test stubs"""

    def test_add_component(self):
        """Test case for add_component

        Create a new component
        """
        component = {
  "name" : "name",
  "id" : "id",
  "title" : "title"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/component',
            method='POST',
            headers=headers,
            data=json.dumps(component),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_component(self):
        """Test case for delete_component

        Delete a single component
        """
        headers = { 
        }
        response = self.client.open(
            '/component/{component_id}'.format(component_id='component_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_component(self):
        """Test case for get_component

        Get a single component
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/component/{component_id}'.format(component_id='component_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_component_list(self):
        """Test case for get_component_list

        Get a list of components
        """
        query_string = [('commit', 'commit_example'),
                        ('image_tag', 'image_tag_example'),
                        ('template_ref', 'template_ref_example'),
                        ('revision', 'revision_example'),
                        ('version', 'version_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/component',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_component(self):
        """Test case for update_component

        Update a single component
        """
        component = {
  "name" : "name",
  "id" : "id",
  "title" : "title"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/component/{component_id}'.format(component_id='component_id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(component),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
