# coding: utf-8

"""
    Fanlens API

     Fanlens API to handle \"activities\". Predictions are performed automatically and can be managed here ## Concepts The API consists of 4 main concepts: sources, activities and tags (bundled in tagsets) and models used for predictions. * An activity is a text based action performed by a user, e.g. a Facebook Comment or a Tweet. * A source is the originator of these activities and is used for importing. Currently Facebook, Twitter, and Generic Sources are supported. * A tag is a piece of meta information that is used to build specialized speech models, e.g. \"positive\", or \"negative\". They are bundled in tagsets for convenience, e.g. \"Emotion\".

    OpenAPI spec version: 4.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TagChangeSet(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'add': 'Tags',
        'remove': 'Tags'
    }

    attribute_map = {
        'add': 'add',
        'remove': 'remove'
    }

    def __init__(self, add=None, remove=None):
        """
        TagChangeSet - a model defined in Swagger
        """

        self._add = None
        self._remove = None

        if add is not None:
          self.add = add
        if remove is not None:
          self.remove = remove

    @property
    def add(self):
        """
        Gets the add of this TagChangeSet.

        :return: The add of this TagChangeSet.
        :rtype: Tags
        """
        return self._add

    @add.setter
    def add(self, add):
        """
        Sets the add of this TagChangeSet.

        :param add: The add of this TagChangeSet.
        :type: Tags
        """

        self._add = add

    @property
    def remove(self):
        """
        Gets the remove of this TagChangeSet.

        :return: The remove of this TagChangeSet.
        :rtype: Tags
        """
        return self._remove

    @remove.setter
    def remove(self, remove):
        """
        Sets the remove of this TagChangeSet.

        :param remove: The remove of this TagChangeSet.
        :type: Tags
        """

        self._remove = remove

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TagChangeSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other