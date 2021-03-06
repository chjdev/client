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


class TextPredictionQuery(object):
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
        'text': 'str',
        'model_query': 'ModelQuery'
    }

    attribute_map = {
        'text': 'text',
        'model_query': 'model_query'
    }

    def __init__(self, text=None, model_query=None):
        """
        TextPredictionQuery - a model defined in Swagger
        """

        self._text = None
        self._model_query = None

        self.text = text
        if model_query is not None:
          self.model_query = model_query

    @property
    def text(self):
        """
        Gets the text of this TextPredictionQuery.
        The text to fetch prediction for. English only atm.

        :return: The text of this TextPredictionQuery.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this TextPredictionQuery.
        The text to fetch prediction for. English only atm.

        :param text: The text of this TextPredictionQuery.
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")
        if text is not None and len(text) > 7000:
            raise ValueError("Invalid value for `text`, length must be less than or equal to `7000`")
        if text is not None and len(text) < 24:
            raise ValueError("Invalid value for `text`, length must be greater than or equal to `24`")

        self._text = text

    @property
    def model_query(self):
        """
        Gets the model_query of this TextPredictionQuery.

        :return: The model_query of this TextPredictionQuery.
        :rtype: ModelQuery
        """
        return self._model_query

    @model_query.setter
    def model_query(self, model_query):
        """
        Sets the model_query of this TextPredictionQuery.

        :param model_query: The model_query of this TextPredictionQuery.
        :type: ModelQuery
        """

        self._model_query = model_query

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
        if not isinstance(other, TextPredictionQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
