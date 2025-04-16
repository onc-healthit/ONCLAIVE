# Consolidated Test Plan for Plan Net

## Generated on: 2025-04-02 12:16:24

## Table of Contents

- [**Functional Area**](#**functional-area**)
  - [REQ-001-000-03: Application shall not send consumer identifiable information.](#req-001-000-03)
  - [REQ-001-000-08: Application should be able to display or store Must Support data elements.](#req-001-000-08)
- [**Implementation Pattern**](#**implementation-pattern**)
  - [REQ-001-000-07: Application shall process resource instances containing Must Support data elements without errors.](#req-001-000-07)
  - [REQ-001-000-10: Application (Consumer App) shall process resource instances containing Must Support data elements with missing information.](#req-001-000-10)
- [**Search**](#**search**)
  - [REQ-001-000-12: Application should track content changes using the _lastUpdated search parameter.](#req-001-000-12)
- [**System Component**](#**system-component**)
  - [REQ-001-000-13: Application should periodically check for deleted data using the _id search parameter.](#req-001-000-13)
- [Data Validation](#data-validation)
  - [REQ-001-000-09: Application shall interpret missing Must Support data elements as data not present.](#req-001-000-09)
- [Server](#server)
  - [REQ-001-000-01: Server shall not require authentication.](#req-001-000-01)
  - [REQ-001-000-02: Server shall not store consumer identifiable information.](#req-001-000-02)
  - [REQ-001-000-04: Server shall populate all Must Support data elements in query results.](#req-001-000-04)
  - [REQ-001-000-05: Server shall not include missing Must Support data elements with minimum cardinality 0.](#req-001-000-05)
  - [REQ-001-000-06: Server shall send reason for missing Must Support data elements with minimum cardinality > 0.](#req-001-000-06)
  - [REQ-001-000-11: Server shall provide the lastUpdate timestamp in profiles.](#req-001-000-11)

## Test Specifications

<a id='**functional-area**'></a>

## **Functional Area**

<a id='req-001-000-03'></a>

### REQ-001-000-03: Application shall not send consumer identifiable information.

**Description**: "A directory mobile application shall not send consumer identifiable information when querying a Plan-Net service."

**Actor**: Application

**Conformance**: SHALL NOT

## Test Specification for REQ-001-000-03

**1. Requirement Analysis**

* **Testability Assessment:** Hybrid (Combination of automated API testing and manual inspection of logs/traffic)
* **Complexity:** Moderate 
* **Prerequisites:**
    * A running instance of the directory mobile application.
    * Access to the Plan-Net service with appropriate authentication.
    * Tools for capturing and inspecting network traffic (e.g., Fiddler, Wireshark).
    * A list of data elements considered "consumer identifiable information" according to the relevant privacy regulations and context (e.g., name, address, date of birth, social security number, medical record number).

**2. Test Implementation Strategy**

* **Required FHIR Operations:**
    * **Search:** Execute various search operations against the Plan-Net service that the mobile application is designed to perform.
* **Test Data Requirements:**
    * **Valid Search Parameters:** A set of valid search parameters that the application uses for querying Plan-Net.
    * **Potentially Identifiable Data:**  A list of data elements classified as "consumer identifiable information." 
* **Validation Criteria:**
    * **Network Traffic Inspection:** Analyze the captured network traffic between the application and Plan-Net service. Verify that none of the "consumer identifiable information" is present in:
        * Request URLs
        * Request headers
        * Request bodies
    * **Application Logs (Optional):**  If available, review application logs for any evidence of attempts to send identifiable information.

**3. Pseudocode Implementation**

```python
# Test Case: TC_REQ_001_000_03_001 - Verify no identifiable information is sent during search

def test_no_identifiable_info_sent():
  """
  This test case verifies that the application does not send consumer 
  identifiable information when querying the Plan-Net service.
  """

  # 1. Start network traffic capture.
  start_traffic_capture()

  # 2. Define valid search parameters (excluding identifiable information)
  search_params = {
    "type": "Practitioner",
    "specialty": "Cardiology" 
  }

  # 3. Execute the search operation using the mobile application.
  search_results = app.search_plan_net(search_params)

  # 4. Stop network traffic capture.
  stop_traffic_capture()

  # 5. Analyze captured network traffic.
  traffic_data = get_captured_traffic()

  # 6. Define list of identifiable information fields.
  identifiable_fields = ["name", "address", "birthDate", "ssn", "medicalRecordNumber"]

  # 7. Assert that no identifiable information is present in the traffic.
  for field in identifiable_fields:
    assert not is_field_present_in_traffic(traffic_data, field), \
      f"Identifiable information '{field}' found in network traffic."

  # 8. (Optional) Analyze application logs for any related errors or warnings.
  analyze_app_logs()
```

**4. Potential Issues and Edge Cases**

* **Data Encoding:**  The application might attempt to obfuscate or encode identifiable information. The test should consider various encoding techniques and data formats.
* **Indirect Identifiers:**  The application might send data that can be combined with other information to re-identify individuals (e.g., rare medical conditions, specific dates).
* **Caching:**  The application might cache data locally, which could include identifiable information. The test should account for caching mechanisms.
* **Third-Party Libraries:**  Third-party libraries used by the application might have different data handling practices. 
* **Performance:**  Capturing and analyzing network traffic can be resource-intensive, especially for large data transfers.

**Security Considerations:**

* **Data Sanitization:**  Ensure that any test data used, especially for identifiable information, is properly sanitized and does not contain real user data.
* **Secure Test Environment:** Conduct testing in a controlled environment isolated from production systems to prevent accidental data leaks. 


---

<a id='req-001-000-08'></a>

### REQ-001-000-08: Application should be able to display or store Must Support data elements.

**Description**: "The application should be capable of displaying the data elements for human use or storing the information for other purposes."

**Actor**: Application

**Conformance**: SHOULD

## Test Specification for REQ-001-000-08: Display or Store Must Support Data Elements

### 1. Requirement Analysis

* **Testability Assessment:** Hybrid (Combination of Automatic and Manual)
* **Complexity:** Moderate
* **Prerequisites:**
    * A running instance of the application under test.
    * Access to the application's user interface (for display testing).
    * Access to the application's data storage (for storage testing).
    * A list of Must Support data elements defined in the FHIR Implementation Guide.
    * Test FHIR resources containing the Must Support data elements.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * **Create:** Send a POST request to create a new resource containing Must Support data elements.
    * **Read:** Send a GET request to retrieve the created resource.
    * **Search:** (Optional) Send a GET request with search parameters to retrieve resources containing specific Must Support data elements.

* **Test Data Requirements:**
    * **Valid FHIR Resources:** Create various FHIR resources (e.g., Patient, Observation) containing the Must Support data elements.
    * **Invalid FHIR Resources:** (Optional) Create FHIR resources with missing or invalid values for Must Support data elements to test error handling.

* **Validation Criteria:**
    * **Display:** Manually verify that the application's user interface displays all Must Support data elements correctly and in a user-friendly manner.
    * **Storage:** 
        * Automatically verify that the application successfully stores all Must Support data elements received via the API.
        * Query the data storage directly to confirm the presence and accuracy of the stored Must Support data elements.

### 3. Pseudocode Implementation

```python
# Test Case 1: Display and Store Must Support Data Elements

# Step 1: Prepare Test Data
test_patient = {
    "resourceType": "Patient",
    "name": [{"family": "Test", "given": ["John"]}],
    "birthDate": "1980-01-01",
    # ... other Must Support data elements for Patient resource
}

# Step 2: Create Resource via API
response = send_fhir_request("POST", "/Patient", test_patient)

# Step 3: Validate API Response
assert response.status_code == 201, f"Failed to create Patient: {response.text}"
patient_id = response.json()["id"]

# Step 4: Retrieve Resource via API
response = send_fhir_request("GET", f"/Patient/{patient_id}")

# Step 5: Validate Retrieved Data
assert response.status_code == 200, f"Failed to retrieve Patient: {response.text}"
retrieved_patient = response.json()
# Assert that all Must Support data elements are present and match the original values

# Step 6: Manually Verify Display (in UI)
# Navigate to the Patient details page in the application
# Visually inspect that all Must Support data elements are displayed correctly

# Step 7: Verify Storage (optional, depending on access)
# Query the application's database directly to confirm the presence and accuracy of stored Must Support data elements

# Test Case 2: Handle Missing Must Support Data Elements (Negative Test)

# ... Similar to Test Case 1, but with missing or invalid data elements
# Validate that the application handles these cases gracefully, either rejecting the request or providing appropriate error messages.
```

### 4. Potential Issues and Edge Cases

* **Data Type Validation:** Ensure the application correctly validates the data types of Must Support elements.
* **Code System Validation:** Verify that the application enforces any specified code systems for coded Must Support elements.
* **Localization:** Test the display of Must Support data elements in different languages and locales.
* **Performance:** Consider the performance impact of storing and retrieving large volumes of data for Must Support elements.
* **Security:** Ensure that sensitive Must Support data elements are handled securely, both in storage and during display.

This test specification provides a comprehensive framework for testing the requirement. The specific implementation details and test cases will need to be tailored based on the specific FHIR Implementation Guide and the application under test. 


---



<a id='**implementation-pattern**'></a>

## **Implementation Pattern**

<a id='req-001-000-07'></a>

### REQ-001-000-07: Application shall process resource instances containing Must Support data elements without errors.

**Description**: "The application shall be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."

**Actor**: Application

**Conformance**: SHALL

## Test Specification for REQ-001-000-07: Processing Must Support Data Elements

### 1. Requirement Analysis

**Testability Assessment:** Automatic
**Complexity:** Moderate
**Prerequisites:**
* A running instance of the application under test.
* Access to the FHIR server used by the application.
* A list of resources and their "Must Support" data elements as defined by the relevant FHIR Implementation Guide.
* Test data generation capabilities for creating FHIR resources.

### 2. Test Implementation Strategy

**Required FHIR Operations:**
* **Create:**  POST [FHIR Server Base URL]/[Resource Type]
* **Read:** GET [FHIR Server Base URL]/[Resource Type]/[ResourceId]

**Test Data Requirements:**
* For each resource type relevant to the application:
    * Generate valid FHIR resource instances.
    * Include all "Must Support" data elements with valid values according to their data types and constraints.
* Generate a second set of resources with missing "Must Support" elements.

**Validation Criteria:**
* **Positive Test Cases:**
    * The application should successfully create the resource via the FHIR API without returning an error.
    * The application should be able to retrieve the created resource via the FHIR API without returning an error.
    * Verify that the returned resource contains all the "Must Support" data elements as provided in the initial request.
* **Negative Test Cases:**
    * The application should gracefully handle resources with missing "Must Support" elements.
    * The behavior (rejection, default values, etc.) should be documented in the implementation guide and tested accordingly.

### 3. Pseudocode Implementation

```python
# Import necessary libraries (e.g., requests for API calls, json for data handling)

def test_must_support_elements(resource_type, test_data):
  """
  Tests the application's ability to process Must Support data elements.

  Args:
    resource_type: The type of FHIR resource being tested (e.g., "Patient", "Observation").
    test_data: A dictionary containing two lists of test resources:
      - "valid_resources": Resources with all Must Support elements.
      - "invalid_resources": Resources with missing Must Support elements.

  Returns:
    A list of dictionaries, each containing the test result details.
  """

  results = []

  # Positive Test Cases
  for resource in test_data["valid_resources"]:
    try:
      # Create the resource
      response = requests.post(f"{FHIR_SERVER_URL}/{resource_type}", json=resource)
      response.raise_for_status()  # Raise an exception for bad status codes

      # Retrieve the created resource
      resource_id = response.json()["id"]
      get_response = requests.get(f"{FHIR_SERVER_URL}/{resource_type}/{resource_id}")
      get_response.raise_for_status()

      # Validate the returned resource (check for presence of Must Support elements)
      assert all(element in get_response.json() for element in MUST_SUPPORT_ELEMENTS[resource_type]), "Missing Must Support element"

      results.append({"resource": resource, "result": "Pass", "message": "Resource processed successfully"})

    except Exception as e:
      results.append({"resource": resource, "result": "Fail", "message": str(e)})

  # Negative Test Cases (implementation-dependent)
  for resource in test_data["invalid_resources"]:
    try:
      # Attempt to create the resource (expecting specific behavior)
      response = requests.post(f"{FHIR_SERVER_URL}/{resource_type}", json=resource)

      # Validate the response based on expected behavior (e.g., error code, warning message)
      # ...

    except Exception as e:
      # Handle exceptions based on expected behavior
      # ...

  return results

# Example usage
test_results = test_must_support_elements("Patient", patient_test_data)
print(test_results)
```

### 4. Potential Issues and Edge Cases

* **Data Type Validation:** Ensure the test data includes edge cases for data types (e.g., maximum string lengths, date formats) within the "Must Support" elements.
* **Code System Validation:** If "Must Support" elements use coded values, test with valid and invalid codes from the designated code systems.
* **Cardinality Constraints:** Test scenarios where "Must Support" elements have cardinality constraints (e.g., minimum/maximum occurrences).
* **Performance:**  Large resource instances with numerous "Must Support" elements could impact performance. Consider testing with varying data sizes.
* **Security:**  Ensure sensitive data within "Must Support" elements is handled securely during testing and data generation. 


---

<a id='req-001-000-10'></a>

### REQ-001-000-10: Application (Consumer App) shall process resource instances containing Must Support data elements with missing information.

**Description**: "Consumer App actors shall be able to process resource instances containing Must Support data elements asserting missing information."

**Actor**: Application (Consumer App)

**Conformance**: SHALL

## Test Specification for REQ-001-000-10: Processing Must Support Data Elements with Missing Information

### 1. Requirement Analysis

**Testability Assessment:** Automatic
**Complexity:** Moderate
**Prerequisites:**
* A running FHIR server with the relevant profiles and resources loaded.
* A test client capable of making FHIR API calls.
* Test data representing resources with Must Support data elements marked as missing.

### 2. Test Implementation Strategy

**Required FHIR Operations:**

* **Create:** POST [base]/[resourceType] - To create a resource instance with missing Must Support data elements.
* **Read:** GET [base]/[resourceType]/[id] - To retrieve the created resource and verify its content.

**Test Data Requirements:**

* **Resource Type:** Define the specific FHIR resource type to be tested (e.g., Patient, Observation).
* **Must Support Data Elements:** Identify the data elements within the chosen resource type that are marked as "Must Support" in the relevant profile.
* **Missing Information Representation:** Determine how missing information will be represented in the test data (e.g., empty string "", null value, specific code like "unknown").

**Validation Criteria:**

* **Successful Resource Creation:** The FHIR server should accept the POST request and create the resource instance even with missing Must Support data elements. The response should return a 201 Created status code and a Location header pointing to the newly created resource.
* **Accurate Data Persistence:** The GET request should retrieve the created resource, and the response should accurately reflect the missing Must Support data elements as they were provided in the initial POST request.

### 3. Pseudocode Implementation

```python
# Test Case: Processing Must Support Data Elements with Missing Information

# Define test data
resource_type = "Patient"
must_support_element = "birthDate"
missing_info_representation = ""

# Construct the resource instance with missing data
test_resource = {
    "resourceType": resource_type,
    must_support_element: missing_info_representation,
    # ... other required elements ...
}

# Create the resource on the FHIR server
response = fhir_client.post(f"/{resource_type}", json=test_resource)

# Validate successful resource creation
assert response.status_code == 201
resource_location = response.headers["Location"]

# Retrieve the created resource
response = fhir_client.get(resource_location)

# Validate accurate data persistence
assert response.status_code == 200
retrieved_resource = response.json()
assert retrieved_resource[must_support_element] == missing_info_representation

# Test Case Passed
print(f"Successfully processed resource with missing '{must_support_element}' element.")
```

### 4. Potential Issues and Edge Cases

* **Data Type Validation:** Ensure the missing information representation aligns with the data type of the Must Support element. For example, an empty string might not be valid for a date element.
* **Profile-Specific Constraints:** Consider any additional constraints defined in the profile that might impact the handling of missing Must Support elements.
* **Server-Side Behavior:** Different FHIR servers might have varying levels of tolerance for missing data. Test against multiple server implementations if possible.
* **Performance Impact:** Evaluate the performance impact of processing resources with a large number of missing Must Support elements.
* **Security Considerations:** Ensure that sensitive data is not inadvertently exposed or manipulated due to the handling of missing data elements. 


---



<a id='**search**'></a>

## **Search**

<a id='req-001-000-12'></a>

### REQ-001-000-12: Application should track content changes using the _lastUpdated search parameter.

**Description**: "Clients that cache query results can track additions or modifications to directory content through queries that filter content using the _lastUpdated search parameter."

**Actor**: Application

**Conformance**: SHOULD

## Test Specification for REQ-001-000-12: Tracking Content Changes with _lastUpdated

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running FHIR server with resources that support the `_lastUpdated` search parameter.
    * Test client capable of making FHIR API calls.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * `GET [base]/[resource type]?_lastUpdated=[date]`
* **Test Data Requirements:**
    * At least one existing resource of the chosen type.
    * Timestamp of when the test begins (before any modifications).
* **Validation Criteria:**
    * **Positive Test:** A subsequent search using `_lastUpdated` with the initial timestamp should return the modified/added resources.
    * **Negative Test:** A subsequent search using `_lastUpdated` with a future timestamp should return an empty result set.

### 3. Pseudocode Implementation

```python
# Test Setup
base_url = "[FHIR Server Base URL]"
resource_type = "[Resource Type]"
initial_timestamp = current_timestamp()

# Test 1: Positive Case - Detect Changes
def test_detect_changes():
  # Modify or create a resource
  create_or_update_resource(base_url, resource_type)

  # Search for changes after modification
  response = send_fhir_request("GET", f"{base_url}/{resource_type}?_lastUpdated={initial_timestamp}")

  # Validate response
  assert response.status_code == 200
  assert len(response.json()['entry']) > 0

# Test 2: Negative Case - No Changes
def test_no_changes():
  future_timestamp = current_timestamp() + timedelta(hours=1) # Example future time

  # Search for changes in the future
  response = send_fhir_request("GET", f"{base_url}/{resource_type}?_lastUpdated={future_timestamp}")

  # Validate response
  assert response.status_code == 200
  assert len(response.json()['entry']) == 0

# Helper Function
def send_fhir_request(method, url, headers=None, data=None):
  # Implement logic to send FHIR API requests
  # Handle authentication, headers, data formatting, etc.
  pass

# Execute Tests
test_detect_changes()
test_no_changes()
```

### 4. Potential Issues and Edge Cases

* **Time Zone Handling:** Ensure consistent time zone handling between the client and server to avoid discrepancies in `_lastUpdated` values.
* **Resource Bundles:** Test the behavior with bundled resources to ensure changes within bundles are correctly reflected.
* **Deleted Resources:** Verify if deleted resources are included in the results or if a different mechanism is used to track deletions.
* **Performance:** For large datasets, consider testing the performance impact of using the `_lastUpdated` parameter and explore pagination options.
* **Security:** If the application implements access control, ensure that the `_lastUpdated` parameter doesn't bypass any security measures and only returns authorized resources. 


---



<a id='**system-component**'></a>

## **System Component**

<a id='req-001-000-13'></a>

### REQ-001-000-13: Application should periodically check for deleted data using the _id search parameter.

**Description**: "Clients should periodically check that data cached from past queries has not been deleted by querying for the same elements by _id."

**Actor**: Application

**Conformance**: SHOULD

## Test Specification for REQ-001-000-13: Periodically Check for Deleted Data

### 1. Requirement Analysis

* **Testability Assessment:** Hybrid (requires both automated setup and manual verification)
* **Complexity:** Moderate
* **Prerequisites:**
    * A running FHIR server with test data loaded.
    * A client application capable of making FHIR API calls.
    * At least one resource instance in the FHIR server that can be deleted for testing purposes.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * **READ:** Retrieve a specific resource instance by its logical ID (`GET [base]/[resourceType]/[id]`).
* **Test Data Requirements:**
    * **Initial Data:** At least one instance of any FHIR resource type (e.g., Patient).
* **Validation Criteria:**
    * **Positive Test Case:** 
        1. The client retrieves a resource by its ID.
        2. The resource is successfully retrieved (HTTP 200 OK).
        3. The client waits for the defined period.
        4. The resource is deleted on the server.
        5. The client attempts to retrieve the same resource by its ID.
        6. The server returns a 404 Not Found error.
    * **Negative Test Case:**
        1. The client retrieves a resource by its ID.
        2. The resource is successfully retrieved (HTTP 200 OK).
        3. The client waits for the defined period.
        4. The client attempts to retrieve the same resource by its ID.
        5. The resource is successfully retrieved (HTTP 200 OK).

### 3. Pseudocode Implementation

```python
# Test Case: Periodically Check for Deleted Data

# Define test parameters
resource_type = "Patient"  # Replace with desired resource type
resource_id = "12345"  # Replace with actual resource ID
polling_interval = 60  # Seconds to wait between checks

# Positive Test Case
def test_deleted_resource_not_found():
  # 1. Retrieve the resource
  initial_response = fhir_client.read(resource_type, resource_id)
  assert initial_response.status_code == 200

  # 2. Wait for the defined period
  time.sleep(polling_interval)

  # 3. Delete the resource on the server (manual step)
  # ...

  # 4. Attempt to retrieve the resource again
  try:
    deleted_response = fhir_client.read(resource_type, resource_id)
  except requests.exceptions.HTTPError as e:
    assert e.response.status_code == 404
  else:
    assert False, f"Expected 404 Not Found, but got {deleted_response.status_code}"

# Negative Test Case
def test_existing_resource_still_found():
  # 1. Retrieve the resource
  initial_response = fhir_client.read(resource_type, resource_id)
  assert initial_response.status_code == 200

  # 2. Wait for the defined period
  time.sleep(polling_interval)

  # 3. Attempt to retrieve the resource again
  repeat_response = fhir_client.read(resource_type, resource_id)
  assert repeat_response.status_code == 200
```

### 4. Potential Issues and Edge Cases

* **Resource Deletion Timing:** The test relies on manual deletion of the resource within the defined polling interval. This could lead to inconsistent results if not synchronized properly.
* **Caching Mechanisms:** The client application might have its own caching mechanisms, which could affect the test results. Ensure the client cache is appropriately invalidated or bypassed for this test.
* **Performance Impact:** Frequent polling for deleted resources can impact performance, especially with large datasets. Consider the frequency of checks and potential optimization strategies.
* **Resource History:** The test assumes the resource is permanently deleted. If the server retains resource history, the client should also check for deleted resource versions.
* **Security Considerations:** Ensure the client application has appropriate authorization to access and delete resources during testing.


---



<a id='data-validation'></a>

## Data Validation

<a id='req-001-000-09'></a>

### REQ-001-000-09: Application shall interpret missing Must Support data elements as data not present.

**Description**: "When querying Health Plan API actors, the application shall interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."

**Actor**: Application

**Conformance**: SHALL

## Test Specification for REQ-001-000-09: Missing Must Support Data Elements

### 1. Requirement Analysis

* **Testability Assessment:** **Automatic** - This requirement can be tested automatically using API calls and response validation.
* **Complexity:** **Simple** - The logic and validation are straightforward.
* **Prerequisites:**
    * A running instance of the application under test.
    * Access to a FHIR server (Health Plan API actor) with configurable resources.
    * Knowledge of specific Must Support data elements within the target resources.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * **Search (GET):** To query for resources from the Health Plan API actor.
* **Test Data Requirements:**
    * **Resource Type:** Define the specific FHIR resource type to be queried (e.g., Patient, Coverage).
    * **Must Support Element:** Identify the specific Must Support data element within the resource that will be omitted in the test data.
* **Validation Criteria:**
    * **HTTP Status Code:** Verify a successful response (e.g., 200 OK).
    * **Response Body:**  Assert that the returned resource instances do not contain the specified Must Support data element.
    * **Application Behavior:** Ensure the application does not throw errors, crash, or misinterpret the missing data. It should handle the absence gracefully. 

### 3. Pseudocode Implementation

```python
# Test Case: Missing Must Support Element

# Define test parameters
resource_type = "Patient"  # Example resource
must_support_element = "birthDate"  # Example Must Support element

# Construct the search URL
search_url = f"/{resource_type}?_summary=true"  # Use _summary=true for lighter responses

# Perform the search operation
response = send_request("GET", search_url)

# Validate the response
if response.status_code == 200:
    # Parse the response body (assuming JSON format)
    response_data = response.json()

    # Iterate through returned resources (if any)
    for resource in response_data.get("entry", []):
        # Check if the Must Support element is present
        if must_support_element in resource["resource"]:
            test_failed(f"Must Support element '{must_support_element}' unexpectedly found in resource.")
        else:
            test_passed(f"Must Support element '{must_support_element}' correctly not present.")
else:
    test_failed(f"Request failed with status code: {response.status_code}")
```

### 4. Potential Issues and Edge Cases

* **Data Presence in Other Systems:** The application should be tested to ensure it doesn't assume data is globally missing if the Must Support element is absent from one specific system.
* **Resource Cardinality:**  Test with resources where the Must Support element has a cardinality of 0..1 (optional) and ensure the application handles both presence and absence correctly. 
* **Performance:**  Consider testing with large result sets to ensure performance is not impacted by the logic of handling missing data.
* **Security:** If the application logs the missing data, ensure no sensitive information is exposed in the logs. 


---



<a id='server'></a>

## Server

<a id='req-001-000-01'></a>

### REQ-001-000-01: Server shall not require authentication.

**Description**: "The server shall not require authentication for access to the Plan-Net service."

**Actor**: Server

**Conformance**: SHOULD

## Test Specification for REQ-001-000-01: Server Authentication Not Required

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running FHIR server instance that implements the Plan-Net service.
    * The base URL of the FHIR server.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * HTTP GET request to a Plan-Net resource endpoint (e.g., `/PlanDefinition`)
* **Test Data Requirements:**
    * None. This test focuses on accessing the resource without authentication.
* **Validation Criteria:**
    * **Positive Test Case:** A successful HTTP status code (2xx) is returned, indicating access to the resource without authentication.
    * **Negative Test Case:**  N/A - The requirement uses "SHOULD", meaning authentication is not strictly prohibited. A negative test case is not applicable here.

### 3. Pseudocode Implementation

```python
# Import required libraries (e.g., requests)

def test_server_authentication_not_required():
  """
  Verifies that the server does not require authentication for accessing Plan-Net resources.
  """

  base_url = "https://your-fhir-server.com/fhir"  # Replace with your FHIR server base URL
  resource_type = "PlanDefinition"  # Example resource type from Plan-Net
  url = f"{base_url}/{resource_type}"

  try:
    response = requests.get(url)

    # Assert successful response
    assert response.status_code >= 200 and response.status_code < 300, f"Expected successful status code, got {response.status_code}"
    print("Test Passed: Server allows access to Plan-Net resources without authentication.")

  except requests.exceptions.RequestException as e:
    print(f"Test Failed: An error occurred while accessing the server: {e}")

# Run the test
test_server_authentication_not_required()
```

### 4. Potential Issues and Edge Cases

* **Corner Cases:**
    * The server might require authentication for specific Plan-Net resource operations (e.g., write operations) even if read access is allowed without authentication. This test only covers basic read access.
* **Performance Considerations:**
    * While not directly related to the requirement, continuously allowing unauthenticated access might have performance implications if the server experiences a high volume of requests.
* **Security Considerations:**
    * The "SHOULD" conformance level implies flexibility. While this test verifies the server doesn't *require* authentication, it's crucial to assess the security implications of allowing unauthenticated access in the specific implementation context. Consider implementing appropriate authorization mechanisms to control access to sensitive data, even if authentication is not mandatory. 


---

<a id='req-001-000-02'></a>

### REQ-001-000-02: Server shall not store consumer identifiable information.

**Description**: "A conformant Plan-Net service shall not store any consumer identifiable information."

**Actor**: Server

**Conformance**: SHALL NOT

## Test Specification for REQ-001-000-02: Server Shall Not Store Consumer Identifiable Information

### 1. Requirement Analysis

* **Testability Assessment:**  Hybrid (Manual inspection combined with automated API calls)
* **Complexity:** Moderate
* **Prerequisites:**
    * A deployed and running instance of the Plan-Net FHIR service.
    * Access to server logs or database for manual inspection (depending on the system architecture).
    * Defined test patient data containing identifiable information (e.g., name, address, social security number).
    * Tools for making FHIR API calls (e.g., Postman, cURL, FHIR client library).

### 2. Test Implementation Strategy

**2.1. Required FHIR Operations:**

1. **Create:** Use the FHIR `POST` operation to create a new patient resource on the server.
2. **Read:** Use the FHIR `GET` operation to retrieve the created patient resource.
3. **Search:** Use the FHIR `GET` operation with search parameters to query for patients.
4. **Delete:** Use the FHIR `DELETE` operation to remove the created patient resource.

**2.2. Test Data Requirements:**

* **Test Patient Data:**
    * Create a set of test patient data that includes both identifiable and non-identifiable elements.
    * **Identifiable elements:** Name, address, phone number, email, social security number, etc.
    * **Non-identifiable elements:**  De-identified data like age, gender, clinical information.

**2.3. Validation Criteria:**

* **Automated Checks:**
    * **Response Codes:** Verify that all FHIR API calls return the expected HTTP status codes.
    * **Response Body:** 
        * After the `Create` operation, ensure the response body does NOT contain the identifiable elements of the test patient data.
        * After the `Read` and `Search` operations, ensure the returned patient resource does NOT contain the identifiable elements.
* **Manual Inspection (If applicable):**
    * **Server Logs:** Analyze server logs for any logging of consumer identifiable information during the test execution.
    * **Database:** If direct access is possible, inspect the database to confirm that no identifiable information is stored.

### 3. Pseudocode Implementation

```python
# Import necessary libraries (e.g., FHIR client library)

# Define test data
test_patient_data = {
    "resourceType": "Patient",
    "name": [{"family": "Doe", "given": ["John"]} ],
    "address": [{"postalCode": "90210"}],
    # ... other identifiable and non-identifiable elements
}

# Test Case 1: Create Patient and Verify Response
def test_create_patient():
    response = fhir_client.post('Patient', data=test_patient_data)
    assert response.status_code == 201  # Created
    assert "Doe" not in response.text  # Check for identifiable information
    assert "90210" not in response.text
    return response.json()["id"]  # Return patient ID

# Test Case 2: Read Patient and Verify Response
def test_read_patient(patient_id):
    response = fhir_client.get(f'Patient/{patient_id}')
    assert response.status_code == 200  # OK
    assert "Doe" not in response.text
    assert "90210" not in response.text

# Test Case 3: Search Patient and Verify Response (Negative Test)
def test_search_patient():
    response = fhir_client.get('Patient?family=Doe')
    assert response.status_code == 200  # OK
    assert response.json()["total"] == 0  # No matching patients

# Test Case 4: Delete Patient
def test_delete_patient(patient_id):
    response = fhir_client.delete(f'Patient/{patient_id}')
    assert response.status_code == 204  # No Content

# Execute Tests
patient_id = test_create_patient()
test_read_patient(patient_id)
test_search_patient()
test_delete_patient(patient_id)

# Manual Inspection: 
# - Review server logs for any logging of identifiable information.
# - If applicable, inspect the database to confirm no identifiable information is stored.
```

### 4. Potential Issues and Edge Cases

* **Indirect Identifiers:** The system might store information that could be combined with other data to re-identify individuals (e.g., rare diseases, specific dates of service).
* **Logging Practices:** Ensure that logging levels are appropriately configured to prevent accidental logging of identifiable information.
* **Data Retention Policies:**  Verify that any cached or temporary data is purged according to a strict data retention policy.
* **Third-Party Systems:** If the system interacts with third-party services, ensure they also comply with the requirement not to store identifiable information.
* **Performance Impact:**  De-identification and data masking techniques can impact system performance. Consider these trade-offs during implementation.

**Note:** This test specification provides a starting point. You should adapt and expand it based on the specific implementation details of your Plan-Net FHIR service. 


---

<a id='req-001-000-04'></a>

### REQ-001-000-04: Server shall populate all Must Support data elements in query results.

**Description**: "The server shall populate all Must Support data elements in the resource instance returned as part of the query results."

**Actor**: Server (Health Plan API)

**Conformance**: SHALL

## Test Specification for REQ-001-000-04: Server Population of Must Support Data Elements

### 1. Requirement Analysis

* **Testability Assessment**:  **Automatic** (can be automated with FHIR client libraries)
* **Complexity**: **Moderate** (requires understanding of FHIR profiles and Must Support)
* **Prerequisites**:
    * A running FHIR server (Health Plan API) conforming to the Implementation Guide.
    * Access to the FHIR Implementation Guide defining the resources and profiles with "Must Support" elements.
    * A FHIR client library or testing tool.
    * Test data representing valid resources conforming to the profiles in the IG. 

### 2. Test Implementation Strategy

* **Required FHIR Operations**:
    * **Search Operation**:  Execute search queries against the target resources defined in the IG.
* **Test Data Requirements**:
    * **Valid Resources**: Instances of resources conforming to the profiles in the IG. These resources should include data for both "Must Support" and optional elements.
* **Validation Criteria**:
    * **Presence Check**: For each returned resource instance, verify that all data elements marked as "Must Support" in the corresponding profile are present.
    * **Data Type Check**: Ensure that the populated data elements have the correct data type as defined in the profile.
    * **Cardinality Check**: Verify that the number of repetitions for the data element adheres to the cardinality defined in the profile.

### 3. Pseudocode Implementation

```python
# Import necessary FHIR libraries
from fhir.resources.patient import Patient
from fhir_client import FHIRClient

# Define FHIR server endpoint
fhir_server_url = "https://your-fhir-server/fhir"

# Initialize FHIR client
client = FHIRClient(fhir_server_url)

def test_must_support_elements(resource_type: str, search_params: dict = None):
  """
  Tests if the server populates all Must Support data elements in query results.

  Args:
    resource_type: The type of FHIR resource to query (e.g., 'Patient').
    search_params: (Optional) Search parameters for the query.

  Raises:
    AssertionError: If any Must Support element is missing or invalid.
  """

  # Execute the search operation
  response = client.search(resource_type, search_params)

  # Check for successful response
  assert response.status_code == 200, f"Error: Unexpected status code {response.status_code}"

  # Get the Bundle resource from the response
  bundle = response.resource

  # Iterate through each resource in the Bundle
  for entry in bundle.entry:
    resource = entry.resource

    # Get the corresponding profile from the IG based on resource type
    profile = get_profile_from_ig(resource.resource_type) # Implementation-specific function

    # Get all Must Support elements from the profile
    must_support_elements = get_must_support_elements(profile) # Implementation-specific function

    # Validate presence and data type of each Must Support element
    for element in must_support_elements:
      element_path = element.get('path')
      assert hasattr(resource, element_path), f"Must Support element '{element_path}' is missing in resource."

      # Add data type and cardinality checks here based on profile definition

# Example usage
test_must_support_elements('Patient', {'birthdate': 'ge2000-01-01'}) 
```

### 4. Potential Issues and Edge Cases

* **Complex Profiles**: Handling deeply nested data structures and complex element definitions within profiles might require more sophisticated validation logic.
* **Code Systems and Value Sets**:  Verification should include checks for correct usage of codes from specified code systems and value sets.
* **Performance**:  Testing with large datasets might impact performance. Consider optimizing test data and queries.
* **Security**: Ensure test data does not contain sensitive information and that the testing environment is secure.
* **IG Updates**:  Tests need to be updated when the FHIR IG or the profiles within it are modified. 


---

<a id='req-001-000-05'></a>

### REQ-001-000-05: Server shall not include missing Must Support data elements with minimum cardinality 0.

**Description**: "If information on a Must Support data element is not present and the minimum cardinality is 0, the server shall not include the data element in the resource instance returned as part of the query results."

**Actor**: Server (Health Plan API)

**Conformance**: SHALL NOT

## Test Specification for REQ-001-000-05: Server Shall Not Include Missing Must Support Data Elements with Minimum Cardinality 0

### 1. Requirement Analysis

**Testability Assessment:** Automatic
**Complexity:** Simple
**Prerequisites:**
* A running FHIR server implementing the Health Plan API.
* Knowledge of a Must Support data element with minimum cardinality 0 within the scope of the Health Plan API. For this example, let's assume the element is `Observation.component.valueQuantity` (this is just an example, replace with an actual element from your implementation guide). 

### 2. Test Implementation Strategy

**Required FHIR Operations:**
* **READ:** To retrieve a resource instance.

**Test Data Requirements:**
* **Resource Instance:** A resource containing the `Observation` resource with at least one `component` where `valueQuantity` is **not** populated.

**Validation Criteria:**
* **Positive Test Case:** The response should NOT include the `valueQuantity` element within the `component` element of the returned `Observation` resource.
* **Negative Test Case:** (Not applicable for SHALL NOT requirement)

### 3. Pseudocode Implementation

```python
# Test Case: REQ-001-000-05 - Positive Test Case

# **Setup**
# 1. Ensure the FHIR server is running and accessible.
# 2. Have the ID of an Observation resource instance where 'component.valueQuantity' is not populated.

# **Test Execution**
function test_REQ_001_000_05_positive():
  observation_id = "<Observation_resource_ID>"
  response = fhir_client.read("Observation", observation_id)

  if response.status_code == 200:
    observation = response.resource
    for component in observation.component:
      if "valueQuantity" in component:
        raise AssertionError("Test Failed: 'valueQuantity' element present in response when it should be absent.")
    print("Test Passed: 'valueQuantity' element not included in response.")
  else:
    raise AssertionError(f"Test Failed: Unable to retrieve Observation resource. Status Code: {response.status_code}")

# Run the test case
test_REQ_001_000_05_positive()
```

### 4. Potential Issues and Edge Cases

* **Resource Complexity:** The test case assumes a simple structure. For complex resources with nested data elements, the validation logic needs to be adjusted to traverse the resource structure accurately.
* **Data Type Variations:** The example focuses on `valueQuantity`. The test logic should be adaptable for other data types.
* **Performance:** Retrieving large resources might impact test execution time. Consider using smaller resources or specific search parameters to optimize performance.
* **FHIR Server Variations:** Different FHIR server implementations might have subtle variations in behavior. It's crucial to test against the specific server being used in the production environment. 


---

<a id='req-001-000-06'></a>

### REQ-001-000-06: Server shall send reason for missing Must Support data elements with minimum cardinality > 0.

**Description**: "If information on a Must Support data element is not present and the minimum cardinality is > 0, the server shall send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."

**Actor**: Server (Health Plan API)

**Conformance**: SHALL

## Test Specification for REQ-001-000-06: Missing Must Support Data Elements

### 1. Requirement Analysis

**Testability Assessment:** Automatic
**Complexity:** Moderate
**Prerequisites:**
* A running FHIR server implementing the target Health Plan API.
* Knowledge of Must Support data elements with minimum cardinality > 0 within the implemented resources.
* Test data representing resources with missing Must Support data elements.

### 2. Test Implementation Strategy

**Required FHIR Operations:**

* **Create:** Create resources with missing Must Support data elements.
* **Read:** Retrieve the created resources.

**Test Data Requirements:**

* **Valid Resources:**  Resources conforming to the FHIR profile with all required data elements.
* **Invalid Resources:** Resources with specific Must Support data elements (minimum cardinality > 0) intentionally omitted.

**Validation Criteria:**

* **Positive Test Cases:**
    * Verify that the server responds with an HTTP 201 Created status code for the creation of resources with missing Must Support data elements, indicating acceptance of the request.
    * Verify that the server includes either a valid `nullFlavor` code from the corresponding value set or a `dataAbsentReason` extension within the response for each missing Must Support data element.
* **Negative Test Cases:**
    * Verify that the server responds with an HTTP 4xx (e.g., 400 Bad Request) status code when attempting to create resources missing required data elements that are not Must Support and have no mechanism for indicating absence.

### 3. Pseudocode Implementation

```python
# Test Case: Missing Must Support Data Element with nullFlavor

# Test Data
resource = {
  "resourceType": "Patient",
  "name": [
    {
      "use": "official",
      "family": "Doe",
      "given": [
        "John"
      ]
    }
  ],
  # Missing Must Support element 'birthDate' with minimum cardinality > 0
  "gender": "male"
}

# Create Resource
response = fhir_client.create(resource)

# Assertions
assert response.status_code == 201
assert "dataAbsentReason" in response.json()["birthDate"] or "nullFlavor" in response.json()["birthDate"]


# Test Case: Missing Must Support Data Element with dataAbsentReason extension

# Test Data
resource = {
  "resourceType": "Observation",
  "status": "final",
  "code": {
    "coding": [
      {
        "system": "http://loinc.org",
        "code": "15074-8"
      }
    ]
  },
  # Missing Must Support element 'valueQuantity' with minimum cardinality > 0
  "extension": [
    {
      "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
      "valueCode": "unknown"
    }
  ]
}

# Create Resource
response = fhir_client.create(resource)

# Assertions
assert response.status_code == 201
assert response.json()["valueQuantity"]["extension"][0]["valueCode"] == "unknown"


# Negative Test Case: Missing Required Data Element (not Must Support)

# Test Data
resource = {
  "resourceType": "Patient",
  # Missing required element 'name' with no mechanism for indicating absence
  "gender": "male"
}

# Create Resource
response = fhir_client.create(resource)

# Assertions
assert response.status_code == 400
```

### 4. Potential Issues and Edge Cases

* **Resource Complexity:** Testing with deeply nested resources and various data types might require more complex test data and validation logic.
* **Value Set Constraints:** Ensure the server correctly validates `nullFlavor` codes against the specified value sets.
* **Performance:** Consider the performance impact of creating and retrieving large resources with numerous missing data elements.
* **Security:** Test for potential vulnerabilities related to manipulating `dataAbsentReason` extensions or `nullFlavor` codes.

This test specification provides a starting point for verifying the server's compliance with REQ-001-000-06. Further refinement and expansion based on specific implementation details and edge cases are encouraged. 


---

<a id='req-001-000-11'></a>

### REQ-001-000-11: Server shall provide the lastUpdate timestamp in profiles.

**Description**: "The server shall provide the lastUpdate timestamp as part of the profile's data content."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-001-000-11: Server shall provide the lastUpdate timestamp in profiles.

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running FHIR server that implements the target profiles.
    * Access credentials to the FHIR server (if applicable).

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * `GET [base]/StructureDefinition/[profile-id]` - Retrieve the specified profile.

* **Test Data Requirements:**
    * A list of `profile-id` values representing the profiles to be tested.

* **Validation Criteria:**
    * **Positive Test Case:** The response for each profile retrieval MUST:
        * Return an HTTP status code 200 (OK).
        * Contain a valid FHIR StructureDefinition resource.
        * The StructureDefinition resource MUST contain a non-empty `lastUpdate` element with a valid timestamp value conforming to the FHIR dateTime format.
    * **Negative Test Case:** (Optional, depends on server behavior)
        * If the server is expected to reject requests for non-existent profiles, attempt to retrieve a non-existent profile. The server SHOULD return an HTTP status code 404 (Not Found).

### 3. Pseudocode Implementation

```python
# Test Case: Verify lastUpdate timestamp in profiles

# Input:
#   fhir_client: Initialized FHIR client object
#   profile_ids: List of profile IDs to test

def test_profile_last_update(fhir_client, profile_ids):
  for profile_id in profile_ids:
    try:
      # Retrieve the profile
      response = fhir_client.get(f"StructureDefinition/{profile_id}")

      # Validate HTTP status code
      assert response.status_code == 200, f"Failed to retrieve profile {profile_id}. Status code: {response.status_code}"

      # Parse the response as a FHIR resource
      profile = response.json()

      # Validate lastUpdate element exists and is not empty
      assert "lastUpdate" in profile, f"Profile {profile_id} missing 'lastUpdate' element."
      assert profile["lastUpdate"], f"Profile {profile_id} has an empty 'lastUpdate' element."

      # Validate lastUpdate format (optional, requires additional validation logic)
      # ...

      print(f"Profile {profile_id}: lastUpdate timestamp validated successfully.")

    except Exception as e:
      print(f"Error during validation of profile {profile_id}: {e}")

# Example usage:
# test_profile_last_update(fhir_client, ["MyProfile-v1", "AnotherProfile-v2"])
```

### 4. Potential Issues and Edge Cases

* **Invalid Timestamp Format:** The server might return a `lastUpdate` value that doesn't conform to the FHIR dateTime format. The test should ideally include validation logic to check the format.
* **Timezone Handling:** The test should consider potential issues related to different timezones and ensure consistent interpretation of the timestamp.
* **Performance:** Retrieving multiple profiles might impact performance. Consider implementing pagination or limiting the number of profiles tested in a single run.
* **Security:** Ensure the test script handles authentication and authorization appropriately if the FHIR server requires it.
* **Server-Specific Behavior:** The test implementation might need adjustments based on specific error handling and response formats of the target FHIR server. 


---



