# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from versiongrid.models.version import Version  # noqa: E501
from versiongrid.models.version_list import VersionList  # noqa: E501
from versiongrid.test import BaseTestCase


class TestVersionController(BaseTestCase):
    """VersionController integration test stubs"""

    def test_add_version(self):
        """Test case for add_version

        Create a new version
        """
        version = {
  "component_id" : "component_id",
  "environments" : [ {
    "name" : "name",
    "deployed_date" : "deployed_date"
  }, {
    "name" : "name",
    "deployed_date" : "deployed_date"
  } ],
  "template_ref" : "template_ref",
  "created" : "created",
  "commit" : "commit",
  "id" : "id",
  "image_tag" : "image_tag",
  "version" : "version",
  "revision" : "revision"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/version',
            method='POST',
            headers=headers,
            data=json.dumps(version),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_version(self):
        """Test case for delete_version

        Delete a single version
        """
        headers = { 
        }
        response = self.client.open(
            '/version/{version_id}'.format(version_id='version_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_version(self):
        """Test case for get_version

        Get a single version
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/version/{version_id}'.format(version_id='version_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_version_list(self):
        """Test case for get_version_list

        Get a list of versions
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
            '/version',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_version(self):
        """Test case for update_version

        Update a single version
        """
        version = {
  "component_id" : "component_id",
  "environments" : [ {
    "name" : "name",
    "deployed_date" : "deployed_date"
  }, {
    "name" : "name",
    "deployed_date" : "deployed_date"
  } ],
  "template_ref" : "template_ref",
  "created" : "created",
  "commit" : "commit",
  "id" : "id",
  "image_tag" : "image_tag",
  "version" : "version",
  "revision" : "revision"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/version/{version_id}'.format(version_id='version_id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(version),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
