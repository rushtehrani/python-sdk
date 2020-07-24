# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.12.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import onepanel.core.api
from onepanel.core.api.models.statistics import Statistics  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestStatistics(unittest.TestCase):
    """Statistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Statistics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.statistics.Statistics()  # noqa: E501
        if include_optional :
            return Statistics(
                workflow_status = '0', 
                workflow_template_id = '0'
            )
        else :
            return Statistics(
        )

    def testStatistics(self):
        """Test Statistics"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
