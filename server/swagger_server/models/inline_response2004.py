# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.golemiolast_data_vehicles import GolemiolastDataVehicles  # noqa: F401,E501
from swagger_server import util


class InlineResponse2004(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, lineid: str=None, vehicles: GolemiolastDataVehicles=None):  # noqa: E501
        """InlineResponse2004 - a model defined in Swagger

        :param lineid: The lineid of this InlineResponse2004.  # noqa: E501
        :type lineid: str
        :param vehicles: The vehicles of this InlineResponse2004.  # noqa: E501
        :type vehicles: GolemiolastDataVehicles
        """
        self.swagger_types = {
            'lineid': str,
            'vehicles': GolemiolastDataVehicles
        }

        self.attribute_map = {
            'lineid': 'lineid',
            'vehicles': 'vehicles'
        }
        self._lineid = lineid
        self._vehicles = vehicles

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2004':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_4 of this InlineResponse2004.  # noqa: E501
        :rtype: InlineResponse2004
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lineid(self) -> str:
        """Gets the lineid of this InlineResponse2004.

        Identifier of a PT line (numeric / alphanumeric).  # noqa: E501

        :return: The lineid of this InlineResponse2004.
        :rtype: str
        """
        return self._lineid

    @lineid.setter
    def lineid(self, lineid: str):
        """Sets the lineid of this InlineResponse2004.

        Identifier of a PT line (numeric / alphanumeric).  # noqa: E501

        :param lineid: The lineid of this InlineResponse2004.
        :type lineid: str
        """
        if lineid is None:
            raise ValueError("Invalid value for `lineid`, must not be `None`")  # noqa: E501

        self._lineid = lineid

    @property
    def vehicles(self) -> GolemiolastDataVehicles:
        """Gets the vehicles of this InlineResponse2004.


        :return: The vehicles of this InlineResponse2004.
        :rtype: GolemiolastDataVehicles
        """
        return self._vehicles

    @vehicles.setter
    def vehicles(self, vehicles: GolemiolastDataVehicles):
        """Sets the vehicles of this InlineResponse2004.


        :param vehicles: The vehicles of this InlineResponse2004.
        :type vehicles: GolemiolastDataVehicles
        """

        self._vehicles = vehicles
