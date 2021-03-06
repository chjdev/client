# coding: utf-8

"""
    Fanlens API

     Fanlens API to handle \"activities\". Predictions are performed automatically and can be managed here ## Concepts The API consists of 4 main concepts: sources, activities and tags (bundled in tagsets) and models used for predictions. * An activity is a text based action performed by a user, e.g. a Facebook Comment or a Tweet. * A source is the originator of these activities and is used for importing. Currently Facebook, Twitter, and Generic Sources are supported. * A tag is a piece of meta information that is used to build specialized speech models, e.g. \"positive\", or \"negative\". They are bundled in tagsets for convenience, e.g. \"Emotion\".

    OpenAPI spec version: 4.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class SourcesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def sources_get(self, **kwargs):
        """
        Get sources of current user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sources_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: SourcesList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.sources_get_with_http_info(**kwargs)
        else:
            (data) = self.sources_get_with_http_info(**kwargs)
            return data

    def sources_get_with_http_info(self, **kwargs):
        """
        Get sources of current user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sources_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: SourcesList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sources_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/sources/', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SourcesList',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def sources_post(self, source, **kwargs):
        """
        Create a new Source
        Currently supported types: facebook, twitter, generic
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sources_post(source, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Source source: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.sources_post_with_http_info(source, **kwargs)
        else:
            (data) = self.sources_post_with_http_info(source, **kwargs)
            return data

    def sources_post_with_http_info(self, source, **kwargs):
        """
        Create a new Source
        Currently supported types: facebook, twitter, generic
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sources_post_with_http_info(source, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Source source: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sources_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source' is set
        if ('source' not in params) or (params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `sources_post`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'source' in params:
            body_params = params['source']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/sources/', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def sources_source_id_delete(self, source_id, **kwargs):
        """
        Remove the source, **WARNING!** This will remove all data associated with the source!
        **WARNING!** This will remove all data associated with the source!
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sources_source_id_delete(source_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int source_id: (required)
        :return: Ok
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.sources_source_id_delete_with_http_info(source_id, **kwargs)
        else:
            (data) = self.sources_source_id_delete_with_http_info(source_id, **kwargs)
            return data

    def sources_source_id_delete_with_http_info(self, source_id, **kwargs):
        """
        Remove the source, **WARNING!** This will remove all data associated with the source!
        **WARNING!** This will remove all data associated with the source!
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sources_source_id_delete_with_http_info(source_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int source_id: (required)
        :return: Ok
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sources_source_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params) or (params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `sources_source_id_delete`")


        collection_formats = {}

        path_params = {}
        if 'source_id' in params:
            path_params['source_id'] = params['source_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/sources/{source_id}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Ok',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def sources_source_id_get(self, source_id, **kwargs):
        """
        Get source
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sources_source_id_get(source_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int source_id: (required)
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.sources_source_id_get_with_http_info(source_id, **kwargs)
        else:
            (data) = self.sources_source_id_get_with_http_info(source_id, **kwargs)
            return data

    def sources_source_id_get_with_http_info(self, source_id, **kwargs):
        """
        Get source
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sources_source_id_get_with_http_info(source_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int source_id: (required)
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sources_source_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params) or (params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `sources_source_id_get`")


        collection_formats = {}

        path_params = {}
        if 'source_id' in params:
            path_params['source_id'] = params['source_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/sources/{source_id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Source',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def sources_source_id_patch(self, source_id, source, **kwargs):
        """
        Update the source.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sources_source_id_patch(source_id, source, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int source_id: (required)
        :param Source source: Fields can be a subset of a full source. Will update only the specified fields. (required)
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.sources_source_id_patch_with_http_info(source_id, source, **kwargs)
        else:
            (data) = self.sources_source_id_patch_with_http_info(source_id, source, **kwargs)
            return data

    def sources_source_id_patch_with_http_info(self, source_id, source, **kwargs):
        """
        Update the source.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sources_source_id_patch_with_http_info(source_id, source, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int source_id: (required)
        :param Source source: Fields can be a subset of a full source. Will update only the specified fields. (required)
        :return: Source
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source_id', 'source']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sources_source_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_id' is set
        if ('source_id' not in params) or (params['source_id'] is None):
            raise ValueError("Missing the required parameter `source_id` when calling `sources_source_id_patch`")
        # verify the required parameter 'source' is set
        if ('source' not in params) or (params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `sources_source_id_patch`")


        collection_formats = {}

        path_params = {}
        if 'source_id' in params:
            path_params['source_id'] = params['source_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'source' in params:
            body_params = params['source']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['jwt']

        return self.api_client.call_api('/sources/{source_id}', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Source',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
