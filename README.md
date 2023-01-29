# swagger-client
This is a development Swagger-supported server based on the OpenAPI 3.1  specification. You can find out more about Swagger at  [https://swagger.io](https://swagger.io).

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['X-Access-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Access-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CameaApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve detector ids
    api_response = api_instance.camea_get_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CameaApi->camea_get_endpoints: %s\n" % e)

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['X-Access-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Access-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CameaApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve last data from CAMEA detectors
    api_response = api_instance.camea_get_last_data()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CameaApi->camea_get_last_data: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://k611-410h.fd.cvut.cz:8080/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CameaApi* | [**camea_get_endpoints**](docs/CameaApi.md#camea_get_endpoints) | **GET** /camea/endpoints | Retrieve detector ids
*CameaApi* | [**camea_get_last_data**](docs/CameaApi.md#camea_get_last_data) | **GET** /camea/lastData | Retrieve last data from CAMEA detectors
*ScalaApi* | [**scala_get_endpoints**](docs/ScalaApi.md#scala_get_endpoints) | **GET** /scala/endpoints | Retrieve intersection and detector ids
*ScalaApi* | [**scala_get_last_data**](docs/ScalaApi.md#scala_get_last_data) | **GET** /scala/lastData | Retrieve last data from SCALA detectors

## Documentation For Models

 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2001Detector](docs/InlineResponse2001Detector.md)
 - [InlineResponse2001Intersection](docs/InlineResponse2001Intersection.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [ScalalastDataData](docs/ScalalastDataData.md)
 - [ScalalastDataDetectors](docs/ScalalastDataDetectors.md)

## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: X-Access-Token
- **Location**: HTTP header


## Author

d3e@fd.cvut.cz
