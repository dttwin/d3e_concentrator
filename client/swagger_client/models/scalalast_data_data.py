# coding: utf-8

"""
    Traffic data concentrator - OpenAPI 3.0

    This is a development Swagger-supported server based on the OpenAPI 3.0 specification. You can find out more about Swagger at  [https://swagger.io](https://swagger.io).  # noqa: E501

    OpenAPI spec version: 0.9.4
    Contact: d3e@fd.cvut.cz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ScalalastDataData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cnt': 'int',
        'spd': 'int',
        'occ': 'int',
        'time_start': 'str',
        'time_stop': 'str'
    }

    attribute_map = {
        'cnt': 'cnt',
        'spd': 'spd',
        'occ': 'occ',
        'time_start': 'time_start',
        'time_stop': 'time_stop'
    }

    def __init__(self, cnt=None, spd=None, occ=None, time_start=None, time_stop=None):  # noqa: E501
        """ScalalastDataData - a model defined in Swagger"""  # noqa: E501
        self._cnt = None
        self._spd = None
        self._occ = None
        self._time_start = None
        self._time_stop = None
        self.discriminator = None
        self.cnt = cnt
        self.spd = spd
        self.occ = occ
        if time_start is not None:
            self.time_start = time_start
        if time_stop is not None:
            self.time_stop = time_stop

    @property
    def cnt(self):
        """Gets the cnt of this ScalalastDataData.  # noqa: E501


        :return: The cnt of this ScalalastDataData.  # noqa: E501
        :rtype: int
        """
        return self._cnt

    @cnt.setter
    def cnt(self, cnt):
        """Sets the cnt of this ScalalastDataData.


        :param cnt: The cnt of this ScalalastDataData.  # noqa: E501
        :type: int
        """
        if cnt is None:
            raise ValueError("Invalid value for `cnt`, must not be `None`")  # noqa: E501

        self._cnt = cnt

    @property
    def spd(self):
        """Gets the spd of this ScalalastDataData.  # noqa: E501


        :return: The spd of this ScalalastDataData.  # noqa: E501
        :rtype: int
        """
        return self._spd

    @spd.setter
    def spd(self, spd):
        """Sets the spd of this ScalalastDataData.


        :param spd: The spd of this ScalalastDataData.  # noqa: E501
        :type: int
        """
        if spd is None:
            raise ValueError("Invalid value for `spd`, must not be `None`")  # noqa: E501

        self._spd = spd

    @property
    def occ(self):
        """Gets the occ of this ScalalastDataData.  # noqa: E501


        :return: The occ of this ScalalastDataData.  # noqa: E501
        :rtype: int
        """
        return self._occ

    @occ.setter
    def occ(self, occ):
        """Sets the occ of this ScalalastDataData.


        :param occ: The occ of this ScalalastDataData.  # noqa: E501
        :type: int
        """
        if occ is None:
            raise ValueError("Invalid value for `occ`, must not be `None`")  # noqa: E501

        self._occ = occ

    @property
    def time_start(self):
        """Gets the time_start of this ScalalastDataData.  # noqa: E501

        Start of the measurement period as reported by SCALA.  # noqa: E501

        :return: The time_start of this ScalalastDataData.  # noqa: E501
        :rtype: str
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """Sets the time_start of this ScalalastDataData.

        Start of the measurement period as reported by SCALA.  # noqa: E501

        :param time_start: The time_start of this ScalalastDataData.  # noqa: E501
        :type: str
        """

        self._time_start = time_start

    @property
    def time_stop(self):
        """Gets the time_stop of this ScalalastDataData.  # noqa: E501

        End of the measurement period as reported by SCALA.  # noqa: E501

        :return: The time_stop of this ScalalastDataData.  # noqa: E501
        :rtype: str
        """
        return self._time_stop

    @time_stop.setter
    def time_stop(self, time_stop):
        """Sets the time_stop of this ScalalastDataData.

        End of the measurement period as reported by SCALA.  # noqa: E501

        :param time_stop: The time_stop of this ScalalastDataData.  # noqa: E501
        :type: str
        """

        self._time_stop = time_stop

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ScalalastDataData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScalalastDataData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
