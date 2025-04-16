# Consolidated Test Kit for Plan Net

## Generated on: 2025-03-19 12:40:08

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

## Test Specification

**Requirement:** 

**(Please provide the actual requirement details from your FHIR Implementation Guide to be analyzed. This will allow for a more accurate and relevant test specification.)**

**Example Placeholder Requirement:**

**R1**
* **Summary**: Patient resources SHALL include a valid birthDate.
* **Description**: All Patient resources must have a populated birthDate element conforming to the FHIR Date datatype.
* **Verification**: Automated Testing
* **Actor**: Server
* **Conformance**: SHALL
* **Conditional**: N/A
* **Source**: FHIR DSTU2

---

## 1. Requirement Analysis

* **Testability Assessment**: Automatic
* **Complexity**: Simple
* **Prerequisites**:
    * Running FHIR server compliant with the target FHIR version (e.g., DSTU2).
    * Ability to send HTTP requests to the FHIR server.

## 2. Test Implementation Strategy

* **Required FHIR Operations**: 
    * `POST /Patient` (Create a new Patient resource)
    * `GET /Patient/{id}` (Read an existing Patient resource)
* **Test Data Requirements**:
    * Valid Patient resource with a `birthDate` element in FHIR Date format (YYYY-MM-DD).
    * Invalid Patient resource with a missing `birthDate` element.
    * Invalid Patient resource with an incorrectly formatted `birthDate` element.
* **Validation Criteria**:
    * **Positive Test Case:** Successful creation (HTTP 201 Created) of a Patient resource with a valid `birthDate`. Successful retrieval (HTTP 200 OK) of the created Patient resource, confirming the presence and format of the `birthDate`.
    * **Negative Test Cases:** 
        * Attempt to create a Patient resource without a `birthDate` should result in an HTTP 400 Bad Request error.
        * Attempt to create a Patient resource with an invalid `birthDate` format should result in an HTTP 400 Bad Request error.

## 3. Pseudocode Implementation

```python
# Test Case 1: Create Patient with valid birthDate (Positive)
def test_create_patient_with_valid_birthdate():
  # Prepare test data
  patient_data = {
    "resourceType": "Patient",
    "birthDate": "1980-01-15"  # Valid FHIR Date format
  }

  # Send POST request to create Patient
  response = send_fhir_request("POST", "/Patient", patient_data)

  # Validate response
  assert response.status_code == 201, f"Expected 201 Created, got {response.status_code}"
  patient_id = response.json()["id"]

  # Retrieve created Patient resource
  response = send_fhir_request("GET", f"/Patient/{patient_id}")

  # Validate birthDate in retrieved resource
  assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
  assert "birthDate" in response.json(), "birthDate element missing in response"
  assert response.json()["birthDate"] == "1980-01-15", "Incorrect birthDate value"

# Test Case 2: Create Patient without birthDate (Negative)
def test_create_patient_without_birthdate():
  # Prepare test data (missing birthDate)
  patient_data = {
    "resourceType": "Patient"
  }

  # Send POST request to create Patient
  response = send_fhir_request("POST", "/Patient", patient_data)

  # Validate response - expect error
  assert response.status_code == 400, f"Expected 400 Bad Request, got {response.status_code}"
  assert "birthDate is required" in response.text, "Missing expected error message"

# Test Case 3: Create Patient with invalid birthDate format (Negative)
def test_create_patient_with_invalid_birthdate_format():
  # Prepare test data (invalid birthDate format)
  patient_data = {
    "resourceType": "Patient",
    "birthDate": "15-01-1980"  # Invalid format
  }

  # Send POST request to create Patient
  response = send_fhir_request("POST", "/Patient", patient_data)

  # Validate response - expect error
  assert response.status_code == 400, f"Expected 400 Bad Request, got {response.status_code}"
  assert "Invalid date format" in response.text, "Missing expected error message"

# Helper function to send FHIR requests (replace with your implementation)
def send_fhir_request(method, endpoint, data=None):
  # ... Your implementation to send FHIR requests ...
  pass
```

## 4. Potential Issues and Edge Cases

* **Timezones:** The FHIR Date datatype does not include timezone information. Ensure the server and test client handle dates consistently.
* **Data Types:** Consider testing with edge-case values for the Date datatype, such as leap years and the first/last days of months.
* **Performance:** If testing with a large volume of Patient resources, consider the performance implications and potential for rate limiting on the server.
* **Security:** Ensure test data does not contain sensitive information and that the testing environment is secure. 


---

<a id='req-auth-01'></a>

### REQ-AUTH-01: Prohibit authentication requirements for service access

**Description**: "Server SHALL NOT require authentication for service access and SHALL NOT maintain records associating consumers with queried entities."

**Actor**: Server

**Conformance**: SHALL NOT

## Test Specification: REQ-AUTH-01 - Prohibit Authentication Requirements

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:** 
    * A running FHIR server instance implementing the target implementation guide.
    * A valid FHIR resource endpoint (e.g., `Patient`, `Observation`).

### 2. Test Implementation Strategy

* **Required FHIR Operations:** 
    * `GET` request to a FHIR resource endpoint.
* **Test Data Requirements:** 
    * No specific test data is required for this test.
* **Validation Criteria:**
    * **Positive Case:** A successful `GET` request without authentication should return a HTTP status code `200 OK` and a valid FHIR Bundle resource.
    * **Negative Case:** A `GET` request with authentication (using any mechanism) should return a HTTP status code other than `401 Unauthorized` or `403 Forbidden`, indicating authentication is not a requirement.

### 3. Pseudocode Implementation

```python
# Test Case 1: Access without authentication
response = send_fhir_request('GET', 'http://fhir-server/Patient', headers={})

if response.status_code == 200 and 'application/fhir+json' in response.headers['Content-Type']:
    print("Test Case 1: PASS - Successful access without authentication.")
else:
    print(f"Test Case 1: FAIL - Unexpected response: {response.status_code} {response.text}")

# Test Case 2: Access with authentication (simulated)
response = send_fhir_request('GET', 'http://fhir-server/Patient', headers={'Authorization': 'Bearer invalid-token'})

if response.status_code not in [401, 403]:
    print("Test Case 2: PASS - Authentication not required for access.")
else:
    print(f"Test Case 2: FAIL - Authentication enforced: {response.status_code} {response.text}")

# Helper function to send FHIR requests
def send_fhir_request(method, url, headers={}, data=None):
    # Implement your preferred HTTP request library here (e.g., requests)
    # ...
    return response
```

### 4. Potential Issues and Edge Cases

* **Server Configuration:** Ensure the FHIR server is not behind any additional authentication layers (e.g., reverse proxy) that might interfere with the test.
* **Resource Specific Behavior:** While the requirement targets general service access, certain resources might have specific authorization rules. Consider testing with different resource types.
* **Rate Limiting:** Continuous testing without authentication might trigger rate limiting. Implement appropriate delays or use test accounts if necessary.
* **Logging and Auditing:** Verify the server does not log any personally identifiable information (PII) or create audit trails that could associate users with accessed resources. This aspect might require manual inspection of server logs. 


---

<a id='req-client-01'></a>

### REQ-CLIENT-01: Prohibit sending consumer identifiable information in queries

**Description**: "Client SHALL NOT send consumer identifiable information when querying the service."

**Actor**: Client (Directory Mobile Application)

**Conformance**: SHALL NOT

## Test Specification for REQ-CLIENT-01: Prohibit Sending Consumer Identifiable Information in Queries

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Moderate
* **Prerequisites:**
    * A running instance of the Directory Mobile Application (Client).
    * Access to the client's network traffic or logs.
    * A list of defined "consumer identifiable information" elements based on the FHIR Implementation Guide and relevant privacy regulations (e.g., name, address, phone number, email, social security number, medical record number).

### 2. Test Implementation Strategy

* **Required FHIR Operations:** Any FHIR query operation initiated by the client, such as:
    * `GET [base]/Patient?name=John`
    * `POST [base]/Patient/$search` (with identifiable information in the request body)
* **Test Data Requirements:**
    * A set of valid FHIR resources for querying.
    * A list of test queries containing various combinations of identifiable information.
* **Validation Criteria:**
    * **Positive Test Case:** The client request does NOT contain any defined "consumer identifiable information" in the URL parameters or request body.
    * **Negative Test Case:** The client request contains at least one instance of defined "consumer identifiable information" in the URL parameters or request body.

### 3. Pseudocode Implementation

```python
# Define a list of identifiable information elements
identifiable_elements = ["name", "address", "telecom", "birthDate", "identifier"] 

def test_prohibit_identifiable_info_in_queries(client, test_queries):
  """
  Tests if the client sends identifiable information in FHIR queries.

  Args:
    client: The Directory Mobile Application client.
    test_queries: A list of test queries to execute.

  Returns:
    A list of tuples, each containing the query and a boolean indicating 
    whether the query passed the test (True) or failed (False).
  """
  results = []
  for query in test_queries:
    try:
      # Execute the query using the client
      response = client.execute_query(query)

      # Check if the request contains identifiable information
      request_contains_pii = False
      for element in identifiable_elements:
        if element in query: # Check both URL and request body
          request_contains_pii = True
          break

      # Append the result to the list
      results.append((query, not request_contains_pii))

    except Exception as e:
      print(f"Error executing query: {query}. Error: {e}")
      results.append((query, False)) # Mark as failed if an error occurs

  return results

# Example usage:
test_queries = [
  "GET [base]/Patient?family=Smith", 
  "POST [base]/Patient/$search", # Assuming request body contains PII
  "GET [base]/Observation?code=http://loinc.org|15074-8"
]
test_results = test_prohibit_identifiable_info_in_queries(client, test_queries)

# Print the results
for query, passed in test_results:
  print(f"Query: {query}, Passed: {'Yes' if passed else 'No'}")
```

### 4. Potential Issues and Edge Cases

* **Encoded Information:** The client might attempt to send encoded identifiable information. The test should be able to decode and detect such information.
* **Partial Information:** The client might send partial identifiable information, like only the first name. The test should consider defining and detecting such cases.
* **Indirect Identifiers:** The client might use combinations of seemingly harmless data elements that can indirectly identify a consumer. This requires careful consideration of data privacy regulations and context-specific identifiers.
* **Performance:** Inspecting every client request for a large number of identifiable elements might impact performance. Consider optimizing the detection algorithm and using efficient data structures.
* **Security:** Accessing and logging client requests, even for testing, raises privacy concerns. Ensure appropriate security measures and data anonymization techniques are in place. 


---

<a id='req-data-01'></a>

### REQ-DATA-01: Populate all Must Support data elements in query results

**Description**: "Server SHALL populate all Must Support data elements in query results."

**Actor**: Server (Health Plan API)

**Conformance**: SHALL

## Test Specification for REQ-DATA-01: Populate all Must Support data elements in query results

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Moderate
* **Prerequisites:**
    * A running instance of the Health Plan API (Server)
    * Access to the FHIR Implementation Guide defining "Must Support" data elements for the resources being queried.
    * Test data loaded into the server, including resources with both "Must Support" and optional elements populated.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * `GET` requests to the appropriate resource endpoint(s) defined by the FHIR Implementation Guide.
* **Test Data Requirements:**
    * A set of test resources with known values:
        * Some resources should have all "Must Support" elements populated.
        * Some resources can have only a subset of "Must Support" elements populated (to test negative cases).
* **Validation Criteria:**
    * For each resource returned in the query response:
        * **Positive Test:** Verify that all data elements marked as "Must Support" in the FHIR Implementation Guide are present in the returned resource.
        * **Negative Test:** Verify that the server returns an appropriate error code (e.g., 4xx) if a "Must Support" element is missing from the requested resource.

### 3. Pseudocode Implementation

```python
# Input: 
#   resource_type: The type of FHIR resource to query (e.g., "Patient", "Observation")
#   must_support_elements: A list of "Must Support" element paths for the given resource_type 
#                          as defined in the FHIR Implementation Guide.

def test_must_support_elements(resource_type, must_support_elements):
  """
  Tests if the server populates all "Must Support" data elements in query results.
  """

  # Construct the FHIR API query URL
  base_url = "https://[server_base_url]/fhir" # Replace with actual server base URL
  query_url = f"{base_url}/{resource_type}" 

  # Execute the GET request
  response = requests.get(query_url)

  # Check for successful response
  if response.status_code == 200:
    # Parse the response bundle
    bundle = fhir.resources.FHIRResource.parse_obj(response.json())

    # Iterate through each resource in the bundle
    for entry in bundle.entry:
      resource = entry.resource

      # Check if all "Must Support" elements are present
      for element_path in must_support_elements:
        try:
          # Attempt to access the element using its path
          value = reduce(getattr, element_path.split("."), resource)

          # Assert that the element is not None
          assert value is not None, f"Must Support element '{element_path}' is missing in resource {resource.id}"

        except AttributeError:
          # Handle cases where the element path is invalid
          print(f"Error: Invalid element path '{element_path}' for resource type '{resource_type}'")
          return False

    # All checks passed
    print(f"Test Passed: All 'Must Support' elements present in '{resource_type}' resources.")
    return True

  else:
    # Handle unsuccessful response
    print(f"Error: Request failed with status code {response.status_code} - {response.text}")
    return False

# Example usage:
test_must_support_elements("Patient", ["name[0].family", "birthDate"])
```

### 4. Potential Issues and Edge Cases

* **Complex Data Types:** The pseudocode assumes simple data types. For complex types like CodeableConcept or extensions, additional logic is needed to check for required sub-elements.
* **Conditional Must Support:** The Implementation Guide might define "Must Support" elements conditionally based on other element values. The test needs to account for these conditions.
* **Resource Referencing:** If a "Must Support" element is a reference to another resource, the test should verify the reference's validity and potentially the presence of "Must Support" elements in the referenced resource.
* **Performance:** Querying for a large number of resources can impact performance. Consider using pagination or limiting the number of resources retrieved.
* **Security:** Ensure the test environment uses appropriate authentication and authorization mechanisms to access protected health information. 


---

<a id='req-data-02'></a>

### REQ-DATA-02: No summary

**Description**: "Server SHALL NOT include Must Support data elements with minimum cardinality 0 in the response if information is not present."

**Actor**: Server (Health Plan API)

**Conformance**: SHALL NOT

## Test Specification for REQ-DATA-02

**1. Requirement Analysis**

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running FHIR server implementing the target Health Plan API.
    * A list of resources and their corresponding Must Support data elements with minimum cardinality 0. This list should be derived from the applicable FHIR profiles and extensions defined in the Implementation Guide.

**2. Test Implementation Strategy**

* **Required FHIR Operations:** 
    * `GET` requests to retrieve resources from the server.
* **Test Data Requirements:**
    * For each resource and Must Support data element with minimum cardinality 0, prepare test data that deliberately omits the element. For example, if testing the `Patient.name` element (which can be 0..*), create a Patient resource without the `name` element.
* **Validation Criteria:**
    * Verify that the response does NOT contain the Must Support data element with minimum cardinality 0.

**3. Pseudocode Implementation**

```python
# Input:
#   resource_type: FHIR resource type (e.g., "Patient")
#   element_path: Path to the Must Support element (e.g., "name")

def test_absent_optional_element(resource_type, element_path):
  """
  Tests that the server does not return Must Support elements with 
  minimum cardinality 0 if no information is present.
  """

  # Construct the FHIR resource URL
  resource_url = f"{base_url}/{resource_type}" 

  # Make the GET request
  response = requests.get(resource_url)

  # Check for successful response
  assert response.status_code == 200, f"Request failed with status code: {response.status_code}"

  # Parse the response as JSON
  response_json = response.json()

  # Check if the element is present in the response
  if element_path in str(response_json):
    # Test failed: Element should not be present
    assert False, f"Element '{element_path}' found in response when it should be absent."
  else:
    # Test passed: Element is not present as expected
    print(f"Test passed for resource: {resource_type}, element: {element_path}")
```

**4. Potential Issues and Edge Cases**

* **Corner Cases:**
    * **Nested data elements:** The test should be able to handle nested data elements within a resource.
    * **Arrays:** Ensure the test correctly handles cases where the Must Support element is an array with a minimum cardinality of 0.
* **Performance Considerations:** 
    * Executing a large number of tests can impact performance. Consider optimizing test data and execution strategy.
* **Security Considerations:**
    * Ensure test data does not contain sensitive information.
    * Use appropriate authentication and authorization mechanisms when interacting with the FHIR server. 

**Additional Notes:**

* This test specification focuses on verifying the absence of optional Must Support elements. It does not cover other aspects of the response, such as HTTP status codes or response headers.
* The provided pseudocode is a simplified example and may require adjustments based on the specific testing framework and programming language used. 
* This test should be included as part of a comprehensive test suite that covers all aspects of the FHIR Implementation Guide. 


---

<a id='req-data-03'></a>

### REQ-DATA-03: No summary

**Description**: "Server SHALL provide a reason for missing information for Must Support data elements with minimum cardinality > 0 using nullFlavors or the dataAbsentReason extension."

**Actor**: Server (Health Plan API)

**Conformance**: SHALL

## Test Specification for REQ-DATA-03

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Moderate
* **Prerequisites:**
    * A running FHIR server compliant with the base specification and the Implementation Guide.
    * Access to test patients with potentially missing "Must Support" data elements.
    * Knowledge of "Must Support" data elements as defined by the Implementation Guide.

### 2. Test Implementation Strategy

* **Required FHIR Operations:** 
    * `read`: To retrieve resources with potentially missing data.
* **Test Data Requirements:**
    * A set of resources (e.g., Patient, Observation) containing "Must Support" data elements.
    * Some resources should have missing "Must Support" data elements.
* **Validation Criteria:**
    * For each "Must Support" data element with minimum cardinality > 0 that is missing:
        * Verify the presence of either:
            * A valid `nullFlavor` code within the element.
            * A `dataAbsentReason` extension with a valid code.
    * If neither `nullFlavor` nor `dataAbsentReason` is present, the test fails.

### 3. Pseudocode Implementation

```python
# Define a function to check for missing data reasons
def check_missing_data_reason(resource, element_path):
  """
  Checks for valid nullFlavor or dataAbsentReason for a missing element.

  Args:
    resource: The FHIR resource being validated.
    element_path: The path to the "Must Support" element.

  Returns:
    True if a valid reason is found, False otherwise.
  """
  element = resource.get(element_path)

  # Check if element is missing
  if element is None:
    # Check for nullFlavor
    if resource.get("nullFlavor"):
      return True
    # Check for dataAbsentReason extension
    for extension in resource.get("extension", []):
      if extension.get("url") == "http://hl7.org/fhir/StructureDefinition/data-absent-reason" and extension.get("valueCodeableConcept"):
        return True
    # No valid reason found
    return False
  else:
    return True  # Element is present, no need to check for reasons

# Example test case
def test_missing_patient_birthdate():
  """
  Tests if a missing Patient.birthDate has a valid reason.
  """
  # Retrieve a Patient resource with potentially missing birthDate
  patient = client.read("Patient", "123")

  # Define the path to the "Must Support" element
  element_path = "birthDate"

  # Assert that the check_missing_data_reason function returns True
  assert check_missing_data_reason(patient, element_path), f"Missing data reason for {element_path} in Patient/{patient.id}"

# Run multiple test cases with different resources and elements
# ...
```

### 4. Potential Issues and Edge Cases

* **Complex Data Types:** The pseudocode example focuses on simple data types. For complex types, the logic needs to be recursively applied to nested elements.
* **Performance:** Checking for missing data reasons on large resources or datasets could impact performance. Consider optimizing the validation logic or using selective testing.
* **Ambiguous Requirements:** The Implementation Guide should clearly define valid `nullFlavor` and `dataAbsentReason` codes. Ambiguity could lead to inconsistent test results.
* **Data Sensitivity:** Ensure test data is appropriately anonymized or de-identified to protect patient privacy.
* **Extension Handling:** The test should handle cases where the `dataAbsentReason` extension is present but contains an invalid or unexpected code. 


---

<a id='req-client-02'></a>

### REQ-CLIENT-02: No summary

**Description**: "Client SHALL process resource instances containing Must Support data elements without errors."

**Actor**: Client (Application)

**Conformance**: SHALL

## Test Specification for REQ-CLIENT-02: Handling Must Support Data Elements

### 1. Requirement Analysis

**Testability Assessment:** Automatic
**Complexity:** Moderate
**Prerequisites:** 
* A running FHIR server with the target Implementation Guide loaded.
* A client application capable of making FHIR API calls.
* Test data containing resources with "Must Support" data elements as defined by the Implementation Guide.

### 2. Test Implementation Strategy

**Required FHIR Operations:**
* **READ:** Retrieve resources containing "Must Support" data elements.
* **CREATE:** Attempt to create resources with missing "Must Support" data elements.
* **UPDATE:** Attempt to update resources, removing "Must Support" data elements.

**Test Data Requirements:**
* **Valid Resource:** A resource instance conforming to the Implementation Guide, including all "Must Support" data elements.
* **Invalid Resource (Missing Data):** A resource instance missing one or more "Must Support" data elements.
* **Invalid Resource (Modified Data):** A valid resource instance where a "Must Support" data element is modified to an invalid value (if applicable).

**Validation Criteria:**
* **READ:** 
    * Client should successfully retrieve the resource.
    * No errors should be logged by the client related to the "Must Support" data elements.
* **CREATE:**
    * Client should receive a `400 Bad Request` error response from the server.
    * The error response should clearly indicate the missing "Must Support" data element(s).
* **UPDATE:**
    * Client should receive a `400 Bad Request` error response from the server.
    * The error response should clearly indicate the "Must Support" data element that cannot be removed or modified.

### 3. Pseudocode Implementation

```python
# Test Case 1: READ Resource with Must Support Data Elements
def test_read_must_support_data():
  # Given: A valid resource ID with Must Support data elements
  resource_id = "example-resource-id"

  # When: The client retrieves the resource
  response = client.read("ResourceName", resource_id)

  # Then: The request should be successful
  assert response.status_code == 200

  # And: The response should contain the expected Must Support data
  assert "must_support_element" in response.json()

# Test Case 2: CREATE Resource with Missing Must Support Data Elements
def test_create_missing_must_support_data():
  # Given: A resource instance missing a Must Support data element
  invalid_resource = {
    # ... other data elements
  }

  # When: The client attempts to create the resource
  response = client.create("ResourceName", invalid_resource)

  # Then: The request should be rejected with a 400 Bad Request error
  assert response.status_code == 400

  # And: The error response should indicate the missing data element
  assert "Must Support data element 'must_support_element' is required" in response.text

# Test Case 3: UPDATE Resource Removing Must Support Data Elements
def test_update_remove_must_support_data():
  # Given: A valid resource ID and an updated resource with a Must Support element removed
  resource_id = "example-resource-id"
  updated_resource = {
    # ... other data elements, excluding the Must Support element
  }

  # When: The client attempts to update the resource
  response = client.update("ResourceName", resource_id, updated_resource)

  # Then: The request should be rejected with a 400 Bad Request error
  assert response.status_code == 400

  # And: The error response should indicate the issue with the Must Support element
  assert "Cannot remove or modify Must Support data element 'must_support_element'" in response.text
```

### 4. Potential Issues and Edge Cases

* **Complex Data Types:** The Implementation Guide might define "Must Support" elements within complex data types. Tests should cover scenarios where these nested elements are missing or invalid.
* **Conditional Must Support:** The "Must Support" designation might be conditional based on other data elements. Tests should cover various combinations to ensure proper handling.
* **Data Type Validation:** Ensure the client correctly validates the data type and format of "Must Support" elements as defined in the Implementation Guide.
* **Performance:**  Testing with large resources containing many "Must Support" elements can help identify potential performance bottlenecks in the client's processing.
* **Security:** If the "Must Support" data elements contain sensitive information, ensure the client handles them securely during processing and storage. 


---

<a id='req-client-03'></a>

### REQ-CLIENT-03: No summary

**Description**: "Client SHOULD display or store Must Support data elements for human use."

**Actor**: Client (Application)

**Conformance**: SHOULD

## Test Specification for REQ-CLIENT-03

### 1. Requirement Analysis

**Requirement:** Client SHOULD display or store Must Support data elements for human use.

* **Testability Assessment:** Hybrid (Manual inspection of display/storage combined with automated API interaction)
* **Complexity:** Moderate 
* **Prerequisites:**
    * A running instance of the client application under test.
    * Access to the client's user interface or data storage mechanism.
    * A list of Must Support data elements defined in the relevant FHIR Implementation Guide.
    * Test FHIR resources containing both populated and absent Must Support elements.

### 2. Test Implementation Strategy

**Required FHIR Operations:**

* **Read Operation:** Retrieve FHIR resources relevant to the client application.

**Test Data Requirements:**

* **Test Resource 1:** A FHIR resource instance with all Must Support elements populated with valid data.
* **Test Resource 2:** A FHIR resource instance with one or more Must Support elements absent.

**Validation Criteria:**

1. **Display:** For each Must Support element:
    * **Positive Test:** Verify that the client application displays the element and its value (if populated) in a human-readable format.
    * **Negative Test:** Verify that the client application appropriately handles and displays the absence of a Must Support element (e.g., displays a placeholder, message, or visual cue).
2. **Storage:** For each Must Support element:
    * **Positive Test:** Verify that the client application persists the element and its value (if populated) in its storage mechanism.
    * **Negative Test:** Verify that the client application appropriately handles the absence of a Must Support element in its storage (e.g., stores a null value, specific flag, or utilizes a schema that allows for optional elements).

### 3. Pseudocode Implementation

```python
# Input: 
#   client: Client application under test
#   resource_type: FHIR resource type (e.g., 'Patient', 'Observation')
#   must_support_elements: List of Must Support element paths (e.g., 'Patient.name', 'Observation.valueQuantity')

# Test Case 1: Display of Must Support elements
def test_display_must_support(client, resource_type, must_support_elements):
  # Retrieve test resources (populated and with missing elements)
  populated_resource = client.read(resource_type, '<resource_id_1>')
  partially_populated_resource = client.read(resource_type, '<resource_id_2>')

  # Verify display of populated Must Support elements
  for element_path in must_support_elements:
    assert client.is_element_displayed(populated_resource, element_path), f"Element '{element_path}' not displayed."

  # Verify handling of absent Must Support elements
  for element_path in must_support_elements:
    if not client.is_element_populated(partially_populated_resource, element_path):
      assert client.is_missing_element_handled(partially_populated_resource, element_path), f"Missing element '{element_path}' not handled appropriately."

# Test Case 2: Storage of Must Support elements
def test_store_must_support(client, resource_type, must_support_elements):
  # Retrieve stored test resources
  stored_populated_resource = client.get_stored_resource(resource_type, '<resource_id_1>')
  stored_partially_populated_resource = client.get_stored_resource(resource_type, '<resource_id_2>')

  # Verify storage of populated Must Support elements
  for element_path in must_support_elements:
    assert client.is_element_stored(stored_populated_resource, element_path), f"Element '{element_path}' not stored."

  # Verify handling of absent Must Support elements in storage
  for element_path in must_support_elements:
    if not client.is_element_populated(stored_partially_populated_resource, element_path):
      assert client.is_missing_element_handled_in_storage(stored_partially_populated_resource, element_path), f"Missing element '{element_path}' not handled appropriately in storage."
```

### 4. Potential Issues and Edge Cases

* **Complex Data Types:** The client may need to handle the display and storage of Must Support elements within complex data types (e.g., nested elements, arrays).
* **User Interface Variations:** Different UI elements or views within the client application may present Must Support data differently. Testing should cover all relevant UI components.
* **Data Sensitivity:**  The client should appropriately handle the display and storage of sensitive Must Support data, considering privacy and security concerns.
* **Performance:** Retrieving and processing large resources with numerous Must Support elements could impact performance.
* **Data Storage Format:** The test should consider various data storage formats used by the client (e.g., relational databases, NoSQL databases) and adapt validation checks accordingly. 


---

<a id='req-client-04'></a>

### REQ-CLIENT-04: No summary

**Description**: "Client SHALL interpret missing Must Support data elements as not present in the Health Plan API system."

**Actor**: Client (Application)

**Conformance**: SHALL

## Test Specification for REQ-CLIENT-04: Handling Missing Must Support Data Elements

### 1. Requirement Analysis

* **Testability Assessment:**  **Automatic** (can be automated with appropriate test tooling)
* **Complexity:** **Simple** 
* **Prerequisites:**
    * A running instance of the Health Plan API system under test.
    * A client application capable of making FHIR API calls.
    * Test data setup with resources containing both present and missing "Must Support" data elements.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * **READ:** Retrieve resources (e.g., Patient, Observation) from the Health Plan API.
* **Test Data Requirements:**
    * **Resource Type:**  Choose a resource type relevant to the Health Plan API (e.g., Patient).
    * **Must Support Elements:** Identify "Must Support" data elements within the chosen resource type as defined by the FHIR Implementation Guide.
    * **Test Data Variations:**
        * **Scenario 1 (Positive):** Resource with all "Must Support" elements present.
        * **Scenario 2 (Negative):** Resource with one or more "Must Support" elements missing. 
* **Validation Criteria:**
    * **Scenario 1:** The client should successfully process the resource and be able to access all "Must Support" elements.
    * **Scenario 2:** The client should NOT throw an error when encountering missing "Must Support" elements. The client should interpret these elements as not present in the Health Plan API system and handle them gracefully (e.g., by using default values, providing appropriate user feedback, or skipping logic dependent on those elements).

### 3. Pseudocode Implementation

```python
# Test Case: REQ-CLIENT-04 - Handling Missing Must Support Data Elements

def test_missing_must_support_elements(client, test_data):
  """
  Verifies that the client handles missing "Must Support" data elements gracefully.

  Args:
    client: The FHIR client instance.
    test_data: A dictionary containing test data with the following keys:
      - resource_type: The FHIR resource type (e.g., 'Patient').
      - resource_id_with_all_elements: The ID of a resource with all "Must Support" elements present.
      - resource_id_with_missing_elements: The ID of a resource with one or more "Must Support" elements missing.
  """

  # Scenario 1: Resource with all "Must Support" elements present
  try:
    response = client.read(test_data['resource_type'], test_data['resource_id_with_all_elements'])
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    # Add assertions to validate the presence of all "Must Support" elements in the response

  except Exception as e:
    assert False, f"Error retrieving resource with all 'Must Support' elements: {e}"

  # Scenario 2: Resource with missing "Must Support" elements
  try:
    response = client.read(test_data['resource_type'], test_data['resource_id_with_missing_elements'])
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    # Add assertions to validate that the client handles missing elements gracefully (e.g., no errors thrown)

  except Exception as e:
    assert False, f"Error retrieving resource with missing 'Must Support' elements: {e}"
```

### 4. Potential Issues and Edge Cases

* **Resource Variations:** Test with various resource types and different combinations of missing "Must Support" elements.
* **Data Types:** Consider different data types of "Must Support" elements (e.g., string, date, CodeableConcept) and how their absence might impact client logic.
* **Client-Specific Logic:** The test should account for how the client application specifically handles missing data. This might involve checking for default values, logging warnings, or providing user feedback.
* **Performance:**  If the client retrieves large resources, ensure that handling missing elements doesn't introduce performance bottlenecks.
* **Security:**  Verify that the client doesn't expose sensitive information or make incorrect assumptions based on the absence of "Must Support" data. 


---

<a id='req-client-05'></a>

### REQ-CLIENT-05: No summary

**Description**: "Client SHALL process resource instances containing Must Support data elements asserting missing information."

**Actor**: Client (Consumer App)

**Conformance**: SHALL

## Test Specification for REQ-CLIENT-05: Processing Must Support Data Elements with Missing Information

### 1. Requirement Analysis

* **Testability Assessment:**  Automatic
* **Complexity:** Moderate
* **Prerequisites:**
    * A running FHIR server with the target Implementation Guide loaded.
    * A test client capable of making FHIR API calls and parsing responses.
    * Test data containing resources with Must Support elements, including instances where data is asserted as missing.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * **READ:** Retrieve resources containing Must Support elements with missing data assertions.
* **Test Data Requirements:**
    * **Resource Type:**  Specify the resource type(s) to be tested (e.g., Patient, Observation).
    * **Must Support Elements:** Identify the specific Must Support elements within the chosen resource type.
    * **Missing Data Assertions:** Define how missing information is asserted (e.g., using `dataAbsentReason` extension with appropriate codes like "unknown", "not-asked", etc.).
* **Validation Criteria:**
    * **Successful Processing:** The client should successfully parse the resource without errors, even with the presence of Must Support elements asserting missing information.
    * **Appropriate Handling:** The client should handle missing data assertions according to the application's specific requirements. This might involve:
        * Displaying specific messages to the user.
        * Triggering workflows for data completion.
        * Logging the missing information for analysis.

### 3. Pseudocode Implementation

```python
# Test Case: Process Resource with Must Support Element Asserting Missing Information

def test_process_must_support_missing_data():
  """
  Verifies the client can process resources with Must Support elements 
  containing missing data assertions.
  """

  # 1. Prepare Test Data
  resource_type = "Patient"  # Replace with the desired resource type
  must_support_element = "birthDate"  # Replace with the actual element name
  test_patient = {
    "resourceType": resource_type,
    "name": [{"family": "Doe", "given": ["John"]}],
    must_support_element: {
      "extension": [
        {
          "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
          "valueCode": "unknown"
        }
      ]
    }
  }

  # 2. Send Request to FHIR Server
  response = fhir_client.create(resource_type, test_patient)

  # 3. Validate Response
  assert response.status_code == 201, f"Failed to create {resource_type} resource: {response.text}"

  # 4. Retrieve and Process the Resource
  retrieved_patient = fhir_client.read(resource_type, response.json()["id"])
  assert retrieved_patient.status_code == 200, f"Failed to read {resource_type} resource: {retrieved_patient.text}"

  # 5. Check for Successful Parsing and Handling of Missing Data Assertion
  # (Implementation-specific logic based on application requirements)
  if "dataAbsentReason" in retrieved_patient.json()[must_support_element]:
    # Handle missing data assertion (e.g., display message, log information)
    print(f"Must Support element '{must_support_element}' has missing data: {retrieved_patient.json()[must_support_element]}")
  else:
    raise AssertionError(f"Missing data assertion not found in Must Support element '{must_support_element}'")

```

### 4. Potential Issues and Edge Cases

* **Different Assertion Methods:** The test should cover various ways missing information is asserted (e.g., different `dataAbsentReason` codes, empty elements with specific flags).
* **Multiple Must Support Elements:** Test resources with multiple Must Support elements, some with and some without missing data assertions.
* **Resource Combinations:** Test different resource types and combinations of Must Support elements to ensure comprehensive coverage.
* **Performance:**  Evaluate the client's performance when processing resources with a large number of Must Support elements and missing data assertions.
* **Security:** Ensure that the client handles missing data assertions securely, especially when displaying information to users or triggering sensitive workflows. 


---

<a id='req-cache-01'></a>

### REQ-CACHE-01: Utilize appropriate methods for tracking directory content updates

**Description**: "Client SHOULD utilize the _lastUpdated search parameter to track additions or modifications to directory content. Client SHOULD periodically verify cached data existence using _id queries."

**Actor**: Client

**Conformance**: SHOULD

## Test Specification for REQ-CACHE-01: Utilize Appropriate Methods for Tracking Directory Content Updates

### 1. Requirement Analysis

* **Testability Assessment:** Hybrid (Automatic API calls with Manual verification of client behavior)
* **Complexity:** Moderate
* **Prerequisites:**
    * A running FHIR server with directory resources populated.
    * A client application configured to interact with the FHIR server.
    * Access to client-side caching mechanisms (if applicable).

### 2. Test Implementation Strategy

#### 2.1 Required FHIR Operations:

1. **Search Operation with _lastUpdated:**
    * `GET [base]/[resourceType]?_lastUpdated=gt[lastUpdatedTimestamp]`
    * Used to retrieve resources updated after a specific timestamp.
2. **Read Operation with _id:**
    * `GET [base]/[resourceType]/[id]`
    * Used to verify the existence of a specific resource.

#### 2.2 Test Data Requirements:

* **Initial Data:** A set of pre-existing directory resources on the server.
* **Updated Data:** Modifications or additions to existing resources, or new resources.
* **Timestamps:** Track timestamps for initial data load and subsequent updates.

#### 2.3 Validation Criteria:

* **Positive Test Cases:**
    * Verify the client successfully retrieves updated resources using `_lastUpdated`.
    * Verify the client correctly identifies and updates its cache with new/modified data.
    * Verify the client uses `_id` to confirm the existence of cached data before accessing the server.
* **Negative Test Cases:**
    * Verify the client handles scenarios where the `_lastUpdated` parameter returns no results (no updates).
    * Verify the client handles cases where `_id` queries return a 404 (resource not found) and refreshes its cache.

### 3. Pseudocode Implementation

```python
# Test Case: Verify client utilizes _lastUpdated and _id for cache management

def test_cache_management():
  # Setup
  initial_lastUpdated = get_current_timestamp()
  initial_resources = client.search_resources(resourceType, _lastUpdated=f"lt{initial_lastUpdated}")
  # Assuming client caches initial_resources

  # Trigger update on the server
  update_server_resources(resourceType)

  # Test _lastUpdated usage
  updated_resources = client.search_resources(resourceType, _lastUpdated=f"gt{initial_lastUpdated}")
  assert len(updated_resources) > 0, "Client failed to retrieve updated resources using _lastUpdated"

  # Test _id usage for cache validation
  for resource in initial_resources:
    try:
      client.get_resource(resourceType, resource.id) # Assuming client checks cache first
    except ResourceNotFoundException:
      # Cache miss - verify client fetches and updates cache
      fetched_resource = client.get_resource_from_server(resourceType, resource.id)
      assert fetched_resource is not None, "Client failed to fetch and update cache on resource not found"
    else:
      # Cache hit - no further action needed
      pass

  # Additional Assertions:
  # - Verify client cache content matches server state after updates
  # - Verify client handles pagination if the number of updated resources is large

# Helper functions
def get_current_timestamp():
  # ... returns current timestamp in FHIR format
def update_server_resources(resourceType):
  # ... performs updates on the server for the given resource type
```

### 4. Potential Issues and Edge Cases

* **Clock Synchronization:** Ensure client and server clocks are synchronized to avoid inaccurate `_lastUpdated` comparisons.
* **Resource Deletion:** Implement logic to handle deleted resources, potentially using the `_lastUpdated` parameter on the deletion time.
* **High Update Frequency:**  Consider performance implications of frequent polling with `_lastUpdated`. Implement appropriate caching strategies and backoff mechanisms.
* **Partial Updates:**  Ensure the client handles scenarios where only specific fields within a resource are updated.
* **Security:**  If using client-side caching, implement appropriate security measures to protect sensitive data. 


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

## Test Specification for REQ-RESOURCE-01

### 1. Requirement Analysis

**Testability Assessment:** Hybrid (Automatic for API interactions, Manual for profile conformance inspection)

**Complexity:** Moderate

**Prerequisites:**

* A running FHIR server that implements the target Implementation Guide.
* Test credentials (if applicable) to access the FHIR server.
* A FHIR client library or testing tool capable of making API requests and validating responses.
* Access to the defined Plan-Net profile definitions (StructureDefinitions).

### 2. Test Implementation Strategy

#### Required FHIR Operations:

* **Read:** `/ResourceTypeId/{id}` for each resource type.
* **Vread:** `/ResourceTypeId/{id}/_history/{vid}` for each resource type (SHOULD).
* **Search Type:** `/ResourceTypeId?parameter=value` for each resource type.

#### Test Data Requirements:

* **Valid Resources:**  At least one instance of each resource type (Endpoint, HealthcareService, InsurancePlan, Location, Organization) conforming to the specified Plan-Net profiles.
* **Invalid Resources:**  At least one instance of each resource type that violates the constraints defined in the Plan-Net profiles.
* **Search Parameters:**  A set of valid search parameters for each resource type as defined in the profiles and supported by the server.

#### Validation Criteria:

* **HTTP Status Codes:**
    * Successful requests (read, vread, search-type): 200 OK
    * Requests for non-existent resources: 404 Not Found
    * Requests with invalid parameters: 400 Bad Request
* **Resource Conformance:**
    * Returned resources MUST conform to the specified Plan-Net profiles. This can be validated using a FHIR validator tool.
* **Interaction Support:**
    * Server MUST respond correctly to all required interactions (read, search-type).
    * Server SHOULD respond correctly to the vread interaction.
* **Error Handling:**
    * Server should return appropriate OperationOutcome resources for errors.

### 3. Pseudocode Implementation

```python
# Test Suite: REQ-RESOURCE-01 - Resource Profiles and Interactions

# Resources to test
resources = [
    {"type": "Endpoint", "profile": "StructureDefinition-plannet-Endpoint.html"},
    {"type": "HealthcareService", "profile": "StructureDefinition-plannet-HealthcareService.html"},
    {"type": "InsurancePlan", "profile": "StructureDefinition-plannet-InsurancePlan.html"},
    {"type": "Location", "profile": "StructureDefinition-plannet-Location.html"},
    {"type": "Organization", "profile": "StructureDefinition-plannet-Network.html"},
    {"type": "Organization", "profile": "StructureDefinition-plannet-Organization.html"}
]

for resource in resources:
    # Test Read Interaction
    test_read_interaction(resource["type"])

    # Test Vread Interaction (SHOULD)
    test_vread_interaction(resource["type"])

    # Test Search-Type Interaction
    test_search_type_interaction(resource["type"])

    # Test Resource Conformance to Profile
    test_resource_conformance(resource["type"], resource["profile"])

# Function to test Read Interaction
def test_read_interaction(resource_type):
    # Construct the Read request URL
    url = f"/{resource_type}/{valid_resource_id}"
    
    # Make the request and store the response
    response = fhir_client.read(resource_type, valid_resource_id)

    # Assert response status code is 200 OK
    assert response.status_code == 200, f"Read interaction failed for {resource_type}. Expected 200, got {response.status_code}"

# Function to test Vread Interaction (SHOULD)
def test_vread_interaction(resource_type):
    # Construct the Vread request URL
    url = f"/{resource_type}/{valid_resource_id}/_history/{valid_version_id}"

    # Make the request and store the response
    response = fhir_client.vread(resource_type, valid_resource_id, valid_version_id)

    # Assert response status code is 200 OK
    assert response.status_code == 200, f"Vread interaction failed for {resource_type}. Expected 200, got {response.status_code}"

# Function to test Search-Type Interaction
def test_search_type_interaction(resource_type):
    # Construct the Search-Type request URL with valid search parameters
    url = f"/{resource_type}?{valid_search_parameter}={valid_search_value}"

    # Make the request and store the response
    response = fhir_client.search(resource_type, params={valid_search_parameter: valid_search_value})

    # Assert response status code is 200 OK
    assert response.status_code == 200, f"Search-Type interaction failed for {resource_type}. Expected 200, got {response.status_code}"

# Function to test Resource Conformance to Profile
def test_resource_conformance(resource_type, profile_url):
    # Retrieve a resource instance using Read interaction
    response = fhir_client.read(resource_type, valid_resource_id)

    # Validate the resource against the specified profile using a FHIR validator
    validation_result = validate_resource(response.json(), profile_url)

    # Assert validation is successful
    assert validation_result.success, f"Resource conformance failed for {resource_type} against profile {profile_url}. Errors: {validation_result.errors}"
```

### 4. Potential Issues and Edge Cases:

* **Profile Validation:**  Automated profile validation can be complex. Ensure the chosen validator and its configuration are appropriate for the Plan-Net profiles.
* **Search Parameter Coverage:**  Testing all possible search parameters can be extensive. Prioritize testing commonly used and clinically relevant parameters.
* **Data Setup and Teardown:**  Ensure test data is correctly loaded and cleaned up after each test run to avoid conflicts.
* **Performance:**  Consider performance implications of large datasets and complex searches.
* **Security:**  Use appropriate authentication and authorization mechanisms for accessing the FHIR server.
* **Edge Cases:** Test with resources containing optional elements, extensions, and edge-case data values to ensure robust validation. 


---

<a id='req-resource-02'></a>

### REQ-RESOURCE-02: Support required search parameters

**Description**: "Server SHALL support all search parameters defined for each Plan-Net resource profile."

**Actor**: Server

**Conformance**: SHALL

## Test Specification: REQ-RESOURCE-02 - Support Required Search Parameters

### 1. Requirement Analysis

**Testability Assessment:** Automatic
**Complexity:** Moderate
**Prerequisites:**
    * A running FHIR server conforming to the implementation guide.
    * Knowledge of the base Plan-Net resource profiles and their defined search parameters.
    * Test data loaded into the FHIR server representing valid Plan-Net resources.

### 2. Test Implementation Strategy

**Required FHIR Operations:**
    * `GET [base]/PlanNet?{search-parameter}={search-value}`

**Test Data Requirements:**
    * A set of Plan-Net resources loaded into the server with varying values for each search parameter defined in their respective profiles.

**Validation Criteria:**
    * **HTTP Status Code:** Verify a `200 OK` response for valid searches.
    * **Response Content:**
        * The response bundle SHOULD contain only resources matching the search criteria.
        * The response bundle SHOULD include all resources matching the search criteria.
    * **Error Handling:**
        * Verify appropriate HTTP status codes (e.g., `400 Bad Request`) and OperationOutcome resources are returned for invalid search parameters or values.

### 3. Pseudocode Implementation

```python
# Define a function to test a single search parameter
def test_search_parameter(resource_type, search_parameter, search_value):
  """
  Tests a single search parameter for a given resource type.

  Args:
    resource_type: The FHIR resource type (e.g., "PlanDefinition").
    search_parameter: The name of the search parameter to test.
    search_value: The value to search for.

  Returns:
    True if the search is successful and meets validation criteria, False otherwise.
  """

  # Construct the search URL
  search_url = f"{base_url}/{resource_type}?{search_parameter}={search_value}"

  # Execute the search request
  response = requests.get(search_url, headers=headers)

  # Validate the response
  if response.status_code == 200:
    # Parse the response bundle
    bundle = fhir_parser.parse_resource(response.text)

    # Check if all resources in the bundle match the search criteria
    for entry in bundle.entry:
      resource = entry.resource
      # Implement logic to check if the resource matches the search criteria
      # based on the specific search parameter and value.
      if not resource_matches_criteria(resource, search_parameter, search_value):
        print(f"ERROR: Resource {resource.id} does not match search criteria.")
        return False

    # Check if the bundle contains all expected resources (This might require additional logic)
    if not all_expected_resources_present(bundle, resource_type, search_parameter, search_value):
      print(f"ERROR: Not all expected resources found for search criteria.")
      return False

    print(f"SUCCESS: Search parameter '{search_parameter}' validated successfully.")
    return True
  else:
    print(f"ERROR: Unexpected status code: {response.status_code}")
    print(response.text)
    return False

# Main test execution
for resource_type in plan_net_resource_types:
  # Retrieve the search parameters defined for the resource profile
  search_parameters = get_search_parameters_from_profile(resource_type)

  # Iterate through each search parameter and execute the test
  for search_parameter in search_parameters:
    # Retrieve test data for the specific search parameter
    test_data = get_test_data(resource_type, search_parameter)

    # Iterate through each test data item and execute the search
    for data_item in test_data:
      search_value = data_item["search_value"]
      test_result = test_search_parameter(resource_type, search_parameter, search_value)

      # Log the test result
      if test_result:
        print(f"Test Passed for {resource_type} - {search_parameter}:{search_value}")
      else:
        print(f"Test Failed for {resource_type} - {search_parameter}:{search_value}")
```

### 4. Potential Issues and Edge Cases

* **Complex Search Parameters:**  The pseudocode assumes simple equality checks for search parameters. More complex parameters (e.g., date ranges, token systems) will require additional logic.
* **Pagination:** If the number of matching resources exceeds the server's page size, the test needs to handle pagination to ensure all resources are validated.
* **Performance:**  Testing with a large dataset can be time-consuming. Consider optimizing test data and search queries for performance.
* **Security:**  Ensure test data does not contain sensitive information and that the test environment is appropriately secured.
* **Data Variations:** Test with various data types, including edge cases like empty strings, special characters, and very long values, to ensure robust handling.
* **Search Parameter Combinations:**  Consider testing combinations of search parameters to ensure they function correctly together.

This test specification provides a starting point for testing the "Support required search parameters" requirement. The specific implementation will need to be adapted based on the implementation guide's details and the testing framework used. 


---

<a id='req-resource-03'></a>

### REQ-RESOURCE-03: Support required _includes and _revincludes

**Description**: "Server SHALL support all _includes and _revincludes defined for each Plan-Net resource profile."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-RESOURCE-03: Support Required _includes and _revincludes

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Moderate
* **Prerequisites:**
    * A running FHIR server that implements the Plan-Net Implementation Guide.
    * Access to the CapabilityStatement of the server to identify supported _include and _revinclude parameters for each Plan-Net resource profile.
    * Test data consisting of various Plan-Net resources with established relationships that can be tested with _include and _revinclude parameters.

### 2. Test Implementation Strategy

* **Required FHIR Operations:** 
    * `GET` requests to read resources with specific _include and _revinclude parameters.
* **Test Data Requirements:**
    * A set of Plan-Net resources with pre-defined relationships. For example:
        * A `Coverage` resource linked to a `Patient` resource.
        * A `Claim` resource linked to a `Coverage` and a `Practitioner` resource.
    * The specific _include and _revinclude parameters defined for each Plan-Net resource profile in the Implementation Guide.
* **Validation Criteria:**
    * Verify that the response for each request includes the correct related resources as specified by the _include or _revinclude parameter.
    * Verify that the response code is 200 (OK) for successful requests.
    * Verify that the response conforms to the FHIR specification and any additional constraints defined in the Plan-Net Implementation Guide.

### 3. Pseudocode Implementation

```python
# Test Case: Verify _include functionality for Coverage resource

def test_coverage_include_patient():
  """
  Tests if the server correctly includes the Patient resource 
  when using the _include parameter with Coverage.
  """

  # 1. Retrieve the Coverage resource ID with a known linked Patient.
  coverage_id = get_coverage_id_with_patient()

  # 2. Construct the URL with the _include parameter.
  url = f"{fhir_server_base_url}/Coverage/{coverage_id}?_include=Coverage:patient"

  # 3. Make the GET request.
  response = requests.get(url, headers=fhir_headers)

  # 4. Assertions.
  assert response.status_code == 200, f"Request failed: {response.text}"
  assert "Patient" in response.json()["included"][0]["resource"]["resourceType"], "Patient resource not included."

# Test Case: Verify _revinclude functionality for Patient resource

def test_patient_revinclude_coverage():
  """
  Tests if the server correctly includes the Coverage resource 
  when using the _revinclude parameter with Patient.
  """

  # 1. Retrieve a Patient resource ID with a known linked Coverage.
  patient_id = get_patient_id_with_coverage()

  # 2. Construct the URL with the _revinclude parameter.
  url = f"{fhir_server_base_url}/Patient/{patient_id}?_revinclude=Coverage:patient"

  # 3. Make the GET request.
  response = requests.get(url, headers=fhir_headers)

  # 4. Assertions.
  assert response.status_code == 200, f"Request failed: {response.text}"
  assert "Coverage" in response.json()["included"][0]["resource"]["resourceType"], "Coverage resource not included."

# Additional test cases for other resources and combinations of _include/_revinclude parameters should be added.
```

### 4. Potential Issues and Edge Cases

* **Circular References:** The Implementation Guide should define how to handle circular references when using _include and _revinclude to avoid infinite loops. Tests should cover these scenarios.
* **Performance:**  Excessive use of _include and _revinclude can impact performance. Tests should consider realistic scenarios and evaluate response times.
* **Security and Privacy:** Ensure that sensitive information is not inadvertently exposed through _include and _revinclude. Tests should verify that authorization mechanisms are correctly enforced.
* **Unsupported Combinations:** The server might not support all possible combinations of _include and _revinclude parameters. Tests should verify the server's behavior in such cases and ensure appropriate error handling.
* **Parameter Validation:** The server should correctly validate the provided _include and _revinclude parameters and return an error for invalid values. Tests should include invalid parameters to verify this behavior. 


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

## Test Specification for REQ-SERVER-01: RESTful Behavior and Response Codes

### 1. Requirement Analysis

**Testability Assessment:** Automatic
**Complexity:** Moderate
**Prerequisites:**
* A running FHIR server that implements the target API version.
* Test client capable of making FHIR API calls (e.g., Postman, RestAssured).
* Authentication credentials if required by the server.
* Pre-populated resources for testing 410 Gone (deleted resource) scenario.

### 2. Test Implementation Strategy

**Required FHIR Operations:**
* `GET`, `POST`, `PUT`, `DELETE` requests to various resources.

**Test Data Requirements:**
* Valid and invalid resource instances (JSON or XML) for different FHIR resources.
* Valid and invalid search parameters for `GET` requests.
* Resource IDs for existing and non-existing resources.

**Validation Criteria:**
* Verify the returned HTTP status code matches the expected code for each scenario.
* Optionally, verify the response body contains relevant error messages for negative test cases.

### 3. Pseudocode Implementation

```python
# Test Case 1: 400 Bad Request (invalid parameter)
function test_bad_request():
  # Construct an invalid GET request with an invalid search parameter
  response = send_request("GET", "/Patient?invalidParameter=value")
  assert response.status_code == 400
  # Optionally, assert the response body contains an error message

# Test Case 2: 401 Unauthorized
function test_unauthorized():
  # Send a request without authentication or with invalid credentials
  response = send_request("GET", "/Patient") 
  assert response.status_code == 401

# Test Case 3: 403 Forbidden (insufficient scope)
function test_forbidden():
  # Assuming user has insufficient scope for creating Patient resources
  response = send_request("POST", "/Patient", data=valid_patient_resource)
  assert response.status_code == 403

# Test Case 4: 404 Not Found (unknown resource)
function test_not_found():
  # Request a non-existing resource ID
  response = send_request("GET", "/Patient/non-existing-id")
  assert response.status_code == 404

# Test Case 5: 410 Gone (deleted resource)
function test_gone():
  # Assuming a resource with id 'deleted-resource-id' was previously deleted
  response = send_request("GET", "/Patient/deleted-resource-id")
  assert response.status_code == 410

# Positive Test Case: 200 OK (successful GET request)
function test_successful_get():
  response = send_request("GET", "/Patient")
  assert response.status_code == 200

# Helper function to send requests with optional authentication and data
function send_request(method, endpoint, data=None, headers=None):
  # Implement logic to send the request using chosen test client
  # Include authentication headers if required
  # Return the response object
```

### 4. Potential Issues and Edge Cases

* **Server-specific error handling:** The FHIR specification provides guidelines, but servers might have custom error message formats. Tests should be adaptable to handle variations.
* **Authentication and authorization complexity:** Testing various authorization scenarios with different user roles and permissions can be complex.
* **Resource lifecycle management:** For testing `410 Gone`, ensure resources are properly created and deleted within the test setup and teardown phases.
* **Performance testing:** While not explicitly mentioned in the requirement, consider adding performance tests for different response codes under load to ensure server stability.
* **Security considerations:**  Ensure test data doesn't contain sensitive information. Test for potential vulnerabilities like information leakage in error messages. 


---

<a id='req-server-02'></a>

### REQ-SERVER-02: Support JSON format and identify supported profiles

**Description**: "Server SHALL support JSON format for all interactions and identify supported Plan-Net profiles in the `meta.profile` attribute of each resource instance."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-SERVER-02: Support JSON format and identify supported profiles

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running FHIR server that implements the Plan-Net Implementation Guide.
    * A test client capable of making FHIR API calls and parsing JSON responses.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * **READ:**  `/PlanDefinition` (or any other resource type defined in Plan-Net)
* **Test Data Requirements:**
    * No specific test data is required. Any valid resource instance conforming to a Plan-Net profile can be used.
* **Validation Criteria:**
    * **Response Format:** The server MUST return a valid JSON response for the requested resource.
    * **Content-Type Header:** The response MUST include a `Content-Type` header with the value `application/fhir+json`.
    * **Profile Identification:** The returned resource instance MUST include a `meta.profile` element.
    * **Profile Validity:** The value(s) in the `meta.profile` element MUST be valid URLs pointing to the Plan-Net profile(s) the resource conforms to.

### 3. Pseudocode Implementation

```python
# Test Case: Verify JSON support and profile identification

def test_json_support_and_profile_identification(fhir_client):
  """
  Tests that the server supports JSON format and identifies supported profiles.
  """

  # 1. Send a READ request for a PlanDefinition resource
  response = fhir_client.read('PlanDefinition', '123') # Replace '123' with a valid resource ID

  # 2. Check for successful response
  assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

  # 3. Verify Content-Type header
  assert response.headers['Content-Type'] == 'application/fhir+json', "Content-Type header should be 'application/fhir+json'"

  # 4. Parse the JSON response
  try:
    resource = response.json()
  except json.JSONDecodeError:
    assert False, "Response is not valid JSON"

  # 5. Verify presence and validity of meta.profile
  assert 'meta' in resource and 'profile' in resource['meta'], "Resource is missing 'meta.profile' element"
  
  for profile_url in resource['meta']['profile']:
    assert is_valid_url(profile_url), f"Invalid profile URL: {profile_url}"
    assert "http://hl7.org/fhir/PlanNet/" in profile_url, f"Profile URL does not belong to Plan-Net: {profile_url}"

  print("Test passed successfully.")

# Helper function to validate URLs
def is_valid_url(url):
  """
  Checks if the given string is a valid URL.
  """
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False
```

### 4. Potential Issues and Edge Cases

* **Multiple Profiles:** The resource might conform to multiple Plan-Net profiles. The test should verify all listed profiles.
* **Profile Cardinality:** The test should handle cases where `meta.profile` might be absent (if not required by the base FHIR specification) or contain zero or multiple profile URLs.
* **Performance:**  Repeatedly fetching large resources can impact performance. Consider using smaller resources or mocking the server response for performance testing.
* **Security:** Ensure the test client uses appropriate authentication and authorization mechanisms if the FHIR server requires them. 


---

<a id='req-server-03'></a>

### REQ-SERVER-03: Support combined search parameters and chaining

**Description**: "Server SHALL support search parameters individually and in combination. Server SHALL support forward and reverse chaining for search parameters with the 'chain' property."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-SERVER-03: Combined Search Parameters and Chaining

### 1. Requirement Analysis

- **Testability Assessment:** Automatic
- **Complexity:** Moderate
- **Prerequisites:**
    - A running FHIR server that implements the target Implementation Guide.
    - Pre-populated FHIR resources with relationships that can be used for chaining. For example:
        - Patients with linked Observations.
        - Encounters with linked Practitioners and Organizations.

### 2. Test Implementation Strategy

#### 2.1 Required FHIR Operations

- **Search:**  `/Resource?search-param1=value1&search-param2=value2` (for combined search)
- **Search with chaining:** `/Resource?param1=value1&_has:ResourceType:search-param2=value2` (for forward chaining)
- **Search with reverse chaining:** `/Resource?param1=value1&_has:ResourceType:search-param1:inclusion=this` (for reverse chaining)

#### 2.2 Test Data Requirements

- **Patients:**
    - Patient 1: `{"resourceType": "Patient", "gender": "male", "birthDate": "1980-01-01"}`
    - Patient 2: `{"resourceType": "Patient", "gender": "female", "birthDate": "1975-05-05"}`
- **Observations:**
    - Observation 1: `{"resourceType": "Observation", "status": "final", "subject": {"reference": "Patient/1"}}`
    - Observation 2: `{"resourceType": "Observation", "status": "preliminary", "subject": {"reference": "Patient/2"}}`

#### 2.3 Validation Criteria

- **HTTP Status Code:** 200 (OK) for successful searches.
- **Content-Type:** `application/fhir+json`
- **Resource Type:** Bundle with entries matching the search criteria.
- **Combined Search:** Verify the returned resources match all specified search parameters.
- **Forward Chaining:** Verify the returned resources have the specified relationship with other resources matching the chained search parameters.
- **Reverse Chaining:** Verify the returned resources are referenced by other resources matching the chained search parameters.

### 3. Pseudocode Implementation

```python
# Test Case 1: Combined Search
def test_combined_search(fhir_client):
  """Verify server supports combined search parameters."""
  response = fhir_client.search('Patient', params={'gender': 'male', 'birthdate': 'ge1980-01-01'})
  assert response.status_code == 200
  assert 'application/fhir+json' in response.headers['Content-Type']
  assert len(response.json()['entry']) > 0  # Assuming data exists

# Test Case 2: Forward Chaining
def test_forward_chaining(fhir_client):
  """Verify server supports forward chaining with _has parameter."""
  response = fhir_client.search('Patient', params={'_has': 'Observation:subject:status=final'})
  assert response.status_code == 200
  assert 'application/fhir+json' in response.headers['Content-Type']
  # Verify returned Patients have Observations with status 'final'
  for entry in response.json()['entry']:
    patient_id = entry['resource']['id']
    observation_response = fhir_client.search('Observation', params={'subject': f'Patient/{patient_id}', 'status': 'final'})
    assert observation_response.status_code == 200
    assert len(observation_response.json()['entry']) > 0

# Test Case 3: Reverse Chaining
def test_reverse_chaining(fhir_client):
  """Verify server supports reverse chaining with _has parameter and inclusion."""
  response = fhir_client.search('Observation', params={'status': 'final', '_has': 'Observation:subject:Patient:_id:inclusion=this'})
  assert response.status_code == 200
  assert 'application/fhir+json' in response.headers['Content-Type']
  # Verify returned Observations are linked to Patients
  for entry in response.json()['entry']:
    assert 'subject' in entry['resource'] and 'reference' in entry['resource']['subject']

# Error Handling Example
def test_invalid_search_parameter(fhir_client):
  """Verify server returns an error for invalid search parameters."""
  response = fhir_client.search('Patient', params={'invalid-param': 'value'})
  assert response.status_code == 400  # Or another appropriate error code
```

### 4. Potential Issues and Edge Cases

- **Performance:** Test with large datasets to assess performance impact of complex chained searches.
- **Security:** Ensure chained searches respect authorization and access control rules.
- **Chaining Depth:** Test with multiple levels of chaining to ensure correct functionality and performance.
- **Parameter Combinations:** Test various combinations of search parameters, including optional parameters and modifiers.
- **Resource Types:** Conduct tests with different resource types and their specific search parameters and chaining capabilities.
- **Error Handling:** Verify appropriate error responses for invalid search parameters, chaining syntax errors, and unauthorized requests. 


---

<a id='req-server-04'></a>

### REQ-SERVER-04: Support XML format

**Description**: "Server SHOULD support XML format for all interactions."

**Actor**: Server

**Conformance**: SHOULD

## Test Specification: REQ-SERVER-04 - Support XML Format

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running FHIR server under test.
    * A test client capable of sending requests and receiving responses in XML format.
    * Test data in FHIR XML format (can be minimal, like a Patient resource).

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * **Read:** `GET [base]/[resourceType]/[id]`
    * **Create:** `POST [base]/[resourceType]`
    * **Update:** `PUT [base]/[resourceType]/[id]`
    * **Delete:** `DELETE [base]/[resourceType]/[id]`
    * **Search:** `GET [base]/[resourceType]?search parameters`
* **Test Data Requirements:**
    * A valid FHIR resource in XML format (e.g., Patient).
* **Validation Criteria:**
    * **HTTP Status Code:** Verify the server returns a success status code (2xx) for valid requests and appropriate error codes (4xx/5xx) for invalid requests.
    * **Content-Type Header:** Verify the server responds with `Content-Type: application/fhir+xml` for successful requests.
    * **Response Body:** Verify the response body is a valid FHIR resource in XML format.

### 3. Pseudocode Implementation

```python
# Test Case: REQ-SERVER-04 - XML Support

# Test Data
resource_type = "Patient"
test_patient_xml = """
<Patient xmlns="http://hl7.org/fhir">
  <id value="test-patient"/>
  <name>
    <family value="Test"/>
    <given value="Patient"/>
  </name>
</patient>
"""

# Test Function
def test_xml_support(fhir_client):
  """
  Tests XML support for various FHIR interactions.

  Args:
    fhir_client: An instance of a FHIR client library.
  """

  # Test Read Operation
  try:
    response = fhir_client.read(resource_type, "test-patient", format="xml")
    assert response.status_code == 200, f"Read operation failed with status code: {response.status_code}"
    assert response.headers["Content-Type"] == "application/fhir+xml", f"Invalid Content-Type header: {response.headers['Content-Type']}"
    # Validate response body is a valid FHIR resource in XML format
  except Exception as e:
    assert False, f"Read operation failed with exception: {e}"

  # Test Create Operation
  try:
    response = fhir_client.create(resource_type, test_patient_xml, format="xml")
    assert response.status_code in [201, 200], f"Create operation failed with status code: {response.status_code}"
    assert response.headers["Content-Type"] == "application/fhir+xml", f"Invalid Content-Type header: {response.headers['Content-Type']}"
    # Validate response body is a valid FHIR resource in XML format
  except Exception as e:
    assert False, f"Create operation failed with exception: {e}"

  # Test Update Operation (using the created resource ID)
  # ... similar to Create operation ...

  # Test Delete Operation (using the created resource ID)
  # ... similar to Read operation ...

  # Test Search Operation
  try:
    response = fhir_client.search(resource_type, params={"family": "Test"}, format="xml")
    assert response.status_code == 200, f"Search operation failed with status code: {response.status_code}"
    assert response.headers["Content-Type"] == "application/fhir+xml", f"Invalid Content-Type header: {response.headers['Content-Type']}"
    # Validate response body is a valid FHIR Bundle in XML format
  except Exception as e:
    assert False, f"Search operation failed with exception: {e}"

```

### 4. Potential Issues and Edge Cases

* **Large Resources:** Test with large resources to assess performance impact of XML parsing and serialization.
* **Invalid XML:** Test with invalid XML to ensure the server returns appropriate error messages and doesn't crash.
* **Specific XML Features:** Test with XML features like namespaces and CDATA sections to ensure compatibility.
* **Security Considerations:** Ensure the server handles XML external entity (XXE) vulnerabilities.
* **Resource Validation:** While not explicitly mentioned in the requirement, consider validating the returned XML resources against the FHIR schema to ensure data integrity. 


---

