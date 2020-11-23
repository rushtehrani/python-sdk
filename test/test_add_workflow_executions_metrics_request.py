# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.16.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import onepanel.core.api
from onepanel.core.api.models.add_workflow_executions_metrics_request import AddWorkflowExecutionsMetricsRequest  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestAddWorkflowExecutionsMetricsRequest(unittest.TestCase):
    """AddWorkflowExecutionsMetricsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddWorkflowExecutionsMetricsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.add_workflow_executions_metrics_request.AddWorkflowExecutionsMetricsRequest()  # noqa: E501
        if include_optional :
            return AddWorkflowExecutionsMetricsRequest(
                namespace = '0', 
                uid = '0', 
                override = True, 
                metrics = [
                    onepanel.core.api.models.metric.Metric(
                        name = '0', 
                        value = 1.337, 
                        format = '0', )
                    ]
            )
        else :
            return AddWorkflowExecutionsMetricsRequest(
        )

    def testAddWorkflowExecutionsMetricsRequest(self):
        """Test AddWorkflowExecutionsMetricsRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
