# swagger_client.GolemioApi

All URIs are relative to *https://bolzano.fd.cvut.cz:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**golemio_get_last_data**](GolemioApi.md#golemio_get_last_data) | **GET** /golemio/lastData | Get last data uploaded from the Golemio platform
[**golemio_get_lines**](GolemioApi.md#golemio_get_lines) | **GET** /golemio/lines | Retrieve list of public transport lines covered by golemio

# **golemio_get_last_data**
> list[InlineResponse2004] golemio_get_last_data(updated_since, lineid=lineid)

Get last data uploaded from the Golemio platform

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
api_instance = swagger_client.GolemioApi(swagger_client.ApiClient(configuration))
updated_since = 'updated_since_example' # str | Limit results to the ones updated after (timestamp greater than)
lineid = ['[]'] # list[str] | Line IDs (PT schedule numbers) to retrieve data from (optional) (default to [])

try:
    # Get last data uploaded from the Golemio platform
    api_response = api_instance.golemio_get_last_data(updated_since, lineid=lineid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GolemioApi->golemio_get_last_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_since** | **str**| Limit results to the ones updated after (timestamp greater than) | 
 **lineid** | [**list[str]**](str.md)| Line IDs (PT schedule numbers) to retrieve data from | [optional] [default to []]

### Return type

[**list[InlineResponse2004]**](InlineResponse2004.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **golemio_get_lines**
> list[str] golemio_get_lines()

Retrieve list of public transport lines covered by golemio

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
api_instance = swagger_client.GolemioApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve list of public transport lines covered by golemio
    api_response = api_instance.golemio_get_lines()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GolemioApi->golemio_get_lines: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

