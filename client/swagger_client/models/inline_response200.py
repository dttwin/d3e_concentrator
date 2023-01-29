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

class InlineResponse200(object):
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
        'detectors': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'detectors': 'detectors'
    }

    def __init__(self, id=None, detectors=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._detectors = None
        self.discriminator = None
        self.id = id
        if detectors is not None:
            self.detectors = detectors

    @property
    def id(self):
        """Gets the id of this InlineResponse200.  # noqa: E501

        Identifier of an intersection, in SCALA notation, i.e.  a string \"FD<<district>><<number>>\".  # noqa: E501

        :return: The id of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse200.

        Identifier of an intersection, in SCALA notation, i.e.  a string \"FD<<district>><<number>>\".  # noqa: E501

        :param id: The id of this InlineResponse200.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def detectors(self):
        """Gets the detectors of this InlineResponse200.  # noqa: E501

        List of detector names for the intersection. Detectors  bear both SCALA id and traffic engineering mapping id, represented by a a string \"<<scala_id>>_<<traffic_map_id>>\"  # noqa: E501

        :return: The detectors of this InlineResponse200.  # noqa: E501
        :rtype: list[str]
        """
        return self._detectors

    @detectors.setter
    def detectors(self, detectors):
        """Sets the detectors of this InlineResponse200.

        List of detector names for the intersection. Detectors  bear both SCALA id and traffic engineering mapping id, represented by a a string \"<<scala_id>>_<<traffic_map_id>>\"  # noqa: E501

        :param detectors: The detectors of this InlineResponse200.  # noqa: E501
        :type: list[str]
        """

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
        if issubclass(InlineResponse200, dict):
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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
