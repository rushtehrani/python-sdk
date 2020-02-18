# coding: utf-8

"""
    namespace.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import core.api
from core.api.models.workflow_template import WorkflowTemplate  # noqa: E501
from core.api.rest import ApiException

class TestWorkflowTemplate(unittest.TestCase):
    """WorkflowTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WorkflowTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = core.api.models.workflow_template.WorkflowTemplate()  # noqa: E501
        if include_optional :
            return WorkflowTemplate(
                created_at = '0', 
                uid = '0', 
                name = '0', 
                version = 56, 
                manifest = '0', 
                is_latest = True, 
                is_archived = True
            )
        else :
            return WorkflowTemplate(
        )

    def testWorkflowTemplate(self):
        """Test WorkflowTemplate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
