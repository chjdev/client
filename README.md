# swagger-client
 Fanlens API to handle \"activities\". Predictions are performed automatically and can be managed here ## Concepts The API consists of 4 main concepts: sources, activities and tags (bundled in tagsets) and models used for predictions. * An activity is a text based action performed by a user, e.g. a Facebook Comment or a Tweet. * A source is the originator of these activities and is used for importing. Currently Facebook, Twitter, and Generic Sources are supported. * A tag is a piece of meta information that is used to build specialized speech models, e.g. \"positive\", or \"negative\". They are bundled in tagsets for convenience, e.g. \"Emotion\".

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 4.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7+ 3.4+

Test-Requirements:

Python 3.6+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import client
from client.rest import ApiException
from pprint import pprint

# Configure API key authorization: jwt
client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# client.configuration.api_key_prefix['Authorization'] = 'Bearer'
# create an instance of the API class
api_instance = client.ActivityApi()
source_ids = [56] # list[int] |  (optional)
tagset_ids = [56] # list[int] |  (optional)
tags = ['tags_example'] # list[str] |  (optional)
languages = ['en'] # list[str] | Inferred language of text (optional) (default to en)
count = 8 # int | number of activities to fetch (optional) (default to 8)
max_id = 'max_id_example' # str | used for cursoring (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | DateTime of oldest entry (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | DateTime of newest entry (optional)
random = false # bool | should a random sample be drawn (optional) (default to false)

try:
    # Get a list of activities.
    api_response = api_instance.root_get(source_ids=source_ids, tagset_ids=tagset_ids, tags=tags, languages=languages, count=count, max_id=max_id, since=since, until=until, random=random)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->root_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost/v4*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ActivityApi* | [**root_get**](docs/ActivityApi.md#root_get) | **GET** / | Get a list of activities.
*ActivityApi* | [**source_id_activity_id_delete**](docs/ActivityApi.md#source_id_activity_id_delete) | **DELETE** /{source_id}/{activity_id} | Delete this activity
*ActivityApi* | [**source_id_activity_id_get**](docs/ActivityApi.md#source_id_activity_id_get) | **GET** /{source_id}/{activity_id} | Get this activity
*ActivityApi* | [**source_id_activity_id_put**](docs/ActivityApi.md#source_id_activity_id_put) | **PUT** /{source_id}/{activity_id} | Create or update this activity
*ActivityApi* | [**source_id_activity_id_tags_patch**](docs/ActivityApi.md#source_id_activity_id_tags_patch) | **PATCH** /{source_id}/{activity_id}/tags | Modify tags of activity
*ImportApi* | [**root_post**](docs/ImportApi.md#root_post) | **POST** / | Import a bulk of activities
*ImportApi* | [**source_id_activity_id_delete**](docs/ImportApi.md#source_id_activity_id_delete) | **DELETE** /{source_id}/{activity_id} | Delete this activity
*ImportApi* | [**source_id_activity_id_put**](docs/ImportApi.md#source_id_activity_id_put) | **PUT** /{source_id}/{activity_id} | Create or update this activity
*ModelApi* | [**model_get**](docs/ModelApi.md#model_get) | **GET** /model/ | Get all models of user
*ModelApi* | [**model_model_id_get**](docs/ModelApi.md#model_model_id_get) | **GET** /model/{model_id} | Get meta information about a trained model
*ModelApi* | [**model_prediction_post**](docs/ModelApi.md#model_prediction_post) | **POST** /model/prediction | Get prediction for a provided text based on the best model for source/tagset
*ModelApi* | [**model_search_post**](docs/ModelApi.md#model_search_post) | **POST** /model/search | Get meta information about a trained model
*ModelApi* | [**model_train_post**](docs/ModelApi.md#model_train_post) | **POST** /model/train | Train a new model for a tagset
*SourcesApi* | [**sources_get**](docs/SourcesApi.md#sources_get) | **GET** /sources/ | Get sources of current user
*SourcesApi* | [**sources_post**](docs/SourcesApi.md#sources_post) | **POST** /sources/ | Create a new Source
*SourcesApi* | [**sources_source_id_delete**](docs/SourcesApi.md#sources_source_id_delete) | **DELETE** /sources/{source_id} | Remove the source, **WARNING!** This will remove all data associated with the source!
*SourcesApi* | [**sources_source_id_get**](docs/SourcesApi.md#sources_source_id_get) | **GET** /sources/{source_id} | Get source
*SourcesApi* | [**sources_source_id_patch**](docs/SourcesApi.md#sources_source_id_patch) | **PATCH** /sources/{source_id} | Update the source.
*TagsApi* | [**tags_get**](docs/TagsApi.md#tags_get) | **GET** /tags/ | Get all tags of current user
*TagsApi* | [**tags_tag_delete**](docs/TagsApi.md#tags_tag_delete) | **DELETE** /tags/{tag} | Remove tag and all it&#39;s associations from the system
*TagsApi* | [**tags_tag_get**](docs/TagsApi.md#tags_tag_get) | **GET** /tags/{tag} | Get this tag
*TagsApi* | [**tags_tag_put**](docs/TagsApi.md#tags_tag_put) | **PUT** /tags/{tag} | Add tag to the system
*TagsetsApi* | [**tagsets_get**](docs/TagsetsApi.md#tagsets_get) | **GET** /tagsets/ | Get tagsets of current user
*TagsetsApi* | [**tagsets_post**](docs/TagsetsApi.md#tagsets_post) | **POST** /tagsets/ | Create new tagset
*TagsetsApi* | [**tagsets_tagset_id_delete**](docs/TagsetsApi.md#tagsets_tagset_id_delete) | **DELETE** /tagsets/{tagset_id} | Remove the tagset
*TagsetsApi* | [**tagsets_tagset_id_get**](docs/TagsetsApi.md#tagsets_tagset_id_get) | **GET** /tagsets/{tagset_id} | Get tagset
*TagsetsApi* | [**tagsets_tagset_id_patch**](docs/TagsetsApi.md#tagsets_tagset_id_patch) | **PATCH** /tagsets/{tagset_id} | Update the tagset
*TagsetsApi* | [**tagsets_tagset_id_tag_delete**](docs/TagsetsApi.md#tagsets_tagset_id_tag_delete) | **DELETE** /tagsets/{tagset_id}/{tag} | Remove tag from tagset
*TagsetsApi* | [**tagsets_tagset_id_tag_put**](docs/TagsetsApi.md#tagsets_tagset_id_tag_put) | **PUT** /tagsets/{tagset_id}/{tag} | Add tag to the tagset


## Documentation For Models

 - [Activity](docs/Activity.md)
 - [ActivityList](docs/ActivityList.md)
 - [Error](docs/Error.md)
 - [ImportList](docs/ImportList.md)
 - [Job](docs/Job.md)
 - [Model](docs/Model.md)
 - [ModelImport](docs/ModelImport.md)
 - [ModelList](docs/ModelList.md)
 - [ModelQuery](docs/ModelQuery.md)
 - [ModelTrainJob](docs/ModelTrainJob.md)
 - [Ok](docs/Ok.md)
 - [Prediction](docs/Prediction.md)
 - [SingleTagInfo](docs/SingleTagInfo.md)
 - [Source](docs/Source.md)
 - [SourcesList](docs/SourcesList.md)
 - [Tag](docs/Tag.md)
 - [TagChangeSet](docs/TagChangeSet.md)
 - [TagCounts](docs/TagCounts.md)
 - [TagInfo](docs/TagInfo.md)
 - [TagSet](docs/TagSet.md)
 - [TagSetList](docs/TagSetList.md)
 - [Tags](docs/Tags.md)
 - [TextPrediction](docs/TextPrediction.md)
 - [TextPredictionQuery](docs/TextPredictionQuery.md)
 - [User](docs/User.md)


## Documentation For Authorization


## jwt

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



