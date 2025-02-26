# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ScalalastDataData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, cnt: int=None, spd: int=None, occ: int=None, time_start: str=None, time_stop: str=None):  # noqa: E501
        """ScalalastDataData - a model defined in Swagger

        :param cnt: The cnt of this ScalalastDataData.  # noqa: E501
        :type cnt: int
        :param spd: The spd of this ScalalastDataData.  # noqa: E501
        :type spd: int
        :param occ: The occ of this ScalalastDataData.  # noqa: E501
        :type occ: int
        :param time_start: The time_start of this ScalalastDataData.  # noqa: E501
        :type time_start: str
        :param time_stop: The time_stop of this ScalalastDataData.  # noqa: E501
        :type time_stop: str
        """
        self.swagger_types = {
            'cnt': int,
            'spd': int,
            'occ': int,
            'time_start': str,
            'time_stop': str
        }

        self.attribute_map = {
            'cnt': 'cnt',
            'spd': 'spd',
            'occ': 'occ',
            'time_start': 'time_start',
            'time_stop': 'time_stop'
        }
        self._cnt = cnt
        self._spd = spd
        self._occ = occ
        self._time_start = time_start
        self._time_stop = time_stop

    @classmethod
    def from_dict(cls, dikt) -> 'ScalalastDataData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The scalalastData_data of this ScalalastDataData.  # noqa: E501
        :rtype: ScalalastDataData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cnt(self) -> int:
        """Gets the cnt of this ScalalastDataData.


        :return: The cnt of this ScalalastDataData.
        :rtype: int
        """
        return self._cnt

    @cnt.setter
    def cnt(self, cnt: int):
        """Sets the cnt of this ScalalastDataData.


        :param cnt: The cnt of this ScalalastDataData.
        :type cnt: int
        """
        if cnt is None:
            raise ValueError("Invalid value for `cnt`, must not be `None`")  # noqa: E501

        self._cnt = cnt

    @property
    def spd(self) -> int:
        """Gets the spd of this ScalalastDataData.


        :return: The spd of this ScalalastDataData.
        :rtype: int
        """
        return self._spd

    @spd.setter
    def spd(self, spd: int):
        """Sets the spd of this ScalalastDataData.


        :param spd: The spd of this ScalalastDataData.
        :type spd: int
        """
        if spd is None:
            raise ValueError("Invalid value for `spd`, must not be `None`")  # noqa: E501

        self._spd = spd

    @property
    def occ(self) -> int:
        """Gets the occ of this ScalalastDataData.


        :return: The occ of this ScalalastDataData.
        :rtype: int
        """
        return self._occ

    @occ.setter
    def occ(self, occ: int):
        """Sets the occ of this ScalalastDataData.


        :param occ: The occ of this ScalalastDataData.
        :type occ: int
        """
        if occ is None:
            raise ValueError("Invalid value for `occ`, must not be `None`")  # noqa: E501

        self._occ = occ

    @property
    def time_start(self) -> str:
        """Gets the time_start of this ScalalastDataData.

        Start of the measurement period as reported by SCALA.  # noqa: E501

        :return: The time_start of this ScalalastDataData.
        :rtype: str
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start: str):
        """Sets the time_start of this ScalalastDataData.

        Start of the measurement period as reported by SCALA.  # noqa: E501

        :param time_start: The time_start of this ScalalastDataData.
        :type time_start: str
        """

        self._time_start = time_start

    @property
    def time_stop(self) -> str:
        """Gets the time_stop of this ScalalastDataData.

        End of the measurement period as reported by SCALA.  # noqa: E501

        :return: The time_stop of this ScalalastDataData.
        :rtype: str
        """
        return self._time_stop

    @time_stop.setter
    def time_stop(self, time_stop: str):
        """Sets the time_stop of this ScalalastDataData.

        End of the measurement period as reported by SCALA.  # noqa: E501

        :param time_stop: The time_stop of this ScalalastDataData.
        :type time_stop: str
        """

        self._time_stop = time_stop
