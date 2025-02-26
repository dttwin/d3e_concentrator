# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.inline_response2001_detector import InlineResponse2001Detector  # noqa: F401,E501
from swagger_server import util


class InlineResponse2001Intersection(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, detector: List[InlineResponse2001Detector]=None):  # noqa: E501
        """InlineResponse2001Intersection - a model defined in Swagger

        :param id: The id of this InlineResponse2001Intersection.  # noqa: E501
        :type id: str
        :param detector: The detector of this InlineResponse2001Intersection.  # noqa: E501
        :type detector: List[InlineResponse2001Detector]
        """
        self.swagger_types = {
            'id': str,
            'detector': List[InlineResponse2001Detector]
        }

        self.attribute_map = {
            'id': 'id',
            'detector': 'detector'
        }
        self._id = id
        self._detector = detector

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2001Intersection':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_1_intersection of this InlineResponse2001Intersection.  # noqa: E501
        :rtype: InlineResponse2001Intersection
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this InlineResponse2001Intersection.


        :return: The id of this InlineResponse2001Intersection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this InlineResponse2001Intersection.


        :param id: The id of this InlineResponse2001Intersection.
        :type id: str
        """

        self._id = id

    @property
    def detector(self) -> List[InlineResponse2001Detector]:
        """Gets the detector of this InlineResponse2001Intersection.


        :return: The detector of this InlineResponse2001Intersection.
        :rtype: List[InlineResponse2001Detector]
        """
        return self._detector

    @detector.setter
    def detector(self, detector: List[InlineResponse2001Detector]):
        """Sets the detector of this InlineResponse2001Intersection.


        :param detector: The detector of this InlineResponse2001Intersection.
        :type detector: List[InlineResponse2001Detector]
        """

        self._detector = detector
