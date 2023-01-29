# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCameaController(BaseTestCase):
    """CameaController integration test stubs"""

    def test_camea_get_endpoints(self):
        """Test case for camea_get_endpoints

        Retrieve detector ids
        """
        response = self.client.open(
            '/api/v1/camea/endpoints',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_camea_get_last_data(self):
        """Test case for camea_get_last_data

        Retrieve last data from CAMEA detectors
        """
        response = self.client.open(
            '/api/v1/camea/lastData',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
