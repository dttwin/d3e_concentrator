# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGolemioController(BaseTestCase):
    """GolemioController integration test stubs"""

    def test_golemio_get_last_data(self):
        """Test case for golemio_get_last_data

        Get last data uploaded from the Golemio platform
        """
        query_string = [('lineid', '[]'),
                        ('updated_since', 'updated_since_example')]
        response = self.client.open(
            '/api/v1/golemio/lastData',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_golemio_get_lines(self):
        """Test case for golemio_get_lines

        Retrieve list of public transport lines covered by golemio
        """
        response = self.client.open(
            '/api/v1/golemio/lines',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
