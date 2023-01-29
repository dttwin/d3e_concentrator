# swagger_client.ScalaApi

All URIs are relative to *https://bolzano.fd.cvut.cz:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scala_get_endpoints**](ScalaApi.md#scala_get_endpoints) | **GET** /scala/endpoints | Retrieve intersection and detector ids
[**scala_get_last_data**](ScalaApi.md#scala_get_last_data) | **GET** /scala/lastData | Retrieve last data from SCALA detectors

# **scala_get_endpoints**
> list[InlineResponse200] scala_get_endpoints()

Retrieve intersection and detector ids

No parameters. Returns information about all intersections and their  detectors that are currently hosted by the data store.

### Example
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
api_instance = swagger_client.ScalaApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve intersection and detector ids
    api_response = api_instance.scala_get_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScalaApi->scala_get_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scala_get_last_data**
> list[InlineResponse2002] scala_get_last_data(updated_since, iid=iid)

Retrieve last data from SCALA detectors

Multiple status values can be provided with comma separated strings

### Example
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
api_instance = swagger_client.ScalaApi(swagger_client.ApiClient(configuration))
updated_since = 'updated_since_example' # str | Limit results to the ones updated after (timestamp greater than)
iid = ['[]'] # list[str] | Intersection IDs to retrieve data from (optional) (default to [])

try:
    # Retrieve last data from SCALA detectors
    api_response = api_instance.scala_get_last_data(updated_since, iid=iid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScalaApi->scala_get_last_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_since** | **str**| Limit results to the ones updated after (timestamp greater than) | 
 **iid** | [**list[str]**](str.md)| Intersection IDs to retrieve data from | [optional] [default to []]

### Return type

[**list[InlineResponse2002]**](InlineResponse2002.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

