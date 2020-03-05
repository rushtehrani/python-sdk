# onepanel.core.api
Onepanel Core project API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0-beta1
- Package version: 1.0.0-beta1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/onepanelio/core](https://github.com/onepanelio/core)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install onepanel-core-sdk
```
(you may need to run `pip` with root permission: `sudo pip install onepanel-core-sdk`)

Then import the package:
```python
import onepanel.core.api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import onepanel.core.api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import onepanel.core.api
from onepanel.core.api.rest import ApiException
from pprint import pprint

configuration = onepanel.core.api.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost:8888
configuration.host = "http://localhost:8888"

# Defining host is optional and default to http://localhost:8888
configuration.host = "http://localhost:8888"
# Enter a context with an instance of the API client
with onepanel.core.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onepanel.core.api.NamespaceServiceApi(api_client)
    
    try:
        api_response = api_instance.list_namespaces()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NamespaceServiceApi->list_namespaces: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8888*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*NamespaceServiceApi* | [**list_namespaces**](docs/NamespaceServiceApi.md#list_namespaces) | **GET** /apis/v1beta1/namespaces | 
*SecretServiceApi* | [**add_secret_key_value**](docs/SecretServiceApi.md#add_secret_key_value) | **POST** /apis/v1beta1/{namespace}/secrets/{secret.name} | 
*SecretServiceApi* | [**create_secret**](docs/SecretServiceApi.md#create_secret) | **POST** /apis/v1beta1/{namespace}/secrets | 
*SecretServiceApi* | [**delete_secret**](docs/SecretServiceApi.md#delete_secret) | **DELETE** /apis/v1beta1/{namespace}/secrets/{name} | 
*SecretServiceApi* | [**delete_secret_key**](docs/SecretServiceApi.md#delete_secret_key) | **DELETE** /apis/v1beta1/{namespace}/secrets/{secretName}/keys/{key} | 
*SecretServiceApi* | [**get_secret**](docs/SecretServiceApi.md#get_secret) | **GET** /apis/v1beta1/{namespace}/secrets/{name} | 
*SecretServiceApi* | [**list_secrets**](docs/SecretServiceApi.md#list_secrets) | **GET** /apis/v1beta1/{namespace}/secrets | 
*SecretServiceApi* | [**secret_exists**](docs/SecretServiceApi.md#secret_exists) | **GET** /apis/v1beta1/{namespace}/secrets/{name}/exists | 
*SecretServiceApi* | [**update_secret_key_value**](docs/SecretServiceApi.md#update_secret_key_value) | **PATCH** /apis/v1beta1/{namespace}/secrets/{secret.name} | 
*WorkflowServiceApi* | [**archive_workflow_template**](docs/WorkflowServiceApi.md#archive_workflow_template) | **PUT** /apis/v1beta1/{namespace}/workflow_templates/{uid}/archive | 
*WorkflowServiceApi* | [**create_workflow_execution**](docs/WorkflowServiceApi.md#create_workflow_execution) | **POST** /apis/v1beta1/{namespace}/workflow_executions | 
*WorkflowServiceApi* | [**create_workflow_template**](docs/WorkflowServiceApi.md#create_workflow_template) | **POST** /apis/v1beta1/{namespace}/workflow_templates | 
*WorkflowServiceApi* | [**create_workflow_template_version**](docs/WorkflowServiceApi.md#create_workflow_template_version) | **POST** /apis/v1beta1/{namespace}/workflow_templates/{workflowTemplate.uid}/versions | 
*WorkflowServiceApi* | [**get_artifact**](docs/WorkflowServiceApi.md#get_artifact) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{name}/artifacts/{key} | 
*WorkflowServiceApi* | [**get_workflow_execution**](docs/WorkflowServiceApi.md#get_workflow_execution) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{name} | 
*WorkflowServiceApi* | [**get_workflow_execution_logs**](docs/WorkflowServiceApi.md#get_workflow_execution_logs) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{name}/pods/{podName}/containers/{containerName}/logs | 
*WorkflowServiceApi* | [**get_workflow_execution_metrics**](docs/WorkflowServiceApi.md#get_workflow_execution_metrics) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{name}/pods/{podName}/metrics | 
*WorkflowServiceApi* | [**get_workflow_template**](docs/WorkflowServiceApi.md#get_workflow_template) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid} | 
*WorkflowServiceApi* | [**get_workflow_template2**](docs/WorkflowServiceApi.md#get_workflow_template2) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/versions/{version} | 
*WorkflowServiceApi* | [**list_files**](docs/WorkflowServiceApi.md#list_files) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{name}/files/{path} | 
*WorkflowServiceApi* | [**list_workflow_executions**](docs/WorkflowServiceApi.md#list_workflow_executions) | **GET** /apis/v1beta1/{namespace}/workflow_executions | 
*WorkflowServiceApi* | [**list_workflow_template_versions**](docs/WorkflowServiceApi.md#list_workflow_template_versions) | **GET** /apis/v1beta1/{namespace}/workflow_templates/{uid}/versions | 
*WorkflowServiceApi* | [**list_workflow_templates**](docs/WorkflowServiceApi.md#list_workflow_templates) | **GET** /apis/v1beta1/{namespace}/workflow_templates | 
*WorkflowServiceApi* | [**resubmit_workflow_execution**](docs/WorkflowServiceApi.md#resubmit_workflow_execution) | **PUT** /apis/v1beta1/{namespace}/workflow_executions/{name}/resubmit | 
*WorkflowServiceApi* | [**terminate_workflow_execution**](docs/WorkflowServiceApi.md#terminate_workflow_execution) | **PUT** /apis/v1beta1/{namespace}/workflow_executions/{name}/terminate | 
*WorkflowServiceApi* | [**update_workflow_template_version**](docs/WorkflowServiceApi.md#update_workflow_template_version) | **PUT** /apis/v1beta1/{namespace}/workflow_templates/{workflowTemplate.uid}/versions/{workflowTemplate.version} | 
*WorkflowServiceApi* | [**watch_workflow_execution**](docs/WorkflowServiceApi.md#watch_workflow_execution) | **GET** /apis/v1beta1/{namespace}/workflow_executions/{name}/watch | 


## Documentation For Models

 - [AddSecretKeyValueResponse](docs/AddSecretKeyValueResponse.md)
 - [ArchiveWorkflowTemplateResponse](docs/ArchiveWorkflowTemplateResponse.md)
 - [ArtifactResponse](docs/ArtifactResponse.md)
 - [DeleteSecretKeyResponse](docs/DeleteSecretKeyResponse.md)
 - [DeleteSecretResponse](docs/DeleteSecretResponse.md)
 - [File](docs/File.md)
 - [GetWorkflowExecutionMetricsResponse](docs/GetWorkflowExecutionMetricsResponse.md)
 - [GoogleProtobufAny](docs/GoogleProtobufAny.md)
 - [GrpcGatewayRuntimeError](docs/GrpcGatewayRuntimeError.md)
 - [GrpcGatewayRuntimeStreamError](docs/GrpcGatewayRuntimeStreamError.md)
 - [ListFilesResponse](docs/ListFilesResponse.md)
 - [ListNamespacesResponse](docs/ListNamespacesResponse.md)
 - [ListSecretsResponse](docs/ListSecretsResponse.md)
 - [ListWorkflowExecutionsResponse](docs/ListWorkflowExecutionsResponse.md)
 - [ListWorkflowTemplateVersionsResponse](docs/ListWorkflowTemplateVersionsResponse.md)
 - [ListWorkflowTemplatesResponse](docs/ListWorkflowTemplatesResponse.md)
 - [LogEntry](docs/LogEntry.md)
 - [Metric](docs/Metric.md)
 - [Namespace](docs/Namespace.md)
 - [Secret](docs/Secret.md)
 - [SecretExistsResponse](docs/SecretExistsResponse.md)
 - [StreamResultOfLogEntry](docs/StreamResultOfLogEntry.md)
 - [StreamResultOfWorkflowExecution](docs/StreamResultOfWorkflowExecution.md)
 - [UpdateSecretKeyValueResponse](docs/UpdateSecretKeyValueResponse.md)
 - [WorkflowExecution](docs/WorkflowExecution.md)
 - [WorkflowExecutionParameter](docs/WorkflowExecutionParameter.md)
 - [WorkflowTemplate](docs/WorkflowTemplate.md)


## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: authorization
- **Location**: HTTP header


## Author




