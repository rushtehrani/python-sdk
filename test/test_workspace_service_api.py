# coding: utf-8

"""
    Onepanel Core

    Onepanel Core project API  # noqa: E501

    The version of the OpenAPI document: 1.0.0-beta1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import onepanel.core.api
from onepanel.core.api.api.workspace_service_api import WorkspaceServiceApi  # noqa: E501
from onepanel.core.api.rest import ApiException


class TestWorkspaceServiceApi(unittest.TestCase):
    """WorkspaceServiceApi unit test stubs"""

    def setUp(self):
        self.api = onepanel.core.api.api.workspace_service_api.WorkspaceServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_workspace_service_create_workspace(self):
        """Test case for workspace_service_create_workspace

        """
        pass

    def test_workspace_service_update_workspace_status(self):
        """Test case for workspace_service_update_workspace_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
