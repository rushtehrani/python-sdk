# coding: utf-8

"""
    namespace.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import core.api
from core.api.api.namespace_service_api import NamespaceServiceApi  # noqa: E501
from core.api.rest import ApiException


class TestNamespaceServiceApi(unittest.TestCase):
    """NamespaceServiceApi unit test stubs"""

    def setUp(self):
        self.api = core.api.api.namespace_service_api.NamespaceServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_namespaces(self):
        """Test case for list_namespaces

        """
        pass


if __name__ == '__main__':
    unittest.main()
