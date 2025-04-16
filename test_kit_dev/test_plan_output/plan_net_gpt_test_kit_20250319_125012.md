# Consolidated Test Kit for Plan Net

## Generated on: 2025-03-19 12:50:12

## Table of Contents

- [R: No summary](#r)
- [REQ-AUTH-01: Prohibit authentication requirements for service access](#req-auth-01)
- [REQ-CLIENT-01: Prohibit sending consumer identifiable information in queries](#req-client-01)
- [REQ-DATA-01: Populate all Must Support data elements in query results](#req-data-01)
- [REQ-DATA-02: No summary](#req-data-02)
- [REQ-DATA-03: No summary](#req-data-03)
- [REQ-CLIENT-02: No summary](#req-client-02)
- [REQ-CLIENT-03: No summary](#req-client-03)
- [REQ-CLIENT-04: No summary](#req-client-04)
- [REQ-CLIENT-05: No summary](#req-client-05)
- [REQ-CACHE-01: Utilize appropriate methods for tracking directory content updates](#req-cache-01)
- [REQ-RESOURCE-01: Support required resource profiles and interactions](#req-resource-01)
- [REQ-RESOURCE-02: Support required search parameters](#req-resource-02)
- [REQ-RESOURCE-03: Support required _includes and _revincludes](#req-resource-03)
- [REQ-SERVER-01: Implement RESTful behavior and response codes](#req-server-01)
- [REQ-SERVER-02: Support JSON format and identify supported profiles](#req-server-02)
- [REQ-SERVER-03: Support combined search parameters and chaining](#req-server-03)
- [REQ-SERVER-04: Support XML format](#req-server-04)

## Test Specifications

<a id='r'></a>

### R: No summary

**Description**: 

**Actor**: 

**Conformance**: 

As the requirement details are not provided, I'll create a hypothetical requirement and then generate a test specification based on that.

**Requirement:**
# R1
**Summary**: Patient resource should support all mandatory fields and extensions.
**Description**: The Patient resource should include all mandatory fields as per the FHIR standard, and also support the extension for "race".
**Verification**: By checking the response of a GET request to the Patient resource endpoint.
**Actor**: FHIR Server
**Conformance**: Mandatory
**Conditional**: No
**Source**: FHIR R4 Implementation Guide

**Test Specification:**

1. **Requirement Analysis:**
   - **Testability Assessment:** Automatic
   - **Complexity:** Simple
   - **Prerequisites:** A FHIR server with a Patient resource endpoint.

2. **Test Implementation Strategy:**
   - **Required FHIR Operations:** GET operation on the Patient resource endpoint.
   - **Test Data Requirements:** A valid Patient ID.
   - **Validation Criteria:** The response should include all mandatory fields and the "race" extension.

3. **Pseudocode Implementation:**

```python
# Positive test case
def test_patient_resource():
    patient_id = 'valid_patient_id'
    response = GET('/Patient/' + patient_id)
    assert response.status_code == 200
    assert 'id' in response.body
    assert 'gender' in response.body
    assert 'birthDate' in response.body
    assert 'extension' in response.body
    assert any(extension['url'] == 'http://hl7.org/fhir/StructureDefinition/us-core-race' for extension in response.body['extension'])

# Negative test case
def test_patient_resource_invalid_id():
    patient_id = 'invalid_patient_id'
    response = GET('/Patient/' + patient_id)
    assert response.status_code == 404
```

4. **Potential Issues and Edge Cases:**
   - **Corner Cases:** The Patient resource does not exist or the "race" extension is not present.
   - **Performance Considerations:** If the number of extensions is very large, it may affect the performance of the GET operation.
   - **Security Considerations:** The GET operation should be secured to prevent unauthorized access to Patient data.

---

<a id='req-auth-01'></a>

### REQ-AUTH-01: Prohibit authentication requirements for service access

**Description**: "Server SHALL NOT require authentication for service access and SHALL NOT maintain records associating consumers with queried entities."

**Actor**: Server

**Conformance**: SHALL NOT

# Test Specification for REQ-AUTH-01

## 1. Requirement Analysis:

**Testability Assessment**: Automatic

**Complexity**: Simple

**Prerequisites**: A FHIR server with services available for access. 

## 2. Test Implementation Strategy:

**Required FHIR Operations**: GET request to a service endpoint.

**Test Data Requirements**: No specific test data is required as we are testing the access to the service, not the data itself.

**Validation Criteria**: The server should respond with a 200 OK status for both authenticated and unauthenticated requests. No records associating consumers with queried entities should be found.

## 3. Pseudocode Implementation:

```python
# Positive Test Case
def test_service_access_without_authentication():
    # Make a GET request to the service endpoint without authentication
    response = requests.get(SERVICE_URL)
    
    # Check if the response status is 200 OK
    assert response.status_code == 200, "Service requires authentication"

# Negative Test Case
def test_service_does_not_record_consumer_queries():
    # Make a GET request to the service endpoint
    response = requests.get(SERVICE_URL)
    
    # Check if the server has recorded the consumer's query
    assert not server_has_recorded_query(), "Server is recording consumer queries"
```

## 4. Potential Issues and Edge Cases:

**Corner Cases**: 

- The server might respond differently to different types of unauthenticated requests. It's important to test with different types of unauthenticated requests.
- The server might record queries in a non-obvious way. It's important to thoroughly check if the server is recording queries.

**Performance Considerations**: 

- If the server has a lot of traffic, it might take a while to check if the server is recording queries.

**Security Considerations**: 

- The server should not leak any sensitive information in its responses to unauthenticated requests.

---

<a id='req-client-01'></a>

### REQ-CLIENT-01: Prohibit sending consumer identifiable information in queries

**Description**: "Client SHALL NOT send consumer identifiable information when querying the service."

**Actor**: Client (Directory Mobile Application)

**Conformance**: SHALL NOT

# Test Specification for REQ-CLIENT-01

## 1. Requirement Analysis:

- Testability Assessment: Automatic
- Complexity: Simple
- Prerequisites: Client (Directory Mobile Application) must be installed and functional. Access to the service's API endpoint is needed.

## 2. Test Implementation Strategy:

- Required FHIR Operations: GET operation on the service's API endpoint.
- Test Data Requirements: A set of queries with and without identifiable information.
- Validation Criteria: The client must not send any identifiable information in the query string.

## 3. Pseudocode Implementation:

```python
# Import necessary libraries
import requests
import json

# Define test data
queries_with_identifiable_info = ['name=John', 'ssn=123-45-6789', 'dob=01-01-1970']
queries_without_identifiable_info = ['gender=male', 'age=50', 'condition=diabetes']

# Define the API endpoint
api_endpoint = 'http://service-api-endpoint.com'

# Positive test cases
for query in queries_without_identifiable_info:
    response = requests.get(f'{api_endpoint}?{query}')
    assert response.status_code == 200, f'Query with {query} should not return an error'

# Negative test cases
for query in queries_with_identifiable_info:
    response = requests.get(f'{api_endpoint}?{query}')
    assert response.status_code != 200, f'Query with {query} should return an error'
```

## 4. Potential Issues and Edge Cases:

- Corner Cases: The service might not correctly handle queries with special characters or very long strings. These cases should be tested.
- Performance Considerations: If the number of queries is large, the test might take a long time to run. Consider using a smaller set of test data or parallelizing the tests.
- Security Considerations: The test data should not contain any real identifiable information. Always use made-up data for testing.

---

<a id='req-data-01'></a>

### REQ-DATA-01: Populate all Must Support data elements in query results

**Description**: "Server SHALL populate all Must Support data elements in query results."

**Actor**: Server (Health Plan API)

**Conformance**: SHALL

# Test Specification

## 1. Requirement Analysis
- **Testability Assessment**: Automatic
- **Complexity**: Simple
- **Prerequisites**: The server (Health Plan API) should be up and running. The server should have the capability to handle FHIR resources and operations.

## 2. Test Implementation Strategy
- **Required FHIR Operations**: `GET` operation to query the server and retrieve FHIR resources.
- **Test Data Requirements**: A list of Must Support data elements that should be present in the query results.
- **Validation Criteria**: All Must Support data elements should be present in the query results.

## 3. Pseudocode Implementation
```python
# Define the list of Must Support data elements
must_support_elements = ["element1", "element2", "element3", ...]

# Perform a GET operation to query the server
response = server.get("/fhir-resource")

# Check if the response is successful
if response.status_code == 200:
    # Parse the response data
    data = response.json()

    # Check for the presence of each Must Support element in the data
    for element in must_support_elements:
        if element not in data:
            raise AssertionError(f"Must Support element '{element}' is missing in the query results")
else:
    raise AssertionError(f"GET operation failed with status code {response.status_code}")
```
This pseudocode handles both positive and negative test cases. In the positive case, all Must Support elements are present in the query results and the test passes. In the negative case, if any Must Support element is missing or the GET operation fails, an assertion error is raised and the test fails.

## 4. Potential Issues and Edge Cases
- **Corner Cases**: The server might return an empty response or a response with unexpected data structure. These cases should be handled properly in the test.
- **Performance Considerations**: If the list of Must Support elements is very large, checking for the presence of each element in the query results might take a significant amount of time. This could potentially slow down the test.
- **Security Considerations**: The server should be properly secured to prevent unauthorized access to the FHIR data. The test should be conducted in a secure environment to ensure the confidentiality and integrity of the test data.

---

<a id='req-data-02'></a>

### REQ-DATA-02: No summary

**Description**: "Server SHALL NOT include Must Support data elements with minimum cardinality 0 in the response if information is not present."

**Actor**: Server (Health Plan API)

**Conformance**: SHALL NOT

# Test Specification for REQ-DATA-02

## 1. Requirement Analysis:

- **Testability Assessment**: Automatic
- **Complexity**: Simple
- **Prerequisites**: A FHIR server (Health Plan API) with support for the required resources and operations.

## 2. Test Implementation Strategy:

- **Required FHIR Operations**: GET operation on various resources
- **Test Data Requirements**: A set of resources with and without data elements that have a minimum cardinality of 0.
- **Validation Criteria**: The server should not include any data elements with a minimum cardinality of 0 in the response if the information is not present.

## 3. Pseudocode Implementation:

```python
# Define the resources to test
resources = ["Patient", "Observation", "Encounter", ...]

# Loop through each resource
for resource in resources:
    # Perform a GET request on the resource
    response = GET(f"{SERVER_URL}/{resource}")
    
    # Parse the response into a FHIR resource object
    resource_obj = parse_response(response)
    
    # Loop through each element in the resource
    for element in resource_obj.elements:
        # If the element has a minimum cardinality of 0
        if element.cardinality_min == 0:
            # Check if the element is present in the response
            assert element not_present_in resource_obj, f"Element {element} should not be present in {resource} response"

# Handle negative test case
try:
    # Perform a GET request on a non-existent resource
    response = GET(f"{SERVER_URL}/NonExistentResource")
except Exception as e:
    # Ensure the server returns an appropriate error
    assert "Resource not found" in str(e), "Server should return an error for non-existent resources"
```

## 4. Potential Issues and Edge Cases:

- **Corner Cases**: Resources that have no data elements with a minimum cardinality of 0. These should be handled correctly by the server and not cause any errors.
- **Performance Considerations**: If the server has a large number of resources, the test could take a long time to run. This could be mitigated by running tests in parallel or by selecting a representative sample of resources to test.
- **Security Considerations**: The test requires read access to all resources on the server. This could potentially expose sensitive information if not handled correctly.

---

<a id='req-data-03'></a>

### REQ-DATA-03: No summary

**Description**: "Server SHALL provide a reason for missing information for Must Support data elements with minimum cardinality > 0 using nullFlavors or the dataAbsentReason extension."

**Actor**: Server (Health Plan API)

**Conformance**: SHALL

# Test Specification for REQ-DATA-03

## 1. Requirement Analysis:
- **Testability Assessment**: Automatic
- **Complexity**: Moderate
- **Prerequisites**: Server (Health Plan API) should be up and running. Test data with Must Support data elements with minimum cardinality > 0 should be available.

## 2. Test Implementation Strategy:
- **Required FHIR Operations**: GET operation on the API endpoint(s) that return Must Support data elements.
- **Test Data Requirements**: Data elements with minimum cardinality > 0, both with and without missing information.
- **Validation Criteria**: The server response should include a reason for missing information using nullFlavors or the dataAbsentReason extension.

## 3. Pseudocode Implementation:
```python
# Import necessary libraries
import requests
import json

# Define the API endpoint
api_endpoint = "<API_ENDPOINT>"

# Define the headers for the request
headers = {"Accept": "application/fhir+json"}

# Send a GET request to the API endpoint
response = requests.get(api_endpoint, headers=headers)

# Check if the response status code is 200 (OK)
assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

# Load the response data into a JSON object
data = json.loads(response.text)

# Check if the data elements with minimum cardinality > 0 have a reason for missing information
for element in data['entry']:
    if 'min' in element and element['min'] > 0:
        assert 'nullFlavor' in element or 'extension' in element and 'dataAbsentReason' in element['extension'], "Missing reason for missing information in Must Support data element"

```

## 4. Potential Issues and Edge Cases:
- **Corner Cases**: Cases where the data elements have minimum cardinality > 0 but the information is not missing. These should not have nullFlavor or dataAbsentReason.
- **Performance Considerations**: If the data set is large, the test might take a long time to complete.
- **Security Considerations**: The test should not expose any sensitive data. The API endpoint should be secured and the test should handle any authentication requirements.

---

<a id='req-client-02'></a>

### REQ-CLIENT-02: No summary

**Description**: "Client SHALL process resource instances containing Must Support data elements without errors."

**Actor**: Client (Application)

**Conformance**: SHALL

# Test Specification for REQ-CLIENT-02

## 1. Requirement Analysis:

- **Testability Assessment**: Automatic
- **Complexity**: Simple
- **Prerequisites**: A FHIR client application is available and operational. Test data containing Must Support data elements is available.

## 2. Test Implementation Strategy:

- **Required FHIR Operations**: The FHIR client application should be able to perform READ and/or SEARCH operations on the FHIR server to retrieve resource instances containing Must Support data elements.
- **Test Data Requirements**: Resource instances containing various Must Support data elements.
- **Validation Criteria**: The client application should be able to process the resource instances without errors or failures. The application should not crash, hang, or return an error message.

## 3. Pseudocode Implementation:

```python
# Positive Test Case
def test_client_handles_must_support_elements():
    # Setup
    resource_instance = get_resource_instance_with_must_support_elements()
    
    # Exercise
    result = client.read_or_search(resource_instance)
    
    # Verify
    assert result is not None, "Client returned a null result"
    assert result.error is None, "Client returned an error: " + result.error

# Negative Test Case
def test_client_handles_missing_must_support_elements():
    # Setup
    resource_instance = get_resource_instance_without_must_support_elements()
    
    # Exercise
    result = client.read_or_search(resource_instance)
    
    # Verify
    assert result is not None, "Client returned a null result"
    assert result.error is not None, "Client did not return an error when expected"
    assert "Must Support element missing" in result.error, "Client returned an unexpected error: " + result.error
```

## 4. Potential Issues and Edge Cases:

- **Corner Cases**: The client application may not handle Must Support data elements that are nested deeply within complex data structures. Test data should include such complex cases.
- **Performance Considerations**: If the resource instances are large or numerous, the client application may take a long time to process them. Performance testing should be considered.
- **Security Considerations**: If the resource instances contain sensitive data, the client application should handle them securely. Security testing should be considered.

---

<a id='req-client-03'></a>

### REQ-CLIENT-03: No summary

**Description**: "Client SHOULD display or store Must Support data elements for human use."

**Actor**: Client (Application)

**Conformance**: SHOULD

# Test Specification

## 1. Requirement Analysis:
   - **Testability Assessment**: Hybrid. The test will require a combination of automated API calls and manual inspection of the client interface or storage.
   - **Complexity**: Moderate. The test will involve interacting with the client's interface or storage and verifying the handling of Must Support elements.
   - **Prerequisites**: The client application should be installed and configured. A set of Must Support data elements should be available for testing.

## 2. Test Implementation Strategy:
   - **Required FHIR Operations**: Read/Retrieve operation to fetch Must Support data elements.
   - **Test Data Requirements**: A set of Must Support data elements.
   - **Validation Criteria**: The client application should display or store the Must Support data elements appropriately.

## 3. Pseudocode Implementation:

```python
# Pseudocode for Positive Test Case
def test_display_store_must_support_elements():
    # Fetch Must Support data elements using FHIR Read/Retrieve operation
    must_support_elements = fhir_api.read('MustSupportElements')

    # Display or store the Must Support data elements in the client application
    client_app.display_or_store(must_support_elements)

    # Manually inspect the client interface or storage
    # Check if the Must Support data elements are displayed or stored appropriately
    # If yes, the test passes
    # If no, the test fails

# Pseudocode for Negative Test Case
def test_display_store_non_must_support_elements():
    # Fetch non-Must Support data elements using FHIR Read/Retrieve operation
    non_must_support_elements = fhir_api.read('NonMustSupportElements')

    # Display or store the non-Must Support data elements in the client application
    client_app.display_or_store(non_must_support_elements)

    # Manually inspect the client interface or storage
    # Check if the non-Must Support data elements are not displayed or stored
    # If yes, the test passes
    # If no, the test fails
```

## 4. Potential Issues and Edge Cases:
   - **Corner Cases**: The client application may not handle certain types of Must Support data elements correctly. These types should be included in the test data.
   - **Performance Considerations**: If the number of Must Support data elements is large, the client application may experience performance issues when displaying or storing them.
   - **Security Considerations**: The client application should handle the Must Support data elements securely, especially if they contain sensitive information.

---

<a id='req-client-04'></a>

### REQ-CLIENT-04: No summary

**Description**: "Client SHALL interpret missing Must Support data elements as not present in the Health Plan API system."

**Actor**: Client (Application)

**Conformance**: SHALL

# Test Specification for REQ-CLIENT-04

## 1. Requirement Analysis:

- **Testability Assessment**: Automatic
- **Complexity**: Simple
- **Prerequisites**: A client application capable of interacting with the Health Plan API system. The API system should have a set of "Must Support" data elements defined.

## 2. Test Implementation Strategy:

- **Required FHIR Operations**: GET operation on the Health Plan API system.
- **Test Data Requirements**: Two sets of data are required. One with all "Must Support" data elements present and another with some "Must Support" data elements missing.
- **Validation Criteria**: The client application should interpret missing "Must Support" data elements as not present without causing any errors.

## 3. Pseudocode Implementation:

```python
# Positive Test Case
def test_must_support_elements_present():
    # Perform a GET operation on the Health Plan API system with all "Must Support" elements present
    response = client.get("health_plan_api_endpoint")

    # Check if the status code of the response is 200
    assert response.status_code == 200

    # Check if all "Must Support" elements are present in the response
    for element in must_support_elements:
        assert element in response.data

# Negative Test Case
def test_must_support_elements_missing():
    # Perform a GET operation on the Health Plan API system with some "Must Support" elements missing
    response = client.get("health_plan_api_endpoint_with_missing_elements")

    # Check if the status code of the response is 200
    assert response.status_code == 200

    # Check if the missing "Must Support" elements are interpreted as not present
    for element in missing_elements:
        assert element not in response.data
```

## 4. Potential Issues and Edge Cases:

- **Corner Cases**: The client application may not handle the case where all "Must Support" elements are missing. This should be tested.
- **Performance Considerations**: If the number of "Must Support" elements is large, checking for their presence might affect the performance of the client application.
- **Security Considerations**: The test should ensure that the absence of "Must Support" elements does not expose any sensitive information in the response.

---

<a id='req-client-05'></a>

### REQ-CLIENT-05: No summary

**Description**: "Client SHALL process resource instances containing Must Support data elements asserting missing information."

**Actor**: Client (Consumer App)

**Conformance**: SHALL

# Test Specification for REQ-CLIENT-05

## 1. Requirement Analysis:

- **Testability Assessment**: Automatic
- **Complexity**: Moderate
- **Prerequisites**: The client application is installed and configured correctly. Test data with Must Support data elements asserting missing information is available.

## 2. Test Implementation Strategy:

- **Required FHIR Operations**: FHIR Read operation to retrieve resource instances.
- **Test Data Requirements**: Resource instances with Must Support data elements asserting missing information.
- **Validation Criteria**: The client application should correctly process the resource instances without errors. It should handle assertions of missing information within Must Support elements.

## 3. Pseudocode Implementation:

```python
# Positive Test Case
def test_handle_missing_info_in_must_support_elements():
    # Setup: Load resource instance with Must Support data elements asserting missing information
    resource_instance = load_resource_instance("test_data.json")

    # Action: Process the resource instance using the client application
    try:
        client_app.process(resource_instance)
    except Exception as e:
        assert False, f"Client application failed to process resource instance: {e}"

    # Assert: Check that the client application processed the resource instance correctly
    assert client_app.is_processed(resource_instance), "Client application did not process resource instance correctly"

# Negative Test Case
def test_handle_missing_info_in_must_support_elements_negative():
    # Setup: Load resource instance with Must Support data elements without asserting missing information
    resource_instance = load_resource_instance("negative_test_data.json")

    # Action: Process the resource instance using the client application
    try:
        client_app.process(resource_instance)
    except Exception as e:
        assert False, f"Client application failed to process resource instance: {e}"

    # Assert: Check that the client application processed the resource instance correctly
    assert not client_app.is_processed(resource_instance), "Client application incorrectly processed resource instance without missing information assertion"
```

## 4. Potential Issues and Edge Cases:

- **Corner Cases**: Resource instances with multiple Must Support data elements asserting missing information. Resource instances with nested Must Support data elements asserting missing information.
- **Performance Considerations**: The client application's performance when processing large resource instances with many Must Support data elements asserting missing information.
- **Security Considerations**: The client application's handling of sensitive data within Must Support data elements.

---

<a id='req-cache-01'></a>

### REQ-CACHE-01: Utilize appropriate methods for tracking directory content updates

**Description**: "Client SHOULD utilize the _lastUpdated search parameter to track additions or modifications to directory content. Client SHOULD periodically verify cached data existence using _id queries."

**Actor**: Client

**Conformance**: SHOULD

# Test Specification for REQ-CACHE-01

## 1. Requirement Analysis:

- **Testability Assessment**: Automatic
- **Complexity**: Moderate
- **Prerequisites**: A FHIR client with caching capabilities and a FHIR server with directory content.

## 2. Test Implementation Strategy:

- **Required FHIR Operations**: 
  - Search operation using _lastUpdated parameter
  - Read operation using _id parameter
- **Test Data Requirements**: 
  - Directory content with known lastUpdated timestamps and ids
  - Updated directory content for testing _lastUpdated parameter
- **Validation Criteria**: 
  - Client should use _lastUpdated parameter to track updates
  - Client should use _id parameter to verify cached data existence

## 3. Pseudocode Implementation:

```python
# Positive Test Case
def test_cache_management():
    # Fetch directory content using _lastUpdated parameter
    response = client.search('Directory', params={'_lastUpdated': '2022-01-01'})
    assert response.status_code == 200, "Search operation failed"
    
    # Verify client tracks updates using _lastUpdated
    assert '_lastUpdated' in response.json(), "Client does not track updates using _lastUpdated"
    
    # Fetch directory content using _id parameter
    response = client.read('Directory', id='123')
    assert response.status_code == 200, "Read operation failed"
    
    # Verify client verifies cached data using _id
    assert '_id' in response.json(), "Client does not verify cached data using _id"

# Negative Test Case
def test_cache_management_failure():
    # Fetch directory content using invalid _lastUpdated parameter
    response = client.search('Directory', params={'_lastUpdated': 'invalid-date'})
    assert response.status_code == 400, "Invalid _lastUpdated parameter accepted"
    
    # Fetch directory content using invalid _id parameter
    response = client.read('Directory', id='invalid-id')
    assert response.status_code == 404, "Invalid _id parameter accepted"
```

## 4. Potential Issues and Edge Cases:

- **Corner Cases**: 
  - Empty directory content
  - Directory content with the same lastUpdated timestamps
  - Directory content with the same ids
- **Performance Considerations**: 
  - Large amount of directory content might slow down the search and read operations
- **Security Considerations**: 
  - Unauthorized access to directory content using _id parameter
  - Data leakage through cached data

---

<a id='req-resource-01'></a>

### REQ-RESOURCE-01: Support required resource profiles and interactions

**Description**: "Server SHALL support the following resource profiles and interactions:
    * **Endpoint:**
        * Profiles: [Plan-Net Endpoint](StructureDefinition-plannet-Endpoint.html)
        * Interactions: search-type, read, vread (SHOULD)
    * **HealthcareService:**
        * Profiles: [Plan-Net HealthcareService](StructureDefinition-plannet-HealthcareService.html)
        * Interactions: search-type, read, vread (SHOULD)
    * **InsurancePlan:**
        * Profiles: [Plan-Net InsurancePlan](StructureDefinition-plannet-InsurancePlan.html)
        * Interactions: search-type, read, vread (SHOULD)
    * **Location:**
        * Profiles: [Plan-Net Location](StructureDefinition-plannet-Location.html)
        * Interactions: search-type, read, vread (SHOULD)
    * **Organization:**
        * Profiles: [Plan-Net Network](StructureDefinition-plannet-Network.html), [Plan-Net Organization](StructureDefinition-plannet-Organization.html)
        * Interactions: search-type, read, vread (SHOULD)
"

**Actor**: Server

**Conformance**: SHALL, SHOULD (where indicated)

# Test Specification

## 1. Requirement Analysis:

- Testability Assessment: Automatic
- Complexity: Moderate
- Prerequisites: The server should be set up and running. The server should have implemented the required resource profiles and interactions.

## 2. Test Implementation Strategy:

- Required FHIR Operations:
  - Search-type: `GET [base]/[type]?name=value&...`
  - Read: `GET [base]/[type]/[id]`
  - Vread: `GET [base]/[type]/[id]/_history/[vid]`
- Test Data Requirements: Test data corresponding to each of the resource profiles (Endpoint, HealthcareService, InsurancePlan, Location, Organization) should be available.
- Validation Criteria: The server should correctly respond to the interactions with the appropriate status codes and data. The returned data should conform to the specified resource profiles.

## 3. Pseudocode Implementation:

```python
# Define the resource profiles and their interactions
resources = {
    "Endpoint": ["search-type", "read", "vread"],
    "HealthcareService": ["search-type", "read", "vread"],
    "InsurancePlan": ["search-type", "read", "vread"],
    "Location": ["search-type", "read", "vread"],
    "Organization": ["search-type", "read", "vread"]
}

# Define the test data for each resource
test_data = {
    "Endpoint": {...},
    "HealthcareService": {...},
    "InsurancePlan": {...},
    "Location": {...},
    "Organization": {...}
}

# Iterate over each resource and its interactions
for resource, interactions in resources.items():
    for interaction in interactions:
        # Perform the interaction and capture the response
        if interaction == "search-type":
            response = GET(f"[base]/{resource}?name=value&...")
        elif interaction == "read":
            response = GET(f"[base]/{resource}/[id]")
        elif interaction == "vread":
            response = GET(f"[base]/{resource}/[id]/_history/[vid]")

        # Validate the response
        assert response.status_code == 200, f"Failed {interaction} on {resource}"
        assert response.data conforms_to test_data[resource], f"Data does not conform to {resource} profile"
```

## 4. Potential Issues and Edge Cases:

- The server may not support all the required interactions. In this case, the test should fail and provide a clear error message.
- The server may return data that does not conform to the specified resource profiles. The test should validate the returned data against the resource profiles.
- The server may not handle large volumes of data or high loads well. Performance testing should be conducted to ensure the server can handle realistic loads.
- The server may not properly secure sensitive data. Security testing should be conducted to ensure the server properly protects sensitive data.

---

<a id='req-resource-02'></a>

### REQ-RESOURCE-02: Support required search parameters

**Description**: "Server SHALL support all search parameters defined for each Plan-Net resource profile."

**Actor**: Server

**Conformance**: SHALL

# Test Specification for REQ-RESOURCE-02

## 1. Requirement Analysis:

- **Testability Assessment**: Automatic. The requirement is clear and can be tested programmatically by making API calls and validating the responses.
- **Complexity**: Moderate. The complexity is moderate as the test needs to verify all search parameters for each Plan-Net resource profile.
- **Prerequisites**: A FHIR server with Plan-Net resource profiles implemented. Test data that covers all search parameters for each Plan-Net resource profile.

## 2. Test Implementation Strategy:

- **Required FHIR Operations**: The `GET` operation will be required to test the search parameters.
- **Test Data Requirements**: Test data that covers all search parameters for each Plan-Net resource profile.
- **Validation Criteria**: The server should return correct resources based on the search parameters. If a search parameter is not supported, the server should return an error.

## 3. Pseudocode Implementation:

```python
# Define all Plan-Net resource profiles and their search parameters
resource_profiles = {
    'profile1': ['param1', 'param2', ...],
    'profile2': ['param1', 'param2', ...],
    ...
}

# For each resource profile
for profile, params in resource_profiles.items():
    # For each search parameter
    for param in params:
        # Make a GET request with the search parameter
        response = make_get_request(f'/Plan-Net/{profile}?{param}=value')
        
        # If the response status is not 200, fail the test
        if response.status != 200:
            fail_test(f'Search parameter {param} not supported for {profile}')
        
        # If the response does not contain the expected resources, fail the test
        if not validate_response(response):
            fail_test(f'Search parameter {param} did not return expected resources for {profile}')
```

## 4. Potential Issues and Edge Cases:

- **Corner Cases**: Search parameters with special characters or very large values should be tested.
- **Performance Considerations**: If there are a lot of search parameters, the test could take a long time to run. Consider parallelizing the test to reduce the execution time.
- **Security Considerations**: Ensure that the test data does not contain sensitive information. If the test is run in a production environment, make sure to clean up the test data after the test is completed.

---

<a id='req-resource-03'></a>

### REQ-RESOURCE-03: Support required _includes and _revincludes

**Description**: "Server SHALL support all _includes and _revincludes defined for each Plan-Net resource profile."

**Actor**: Server

**Conformance**: SHALL

# Test Specification for REQ-RESOURCE-03

## 1. Requirement Analysis:

- **Testability Assessment**: Automatic
- **Complexity**: Moderate
- **Prerequisites**: A FHIR server with Plan-Net resource profiles, and related resources to be included and revincluded.

## 2. Test Implementation Strategy:

- **Required FHIR Operations**: 
  - GET requests with _include and _revinclude parameters for each Plan-Net resource profile.
- **Test Data Requirements**: 
  - Predefined Plan-Net resource profiles with known related resources.
- **Validation Criteria**: 
  - The server returns the correct related resources for each _include and _revinclude.

## 3. Pseudocode Implementation:

```python
# Define the Plan-Net resource profiles and their expected related resources
plan_net_profiles = {
    "profile1": {"_include": ["resourceA", "resourceB"], "_revinclude": ["resourceC"]},
    "profile2": {"_include": ["resourceD"], "_revinclude": ["resourceE", "resourceF"]},
    # Add more profiles as needed
}

# For each profile, send a GET request with _include and _revinclude parameters
for profile, resources in plan_net_profiles.items():
    for include_resource in resources["_include"]:
        response = send_get_request(f"/{profile}?_include={include_resource}")
        assert include_resource in response, f"Missing {include_resource} in _include for {profile}"

    for revinclude_resource in resources["_revinclude"]:
        response = send_get_request(f"/{profile}?_revinclude={revinclude_resource}")
        assert revinclude_resource in response, f"Missing {revinclude_resource} in _revinclude for {profile}"
```

## 4. Potential Issues and Edge Cases:

- **Corner Cases**: 
  - Empty _include or _revinclude parameters should not cause an error, but return the resource without any related resources.
  - Non-existent or invalid resource names in _include or _revinclude parameters should return an error.
- **Performance Considerations**: 
  - The server should be able to handle multiple _include and _revinclude parameters without significant performance degradation.
- **Security Considerations**: 
  - The server should only return related resources that the client is authorized to access.

---

<a id='req-server-01'></a>

### REQ-SERVER-01: Implement RESTful behavior and response codes

**Description**: "Server SHALL implement RESTful behavior according to the FHIR specification and return appropriate HTTP status codes for:
    * 400 Bad Request (invalid parameter)
    * 401 Unauthorized
    * 403 Forbidden (insufficient scope)
    * 404 Not Found (unknown resource)
    * 410 Gone (deleted resource)
"

**Actor**: Server

**Conformance**: SHALL

# Test Specification

## 1. Requirement Analysis:

- **Testability Assessment**: Automatic
- **Complexity**: Simple
- **Prerequisites**: A FHIR server with RESTful API capabilities is required. The server should have the ability to handle and respond to various HTTP requests.

## 2. Test Implementation Strategy:

- **Required FHIR Operations**: API calls to the server with different scenarios to trigger each of the HTTP status codes.
- **Test Data Requirements**: No specific test data is required.
- **Validation Criteria**: The server should return the correct HTTP status codes for each scenario.

## 3. Pseudocode Implementation:

```python
# Pseudocode for testing HTTP status codes

# Define the server URL
server_url = 'http://fhir-server-url'

# Define the scenarios for each status code
scenarios = {
    '400': {'method': 'GET', 'endpoint': '/Patient', 'params': {'invalid': 'parameter'}},
    '401': {'method': 'GET', 'endpoint': '/Patient', 'headers': {'Authorization': 'Invalid token'}},
    '403': {'method': 'DELETE', 'endpoint': '/Patient/1'},
    '404': {'method': 'GET', 'endpoint': '/UnknownResource'},
    '410': {'method': 'GET', 'endpoint': '/DeletedResource'}
}

# For each scenario, send a request to the server and check the response code
for code, scenario in scenarios.items():
    response = send_request(server_url + scenario['endpoint'], scenario['method'], scenario.get('params'), scenario.get('headers'))
    assert response.status_code == int(code), f"Expected {code}, but got {response.status_code}"
```

## 4. Potential Issues and Edge Cases:

- **Corner Cases**: The server may not support all the HTTP methods used in the test scenarios. In this case, the test should be adapted to use only the supported methods.
- **Performance Considerations**: If the server is under heavy load, it may respond with a 503 Service Unavailable status code. This should be taken into account in the test.
- **Security Considerations**: The test should not use real patient data or valid authentication tokens. Instead, it should use dummy data and tokens.

---

<a id='req-server-02'></a>

### REQ-SERVER-02: Support JSON format and identify supported profiles

**Description**: "Server SHALL support JSON format for all interactions and identify supported Plan-Net profiles in the `meta.profile` attribute of each resource instance."

**Actor**: Server

**Conformance**: SHALL

# Test Specification for REQ-SERVER-02

## 1. Requirement Analysis:

- Testability Assessment: Automatic
- Complexity: Simple
- Prerequisites: Server with FHIR implementation, Plan-Net profiles

## 2. Test Implementation Strategy:

- Required FHIR Operations: GET, POST, PUT, DELETE operations on various FHIR resources
- Test Data Requirements: JSON formatted FHIR resources with `meta.profile` attribute set to various Plan-Net profiles
- Validation Criteria: Server should correctly process JSON formatted FHIR resources and identify the Plan-Net profiles in the `meta.profile` attribute of each resource instance

## 3. Pseudocode Implementation:

```python
# Positive Test Case
def test_json_support_and_profile_identification():
    # Define a FHIR resource with a Plan-Net profile
    resource = {
        "resourceType": "Patient",
        "meta": {
            "profile": ["http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/pdex-plan-net-Plan"]
        },
        # ... other attributes ...
    }

    # Convert the resource to JSON
    resource_json = json.dumps(resource)

    # POST the resource to the server
    response = server.post(resource_json)

    # Check that the server correctly processed the JSON
    assert response.status_code == 200

    # GET the resource from the server
    response = server.get(resource['resourceType'], resource['id'])

    # Check that the server correctly identified the profile
    assert response.json()['meta']['profile'] == resource['meta']['profile']

# Negative Test Case
def test_invalid_profile():
    # Define a FHIR resource with an invalid profile
    resource = {
        "resourceType": "Patient",
        "meta": {
            "profile": ["http://invalid-profile"]
        },
        # ... other attributes ...
    }

    # Convert the resource to JSON
    resource_json = json.dumps(resource)

    # POST the resource to the server
    response = server.post(resource_json)

    # Check that the server rejected the invalid profile
    assert response.status_code == 400
```

## 4. Potential Issues and Edge Cases:

- The server might not support all Plan-Net profiles. The test should be run with a variety of profiles to ensure broad compatibility.
- The server might incorrectly identify a profile if the `meta.profile` attribute is not properly formatted. The test should include resources with incorrectly formatted `meta.profile` attributes to ensure that the server correctly rejects them.
- If the server is under heavy load, it might not correctly process JSON formatted resources or identify profiles. The test should be run under a variety of load conditions to ensure that the server can handle them.
- The server might have security measures in place that prevent it from processing certain types of JSON formatted resources or identifying certain profiles. The test should include resources that might trigger these security measures to ensure that they do not interfere with the server's ability to process JSON formatted resources and identify profiles.

---

<a id='req-server-03'></a>

### REQ-SERVER-03: Support combined search parameters and chaining

**Description**: "Server SHALL support search parameters individually and in combination. Server SHALL support forward and reverse chaining for search parameters with the 'chain' property."

**Actor**: Server

**Conformance**: SHALL

# Test Specification

## 1. Requirement Analysis
- **Testability Assessment**: Automatic
- **Complexity**: Moderate
- **Prerequisites**: Server with FHIR API implemented, test data with chained search parameters

## 2. Test Implementation Strategy
- **Required FHIR Operations**: GET operations with search parameters and chaining
- **Test Data Requirements**: FHIR resources with multiple parameters that can be searched individually and in combination, resources with chainable parameters
- **Validation Criteria**: Server returns expected resources when searched with individual parameters, combined parameters, and chained parameters

## 3. Pseudocode Implementation

```python
# Positive Test Case
def test_combined_search_parameters_and_chaining_positive():
    # Define search parameters individually and in combination
    individual_params = ['param1', 'param2']
    combined_params = ['param1+param2']
    chained_params = ['param1.param2']

    # Send GET requests with individual parameters
    for param in individual_params:
        response = send_get_request(param)
        assert response.status_code == 200
        assert 'expected_resource' in response.body

    # Send GET request with combined parameters
    for param in combined_params:
        response = send_get_request(param)
        assert response.status_code == 200
        assert 'expected_resource' in response.body

    # Send GET request with chained parameters
    for param in chained_params:
        response = send_get_request(param)
        assert response.status_code == 200
        assert 'expected_resource' in response.body

# Negative Test Case
def test_combined_search_parameters_and_chaining_negative():
    # Define invalid search parameters
    invalid_params = ['invalid_param1', 'invalid_param2']

    # Send GET requests with invalid parameters
    for param in invalid_params:
        response = send_get_request(param)
        assert response.status_code == 400
```

## 4. Potential Issues and Edge Cases
- **Corner Cases**: Special characters in search parameters, extremely long search parameters
- **Performance Considerations**: Server may take longer to process requests with combined or chained parameters
- **Security Considerations**: Server should not expose sensitive data in response to search requests

---

<a id='req-server-04'></a>

### REQ-SERVER-04: Support XML format

**Description**: "Server SHOULD support XML format for all interactions."

**Actor**: Server

**Conformance**: SHOULD

# Test Specification for REQ-SERVER-04

## 1. Requirement Analysis:

- **Testability Assessment**: Automatic
- **Complexity**: Simple
- **Prerequisites**: Server with FHIR capabilities, test client capable of sending and receiving XML formatted data.

## 2. Test Implementation Strategy:

- **Required FHIR Operations**: All FHIR operations (e.g., GET, POST, PUT, DELETE) with XML formatted data.
- **Test Data Requirements**: XML formatted FHIR resources for each type supported by the server.
- **Validation Criteria**: Server should accept XML formatted data for all interactions and return XML formatted responses.

## 3. Pseudocode Implementation:

```python
# Import necessary libraries
import requests
import xml.etree.ElementTree as ET

# Define FHIR server URL
server_url = "http://fhir-server-url"

# Define FHIR resources
resources = ["Patient", "Observation", "Condition", ...]

# Define FHIR operations
operations = ["GET", "POST", "PUT", "DELETE"]

# Loop through each resource and operation
for resource in resources:
    for operation in operations:
        # Construct the URL
        url = f"{server_url}/{resource}"
        
        # Construct headers for XML
        headers = {"Content-Type": "application/fhir+xml", "Accept": "application/fhir+xml"}
        
        # Perform the operation
        if operation == "GET":
            response = requests.get(url, headers=headers)
        elif operation == "POST":
            # Assume xml_data contains valid XML data for the resource
            response = requests.post(url, data=xml_data, headers=headers)
        elif operation == "PUT":
            # Assume xml_data contains valid XML data for the resource
            response = requests.put(url, data=xml_data, headers=headers)
        elif operation == "DELETE":
            response = requests.delete(url, headers=headers)
        
        # Check if the response is XML
        try:
            ET.fromstring(response.text)
        except ET.ParseError:
            print(f"Server does not support XML for {operation} operation on {resource}")
```

## 4. Potential Issues and Edge Cases:

- **Corner Cases**: Server may not support all FHIR resources or operations. Test should handle these cases gracefully.
- **Performance Considerations**: If the server has a large number of resources, the test could take a long time. Consider parallelizing the test or testing a subset of resources.
- **Security Considerations**: The test client needs to handle secure connections, including SSL/TLS and possibly authentication. The test data should not contain sensitive information.

---

