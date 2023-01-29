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

class InlineResponse2002(object):
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
        'id': 'str',
        'timestamp': 'str',
        'detectors': 'list[ScalalastDataDetectors]'
    }

    attribute_map = {
        'id': 'id',
        'timestamp': 'timestamp',
        'detectors': 'detectors'
    }

    def __init__(self, id=None, timestamp=None, detectors=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._timestamp = None
        self._detectors = None
        self.discriminator = None
        self.id = id
        if timestamp is not None:
            self.timestamp = timestamp
        self.detectors = detectors

    @property
    def id(self):
        """Gets the id of this InlineResponse2002.  # noqa: E501

        Intersection id  # noqa: E501

        :return: The id of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2002.

        Intersection id  # noqa: E501

        :param id: The id of this InlineResponse2002.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def timestamp(self):
        """Gets the timestamp of this InlineResponse2002.  # noqa: E501

        Server time when this record has been written into the database.  # noqa: E501

        :return: The timestamp of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this InlineResponse2002.

        Server time when this record has been written into the database.  # noqa: E501

        :param timestamp: The timestamp of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def detectors(self):
        """Gets the detectors of this InlineResponse2002.  # noqa: E501


        :return: The detectors of this InlineResponse2002.  # noqa: E501
        :rtype: list[ScalalastDataDetectors]
        """
        return self._detectors

    @detectors.setter
    def detectors(self, detectors):
        """Sets the detectors of this InlineResponse2002.


        :param detectors: The detectors of this InlineResponse2002.  # noqa: E501
        :type: list[ScalalastDataDetectors]
        """
        if detectors is None:
            raise ValueError("Invalid value for `detectors`, must not be `None`")  # noqa: E501

        self._detectors = detectors

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
        if issubclass(InlineResponse2002, dict):
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
        if not isinstance(other, InlineResponse2002):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
