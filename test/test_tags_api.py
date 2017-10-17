# coding: utf-8

"""
    Fanlens API

     Fanlens API to handle \"activities\". Predictions are performed automatically and can be managed here ## Concepts The API consists of 4 main concepts: sources, activities and tags (bundled in tagsets) and models used for predictions. * An activity is a text based action performed by a user, e.g. a Facebook Comment or a Tweet. * A source is the originator of these activities and is used for importing. Currently Facebook, Twitter, and Generic Sources are supported. * A tag is a piece of meta information that is used to build specialized speech models, e.g. \"positive\", or \"negative\". They are bundled in tagsets for convenience, e.g. \"Emotion\".

    OpenAPI spec version: 4.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.tags_api import TagsApi


class TestTagsApi(unittest.TestCase):
    """ TagsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.tags_api.TagsApi()

    def tearDown(self):
        pass

    def test_tags_get(self):
        """
        Test case for tags_get

        Get all tags of current user
        """
        pass

    def test_tags_tag_delete(self):
        """
        Test case for tags_tag_delete

        Remove tag and all it's associations from the system
        """
        pass

    def test_tags_tag_get(self):
        """
        Test case for tags_tag_get

        Get this tag
        """
        pass

    def test_tags_tag_put(self):
        """
        Test case for tags_tag_put

        Add tag to the system
        """
        pass


if __name__ == '__main__':
    unittest.main()