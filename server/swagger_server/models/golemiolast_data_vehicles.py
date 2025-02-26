# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GolemiolastDataVehicles(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, vehicleno: str=None, latitude: float=None, longitude: float=None, time: str=None):  # noqa: E501
        """GolemiolastDataVehicles - a model defined in Swagger

        :param vehicleno: The vehicleno of this GolemiolastDataVehicles.  # noqa: E501
        :type vehicleno: str
        :param latitude: The latitude of this GolemiolastDataVehicles.  # noqa: E501
        :type latitude: float
        :param longitude: The longitude of this GolemiolastDataVehicles.  # noqa: E501
        :type longitude: float
        :param time: The time of this GolemiolastDataVehicles.  # noqa: E501
        :type time: str
        """
        self.swagger_types = {
            'vehicleno': str,
            'latitude': float,
            'longitude': float,
            'time': str
        }

        self.attribute_map = {
            'vehicleno': 'vehicleno',
            'latitude': 'latitude',
            'longitude': 'longitude',
            'time': 'time'
        }
        self._vehicleno = vehicleno
        self._latitude = latitude
        self._longitude = longitude
        self._time = time

    @classmethod
    def from_dict(cls, dikt) -> 'GolemiolastDataVehicles':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The golemiolastData_vehicles of this GolemiolastDataVehicles.  # noqa: E501
        :rtype: GolemiolastDataVehicles
        """
        return util.deserialize_model(dikt, cls)

    @property
    def vehicleno(self) -> str:
        """Gets the vehicleno of this GolemiolastDataVehicles.

        Unique identifier of the PT vehicle (chasis number, registration number, license plate)  # noqa: E501

        :return: The vehicleno of this GolemiolastDataVehicles.
        :rtype: str
        """
        return self._vehicleno

    @vehicleno.setter
    def vehicleno(self, vehicleno: str):
        """Sets the vehicleno of this GolemiolastDataVehicles.

        Unique identifier of the PT vehicle (chasis number, registration number, license plate)  # noqa: E501

        :param vehicleno: The vehicleno of this GolemiolastDataVehicles.
        :type vehicleno: str
        """

        self._vehicleno = vehicleno

    @property
    def latitude(self) -> float:
        """Gets the latitude of this GolemiolastDataVehicles.

        Numeric WGS84 latitude of the vehicle  # noqa: E501

        :return: The latitude of this GolemiolastDataVehicles.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float):
        """Sets the latitude of this GolemiolastDataVehicles.

        Numeric WGS84 latitude of the vehicle  # noqa: E501

        :param latitude: The latitude of this GolemiolastDataVehicles.
        :type latitude: float
        """

        self._latitude = latitude

    @property
    def longitude(self) -> float:
        """Gets the longitude of this GolemiolastDataVehicles.

        Numeric WGS84 longitude of the vehicle  # noqa: E501

        :return: The longitude of this GolemiolastDataVehicles.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float):
        """Sets the longitude of this GolemiolastDataVehicles.

        Numeric WGS84 longitude of the vehicle  # noqa: E501

        :param longitude: The longitude of this GolemiolastDataVehicles.
        :type longitude: float
        """

        self._longitude = longitude

    @property
    def time(self) -> str:
        """Gets the time of this GolemiolastDataVehicles.

        Timestamp of the position report.  # noqa: E501

        :return: The time of this GolemiolastDataVehicles.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time: str):
        """Sets the time of this GolemiolastDataVehicles.

        Timestamp of the position report.  # noqa: E501

        :param time: The time of this GolemiolastDataVehicles.
        :type time: str
        """

        self._time = time
