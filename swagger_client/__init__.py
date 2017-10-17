# coding: utf-8

"""
    Fanlens API

     Fanlens API to handle \"activities\". Predictions are performed automatically and can be managed here ## Concepts The API consists of 4 main concepts: sources, activities and tags (bundled in tagsets) and models used for predictions. * An activity is a text based action performed by a user, e.g. a Facebook Comment or a Tweet. * A source is the originator of these activities and is used for importing. Currently Facebook, Twitter, and Generic Sources are supported. * A tag is a piece of meta information that is used to build specialized speech models, e.g. \"positive\", or \"negative\". They are bundled in tagsets for convenience, e.g. \"Emotion\".

    OpenAPI spec version: 4.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.activity import Activity
from .models.activity_list import ActivityList
from .models.error import Error
from .models.import_list import ImportList
from .models.job import Job
from .models.model import Model
from .models.model_import import ModelImport
from .models.model_list import ModelList
from .models.model_query import ModelQuery
from .models.model_train_job import ModelTrainJob
from .models.ok import Ok
from .models.prediction import Prediction
from .models.single_tag_info import SingleTagInfo
from .models.source import Source
from .models.sources_list import SourcesList
from .models.tag import Tag
from .models.tag_change_set import TagChangeSet
from .models.tag_counts import TagCounts
from .models.tag_info import TagInfo
from .models.tag_set import TagSet
from .models.tag_set_list import TagSetList
from .models.tags import Tags
from .models.text_prediction import TextPrediction
from .models.text_prediction_query import TextPredictionQuery
from .models.user import User

# import apis into sdk package
from .apis.activity_api import ActivityApi
from .apis.import_api import ImportApi
from .apis.model_api import ModelApi
from .apis.sources_api import SourcesApi
from .apis.tags_api import TagsApi
from .apis.tagsets_api import TagsetsApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()