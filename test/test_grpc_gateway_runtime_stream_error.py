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
from onepanel.core.api.models.grpc_gateway_runtime_stream_error import GrpcGatewayRuntimeStreamError  # noqa: E501
from onepanel.core.api.rest import ApiException

class TestGrpcGatewayRuntimeStreamError(unittest.TestCase):
    """GrpcGatewayRuntimeStreamError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GrpcGatewayRuntimeStreamError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = onepanel.core.api.models.grpc_gateway_runtime_stream_error.GrpcGatewayRuntimeStreamError()  # noqa: E501
        if include_optional :
            return GrpcGatewayRuntimeStreamError(
                grpc_code = 56, 
                http_code = 56, 
                message = '0', 
                http_status = '0', 
                details = [
                    onepanel.core.api.models.google/protobuf/any.google.protobuf.Any(
                        type_url = '0', 
                        value = 'YQ==', )
                    ]
            )
        else :
            return GrpcGatewayRuntimeStreamError(
        )

    def testGrpcGatewayRuntimeStreamError(self):
        """Test GrpcGatewayRuntimeStreamError"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
