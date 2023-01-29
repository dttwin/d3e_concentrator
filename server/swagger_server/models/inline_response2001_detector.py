# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse2001Detector(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None):  # noqa: E501
        """InlineResponse2001Detector - a model defined in Swagger

        :param id: The id of this InlineResponse2001Detector.  # noqa: E501
        :type id: str
        """
        self.swagger_types = {
            'id': str
        }

        self.attribute_map = {
            'id': 'id'
        }
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2001Detector':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_1_detector of this InlineResponse2001Detector.  # noqa: E501
        :rtype: InlineResponse2001Detector
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this InlineResponse2001Detector.


        :return: The id of this InlineResponse2001Detector.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this InlineResponse2001Detector.


        :param id: The id of this InlineResponse2001Detector.
        :type id: str
        """

        self._id = id
