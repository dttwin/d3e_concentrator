# swagger_client.CameaApi

All URIs are relative to *https://bolzano.fd.cvut.cz:8080/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**camea_get_endpoints**](CameaApi.md#camea_get_endpoints) | **GET** /camea/endpoints | Retrieve detector ids
[**camea_get_last_data**](CameaApi.md#camea_get_last_data) | **GET** /camea/lastData | Retrieve last data from CAMEA detectors

# **camea_get_endpoints**
> list[InlineResponse2003] camea_get_endpoints()

Retrieve detector ids

No parameters. Returns information about all Camea detectors that are  actually stored in our data store.

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
api_instance = swagger_client.CameaApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve detector ids
    api_response = api_instance.camea_get_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CameaApi->camea_get_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2003]**](InlineResponse2003.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **camea_get_last_data**
> list[InlineResponse2003] camea_get_last_data()

Retrieve last data from CAMEA detectors

Returns data received since the given timestamp for the given set  of detector names (or data of all available detectors).

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
api_instance = swagger_client.CameaApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve last data from CAMEA detectors
    api_response = api_instance.camea_get_last_data()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CameaApi->camea_get_last_data: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse2003]**](InlineResponse2003.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

