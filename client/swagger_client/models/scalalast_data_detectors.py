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

class ScalalastDataDetectors(object):
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
        '_class': 'str',
        'data': 'ScalalastDataData'
    }

    attribute_map = {
        'id': 'id',
        '_class': 'class',
        'data': 'data'
    }

    def __init__(self, id=None, _class=None, data=None):  # noqa: E501
        """ScalalastDataDetectors - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self.__class = None
        self._data = None
        self.discriminator = None
        self.id = id
        self._class = _class
        self.data = data

    @property
    def id(self):
        """Gets the id of this ScalalastDataDetectors.  # noqa: E501

        Detector ID, contains both numeric ID from SCALA and traffic engineering ID from intersection plans, separated by '_'  # noqa: E501

        :return: The id of this ScalalastDataDetectors.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScalalastDataDetectors.

        Detector ID, contains both numeric ID from SCALA and traffic engineering ID from intersection plans, separated by '_'  # noqa: E501

        :param id: The id of this ScalalastDataDetectors.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def _class(self):
        """Gets the _class of this ScalalastDataDetectors.  # noqa: E501

        Detector class  # noqa: E501

        :return: The _class of this ScalalastDataDetectors.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this ScalalastDataDetectors.

        Detector class  # noqa: E501

        :param _class: The _class of this ScalalastDataDetectors.  # noqa: E501
        :type: str
        """
        if _class is None:
            raise ValueError("Invalid value for `_class`, must not be `None`")  # noqa: E501
        allowed_values = ["ig", "area"]  # noqa: E501
        if _class not in allowed_values:
            raise ValueError(
                "Invalid value for `_class` ({0}), must be one of {1}"  # noqa: E501
                .format(_class, allowed_values)
            )

        self.__class = _class

    @property
    def data(self):
        """Gets the data of this ScalalastDataDetectors.  # noqa: E501


        :return: The data of this ScalalastDataDetectors.  # noqa: E501
        :rtype: ScalalastDataData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ScalalastDataDetectors.


        :param data: The data of this ScalalastDataDetectors.  # noqa: E501
        :type: ScalalastDataData
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if issubclass(ScalalastDataDetectors, dict):
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
        if not isinstance(other, ScalalastDataDetectors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
