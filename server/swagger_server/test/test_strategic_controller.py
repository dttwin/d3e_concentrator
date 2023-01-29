# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStrategicController(BaseTestCase):
    """StrategicController integration test stubs"""

    def test_strategic_get_endpoints(self):
        """Test case for strategic_get_endpoints

        Retrieve strategic detector ids
        """
        response = self.client.open(
            '/api/v1/strategic/endpoints',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_strategic_get_last_data(self):
        """Test case for strategic_get_last_data

        Retrieve last data from strategic detectors
        """
        query_string = [('iid', '[]'),
                        ('updated_since', 'updated_since_example')]
        response = self.client.open(
            '/api/v1/strategic/lastData',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
