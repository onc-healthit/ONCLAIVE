# Code Testability Analysis for Plan Net

## Generated on: 2025-03-19 12:01:36

TEST PLANS:

# REQ-PRIV-001
1. **Is this requirement algorithmically verifiable?** Yes
2. **What FHIR API calls/operations would be needed to test it?** GET request to the Plan-Net service
3. **What assertions/validations would verify conformance?** Assert that the response status code is 200 (OK) and that no authentication headers were sent in the request
4. **What test data prerequisites are needed?** None
5. **Pseudocode:**
```
send GET request to Plan-Net service
assert response status code is 200
assert no authentication headers were sent
```

# REQ-PRIV-002
1. **Is this requirement algorithmically verifiable?** Yes
2. **What FHIR API calls/operations would be needed to test it?** GET request to the Plan-Net service
3. **What assertions/validations would verify conformance?** Assert that the response status code is 200 (OK) and that no consumer identifying information was sent in the request
4. **What test data prerequisites are needed?** None
5. **Pseudocode:**
```
send GET request to Plan-Net service
assert response status code is 200
assert no consumer identifying information was sent
```

# REQ-PRIV-003
1. **Is this requirement algorithmically verifiable?** Partially. We can verify that the client does not send consumer identifiable information, but we cannot verify that the client will never send such information.
2. **What FHIR API calls/operations would be needed to test it?** GET request from the directory mobile application to the Plan-Net service
3. **What assertions/validations would verify conformance?** Assert that no consumer identifiable information was sent in the request
4. **What test data prerequisites are needed?** None
5. **Pseudocode:**
```
send GET request from directory mobile application to Plan-Net service
assert no consumer identifiable information was sent
```

# REQ-DATA-001
1. **Is this requirement algorithmically verifiable?** Yes
2. **What FHIR API calls/operations would be needed to test it?** GET request to the Health Plan API
3. **What assertions/validations would verify conformance?** Assert that all Must Support data elements are present in the response, and that missing data elements are handled as specified
4. **What test data prerequisites are needed?** A list of Must Support data elements
5. **Pseudocode:**
```
send GET request to Health Plan API
for each Must Support data element:
    if element is present in response:
        continue
    else if minimum cardinality is 0:
        assert element is not included in response
    else:
        assert reason for missing information is sent
```

# REQ-APP-001
1. **Is this requirement algorithmically verifiable?** Partially. We can verify that the application does not error when processing Must Support data elements, but we cannot verify that it correctly interprets missing data elements or displays/stores the data elements appropriately.
2. **What FHIR API calls/operations would be needed to test it?** GET request to the application
3. **What assertions/validations would verify conformance?** Assert that the application does not error when processing Must Support data elements
4. **What test data prerequisites are needed?** A list of Must Support data elements
5. **Pseudocode:**
```
send GET request to application
for each Must Support data element:
    if element is present in response:
        continue
    else:
        assert application does not error
```

TEST PLAN:

# REQ-CONS-001
1. **Is this requirement algorithmically verifiable?** Yes
2. **FHIR API calls/operations**: GET
3. **Assertions/validations**: The consumer app should not crash or throw an error when a Must Support element is missing. It should handle the missing data gracefully.
4. **Test data prerequisites**: Resource instances with missing Must Support data elements.
5. **Pseudocode**:
```
FOR each resource instance with missing Must Support data elements
    GET resource instance
    ASSERT that the consumer app does not crash or throw an error
ENDFOR
```

# REQ-DATA-002
1. **Is this requirement algorithmically verifiable?** Yes
2. **FHIR API calls/operations**: GET
3. **Assertions/validations**: The lastUpdate timestamp should be present in the profile's data content.
4. **Test data prerequisites**: Profiles
5. **Pseudocode**:
```
FOR each profile
    GET profile
    ASSERT that lastUpdate timestamp is present in the profile's data content
ENDFOR
```

# REQ-SERV-001
1. **Is this requirement algorithmically verifiable?** Yes
2. **FHIR API calls/operations**: GET
3. **Assertions/validations**: The server should support all profiles defined in the Implementation Guide.
4. **Test data prerequisites**: Profiles defined in the Implementation Guide
5. **Pseudocode**:
```
FOR each profile defined in the Implementation Guide
    GET profile from server
    ASSERT that the server returns the profile without error
ENDFOR
```

# REQ-SERV-002
1. **Is this requirement algorithmically verifiable?** Yes
2. **FHIR API calls/operations**: GET, POST, PUT, DELETE
3. **Assertions/validations**: The server should correctly implement the RESTful behavior according to the FHIR specification.
4. **Test data prerequisites**: Various resources to test the different RESTful operations
5. **Pseudocode**:
```
FOR each RESTful operation (GET, POST, PUT, DELETE)
    Perform operation on a resource
    ASSERT that the server responds correctly according to the FHIR specification
ENDFOR
```

# REQ-SERV-003
1. **Is this requirement algorithmically verifiable?** Yes
2. **FHIR API calls/operations**: Various operations that would trigger the specified HTTP error responses
3. **Assertions/validations**: The server should return the correct HTTP error response for each situation.
4. **Test data prerequisites**: Various operations that would trigger the specified HTTP error responses
5. **Pseudocode**:
```
FOR each operation that should trigger a specific HTTP error response
    Perform operation
    ASSERT that the server returns the correct HTTP error response
ENDFOR
```

# Test Plan

## REQ-SERV-004
1. This requirement is algorithmically verifiable.
2. FHIR API calls/operations needed: Any Plan-Net interaction API call, such as GET, POST, PUT, DELETE.
3. Assertions/validations: The server should be able to process requests and respond in both JSON and XML formats.
4. Test data prerequisites: Test data in both JSON and XML formats.
5. Pseudocode:
```
For each API operation:
    Send request in JSON format
    Assert that the response is successful and in JSON format
    Send request in XML format
    Assert that the response is successful and in XML format
```

## REQ-SERV-005
1. This requirement is algorithmically verifiable.
2. FHIR API calls/operations needed: GET meta.profile attribute for each instance.
3. Assertions/validations: The server should return the supported Plan-Net profiles in the meta.profile attribute.
4. Test data prerequisites: None.
5. Pseudocode:
```
For each instance:
    Send GET request for meta.profile attribute
    Assert that the response includes the supported Plan-Net profiles
```

## REQ-SERV-006
1. This requirement is algorithmically verifiable.
2. FHIR API calls/operations needed: GET with searchParameters for each profile.
3. Assertions/validations: The server should return the correct results when searchParameters are used individually and in combination.
4. Test data prerequisites: Test data that can be searched using the searchParameters.
5. Pseudocode:
```
For each profile:
    For each searchParameter:
        Send GET request with searchParameter
        Assert that the response includes the correct results
    Send GET request with all searchParameters combined
    Assert that the response includes the correct results
```

## REQ-SERV-007
1. This requirement is algorithmically verifiable.
2. FHIR API calls/operations needed: GET with search parameters that specify the 'chain' property.
3. Assertions/validations: The server should return the correct results when forward and reverse chaining is used.
4. Test data prerequisites: Test data that can be searched using the 'chain' property.
5. Pseudocode:
```
For each search parameter that specifies the 'chain' property:
    Send GET request with forward chaining
    Assert that the response includes the correct results
    Send GET request with reverse chaining
    Assert that the response includes the correct results
```

## REQ-SERV-008
1. This requirement is algorithmically verifiable.
2. FHIR API calls/operations needed: Any API call with unauthorized access.
3. Assertions/validations: The server should return an HTTP 401 unauthorized response code.
4. Test data prerequisites: None.
5. Pseudocode:
```
Send unauthorized API request
Assert that the response code is 401
```

TEST PLAN:

**REQ-ENDP-001**
1. This requirement is algorithmically verifiable.
2. FHIR API calls needed: GET [base]/Endpoint
3. Assertions: The server responds with a 200 status code and the response body contains an Endpoint resource that conforms to the Plan-Net Endpoint profile.
4. Test data prerequisites: An Endpoint resource conforming to the Plan-Net profile.
5. Pseudocode:
```
// Send a GET request to the server
response = GET([base]/Endpoint)

// Assert that the response status code is 200
assert(response.status == 200)

// Assert that the response body contains an Endpoint resource
assert(response.body.resourceType == 'Endpoint')

// Assert that the Endpoint resource conforms to the Plan-Net profile
assert(response.body.conformsTo('Plan-Net'))
```

**REQ-ENDP-002**
1. This requirement is algorithmically verifiable.
2. FHIR API calls needed: GET [base]/Endpoint/[id] and GET [base]/Endpoint/[id]/_history/vid
3. Assertions: The server responds with a 200 status code and the response body contains the requested Endpoint resource.
4. Test data prerequisites: An Endpoint resource with a known ID and version.
5. Pseudocode:
```
// Send a GET request to the server
response = GET([base]/Endpoint/[id])

// Assert that the response status code is 200
assert(response.status == 200)

// Assert that the response body contains the requested Endpoint resource
assert(response.body.id == [id])

// Send a GET request to the server for a specific version
response = GET([base]/Endpoint/[id]/_history/vid)

// Assert that the response status code is 200
assert(response.status == 200)

// Assert that the response body contains the requested Endpoint resource version
assert(response.body.versionId == vid)
```

**REQ-ENDP-003**
1. This requirement is algorithmically verifiable.
2. FHIR API calls needed: GET [base]/Endpoint?[parameter=value]&_include=Endpoint:organization
3. Assertions: The server responds with a 200 status code and the response body contains the Endpoint resource and the associated Organization resource.
4. Test data prerequisites: An Endpoint resource with an associated Organization resource.
5. Pseudocode:
```
// Send a GET request to the server
response = GET([base]/Endpoint?[parameter=value]&_include=Endpoint:organization)

// Assert that the response status code is 200
assert(response.status == 200)

// Assert that the response body contains the Endpoint resource and the associated Organization resource
assert(response.body.resources.contains('Endpoint'))
assert(response.body.resources.contains('Organization'))
```

**REQ-ENDP-004**
1. This requirement is algorithmically verifiable.
2. FHIR API calls needed: GET [base]/Endpoint?organization=[value]&_id=[value]&_lastUpdated=[value]
3. Assertions: The server responds with a 200 status code and the response body contains the Endpoint resources that match the search parameters.
4. Test data prerequisites: Endpoint resources that match the search parameters.
5. Pseudocode:
```
// Send a GET request to the server
response = GET([base]/Endpoint?organization=[value]&_id=[value]&_lastUpdated=[value])

// Assert that the response status code is 200
assert(response.status == 200)

// Assert that the response body contains the Endpoint resources that match the search parameters
assert(response.body.resources.contains('Endpoint'))
assert(response.body.resources.every(resource => resource.organization == [value] && resource.id == [value] && resource.lastUpdated == [value]))
```