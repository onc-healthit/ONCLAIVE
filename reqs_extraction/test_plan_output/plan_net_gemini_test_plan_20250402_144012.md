# Consolidated Test Plan for Plan Net

## Generated on: 2025-04-02 14:40:46

## Table of Contents

- [Client](#client)
  - [REQ-06: Use of code `CT` for State](#req-06)
  - [REQ-07: Use of  USPS postal code for State](#req-07)
- [Endpoint](#endpoint)
  - [REQ-16: Populate all Must Support data elements for Health Plan API query results](#req-16)
  - [REQ-17: Omit data elements with minimum cardinality 0 when information is not present](#req-17)
  - [REQ-18: Provide reason for missing data elements with minimum cardinality > 0](#req-18)
  - [REQ-19: Process resource instances containing Must Support data elements without errors](#req-19)
  - [REQ-20: Display or store data elements for human use](#req-20)
  - [REQ-21: Interpret missing Must Support data elements as not present in the Health Plan API system](#req-21)
  - [REQ-22: Process resource instances containing Must Support data elements asserting missing information](#req-22)
- [Organization](#organization)
  - [REQ-24: Define HealthcareServices for Service Search](#req-24)
- [Plan-Net Endpoint](#plan-net-endpoint)
  - [REQ-15: Prohibit sending consumer identifiable information in directory queries](#req-15)
- [Plan-Net InsurancePlan](#plan-net-insuranceplan)
  - [REQ-25: Link Insurance Plans to Networks](#req-25)
- [Practitioner](#practitioner)
  - [REQ-26: Associate Practitioners and Organizations with Networks](#req-26)
- [Server](#server)
  - [REQ-01: Advertise supported canonical URL for SubscriptionTopic](#req-01)
  - [REQ-02: Plan Net Endpoint resources SHALL conform to the PlannetEndpoint profile.](#req-02)
  - [REQ-03: Plan Net HealthcareService resources SHALL conform to the PlannetHealthcareService profile.](#req-03)
  - [REQ-04: Plan Net InsurancePlan resources SHALL conform to the PlannetInsurancePlan profile.](#req-04)
  - [REQ-05: Plan Net Location resources SHALL conform to the PlannetLocation profile.](#req-05)
  - [REQ-08: Networks SHALL have an NPI](#req-08)
  - [REQ-09: Organizations SHALL have an NPI](#req-09)
  - [REQ-10: No summary](#req-10)
  - [REQ-11: Practitioner Role SHALL have a Code](#req-11)
  - [REQ-12: Do not require authentication for Plan-Net service access](#req-12)
  - [REQ-13: Prohibit storage of consumer-identifying information](#req-13)
  - [REQ-14: Prohibit requiring consumer identification for directory queries](#req-14)
  - [REQ-23: Provide lastUpdate timestamp in profile data content](#req-23)
  - [REQ-27: Support Organization Resource for Organization Information](#req-27)
  - [REQ-28: Support OrganizationAffiliation Resource for Role Descriptions](#req-28)
  - [REQ-29: Support HealthcareService Association with Networks via OrganizationAffiliation](#req-29)
  - [REQ-30: Support Endpoint Resource for Technical Details of Electronic Service Endpoints](#req-30)
  - [REQ-31: Support all defined profiles](#req-31)
  - [REQ-32: Implement RESTful behavior according to FHIR specification](#req-32)
  - [REQ-33: Return Status 400 for invalid parameter](#req-33)
  - [REQ-34: Return Status 401/4xx for unauthorized request](#req-34)
  - [REQ-35: Return Status 403 for insufficient scope](#req-35)
  - [REQ-36: Return Status 404 for unknown resource](#req-36)
  - [REQ-37: Return Status 410 for deleted resource](#req-37)
  - [REQ-38: Support JSON source formats](#req-38)
  - [REQ-39: Identify supported Plan-Net profiles in meta.profile attribute](#req-39)
  - [REQ-40: Support searchParameters individually and in combination](#req-40)
  - [REQ-41: Support forward and reverse chaining for search parameters with 'chain' property](#req-41)
  - [REQ-42: Support XML source formats](#req-42)
  - [REQ-43: Reject unauthorized requests with HTTP 401](#req-43)
  - [REQ-44: Support Plan-Net Endpoint profile](#req-44)
  - [REQ-45: Support search-type and read interactions for Endpoint](#req-45)
  - [REQ-46: Support vread interaction for Endpoint](#req-46)
  - [REQ-47: Return Endpoint resource using ID](#req-47)
  - [REQ-48: Return Endpoint resource using ID and version ID](#req-48)
  - [REQ-49: Support _include for Endpoint:organization](#req-49)
  - [REQ-50: Support organization search parameter for Endpoint](#req-50)

## Test Specifications

<a id='client'></a>

## Client

<a id='req-06'></a>

### REQ-06: Use of code `CT` for State

**Description**: "Use code `CT`  - `State` in the element 'address.state'."

**Actor**: Server/Client

**Conformance**: SHALL

## Test Specification for REQ-06: Use of code `CT` for State

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:** 
    * A running FHIR server with the implemented Implementation Guide.
    * Test patient data with an address element.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * `POST` - Create a new patient resource with an address containing the state code `CT`.
    * `GET` - Retrieve the created patient resource.

* **Test Data Requirements:**
    * A valid FHIR Patient resource with:
        * `address.state` element set to `CT`.

* **Validation Criteria:**
    * Verify the HTTP status code of the `POST` request is `201 Created`.
    * Verify the HTTP status code of the `GET` request is `200 OK`.
    * Verify the returned Patient resource contains the `address.state` element with the value `CT`.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://your-fhir-server-url')

# Test data
test_patient = {
  "resourceType": "Patient",
  "name": [
    {
      "family": "Doe",
      "given": ["John"]
    }
  ],
  "address": [
    {
      "state": "CT"
    }
  ]
}

# Test case 1: Successful creation and retrieval with state code 'CT'
begin
  # Create a new patient
  creation_response = client.create(resource: test_patient)

  # Assert creation success
  raise "Patient creation failed: #{creation_response.body}" unless creation_response.success?

  # Retrieve the created patient
  patient_id = creation_response.resource.id
  retrieved_patient = client.read(resource: 'Patient', id: patient_id).resource

  # Assert retrieval success and correct state code
  raise "Patient retrieval failed" unless retrieved_patient
  raise "Incorrect state code: expected 'CT', got '#{retrieved_patient.address.first.state}'" unless retrieved_patient.address.first.state == 'CT'

  puts "Test case 1: PASS"

rescue => e
  puts "Test case 1: FAIL - #{e.message}"
end

# Test case 2: Negative case - Attempt to create with invalid state code
begin
  # Modify test data with invalid state code
  test_patient['address'][0]['state'] = 'INVALID'

  # Attempt to create a patient with invalid state code
  creation_response = client.create(resource: test_patient)

  # Assert creation failure
  raise "Patient creation succeeded with invalid state code" if creation_response.success?

  puts "Test case 2: PASS"

rescue => e
  puts "Test case 2: FAIL - #{e.message}"
end
```

### 4. Potential Issues and Edge Cases

* **Case sensitivity:** Ensure the validation is case-insensitive (e.g., both `CT` and `ct` should be considered valid).
* **Whitespace handling:** Trim any leading or trailing whitespace from the `state` element before validation.
* **Multiple address entries:** If the resource allows multiple addresses, ensure all instances adhere to the requirement.
* **Performance:** Consider the performance impact of validating this requirement for large datasets.
* **Security:** Ensure that sensitive data within the Patient resource is handled securely during testing. 


---

<a id='req-07'></a>

### REQ-07: Use of  USPS postal code for State

**Description**: "Use a valid US Postal Service code for the state of 'CT'."

**Actor**: Server/Client

**Conformance**: SHALL

## Test Specification for REQ-07: Use of USPS Postal Code for State 'CT'

### 1. Requirement Analysis

* **Testability Assessment**: Automatic
* **Complexity**: Simple
* **Prerequisites**: 
    * A running FHIR server with resources that include address information.
    * Access credentials for the FHIR server (if applicable).
    * A test client capable of making FHIR API calls.

### 2. Test Implementation Strategy

* **Required FHIR Operations**: 
    * **Read Operation**:  Retrieve a resource that contains address information with the state field populated (e.g., Patient, Organization).
* **Test Data Requirements**:
    * **Positive Test Case**: A resource with a valid USPS postal code for Connecticut (e.g., '06100', '06525').
    * **Negative Test Case**: A resource with an invalid postal code or a valid postal code that does not belong to Connecticut (e.g., '10001', '90210').
* **Validation Criteria**:
    * **Positive Test Case**: Verify that the server accepts the resource with the valid Connecticut postal code without errors.
    * **Negative Test Case**: Verify that the server rejects the resource with the invalid or out-of-state postal code and returns an appropriate error code (e.g., 400 Bad Request).

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://your-fhir-server-url')
client.use_r4

# Positive Test Case
def test_valid_ct_postal_code(client)
  # Assuming Patient resource with postal code in address field
  patient = FHIR::Patient.new(
    address: [
      {
        postalCode: '06525' # Valid CT postal code
      }
    ]
  )

  begin
    response = client.create(patient)
    
    if response.code == 201 # Created
      puts "Positive Test Case Passed: Valid CT postal code accepted."
    else
      puts "Positive Test Case Failed: Unexpected response code #{response.code}"
    end
  rescue => e
    puts "Positive Test Case Failed: #{e.message}"
  end
end

# Negative Test Case
def test_invalid_ct_postal_code(client)
  # Assuming Patient resource with invalid postal code
  patient = FHIR::Patient.new(
    address: [
      {
        postalCode: '10001' # Invalid CT postal code (belongs to New York)
      }
    ]
  )

  begin
    response = client.create(patient)
    puts "Negative Test Case Failed: Invalid postal code accepted."
  rescue => e
    if e.message.include?("400") # Assuming 400 Bad Request for invalid data
      puts "Negative Test Case Passed: Invalid postal code rejected."
    else
      puts "Negative Test Case Failed: Unexpected error: #{e.message}"
    end
  end
end

# Run the tests
test_valid_ct_postal_code(client)
test_invalid_ct_postal_code(client)
```

### 4. Potential Issues and Edge Cases

* **Data Variations**: Test with various valid Connecticut postal codes and different formats (e.g., with/without the optional 4-digit extension).
* **Resource Types**:  The test cases assume a Patient resource. Adapt the tests for other resource types that contain address information.
* **Server-Side Validation**:  The test relies on the server implementing validation logic for postal codes.  
* **Error Handling**:  The test assumes specific error codes.  Verify the actual error codes returned by the server and adjust the test accordingly.
* **Performance**: Consider the performance impact of validating postal codes, especially for bulk operations. 
* **Security**: Ensure that sensitive data within the test resources is properly anonymized or masked. 


---



<a id='endpoint'></a>

## Endpoint

<a id='req-16'></a>

### REQ-16: Populate all Must Support data elements for Health Plan API query results

**Description**: "Health Plan API actors **SHALL** be capable of populating all Must Support data elements as part of the query results."

**Actor**: Health Plan API

**Conformance**: SHALL

## Test Specification for REQ-16: Populate all Must Support data elements for Health Plan API query results

### 1. Requirement Analysis

* **Testability Assessment**: **Automatic** (can be automated using FHIR client libraries)
* **Complexity**: **Moderate** (requires understanding of Must Support data elements and FHIR resources)
* **Prerequisites**:
    * A running instance of the Health Plan API under test.
    * Access credentials for the API.
    * A list of all Must Support data elements for the relevant FHIR resources being queried.
    * Test data representing various scenarios and edge cases.

### 2. Test Implementation Strategy

* **Required FHIR Operations**:
    * **Search Operation**: Execute search queries against relevant FHIR resources (e.g., Patient, Coverage, Claim).
* **Test Data Requirements**:
    * **Valid search parameters**: Use parameters relevant to the resources being tested.
    * **Data variations**: Include test data that covers different data types, value ranges, and optional elements.
* **Validation Criteria**:
    * **Response Status Code**: Verify a successful response code (e.g., 200 OK).
    * **Must Support Data Elements**: For each returned resource instance:
        * Identify all Must Support data elements based on the FHIR specification and implementation guide.
        * Verify that each Must Support element is present in the response.
        * Verify that the populated values for these elements are of the correct data type and conform to any specified constraints.
    * **Error Handling**: Verify appropriate error responses (e.g., 4xx, 5xx) for invalid requests or data issues.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://<health-plan-api-base-url>')
client.set_bearer_token('<access_token>')

# Define Must Support data elements for the target resource (e.g., Patient)
must_support_elements = {
  'Patient' => ['id', 'name', 'birthDate', 'gender', 'address']
  # Add other resources and their Must Support elements as needed
}

def test_must_support_elements(client, resource_type, search_params)
  # Execute search operation
  response = client.search(resource_type, search: search_params)

  # Validate response status code
  if response.code != 200
    raise "Error: Unexpected response code #{response.code}"
  end

  # Validate Must Support elements for each resource instance
  response.resource.entry.each do |entry|
    resource = entry.resource
    must_support_elements[resource_type].each do |element|
      if !resource.send(element).present?
        raise "Error: Must Support element '#{element}' missing in #{resource_type} with ID #{resource.id}"
      end
      # Add data type and constraint validation as needed
    end
  end
end

# Test Case 1: Valid search with all Must Support elements present
begin
  search_params = { 'family': 'Smith' }
  test_must_support_elements(client, 'Patient', search_params)
  puts "Test Case 1: Passed"
rescue => e
  puts "Test Case 1: Failed - #{e}"
end

# Test Case 2: Edge case with empty search results
begin
  search_params = { 'family': 'NonExistentName' }
  test_must_support_elements(client, 'Patient', search_params)
  puts "Test Case 2: Passed"
rescue => e
  puts "Test Case 2: Failed - #{e}"
end

# Add more test cases for different resources, search parameters, and edge scenarios
```

### 4. Potential Issues and Edge Cases

* **Incomplete Must Support Element List**: Ensure the list of Must Support elements is comprehensive and up-to-date with the FHIR specification and implementation guide.
* **Optional vs. Required Elements**: Differentiate between optional and required elements within the Must Support list. Handle optional elements appropriately in the validation logic.
* **Data Type Validation**: Implement robust data type validation to ensure values adhere to FHIR data types and any additional constraints defined in the implementation guide.
* **Code System Validation**: If applicable, validate that coded elements use valid codes from the specified code systems.
* **Performance**: Consider the performance impact of retrieving and validating large datasets. Implement optimization strategies if necessary.
* **Security**: Ensure secure handling of access tokens and sensitive patient data during testing.

This test specification provides a starting point for testing REQ-16. You should adapt and expand it based on the specific details of the FHIR implementation guide and the Health Plan API under test. 


---

<a id='req-17'></a>

### REQ-17: Omit data elements with minimum cardinality 0 when information is not present

**Description**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0 , the Health Plan API actors **SHALL NOT** include the data elements in the resource instance returned as part of the query results."

**Actor**: Health Plan API

**Conformance**: SHALL NOT

## Test Specification for REQ-17: Omit Optional Data Elements

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running instance of the Health Plan API.
    * Test data with resources containing data elements with minimum cardinality 0.
    * A FHIR client or testing tool capable of making API requests and parsing responses.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * **READ:** To retrieve resources from the Health Plan API.
* **Test Data Requirements:**
    * **Resource Type:** Any resource type with data elements having minimum cardinality 0.
    * **Test Data Variations:**
        * **Scenario 1:** Resource instance with the optional data element populated.
        * **Scenario 2:** Resource instance with the optional data element absent.
* **Validation Criteria:**
    * **Positive Test Case:** When the optional data element is absent in the resource, the API response **SHOULD NOT** include the element.
    * **Negative Test Case:** When the optional data element is present in the resource, the API response **SHOULD** include the element with its value.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://<health-plan-api-base-url>')

# Define resource type and optional element path
resource_type = 'Patient'
optional_element_path = 'telecom.period'

# Test Case 1: Optional element absent
def test_optional_element_absent(client, resource_type, optional_element_path)
  # Search for a resource with the optional element absent
  search_params = { '_elements': optional_element_path }
  response = client.search(resource_type, search: search_params)

  # Assert response success
  assert_true(response.success?, "Request failed: #{response.status}")

  # Assert optional element is not present in the response
  response.resource.entry.each do |entry|
    assert_nil(entry.resource.dig(*optional_element_path.split('.')), "Optional element '#{optional_element_path}' found in response when not expected.")
  end
end

# Test Case 2: Optional element present
def test_optional_element_present(client, resource_type, optional_element_path)
  # Search for a resource with the optional element present
  response = client.search(resource_type)

  # Assert response success
  assert_true(response.success?, "Request failed: #{response.status}")

  # Find a resource with the optional element populated
  resource_with_element = response.resource.entry.find do |entry|
    entry.resource.dig(*optional_element_path.split('.'))
  end

  # Assert a resource with the optional element was found
  assert_not_nil(resource_with_element, "No resource found with optional element '#{optional_element_path}' populated.")

  # Assert optional element is present in the response
  assert_not_nil(resource_with_element.resource.dig(*optional_element_path.split('.')), "Optional element '#{optional_element_path}' not found in response when expected.")
end

# Run test cases
test_optional_element_absent(client, resource_type, optional_element_path)
test_optional_element_present(client, resource_type, optional_element_path)

puts "All tests passed!"
```

### 4. Potential Issues and Edge Cases

* **Nested Data Elements:** The test should be adaptable to handle optional elements nested within complex data types.
* **Resource Variations:**  Testing should cover various resource types and different optional elements within those resources.
* **Performance:**  Consider the performance impact of retrieving large resources with numerous optional elements. The test data should be designed to avoid excessive response sizes.
* **Security:**  Ensure that test data does not contain sensitive patient information. Use de-identified or synthetic data for testing. 


---

<a id='req-18'></a>

### REQ-18: Provide reason for missing data elements with minimum cardinality > 0

**Description**: "In situations where information on a particular data element is not present and the minimum cardinality is >0 **SHALL** send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."

**Actor**: Health Plan API

**Conformance**: SHALL

## Test Specification for FHIR Implementation Guide Requirement REQ-18

### 1. Requirement Analysis

**Requirement ID:** REQ-18

**Summary:** Provide reason for missing data elements with minimum cardinality > 0

**Testability Assessment:** Automatic

**Complexity:** Moderate

**Prerequisites:**

* A running FHIR server implementing the target API.
* Test data sets containing resources with missing data elements that have a minimum cardinality greater than 0.
* Knowledge of the expected nullFlavor values or dataAbsentReason extension URLs for the specific resources and data elements being tested.

### 2. Test Implementation Strategy

**Required FHIR Operations:**

* **Read Operation:** Retrieve resources with potentially missing data elements.

**Test Data Requirements:**

* **Valid Resources:** Resources conforming to the FHIR profile with all required data elements present.
* **Invalid Resources:** Resources with missing data elements that have a minimum cardinality greater than 0. These resources should be designed to test different scenarios:
    * Missing data element with a valid nullFlavor value.
    * Missing data element with a valid dataAbsentReason extension.
    * Missing data element without any reason provided (negative test case).

**Validation Criteria:**

* **Positive Test Cases:**
    * Verify that for each missing data element with minimum cardinality > 0, either a valid nullFlavor value or a dataAbsentReason extension is present.
    * Verify that the provided nullFlavor value or dataAbsentReason extension URL is valid according to the specification.
* **Negative Test Cases:**
    * Verify that the API returns an error or warning when a required data element is missing and no reason is provided.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://fhir-server-endpoint')

# Define a function to test for missing data element reasons
def test_missing_data_element_reason(resource, element_path, expected_reason_values)
  element = resource.get_element(element_path)

  # Check if the element is nil (missing)
  if element.nil?
    # Check for nullFlavor or dataAbsentReason
    if expected_reason_values.include?(resource.get_element("#{element_path}.extension").url) || expected_reason_values.include?(resource.get_element(element_path).nullFlavor)
      puts "PASS: Missing element '#{element_path}' has valid reason."
      return true
    else
      puts "FAIL: Missing element '#{element_path}' has no valid reason."
      return false
    end
  else
    puts "INFO: Element '#{element_path}' is present. Skipping reason check."
    return true
  end
end

# Example usage:
patient = client.read(FHIR::Patient, '12345').resource

# Test for missing 'maritalStatus' element with expected reasons
test_missing_data_element_reason(patient, 'maritalStatus', ['http://hl7.org/fhir/StructureDefinition/data-absent-reason', 'unknown'])

# Test for missing 'deceasedBoolean' element with expected reasons
test_missing_data_element_reason(patient, 'deceasedBoolean', ['http://terminology.hl7.org/CodeSystem/v3-NullFlavor|NI'])

# ... Add more tests for different resources and data elements ...
```

### 4. Potential Issues and Edge Cases

* **Resource Complexity:** Testing complex resources with deeply nested data elements might require recursive functions or specialized logic.
* **Performance:** Testing a large number of resources and data elements can be time-consuming. Consider optimizing the test execution strategy.
* **NullFlavor vs. dataAbsentReason:** Ensure the test cases cover both methods of indicating missing data element reasons and validate their usage according to the specification.
* **Specific Value Sets:** The test data and validation logic should be tailored to the specific value sets used for nullFlavor and dataAbsentReason in the target implementation.
* **Error Handling:** Implement robust error handling to gracefully handle unexpected responses from the FHIR server or invalid data formats.
* **Security:** If testing against a production environment, ensure the test data is properly anonymized and the test execution does not impact real patient data. 


---

<a id='req-19'></a>

### REQ-19: Process resource instances containing Must Support data elements without errors

**Description**: "Application actors **SHALL** be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."

**Actor**: Application

**Conformance**: SHALL

## Test Specification for REQ-19: Process Must Support Data Elements

### 1. Requirement Analysis

* **Testability Assessment:**  Hybrid (Combination of Automatic and Manual)
    * **Automatic:**  Automated tests can be used to send FHIR resources with Must Support elements and verify HTTP status codes and basic response structure.
    * **Manual:** Manual inspection of the application's behavior (e.g., logs, user interface) might be necessary to confirm the absence of errors or failures.
* **Complexity:** Moderate
* **Prerequisites:**
    * A running instance of the application under test.
    * Access to the application's FHIR API endpoint.
    * A list of resources and their corresponding Must Support data elements as defined in the FHIR Implementation Guide.
    * Test FHIR resources containing the Must Support data elements.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * **CREATE:**  Send a POST request to the appropriate resource endpoint with a FHIR resource containing Must Support elements.
    * **UPDATE:** Send a PUT request to update an existing resource with Must Support elements. 

* **Test Data Requirements:**
    * **Valid FHIR Resources:**  Resources conforming to the FHIR specification and the Implementation Guide, including the required Must Support elements.
    * **Variety of Data Types:**  Test resources should include Must Support elements of different data types (e.g., string, code, reference) to ensure comprehensive coverage.

* **Validation Criteria:**
    * **HTTP Status Code:**
        * **Success:** 200 (OK) for UPDATE or 201 (Created) for CREATE.
        * **Failure:** Any other status code indicating an error.
    * **Response Body:**
        * **Success:**  The response should contain the processed resource or an OperationOutcome resource with a success status.
        * **Failure:** The response should not indicate any errors related to the processing of Must Support elements.
    * **Application Logs:** (Manual Inspection)
        * **Success:** No error messages related to Must Support elements.
        * **Failure:** Presence of error messages indicating issues processing Must Support elements.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# **Test Case: Create Resource with Must Support Elements**

def test_create_resource_with_must_support(resource_type, resource_data)
  client = FHIR::Client.new('https://fhir-server-endpoint')
  
  begin
    response = client.create(resource_type, resource_data)

    # Assert successful creation
    assert_equal 201, response.code, "Resource creation failed: #{response.body}"

    # Additional assertions based on the specific resource and implementation guide
    # ...

  rescue => e
    puts "Error creating resource: #{e.message}"
    assert false, "Exception raised during resource creation."
  end
end

# Example Usage:
patient_data = {
  "resourceType": "Patient",
  "name": [
    {
      "family": "Doe",
      "given": ["John"]
    }
  ],
  # ... other required and Must Support elements for Patient resource
}

test_create_resource_with_must_support("Patient", patient_data)

# **Test Case: Update Resource with Must Support Elements**

def test_update_resource_with_must_support(resource_type, resource_id, resource_data)
  client = FHIR::Client.new('https://fhir-server-endpoint')

  begin
    response = client.update(resource_type, resource_id, resource_data)

    # Assert successful update
    assert_equal 200, response.code, "Resource update failed: #{response.body}"

    # Additional assertions based on the specific resource and implementation guide
    # ...

  rescue => e
    puts "Error updating resource: #{e.message}"
    assert false, "Exception raised during resource update."
  end
end

# Example Usage:
updated_patient_data = {
  # ... Must Support elements with updated values
}

test_update_resource_with_must_support("Patient", "12345", updated_patient_data)
```

### 4. Potential Issues and Edge Cases

* **Large Resources:** Test with resources containing a large number of Must Support elements to assess performance impact.
* **Data Type Variations:**  Thoroughly test with Must Support elements of all relevant data types, including complex types like CodeableConcept and Reference.
* **Invalid Data:**  While the requirement focuses on Must Support elements, it's crucial to also test with invalid data in other fields to ensure the application handles errors gracefully and doesn't misinterpret them as Must Support issues.
* **Security Considerations:**  Ensure that the test data does not contain sensitive patient information. Use de-identified or synthetic data for testing purposes. 
* **Resource Interactions:**  Consider testing scenarios where the Must Support elements in one resource might impact the processing of other related resources. 


---

<a id='req-20'></a>

### REQ-20: Display or store data elements for human use

**Description**: "Application actors **SHOULD** be capable of displaying the data elements for human use or storing the information for other purposes."

**Actor**: Application

**Conformance**: SHOULD

## Test Specification for REQ-20: Display or store data elements for human use

### 1. Requirement Analysis

**Testability Assessment:** Hybrid (Manual inspection of display combined with automated data persistence checks)

**Complexity:** Moderate

**Prerequisites:**

* A running instance of the application under test.
* Access to the application's user interface (if applicable).
* Ability to query the application's data storage mechanism (e.g., database).
* A predefined set of FHIR resources containing the data elements relevant to the test.

### 2. Test Implementation Strategy

**Required FHIR Operations:**

* **Create/Update:** To populate the application with the test data.
* **Read:** To retrieve the stored data for verification.

**Test Data Requirements:**

* A set of FHIR resources representing different clinical entities (e.g., Patient, Observation, Condition).
* The resources should contain a variety of data types (e.g., string, date, codeable concept).

**Validation Criteria:**

**Display:**

* **Manual Inspection:** Verify that the application presents the data elements in a human-readable format.
    * Elements should be labelled appropriately.
    * Data types should be rendered correctly (e.g., dates in a standard format).
    * Codeable concepts should display both the code and display text.

**Storage:**

* **Automated Check:** Verify that the application persists the data elements from the FHIR resources.
    * Compare the data elements in the retrieved resources with the original test data.
    * Ensure all required elements are stored.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://example.com/fhir')

# Test data
test_patient = FHIR::Patient.new(
  name: [
    {
      use: 'official',
      given: ['John'],
      family: 'Doe'
    }
  ],
  birthDate: '1980-01-01'
)

# Test Case 1: Data Storage
begin
  # Create the patient resource
  created_patient = client.create(test_patient)

  # Retrieve the created patient resource
  retrieved_patient = client.read(FHIR::Patient, created_patient.id)

  # Validate data persistence
  assert_equal retrieved_patient.name[0].given[0], 'John'
  assert_equal retrieved_patient.birthDate, '1980-01-01'

  puts "Test Case 1: Data Storage - PASSED"
rescue => e
  puts "Test Case 1: Data Storage - FAILED: #{e.message}"
end

# Test Case 2: Data Display (Manual Inspection)
begin
  # Navigate to the patient view in the application UI
  # ...

  # Manually verify that the patient's name and birthdate are displayed correctly
  # ...

  puts "Test Case 2: Data Display - PASSED (Manual Inspection)"
rescue => e
  puts "Test Case 2: Data Display - FAILED (Manual Inspection): #{e.message}"
end
```

### 4. Potential Issues and Edge Cases

* **Large Data Sets:** Test with large FHIR resources to assess performance impact on display and storage.
* **Special Characters:** Include data elements with special characters to ensure proper handling and encoding.
* **Data Types:** Test with all relevant FHIR data types, including complex types like CodeableConcept and Address.
* **Localization:** If the application supports multiple languages, verify data display in each language.
* **Security and Privacy:** Ensure sensitive data elements are handled appropriately based on access control rules and privacy regulations. 
* **Error Handling:** Test how the application handles invalid or missing data elements during both display and storage.


---

<a id='req-21'></a>

### REQ-21: Interpret missing Must Support data elements as not present in the Health Plan API system

**Description**: "When querying Health Plan API actors, Application actors **SHALL** interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."

**Actor**: Application

**Conformance**: SHALL

## Test Specification for REQ-21: Interpret Missing Must Support Data Elements

### 1. Requirement Analysis

* **Testability Assessment:** Hybrid (requires both automated API calls and manual interpretation of results)
* **Complexity:** Moderate
* **Prerequisites:**
    * A running instance of the Health Plan API system under test.
    * An Application actor capable of making FHIR API calls.
    * Knowledge of Must Support data elements for the specific resources being tested.
    * Test data containing resources with missing Must Support elements.

### 2. Test Implementation Strategy

#### 2.1 Required FHIR Operations:

* **READ:**  Retrieve a resource instance from the Health Plan API.
* **SEARCH:** Query for resources with specific criteria that would normally include the Must Support data element.

#### 2.2 Test Data Requirements:

* **Resource Instance with Missing Must Support Data:**  A valid FHIR resource instance with a known Must Support data element intentionally omitted.
* **Resource Instance with Present Must Support Data:** A valid FHIR resource instance with the same Must Support data element present.

#### 2.3 Validation Criteria:

* **Positive Test Case:** When retrieving or searching for a resource with a missing Must Support data element, the Application actor should NOT receive an error. The response should be successful, and the missing data element should be absent from the returned resource.
* **Negative Test Case:** When retrieving or searching for a resource with the Must Support data element present, the Application actor should receive a successful response with the data element included in the returned resource.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://health-plan-api-url')

# Define resource type and Must Support element
resource_type = 'Patient'
must_support_element = 'birthDate'

# Test Case 1: Missing Must Support Element

# Create search criteria (excluding birthDate)
search_criteria = {
  '_count': 10
}

# Perform search
search_results = client.search(resource_type, search_criteria).resource

# Validate results
search_results.entry.each do |entry|
  resource = entry.resource
  begin
    resource.send(must_support_element)
    raise "Error: Must Support element '#{must_support_element}' present when expected to be missing."
  rescue NoMethodError
    # Expected behavior - element is missing
  end
end

puts "Test Case 1 (Missing Element): Passed"

# Test Case 2: Present Must Support Element

# Create search criteria (including birthDate)
search_criteria = {
  '_count': 10,
  'birthDate': 'eq1980'
}

# Perform search
search_results = client.search(resource_type, search_criteria).resource

# Validate results
search_results.entry.each do |entry|
  resource = entry.resource
  begin
    resource.send(must_support_element)
  rescue NoMethodError
    raise "Error: Must Support element '#{must_support_element}' missing when expected to be present."
  end
end

puts "Test Case 2 (Present Element): Passed"
```

### 4. Potential Issues and Edge Cases

* **Resource Structure:** The test script assumes a simple data element structure. Complex nested elements might require more sophisticated parsing.
* **Data Types:** Different data types for the Must Support element might require specific checks within the validation logic.
* **Performance:** Searching for resources without the Must Support element might impact performance if the element is frequently used for indexing.
* **Security:** Ensure that test data does not contain sensitive patient information.
* **FHIR Version:**  Ensure compatibility between the FHIR version used by the Health Plan API and the testing framework.

This test specification provides a starting point for verifying REQ-21. It can be further enhanced and customized based on the specific implementation details of the Health Plan API and the resources being tested. 


---

<a id='req-22'></a>

### REQ-22: Process resource instances containing Must Support data elements asserting missing information

**Description**: "Consumer App actors **SHALL** be able to process resource instances containing Must Support data elements asserting missing information"

**Actor**: Consumer App

**Conformance**: SHALL

## Test Specification for REQ-22: Process Must Support Data Elements with Missing Information

### 1. Requirement Analysis

* **Testability Assessment**:  **Automatic** - This test can be automated using FHIR client libraries to interact with the Consumer App API.
* **Complexity**: **Moderate** - Requires understanding of FHIR Must Support, data element definitions, and potential error handling.
* **Prerequisites**: 
    * A running instance of the Consumer App accessible via its API.
    * Test FHIR resources containing Must Support data elements with missing information.
    * FHIR client library (e.g., FHIR-Client for Ruby).

### 2. Test Implementation Strategy

* **Required FHIR Operations**:
    * **POST /{resourceType}**: Create a new resource instance with missing Must Support data elements.
    * **GET /{resourceType}/{id}**: Retrieve the created resource to verify its persistence.

* **Test Data Requirements**:
    * **Test Resource**: A FHIR resource relevant to the Consumer App's context.
    * **Must Support Data Element**: Identify at least one data element in the chosen resource marked as "Must Support" in the relevant FHIR Implementation Guide.
    * **Variations**: Create multiple test resources with:
        * The Must Support element completely missing.
        * The Must Support element present but empty (e.g., an empty string or array).

* **Validation Criteria**:
    * **Successful Creation**: The Consumer App should successfully create the resource via the POST request, even with the missing Must Support data.
    * **Resource Retrieval**: The GET request should return the created resource, including the missing or empty Must Support element as persisted.
    * **Error Handling**: The Consumer App should not throw an error during resource creation or retrieval due to the missing Must Support data. It may, however, log a warning or provide feedback through other mechanisms as defined in its specifications.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://consumer-app-api-endpoint')

# Define test resource with missing Must Support data element
test_resource = {
  "resourceType": "Observation",
  # ... other required elements ...
  # "valueQuantity": { ... }  <-- Must Support element MISSING
}

# Positive Test Case: Resource creation and retrieval with missing data
begin
  # Create the resource
  created_resource = client.create(test_resource)

  # Assert successful creation
  assert_equal 201, created_resource.code, "Resource creation failed with missing Must Support data"

  # Retrieve the created resource
  retrieved_resource = client.read(created_resource.resourceType, created_resource.id)

  # Assert successful retrieval
  assert_equal 200, retrieved_resource.code, "Resource retrieval failed"

  # Assert Must Support element is missing or empty in the retrieved resource
  assert_nil retrieved_resource.resource.valueQuantity, "Must Support element 'valueQuantity' is not missing"

  puts "Test Passed: Successfully processed resource with missing Must Support data"

rescue => e
  puts "Test Failed: #{e.message}"
end

# Negative Test Case: Example - Invalid resource structure
# ... (Similar structure, but introduce an invalid data type or missing required element)
# ... Assertions should expect an error response from the Consumer App

```

### 4. Potential Issues and Edge Cases

* **Resource Validation**: While the requirement focuses on "Must Support," the Consumer App should ideally still perform basic FHIR resource validation to prevent invalid data. The test should consider cases where missing required elements (not just "Must Support") lead to appropriate error responses.
* **Data Integrity**:  Consider the downstream impact of missing Must Support data. While the Consumer App should process it, other systems relying on this data might encounter issues. The test scope might need expansion to cover integration scenarios.
* **Performance**:  Creating numerous resources with missing data could impact the Consumer App's performance. Consider performance testing with a large dataset.
* **Security**:  Ensure that missing data doesn't introduce security vulnerabilities, especially if the Consumer App exposes this data through other interfaces. 


---



<a id='organization'></a>

## Organization

<a id='req-24'></a>

### REQ-24: Define HealthcareServices for Service Search

**Description**: "All organizations that provide service should define an appropriate set of HealthcareServices to facilitate search."

**Actor**: Organization

**Conformance**: SHOULD

## Test Specification for REQ-24: Define HealthcareServices for Service Search

### 1. Requirement Analysis

* **Testability Assessment:** Hybrid (Automatic API calls with Manual inspection of results)
* **Complexity:** Moderate
* **Prerequisites:**
    * Access to the FHIR server of the organization under test.
    * Authorization to perform search operations on the HealthcareService resource.
    * Knowledge of the organization's service offerings to validate the relevance of returned HealthcareServices.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * `GET /HealthcareService` - Search for HealthcareService resources.
* **Test Data Requirements:**
    * No specific test data is required for this test. The test will rely on the existing HealthcareService resources defined by the organization.
* **Validation Criteria:**
    * **Positive Test Case:**
        * The FHIR server should return a 200 OK response.
        * The response bundle should contain at least one HealthcareService resource.
        * The returned HealthcareService resources should accurately represent the services offered by the organization (Manual inspection required).
    * **Negative Test Case:**
        * N/A - As this is a "SHOULD" requirement, a lack of HealthcareService resources does not automatically constitute a failure. However, it should be flagged for manual review and potential improvement recommendations.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://fhir-server-url')
client.use_r4

# Perform search operation
begin
  search_result = client.search(FHIR::HealthcareService)

  # Check for successful response
  if search_result.code == 200
    puts "Test Passed: Successfully retrieved HealthcareService resources."

    # Further manual inspection required:
    puts "Please manually verify that the returned HealthcareService resources accurately represent the organization's service offerings."

    # Example of accessing resources for manual inspection
    healthcare_services = search_result.resource.entry.map(&:resource)
    healthcare_services.each do |service|
      puts "Service Name: #{service.name}"
      # Inspect other relevant attributes of the HealthcareService resource
    end

  else
    puts "Test Failed: Unexpected response code #{search_result.code}"
  end

rescue => e
  puts "Test Failed: An error occurred during the test execution - #{e.message}"
end
```

### 4. Potential Issues and Edge Cases

* **Corner Cases:**
    * Organizations with a very large number of services might require pagination to retrieve all HealthcareService resources.
    * The test relies on manual inspection to verify the accuracy of the returned resources. This can be subjective and prone to human error.
* **Performance Considerations:**
    * Searching for HealthcareService resources without any search criteria can be resource-intensive, especially for organizations with a large number of services. Consider using specific search parameters to improve performance.
* **Security Considerations:**
    * Ensure that the test script uses appropriate authentication and authorization mechanisms to access the FHIR server.
    * Do not store sensitive information, such as API keys or access tokens, directly within the test script.

This test specification provides a starting point for verifying conformance with REQ-24. Further customization and refinement may be necessary based on the specific context and requirements of the implementation. 


---



<a id='plan-net-endpoint'></a>

## Plan-Net Endpoint

<a id='req-15'></a>

### REQ-15: Prohibit sending consumer identifiable information in directory queries

**Description**: "A directory mobile application **SHALL NOT** send consumer identifiable information when querying a Plan-Net service."

**Actor**: Directory Mobile Application

**Conformance**: SHALL NOT

## Test Specification for REQ-15: Prohibit Sending Consumer Identifiable Information in Directory Queries

### 1. Requirement Analysis

* **Testability Assessment:** Hybrid (Manual inspection of test data alongside automated API calls)
* **Complexity:** Moderate
* **Prerequisites:**
    * A running instance of the Plan-Net service with a publicly accessible FHIR API endpoint.
    * A directory mobile application capable of making FHIR API calls.
    * Test user accounts on the directory mobile application.
    * A predefined list of consumer identifiable information (CII) attributes according to the FHIR implementation guide and relevant privacy regulations (e.g., name, address, phone number, email, social security number, medical record number).

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * **Search Type:** `GET` request to the appropriate FHIR resource endpoint on the Plan-Net service.
    * **Resource:** The specific resource being queried (e.g., Practitioner, Organization).
* **Test Data Requirements:**
    * **Positive Test Cases:**
        * Construct valid search queries that **do not** include any CII attributes.
        * Vary the search parameters and resource types to ensure comprehensive coverage.
    * **Negative Test Cases:**
        * Construct search queries that **intentionally include** various CII attributes.
        * Test different combinations and formats of CII within the search query.
* **Validation Criteria:**
    * **Positive Test Cases:**
        * The Plan-Net service should successfully process the request and return the relevant search results.
        * Verify that the response does not contain any error messages related to CII being present in the query.
    * **Negative Test Cases:**
        * The Plan-Net service should reject the request and return an appropriate error response.
        * Verify that the error message explicitly indicates the presence of CII in the query and cites the relevant requirement (REQ-15).

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configuration
fhir_endpoint = 'https://plan-net-service.com/fhir'
client = FHIR::Client.new(fhir_endpoint)

# Test Data
cii_attributes = ['name', 'address', 'telecom', 'birthDate', 'identifier']
test_queries = {
  positive: ['family=Smith', '_id=12345'],
  negative: ["name=John Doe", "address=123 Main Street", "telecom=+15555551212"]
}

# Test Execution
test_queries.each do |type, queries|
  queries.each do |query|
    begin
      response = client.search(FHIR::Patient, search: { parameters: { query: query } })

      if type == :positive
        # Positive test case assertion
        assert_equal 200, response.code, "Expected 200 OK, got #{response.code} for query: #{query}"
        puts "PASS: Positive test case passed for query: #{query}"
      else
        # Negative test case assertion
        assert_equal 400, response.code, "Expected 400 Bad Request, got #{response.code} for query: #{query}"
        assert_includes response.body, "CII detected in query", "Missing expected error message for query: #{query}"
        puts "PASS: Negative test case passed for query: #{query}"
      end

    rescue => e
      puts "ERROR: An error occurred during test execution: #{e.message}"
    end
  end
end
```

### 4. Potential Issues and Edge Cases

* **Encoding:** Test different encoding methods for CII within the query string (e.g., URL encoding, Base64).
* **Partial Information:**  Test scenarios where only partial CII is included (e.g., only the city from an address).
* **Case Sensitivity:** Ensure the Plan-Net service consistently identifies CII regardless of case sensitivity.
* **Data Type Variations:** Test different data types for CII attributes (e.g., string, date, numerical).
* **Performance:** Evaluate the performance impact of CII detection on the Plan-Net service, especially with large datasets.
* **Security:** Verify that the error messages returned by the Plan-Net service do not inadvertently reveal sensitive information.
* **FHIR Version Specifics:** Ensure the tests are aligned with the specific FHIR version implemented by the Plan-Net service.

This test specification provides a comprehensive framework for verifying the implementation of REQ-15. By addressing potential issues and edge cases, these tests can help ensure the privacy and security of consumer information within the Plan-Net ecosystem. 


---



<a id='plan-net-insuranceplan'></a>

## Plan-Net InsurancePlan

<a id='req-25'></a>

### REQ-25: Link Insurance Plans to Networks

**Description**: "Each payer will offer one or more products -- Insurance Plans -- and each plan is associated with one or more Networks."

**Actor**: Payer

**Conformance**: SHALL

## Test Specification for REQ-25: Link Insurance Plans to Networks

### 1. Requirement Analysis

* **Testability Assessment:**  **Automatic** - This requirement can be automatically tested by inspecting the FHIR resources.
* **Complexity:** **Simple** - The requirement is straightforward and involves verifying a direct relationship between two resources.
* **Prerequisites:**
    * A running FHIR server with the implementation under test deployed.
    * Access credentials to the FHIR server with appropriate permissions to read InsurancePlan and Network resources.
    * Test data containing at least one InsurancePlan resource.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * **READ:** `GET /InsurancePlan/{id}` - To retrieve an InsurancePlan resource.
    * **READ:** `GET /Network?identifier={system|}[code]` - To search for Network resources.

* **Test Data Requirements:**
    * **InsurancePlan Resource:**
        * Must have at least one `network` reference.
        * The `network.reference` should point to a valid Network resource.
    * **Network Resource:**
        * Should exist and be retrievable using the identifier provided in the InsurancePlan's `network` reference.

* **Validation Criteria:**
    * **Positive Test Case:**
        * The InsurancePlan resource MUST contain at least one `network` reference.
        * For each `network` reference in the InsurancePlan resource:
            * A corresponding Network resource MUST exist and be retrievable using the identifier specified in the reference.
    * **Negative Test Case:**
        * An error should be raised if an InsurancePlan resource does not contain any `network` references.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://fhir-server-url')
client.use_r4

# Test Case 1: Positive Test - InsurancePlan linked to Network
def test_insurance_plan_linked_to_network(client, insurance_plan_id)
  begin
    # Retrieve InsurancePlan resource
    insurance_plan = client.read(FHIR::InsurancePlan, insurance_plan_id).resource

    # Check if InsurancePlan has at least one network reference
    raise 'InsurancePlan does not have any network references.' if insurance_plan.network.empty?

    # Validate each network reference
    insurance_plan.network.each do |network_ref|
      network_id = network_ref.reference.split('/').last
      network = client.read(FHIR::Network, network_id).resource

      # Additional validation on the Network resource can be added here if needed
      puts "InsurancePlan #{insurance_plan_id} is linked to Network #{network_id}"
    end

  rescue => e
    puts "Test Failed: #{e.message}"
  end
end

# Test Case 2: Negative Test - InsurancePlan not linked to any Network
def test_insurance_plan_not_linked_to_network(client, insurance_plan_id)
  begin
    # Retrieve InsurancePlan resource
    insurance_plan = client.read(FHIR::InsurancePlan, insurance_plan_id).resource

    # Check if InsurancePlan has at least one network reference
    raise 'InsurancePlan does not have any network references.' if insurance_plan.network.empty?

  rescue => e
    puts "Test Passed (Negative Test): #{e.message}"
  end
end

# Example usage
insurance_plan_id = '12345'
test_insurance_plan_linked_to_network(client, insurance_plan_id)
test_insurance_plan_not_linked_to_network(client, insurance_plan_id)
```

### 4. Potential Issues and Edge Cases

* **Multiple Network References:** The test cases should handle InsurancePlan resources with multiple `network` references and ensure all references are valid.
* **Invalid Network References:** The test cases should handle scenarios where the `network` reference points to a non-existent or inaccessible Network resource and report an error.
* **Performance:** Retrieving and validating a large number of Network resources could impact performance. Consider using search operations with appropriate filters to improve efficiency.
* **Security:** Ensure the test scripts use appropriate authentication and authorization mechanisms to access the FHIR server and resources.
* **Data Variations:** Test with different data variations for InsurancePlan and Network resources to ensure robustness. For example, test with different identifier systems and network types. 


---



<a id='practitioner'></a>

## Practitioner

<a id='req-26'></a>

### REQ-26: Associate Practitioners and Organizations with Networks

**Description**: "Practitioners and Organizations indicate participation in a Network with a link to the Network using a PractitionerRole or OrganizationAffiliation instance, respectively."

**Actor**: Practitioners and Organizations

**Conformance**: SHALL

## Test Specification for REQ-26: Associate Practitioners and Organizations with Networks

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running FHIR server with the Network, Practitioner, Organization, PractitionerRole, and OrganizationAffiliation resources implemented.
    * Existing resources:
        * At least one Network resource.
        * At least one Practitioner resource.
        * At least one Organization resource.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * **READ:** Retrieve PractitionerRole and OrganizationAffiliation resources.
* **Test Data Requirements:**
    * A PractitionerRole resource with a `network` reference pointing to a valid Network resource.
    * An OrganizationAffiliation resource with a `network` reference pointing to a valid Network resource.
* **Validation Criteria:**
    * Verify that the retrieved PractitionerRole resource contains a `network` element referencing a valid Network resource ID.
    * Verify that the retrieved OrganizationAffiliation resource contains a `network` element referencing a valid Network resource ID.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://your-fhir-server-url')

# Test Case 1: Practitioner Network Association
def test_practitioner_network_association(client, practitioner_role_id)
  begin
    # Retrieve PractitionerRole resource
    practitioner_role = client.read(FHIR::PractitionerRole, practitioner_role_id).resource

    # Check if 'network' element exists and contains a reference
    if practitioner_role.network.present? && practitioner_role.network.first.reference.present?
      puts "PASS: PractitionerRole #{practitioner_role_id} has a network reference."
    else
      puts "FAIL: PractitionerRole #{practitioner_role_id} does not have a valid network reference."
    end
  rescue => e
    puts "ERROR: #{e.message}"
  end
end

# Test Case 2: Organization Network Association
def test_organization_network_association(client, organization_affiliation_id)
  begin
    # Retrieve OrganizationAffiliation resource
    organization_affiliation = client.read(FHIR::OrganizationAffiliation, organization_affiliation_id).resource

    # Check if 'network' element exists and contains a reference
    if organization_affiliation.network.present? && organization_affiliation.network.first.reference.present?
      puts "PASS: OrganizationAffiliation #{organization_affiliation_id} has a network reference."
    else
      puts "FAIL: OrganizationAffiliation #{organization_affiliation_id} does not have a valid network reference."
    end
  rescue => e
    puts "ERROR: #{e.message}"
  end
end

# Example usage
test_practitioner_network_association(client, 'practitioner-role-123')
test_organization_network_association(client, 'organization-affiliation-456')
```

### 4. Potential Issues and Edge Cases

* **Multiple Network References:** The requirement doesn't specify if multiple network references are allowed. Test cases should include scenarios with multiple `network` elements in both PractitionerRole and OrganizationAffiliation resources.
* **Invalid Network References:** Test cases should include scenarios with invalid or non-existent Network resource IDs in the `network` reference to ensure proper error handling.
* **Performance:** Consider testing with a large number of PractitionerRole and OrganizationAffiliation resources to assess performance impact.
* **Security:** Ensure that access to PractitionerRole and OrganizationAffiliation resources is properly authorized and that sensitive information within these resources is protected. 


---



<a id='server'></a>

## Server

<a id='req-01'></a>

### REQ-01: Advertise supported canonical URL for SubscriptionTopic

**Description**: "In order to allow for discovery of supported subscription topics, this guide defines the CapabilityStatement SubscriptionTopic Canonical extension. The extension allows server implementers to advertise the canonical URLs of topics available to clients."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-01: Advertise Supported Canonical URL for SubscriptionTopic

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:** 
    * A running FHIR server that implements the SubscriptionTopic resource and the CapabilityStatement SubscriptionTopic Canonical extension as defined in the Implementation Guide.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * `GET /metadata` - Retrieve the server's CapabilityStatement.

* **Test Data Requirements:**
    * None. The test relies on the server's pre-configured CapabilityStatement.

* **Validation Criteria:**
    * **Positive Test Case:** The CapabilityStatement's `rest.resource` array MUST contain an entry for `SubscriptionTopic`. This entry MUST include at least one `extension` element with the following properties:
        * `url`:  The URL of the extension as defined in the Implementation Guide.
        * `valueCanonical`: A valid canonical URL representing a supported SubscriptionTopic.
    * **Negative Test Case:** If the `SubscriptionTopic` resource entry is missing, or the extension is not found or malformed, the test should fail.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://your-fhir-server-url')

# Test Case: Verify SubscriptionTopic Canonical URL advertisement
def test_subscription_topic_canonical_url(client)
  begin
    # Retrieve CapabilityStatement
    capability_statement = client.read(FHIR::CapabilityStatement, nil).resource

    # Find SubscriptionTopic resource in CapabilityStatement
    subscription_topic_resource = capability_statement.rest.resource.find do |resource|
      resource.type == 'SubscriptionTopic'
    end

    # Check if SubscriptionTopic resource exists
    raise 'SubscriptionTopic resource not found in CapabilityStatement' unless subscription_topic_resource

    # Find the required extension
    extension = subscription_topic_resource.extension.find do |ext|
      ext.url == 'http://your-ig-url.org/StructureDefinition/capabilitystatement-subscriptiontopic-canonical'
    end

    # Check if the extension exists and has a valueCanonical
    raise 'SubscriptionTopic Canonical extension not found or missing valueCanonical' unless extension&.valueCanonical

    # Additional validation: Check if valueCanonical is a valid URL (optional)
    # ...

    # Test passed
    puts 'Test Passed: SubscriptionTopic Canonical URL advertised correctly.'
    return true

  rescue => e
    puts "Test Failed: #{e.message}"
    return false
  end
end

# Run the test
test_subscription_topic_canonical_url(client)
```

### 4. Potential Issues and Edge Cases

* **Multiple Canonical URLs:** The server might support multiple SubscriptionTopics. The test should be able to handle and validate multiple `valueCanonical` entries within the extension.
* **Invalid Canonical URLs:** The test should ideally validate that the provided `valueCanonical` URLs are syntactically correct and resolvable.
* **Performance:** Retrieving and parsing the CapabilityStatement might be resource-intensive for servers with large configurations. Consider optimizing the test for performance if necessary.
* **Security:** Ensure that the test does not expose sensitive information from the CapabilityStatement or rely on insecure data access methods. 


---

<a id='req-02'></a>

### REQ-02: Plan Net Endpoint resources SHALL conform to the PlannetEndpoint profile.

**Description**: "**Example**   **ResourceType**   **Profiles** \n[AcmeOfCTPortalEndpoint](Endpoint-AcmeOfCTPortalEndpoint.html)   [Endpoint](http://hl7.org/fhir/R4/endpoint.html)   [PlannetEndpoint](StructureDefinition-plannet-Endpoint.html)"

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-02: Plan Net Endpoint Resource Conformance

### 1. Requirement Analysis

* **Testability Assessment**: Automatic
* **Complexity**: Simple
* **Prerequisites**:
    * A running FHIR server that implements the PlannetEndpoint profile.
    * Test client capable of making FHIR API calls.
    * Access token (if authentication is required).

### 2. Test Implementation Strategy

* **Required FHIR Operations**:
    * `GET /Endpoint` - To retrieve all Endpoint resources.
    * `POST /Endpoint/$validate` - To validate Endpoint resources against the PlannetEndpoint profile.

* **Test Data Requirements**:
    * **Positive Test Case**: A valid Endpoint resource conforming to the PlannetEndpoint profile.
    * **Negative Test Case**: An Endpoint resource that violates the PlannetEndpoint profile constraints (e.g., missing required element).

* **Validation Criteria**:
    * **Positive Test Case**:
        * HTTP status code 200 OK for both GET and POST requests.
        * Response body for POST request should indicate successful validation against the PlannetEndpoint profile.
    * **Negative Test Case**:
        * HTTP status code 400 Bad Request for POST request.
        * Response body for POST request should contain OperationOutcome resource detailing validation errors.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://your-fhir-server/fhir')
client.set_bearer_token('your-access-token')

# Test Case 1: Positive - Valid Endpoint Resource
def test_valid_endpoint(client)
  # Load valid Endpoint resource from file or create one
  valid_endpoint = FHIR::Endpoint.from_json(File.read('valid_endpoint.json'))

  # POST request for validation
  begin
    response = client.validate(resource: valid_endpoint, profile: 'StructureDefinition/plannet-Endpoint')
    
    # Assertions
    assert_equal 200, response.code, 'Expected HTTP 200 OK'
    assert_true response.resource.is_a?(FHIR::OperationOutcome), 'Expected OperationOutcome resource'
    assert_equal 'OperationOutcome', response.resource.resourceType
    assert_true response.resource.issue.empty?, 'Expected no validation errors'

    puts 'Positive Test Case: Valid Endpoint - PASSED'
  rescue => e
    puts "Positive Test Case: Valid Endpoint - FAILED: #{e.message}"
  end
end

# Test Case 2: Negative - Invalid Endpoint Resource
def test_invalid_endpoint(client)
  # Load invalid Endpoint resource from file or create one
  invalid_endpoint = FHIR::Endpoint.from_json(File.read('invalid_endpoint.json'))

  # POST request for validation
  begin
    response = client.validate(resource: invalid_endpoint, profile: 'StructureDefinition/plannet-Endpoint')

    # Assertions
    assert_equal 400, response.code, 'Expected HTTP 400 Bad Request'
    assert_true response.resource.is_a?(FHIR::OperationOutcome), 'Expected OperationOutcome resource'
    assert_equal 'OperationOutcome', response.resource.resourceType
    assert_false response.resource.issue.empty?, 'Expected validation errors'

    puts 'Negative Test Case: Invalid Endpoint - PASSED'
  rescue => e
    puts "Negative Test Case: Invalid Endpoint - FAILED: #{e.message}"
  end
end

# Run test cases
test_valid_endpoint(client)
test_invalid_endpoint(client)
```

### 4. Potential Issues and Edge Cases

* **Profile Retrieval**: The test assumes the PlannetEndpoint profile is available on the server. It might be necessary to retrieve and cache the profile before validation.
* **Server Load**: Running numerous validation requests can impact server performance. Consider load testing and optimizing test execution.
* **Security**: Ensure the test client uses appropriate authentication and authorization mechanisms to access the FHIR server.
* **Edge Cases**: 
    * Test with various data types and values within the Endpoint resource to ensure comprehensive coverage of the profile constraints.
    * Test with different FHIR versions if applicable.
    * Test with different FHIR client libraries to ensure consistent behavior. 


---

<a id='req-03'></a>

### REQ-03: Plan Net HealthcareService resources SHALL conform to the PlannetHealthcareService profile.

**Description**: "**Example**   **ResourceType**   **Profiles** \n[BurrClinicServices](HealthcareService-BurrClinicServices.html)   [HealthcareService](http://hl7.org/fhir/R4/healthcareservice.html)   [PlannetHealthcareService](StructureDefinition-plannet-HealthcareService.html)"

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-03: Plan Net HealthcareService Conformance

### 1. Requirement Analysis

**Testability Assessment:** Automatic
**Complexity:** Simple
**Prerequisites:**
* Running FHIR server under test
* Server should support `search` operation on `HealthcareService` resource
* Test data containing `HealthcareService` resources conforming to the `PlannetHealthcareService` profile

### 2. Test Implementation Strategy

**Required FHIR Operations:**
* `GET [base]/HealthcareService?identifier=[identifier]`

**Test Data Requirements:**
* **Positive Test Case:** A `HealthcareService` resource instance conforming to the `PlannetHealthcareService` profile, identifiable by a specific `identifier`.
* **Negative Test Case:** A `HealthcareService` resource instance **not** conforming to the `PlannetHealthcareService` profile, identifiable by a specific `identifier`.

**Validation Criteria:**
* **Positive Test Case:**
    * Response status code should be `200 OK`.
    * Response body should contain a `Bundle` resource.
    * The `Bundle` should contain at least one `HealthcareService` entry.
    * The returned `HealthcareService` resource should validate against the `PlannetHealthcareService` profile.
* **Negative Test Case:**
    * Response status code should be `200 OK`.
    * Response body should contain a `Bundle` resource.
    * The `Bundle` should contain at least one `HealthcareService` entry.
    * The returned `HealthcareService` resource should **not** validate against the `PlannetHealthcareService` profile.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://[your-fhir-server]/[fhir-base-path]')

# Test data setup
positive_identifier = 'test-healthcare-service-positive'
negative_identifier = 'test-healthcare-service-negative'

# Positive test case
def test_healthcare_service_conformance_positive(client, identifier)
  begin
    response = client.search(FHIR::HealthcareService, search: { parameters: { identifier: identifier } })

    # Validate response code
    assert_equal 200, response.code, "Expected 200 OK, got #{response.code}"

    # Validate resource type and count
    assert_equal 'Bundle', response.resource.resourceType
    assert response.resource.entry.size > 0, 'No HealthcareService resources found'

    # Validate conformance to PlannetHealthcareService profile
    validation_result = client.validate(response.resource.entry.first.resource, profile: 'StructureDefinition/plannet-HealthcareService')
    assert validation_result.valid?, "HealthcareService resource does not conform to PlannetHealthcareService profile: #{validation_result.message}"

    puts 'Positive test case passed.'

  rescue => e
    puts "Error in positive test case: #{e.message}"
  end
end

# Negative test case
def test_healthcare_service_conformance_negative(client, identifier)
  begin
    response = client.search(FHIR::HealthcareService, search: { parameters: { identifier: identifier } })

    # Validate response code
    assert_equal 200, response.code, "Expected 200 OK, got #{response.code}"

    # Validate resource type and count
    assert_equal 'Bundle', response.resource.resourceType
    assert response.resource.entry.size > 0, 'No HealthcareService resources found'

    # Validate non-conformance to PlannetHealthcareService profile
    validation_result = client.validate(response.resource.entry.first.resource, profile: 'StructureDefinition/plannet-HealthcareService')
    assert !validation_result.valid?, 'HealthcareService resource unexpectedly conforms to PlannetHealthcareService profile'

    puts 'Negative test case passed.'

  rescue => e
    puts "Error in negative test case: #{e.message}"
  end
end

# Run tests
test_healthcare_service_conformance_positive(client, positive_identifier)
test_healthcare_service_conformance_negative(client, negative_identifier)
```

### 4. Potential Issues and Edge Cases

* **Profile Validation:** Ensure the FHIR client library used supports profile validation and correctly handles any validation errors.
* **Data Setup:** The test relies on pre-existing test data. Ensure the data is correctly loaded and accessible by the test script.
* **Identifier Uniqueness:** Use unique identifiers for test data to avoid conflicts with existing resources.
* **Server Load:** Consider the impact of running these tests on a production server with high traffic. Implement appropriate error handling and timeouts.
* **Security:** Ensure the test script uses appropriate authentication and authorization mechanisms to access the FHIR server. 


---

<a id='req-04'></a>

### REQ-04: Plan Net InsurancePlan resources SHALL conform to the PlannetInsurancePlan profile.

**Description**: "**Example**   **ResourceType**   **Profiles** \n[AcmeQHPBronze](InsurancePlan-AcmeQHPBronze.html)   [InsurancePlan](http://hl7.org/fhir/R4/insuranceplan.html)   [PlannetInsurancePlan](StructureDefinition-plannet-InsurancePlan.html)"

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-04: Plan Net InsurancePlan Profile Conformance

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running FHIR server that implements the Plan Net IG.
    * Access credentials to the FHIR server with appropriate permissions.
    * Test InsurancePlan resources conforming to the PlannetInsurancePlan profile.
    * Test InsurancePlan resources that do not conform to the PlannetInsurancePlan profile (for negative testing).

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * `POST /InsurancePlan/$validate` (for profile validation)

* **Test Data Requirements:**
    * **Positive Test Cases:**
        * Valid InsurancePlan resources conforming to the PlannetInsurancePlan profile. These resources should include various combinations of required and optional elements with valid data types and value sets.
    * **Negative Test Cases:**
        * Invalid InsurancePlan resources that violate constraints defined in the PlannetInsurancePlan profile. This could include missing required elements, invalid data types, or values outside the allowed value sets.

* **Validation Criteria:**
    * **Positive Test Cases:**
        * The `$validate` operation should return an HTTP status code 200 (OK).
        * The `OperationOutcome` resource in the response body should indicate success with no "error" or "fatal" issues.
    * **Negative Test Cases:**
        * The `$validate` operation should return an HTTP status code 400 (Bad Request).
        * The `OperationOutcome` resource in the response body should contain at least one "error" or "fatal" issue detailing the validation failure and the specific constraint violated.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://your-fhir-server/fhir')
client.set_bearer_token('your-access-token')

# Load test InsurancePlan resources
valid_insurance_plan = FHIR::InsurancePlan.from_json(File.read('valid_insurance_plan.json'))
invalid_insurance_plan = FHIR::InsurancePlan.from_json(File.read('invalid_insurance_plan.json'))

# Define validation function
def validate_insurance_plan(client, insurance_plan)
  begin
    response = client.validate(insurance_plan, profile: 'StructureDefinition/plannet-InsurancePlan')

    if response.code == 200
      puts "Validation successful: #{response.body}"
      return true
    else
      puts "Validation failed: #{response.body}"
      return false
    end
  rescue => e
    puts "Error during validation: #{e.message}"
    return false
  end
end

# Positive test case
puts "Running positive test case..."
if validate_insurance_plan(client, valid_insurance_plan)
  puts "Positive test case passed."
else
  puts "Positive test case failed."
end

# Negative test case
puts "Running negative test case..."
if !validate_insurance_plan(client, invalid_insurance_plan)
  puts "Negative test case passed."
else
  puts "Negative test case failed."
end
```

### 4. Potential Issues and Edge Cases

* **Complex Data Types:** The PlannetInsurancePlan profile might use complex data types with nested elements and constraints. The test cases should cover various combinations and edge cases within these complex types.
* **Code Systems and Value Sets:** Ensure that the test data utilizes the correct code systems and value sets defined in the PlannetInsurancePlan profile. Test cases should include valid and invalid codes to verify proper validation.
* **Performance:** Consider testing with a large number of InsurancePlan resources to assess the performance of the validation process.
* **Security:** Ensure that the test environment is secure and that sensitive data within the test InsurancePlan resources is properly anonymized or masked. 


---

<a id='req-05'></a>

### REQ-05: Plan Net Location resources SHALL conform to the PlannetLocation profile.

**Description**: "**Example**   **ResourceType**   **Profiles** \n[CancerClinicLoc](Location-CancerClinicLoc.html)   [Location](http://hl7.org/fhir/R4/location.html)   [PlannetLocation](StructureDefinition-plannet-Location.html)"

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-05: Plan Net Location Resources Conformance

### 1. Requirement Analysis

* **Testability Assessment**: Automatic
* **Complexity**: Simple
* **Prerequisites**:
    * A running FHIR server that implements the PlannetLocation profile.
    * Test data consisting of valid and invalid Location resources.

### 2. Test Implementation Strategy

* **Required FHIR Operations**:
    * `POST /Location` (Create)
    * `GET /Location/{id}` (Read)

* **Test Data Requirements**:
    * **Valid Location Resource:** A Location resource conforming to the PlannetLocation profile.
    * **Invalid Location Resource:** A Location resource missing a required element or containing an invalid value according to the PlannetLocation profile.

* **Validation Criteria**:
    * **Positive Test Case:**
        * A successful `POST` request with a valid Location resource should return HTTP status code `201 Created`.
        * The returned Location resource should contain the PlannetLocation profile in its `meta.profile` element.
    * **Negative Test Case:**
        * A `POST` request with an invalid Location resource should return HTTP status code `400 Bad Request` or similar error code.
        * The response should contain an OperationOutcome resource detailing the validation errors.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://your-fhir-server/fhir')

# Test Case 1: Valid Location Resource
def test_valid_location(client)
  # Load valid Location resource from file
  valid_location = FHIR::Location.from_json(File.read('valid_location.json'))

  # Create the resource on the server
  response = client.create(valid_location)

  # Assertions
  assert_equal 201, response.code, "Expected 201 Created, got #{response.code}"
  assert_includes response.resource.meta.profile, 'StructureDefinition/plannet-Location', "PlannetLocation profile not found in returned resource"

  # Return the created resource ID for cleanup
  return response.resource.id
end

# Test Case 2: Invalid Location Resource
def test_invalid_location(client)
  # Load invalid Location resource from file
  invalid_location = FHIR::Location.from_json(File.read('invalid_location.json'))

  # Attempt to create the resource on the server
  response = client.create(invalid_location)

  # Assertions
  assert_includes [400, 422], response.code, "Expected 400 or 422 error, got #{response.code}"
  assert_not_nil response.body, "Expected OperationOutcome in response body"

  # Log validation errors
  puts "Validation errors:"
  puts response.body
end

# Run tests
puts "Running test with valid Location resource..."
created_resource_id = test_valid_location(client)
puts "Test passed!"

puts "Running test with invalid Location resource..."
test_invalid_location(client)
puts "Test passed!"

# Cleanup: Delete the created resource
client.destroy(FHIR::Location, created_resource_id) if created_resource_id
```

### 4. Potential Issues and Edge Cases

* **Profile Validation**: Ensure the FHIR server correctly implements and enforces the PlannetLocation profile.
* **Data Types and Constraints**: Test various data types and constraints defined in the profile (e.g., specific value sets, code systems).
* **Edge Cases**: Test boundary conditions for data types (e.g., maximum length of strings) and unusual but valid data combinations.
* **Performance**: Consider testing with a large number of Location resources to assess performance impact.
* **Security**: Verify that authorization and authentication mechanisms are enforced when creating and accessing Location resources. 


---

<a id='req-08'></a>

### REQ-08: Networks SHALL have an NPI

**Description**: "Networks SHALL have an NPI."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-08: Networks SHALL have an NPI

### 1. Requirement Analysis

**Testability Assessment:** Automatic
**Complexity:** Simple
**Prerequisites:** 
* A running FHIR server that implements the Network resource.
* At least one Network resource instance available for testing.

### 2. Test Implementation Strategy

**Required FHIR Operations:**
* **READ:** `GET /Network/{id}`

**Test Data Requirements:**
* A valid Network resource ID.

**Validation Criteria:**
* **Positive Test Case:** The response for the Network resource MUST return a `200 OK` status code and the resource MUST contain a non-empty `identifier` element where at least one identifier has a `system` element with the value "http://hl7.org/fhir/sid/us-npi" and a non-empty `value` element.
* **Negative Test Case:**
    * The response for the Network resource returns a `200 OK` status code but the resource does not contain an `identifier` element.
    * The response for the Network resource returns a `200 OK` status code but the resource does not contain an `identifier` element with a `system` of "http://hl7.org/fhir/sid/us-npi".
    * The response for the Network resource returns a `200 OK` status code but the resource contains an `identifier` element with a `system` of "http://hl7.org/fhir/sid/us-npi" but the `value` element is empty.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://your-fhir-server-url')

# Test Case 1: Positive Test - Network has NPI
def test_network_has_npi(client, network_id)
  begin
    response = client.read(FHIR::Network, network_id)

    assert_equal 200, response.code, "Expected 200 OK, but got #{response.code}"

    network = response.resource
    npi_identifier = network.identifier.find { |id| id.system == 'http://hl7.org/fhir/sid/us-npi' && !id.value.nil? && !id.value.empty? }

    assert_not_nil npi_identifier, "Network resource does not contain an NPI identifier."
    puts "Test Passed: Network has NPI."

  rescue => e
    puts "Test Failed: #{e.message}"
  end
end

# Test Case 2: Negative Test - Network does not have NPI
def test_network_missing_npi(client, network_id)
  begin
    response = client.read(FHIR::Network, network_id)

    assert_equal 200, response.code, "Expected 200 OK, but got #{response.code}"

    network = response.resource
    npi_identifier = network.identifier.find { |id| id.system == 'http://hl7.org/fhir/sid/us-npi' && !id.value.nil? && !id.value.empty? }

    assert_nil npi_identifier, "Network resource should not contain an NPI identifier."
    puts "Test Passed: Network does not have NPI."

  rescue => e
    puts "Test Failed: #{e.message}"
  end
end

# Example usage
network_id = '12345' # Replace with actual Network resource ID

test_network_has_npi(client, network_id)
test_network_missing_npi(client, network_id)
```

### 4. Potential Issues and Edge Cases

* **Multiple Identifiers:** The Network resource may contain multiple identifiers. The test should ensure that at least one identifier represents the NPI.
* **Identifier Data Type:** The `value` element of the NPI identifier should be validated to ensure it conforms to the expected data type and format for NPIs.
* **Performance:**  Testing with a large number of Network resources could impact performance. Consider using a smaller subset for performance testing.
* **Security:** Ensure that test data does not contain sensitive information and that the test environment is appropriately secured. 


---

<a id='req-09'></a>

### REQ-09: Organizations SHALL have an NPI

**Description**: "Organizations SHALL have an NPI."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-09: Organizations SHALL have an NPI

### 1. Requirement Analysis

* **Testability Assessment**: Automatic
* **Complexity**: Simple
* **Prerequisites**:
    * A running FHIR server with the implemented Implementation Guide.
    * Access to create and retrieve Organization resources.

### 2. Test Implementation Strategy

* **Required FHIR Operations**:
    * **Create**: POST /Organization
    * **Read**: GET /Organization/{id}

* **Test Data Requirements**:
    * **Valid Organization Resource**: A JSON representation of an Organization resource with a valid NPI in the `identifier` field.
    * **Invalid Organization Resource**: A JSON representation of an Organization resource without an NPI in the `identifier` field.

* **Validation Criteria**:
    * **Positive Test Case**:
        * A successful POST request with the valid Organization resource should return a `201 Created` status code.
        * A subsequent GET request for the created resource should return a `200 OK` status code and the returned Organization resource should contain the provided NPI in the `identifier` field.
    * **Negative Test Case**:
        * A POST request with the invalid Organization resource should return a `400 Bad Request` (or similar error) status code.
        * The response body should contain an OperationOutcome resource indicating the reason for the failure, specifically mentioning the missing NPI.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# FHIR server base URL
base_url = 'https://your-fhir-server/fhir'

# FHIR client
client = FHIR::Client.new(base_url)

# Test Case 1: Valid Organization with NPI
def test_valid_organization_with_npi(client)
  # Valid Organization resource with NPI
  valid_organization = {
    resourceType: 'Organization',
    identifier: [
      {
        system: 'http://hl7.org/fhir/sid/us-npi',
        value: '1234567890' # Replace with a valid NPI
      }
    ]
    # ... other required fields ...
  }

  # Create the Organization resource
  response = client.create(resource: FHIR::Organization.new(valid_organization))

  # Assertions
  assert_equal 201, response.code, "Expected 201 Created, got #{response.code}"

  # Retrieve the created resource
  created_organization = client.read(FHIR::Organization, response.resource.id).resource

  # Assert NPI presence in the returned resource
  npi_found = created_organization.identifier.any? do |identifier|
    identifier.system == 'http://hl7.org/fhir/sid/us-npi' && identifier.value == '1234567890'
  end

  assert npi_found, "NPI not found in the created Organization resource"
end

# Test Case 2: Invalid Organization without NPI
def test_invalid_organization_without_npi(client)
  # Invalid Organization resource without NPI
  invalid_organization = {
    resourceType: 'Organization'
    # ... other required fields ...
  }

  # Create the Organization resource
  response = client.create(resource: FHIR::Organization.new(invalid_organization))

  # Assertions
  assert_equal 400, response.code, "Expected 400 Bad Request, got #{response.code}"

  # Assert OperationOutcome indicates missing NPI
  assert_includes response.body, 'NPI is required', "OperationOutcome does not mention missing NPI"
end

# Run the test cases
test_valid_organization_with_npi(client)
test_invalid_organization_without_npi(client)

```

### 4. Potential Issues and Edge Cases

* **Invalid NPI format**: The test should include cases with invalid NPI formats (e.g., incorrect length, non-numeric characters) and verify appropriate error handling.
* **Multiple Identifiers**: The test should cover scenarios where the Organization resource has multiple identifiers and ensure the validation specifically targets the NPI identifier.
* **NPI in different identifier systems**: The test should check if the system validates the NPI even if it's present under a different identifier system than the expected 'http://hl7.org/fhir/sid/us-npi'.
* **Performance**:  Consider testing with a large number of Organization resources to assess performance impact.
* **Security**: Ensure the test data uses realistic but non-sensitive NPIs to avoid exposing real-world data. 


---

<a id='req-10'></a>

### REQ-10: No summary

**Description**: "The participating organization SHALL be identified by their NPI in the identifier with a system of  http://hl7.org/fhir/sid/us-npi."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-10: Participating Organization NPI

### 1. Requirement Analysis

**Testability Assessment:** Automatic
**Complexity:** Simple
**Prerequisites:**
* Access to the FHIR server under test.
* Knowledge of a specific resource (e.g., Organization, Practitioner) where the participating organization is identified. 

### 2. Test Implementation Strategy

**Required FHIR Operations:**
* **READ:** Retrieve the resource (e.g., Organization, Practitioner) that should contain the participating organization's identifier.

**Test Data Requirements:**
* **Resource ID:** The logical ID of the resource to be retrieved.

**Validation Criteria:**
1. **Response Status Code:** Verify that the response status code is 200 (OK).
2. **Identifier Presence:** Verify that the resource contains at least one identifier element.
3. **NPI System:** Verify that at least one identifier element has a `system` value of "http://hl7.org/fhir/sid/us-npi".
4. **NPI Value:** Verify that the corresponding `value` element of the identified NPI identifier is a valid NPI (10-digit number).

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# **Test Case: Verify Participating Organization NPI**

def test_participating_organization_npi(client, resource_id)
  begin
    # 1. Retrieve the resource
    response = client.read(FHIR::Organization, resource_id) # Replace FHIR::Organization with the appropriate resource type

    # 2. Validate response status code
    assert_equal 200, response.code, "Expected 200 OK, but got #{response.code}"

    # 3. Extract identifiers from the resource
    identifiers = response.resource.identifier

    # 4. Find the NPI identifier
    npi_identifier = identifiers.find { |identifier| identifier.system == 'http://hl7.org/fhir/sid/us-npi' }

    # 5. Validate NPI identifier presence
    assert_not_nil npi_identifier, "No NPI identifier found in the resource"

    # 6. Validate NPI value format (10-digit number)
    assert_match /^\d{10}$/, npi_identifier.value, "Invalid NPI format: #{npi_identifier.value}"

    puts "Test Passed: Participating organization NPI is present and valid."

  rescue => e
    puts "Test Failed: #{e.message}"
  end
end

# Example usage:
client = FHIR::Client.new('https://your-fhir-server-url')
resource_id = '12345' # Replace with the actual resource ID
test_participating_organization_npi(client, resource_id)
```

### 4. Potential Issues and Edge Cases

* **Multiple Identifiers:** The resource might contain multiple identifiers. The test should handle this by iterating through them and checking if at least one matches the NPI criteria.
* **Missing Identifier:** The resource might not have any identifier element. The test should handle this gracefully and report a clear error message.
* **Invalid NPI Format:** The NPI value might not adhere to the 10-digit format. The test should validate the format and report an error if it's invalid.
* **Resource Type:** The requirement doesn't specify the exact resource type. The test implementation should be adaptable to different resource types where the participating organization is identified.
* **Performance:** Retrieving large resources might impact performance. Consider using search operations with specific parameters to optimize retrieval. 
* **Security:** Ensure appropriate authentication and authorization mechanisms are in place when accessing the FHIR server. 


---

<a id='req-11'></a>

### REQ-11: Practitioner Role SHALL have a Code

**Description**: "Practitioner Roles SHALL have at least one code."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-11: Practitioner Role SHALL have a Code

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running FHIR server with the PractitionerRole resource implemented.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * `POST` - Create a PractitionerRole resource
    * `GET` - Retrieve the created PractitionerRole resource

* **Test Data Requirements:**
    * **Valid PractitionerRole:** A PractitionerRole resource with at least one code element.
    * **Invalid PractitionerRole:** A PractitionerRole resource without any code element.

* **Validation Criteria:**
    * **Positive Test Case:** Verify that the server accepts a PractitionerRole resource with at least one code and returns a `201 Created` status code.
    * **Negative Test Case:** Verify that the server rejects a PractitionerRole resource without any code and returns a `400 Bad Request` (or similar error) status code.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# FHIR Server Endpoint
fhir_server_url = 'https://your-fhir-server/fhir'
client = FHIR::Client.new(fhir_server_url)

# Test Data
valid_practitioner_role = {
  "resourceType": "PractitionerRole",
  "code": [
    {
      "coding": [
        {
          "system": "http://terminology.hl7.org/umls/usps",
          "code": "RNP"
        }
      ]
    }
  ]
}

invalid_practitioner_role = {
  "resourceType": "PractitionerRole"
}

# Positive Test Case
begin
  response = client.create(valid_practitioner_role)
  assert_equal(response.code, 201, "Expected 201 Created, got #{response.code}")
  puts "Positive Test Case: PASSED"
rescue => e
  puts "Positive Test Case: FAILED - #{e.message}"
end

# Negative Test Case
begin
  response = client.create(invalid_practitioner_role)
  puts "Negative Test Case: FAILED - Expected error, got #{response.code}"
rescue => e
  assert_equal(e.message.include?("code is required"), true, "Expected error message about missing code")
  puts "Negative Test Case: PASSED"
end
```

### 4. Potential Issues and Edge Cases

* **Edge Cases:**
    * Test with different code systems and values.
    * Test with multiple code elements.
    * Test with empty code elements (e.g., `code: [{}]`).
* **Performance Considerations:**
    *  For large-scale testing, consider the performance impact of creating and deleting numerous resources. Implement cleanup mechanisms to delete test resources after execution.
* **Security Considerations:**
    * Ensure test data does not contain sensitive information.
    * Use appropriate authentication and authorization mechanisms when interacting with the FHIR server. 


---

<a id='req-12'></a>

### REQ-12: Do not require authentication for Plan-Net service access

**Description**: "Access to the Plan-Net service should not require authentication, and the server should not maintain any records that could associate the consumer with the entities that were queried."

**Actor**: Server

**Conformance**: SHOULD

## Test Specification for REQ-12: Do Not Require Authentication for Plan-Net Service Access

### 1. Requirement Analysis

* **Testability Assessment:** Hybrid (Manual inspection of server logs/configuration alongside automated API calls)
* **Complexity:** Moderate
* **Prerequisites:**
    * Deployed FHIR server with Plan-Net service implemented.
    * Network access to the FHIR server.
    * Tool for making FHIR API calls (e.g., Postman, curl).
    * Access to server logs or configuration to verify no user identification is stored.

### 2. Test Implementation Strategy

#### 2.1 Required FHIR Operations:

* **Read Operation:**  Retrieve resources from the Plan-Net service using the appropriate FHIR endpoint (e.g., `GET /PlanNet`).

#### 2.2 Test Data Requirements:

* No specific test data is required for the API call itself, as the focus is on the authentication aspect.

#### 2.3 Validation Criteria:

* **Successful Response:** The server should return a successful HTTP status code (e.g., 200 OK) without requiring any authentication headers or parameters.
* **No User Identification:** Server logs and configuration should not contain any information that could be used to associate the request with a specific user or client. This requires manual inspection.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'rest-client'
require 'json'

# Test Case 1: Successful access without authentication

def test_plan_net_access_no_auth
  begin
    # Make a GET request to the Plan-Net service endpoint without authentication headers
    response = RestClient.get('https://[your-fhir-server]/PlanNet')

    # Assert successful response code
    if response.code == 200
      puts "Test Passed: Plan-Net service accessed successfully without authentication."
    else
      raise "Test Failed: Unexpected response code: #{response.code}"
    end

  rescue RestClient::ExceptionWithResponse => e
    puts "Test Failed: Request failed with error: #{e.message}"
  end

  # Manual Inspection Required:
  puts "Please inspect server logs and configuration to ensure no user identification is stored."
end

test_plan_net_access_no_auth
```

### 4. Potential Issues and Edge Cases

* **Server Configuration Errors:** The server might be misconfigured and require authentication even though the requirement states otherwise.
* **Logging Practices:** The server might log IP addresses or other metadata that could potentially be used to identify users, even if not explicitly storing user credentials.
* **Caching Mechanisms:** Caching mechanisms on the server or network infrastructure could potentially retain user-specific information.
* **Performance Impact:** Not requiring authentication might have performance implications if the server needs to handle a large volume of requests.

**Recommendations:**

* Thoroughly review server logs and configuration files to ensure compliance.
* Consider implementing rate limiting or other security measures to mitigate potential risks associated with not requiring authentication.
* Document the rationale for not requiring authentication and any potential security implications. 


---

<a id='req-13'></a>

### REQ-13: Prohibit storage of consumer-identifying information

**Description**: "Access to the Plan-Net service should not require authentication, and the server should not maintain any records that could associate the consumer with the entities that were queried."

**Actor**: Server

**Conformance**: SHOULD

## Test Specification for REQ-13: Prohibit Storage of Consumer-Identifying Information

### 1. Requirement Analysis

* **Testability Assessment:** Hybrid (Manual inspection of logs/database combined with automated API calls)
* **Complexity:** Moderate
* **Prerequisites:**
    * Deployed and running instance of the Plan-Net FHIR server
    * Access to server logs or database for inspection
    * Tool for making FHIR API calls (e.g., Postman, cURL)
    * Test data for FHIR resources relevant to Plan-Net service

### 2. Test Implementation Strategy

#### 2.1 Required FHIR Operations:

1. **Create:** Send a POST request to create a resource relevant to the Plan-Net service.
2. **Read:** Send a GET request to retrieve the created resource.
3. **Search:** Send a GET request with search parameters to query for resources.

#### 2.2 Test Data Requirements:

* **Valid FHIR resources:**  Use realistic but anonymized data for resources relevant to the Plan-Net service.
* **Unique identifiers:** Ensure each test case uses unique identifiers to avoid conflicts.

#### 2.3 Validation Criteria:

* **No Authentication:** Verify that all FHIR API calls succeed without requiring authentication.
* **No Consumer Identifiers:**
    * **Logs:** Manually inspect server logs after each test case to confirm no consumer-identifying information is logged (e.g., IP addresses, user agents, session IDs).
    * **Database:**  Inspect the database to ensure no information is stored that could link a consumer to their queries. This includes direct identifiers and indirect identifiers that could be combined to re-identify a consumer.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'
require 'rest-client'

# Configure FHIR client
client = FHIR::Client.new('https://plan-net-server/fhir')

# Test Case 1: Create Resource
test_resource = # Create a valid FHIR resource with anonymized data

begin
  # Send POST request without authentication
  response = client.create(resource: test_resource)

  # Assert successful creation
  assert_equal 201, response.code

  # Log inspection required: Verify no consumer-identifying information is logged.

rescue => e
  puts "Test Case 1 Failed: #{e.message}"
end

# Test Case 2: Read Resource
resource_id = # ID of the created resource

begin
  # Send GET request without authentication
  response = client.read(resource_type: 'ResourceName', id: resource_id)

  # Assert successful retrieval
  assert_equal 200, response.code

  # Log inspection required: Verify no consumer-identifying information is logged.

rescue => e
  puts "Test Case 2 Failed: #{e.message}"
end

# Test Case 3: Search Resources
search_params = {
  # Define search parameters
}

begin
  # Send GET request with search parameters without authentication
  response = client.search(resource_type: 'ResourceName', search: { parameters: search_params })

  # Assert successful search
  assert_equal 200, response.code

  # Log inspection required: Verify no consumer-identifying information is logged.
  # Database inspection required: Verify no consumer-identifiable information is stored.

rescue => e
  puts "Test Case 3 Failed: #{e.message}"
end

# Additional test cases can be added for other FHIR operations and edge cases.
```

### 4. Potential Issues and Edge Cases

* **Indirect Identifiers:**  The server should not store combinations of data that could be used to re-identify a consumer, even if individual data points seem innocuous.
* **Caching:**  Ensure that server-side caching mechanisms do not inadvertently store consumer-identifying information.
* **Error Logging:**  Error logs should be anonymized to prevent accidental storage of consumer data.
* **Performance Impact:**  Evaluate the performance impact of not storing any consumer information. Consider trade-offs between privacy and performance if necessary.
* **Third-Party Services:** If the Plan-Net service relies on third-party services, ensure they also comply with the requirement to not store consumer-identifying information.

This test specification provides a starting point for verifying REQ-13. It is crucial to adapt and expand the test cases based on the specific functionalities and data flows of the Plan-Net service. 


---

<a id='req-14'></a>

### REQ-14: Prohibit requiring consumer identification for directory queries

**Description**: "A conformant Plan-Net service **SHALL NOT** require a directory mobile application to send consumer identifying information in order to query content."

**Actor**: Server

**Conformance**: SHALL NOT

## Test Specification for REQ-14: Prohibit Requiring Consumer Identification for Directory Queries

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:** 
    * A running FHIR server compliant with the Plan-Net implementation guide.
    * A client capable of making FHIR API requests.
    * Test data representing a valid directory query.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * **GET** request to the relevant directory resource endpoint (e.g., `Patient`, `Practitioner`, etc.) with query parameters.
* **Test Data Requirements:**
    * A valid directory query that does not include any consumer identifying information. For example, a query for practitioners based on specialty.
* **Validation Criteria:**
    * **Positive Test Case:** The server **SHALL** successfully process the directory query and return the requested data without requiring any consumer identifying information.
    * **Negative Test Case:** The server **SHALL NOT** return an error or require authentication/authorization based on missing consumer identifying information.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://your-fhir-server-endpoint')

# Define test data - a valid directory query without consumer information
test_query = {
  _summary: 'true',
  specialty: 'http://hl7.org/fhir/us/core/ValueSet/us-core-provider-specialty|cardio'
}

# Positive Test Case
begin
  response = client.search('Practitioner', search: { parameters: test_query })

  # Assert successful response
  assert_equal 200, response.code, "Expected 200 OK, but got #{response.code}"
  puts "Positive Test Case Passed: Server successfully processed the directory query."

rescue => e
  puts "Positive Test Case Failed: #{e.message}"
end

# Negative Test Case (Indirectly tested through the positive case)
# If the server requires consumer information, the positive test would have failed.

```

### 4. Potential Issues and Edge Cases

* **Corner Cases:**
    * Test with various valid directory queries to ensure no specific query triggers the requirement for consumer information.
    * Test with empty query parameters to verify the server handles it gracefully.
* **Performance Considerations:**
    * While not directly related to the requirement, consider performance testing with large datasets to ensure efficient directory queries.
* **Security Considerations:**
    * Verify that the server does not leak any sensitive information in the response, even without requiring consumer identification.
    * Ensure the server implements appropriate rate limiting to prevent abuse. 


---

<a id='req-23'></a>

### REQ-23: Provide lastUpdate timestamp in profile data content

**Description**: "Each profile in this guide requires that the lastUpdate timestamp be provided as part of the profile's data content."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-23: Provide lastUpdate timestamp in profile data content

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running FHIR server implementing the profiles defined in the guide.
    * Access credentials to the FHIR server with appropriate permissions.

### 2. Test Implementation Strategy

* **Required FHIR Operations:** 
    * `GET` request to retrieve a profile resource instance.
* **Test Data Requirements:**
    * A list of profile URLs defined in the implementation guide.
* **Validation Criteria:**
    * Verify that the response body for each profile resource instance contains a non-null `lastUpdate` element.
    * Verify that the `lastUpdate` element conforms to the FHIR dateTime data type format.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://your-fhir-server-url')

# List of profile URLs to test
profile_urls = [
  'http://example.org/fhir/StructureDefinition/MyProfile1',
  'http://example.org/fhir/StructureDefinition/MyProfile2',
  # ... add other profile URLs from the implementation guide
]

# Iterate through each profile URL
profile_urls.each do |profile_url|
  begin
    # Retrieve the profile resource
    response = client.read(FHIR::StructureDefinition, profile_url)

    # Check if the request was successful
    if response.code == 200
      profile = response.resource

      # Check if lastUpdate element exists and is not nil
      if profile.lastUpdate.present?
        puts "PASS: Profile '#{profile_url}' has a lastUpdate timestamp."

        # Validate lastUpdate data type (optional but recommended)
        if profile.lastUpdate.valid?
          puts "     - lastUpdate timestamp format is valid."
        else
          puts "     - WARNING: lastUpdate timestamp format is invalid."
        end
      else
        puts "FAIL: Profile '#{profile_url}' does not have a lastUpdate timestamp."
      end
    else
      puts "ERROR: Could not retrieve profile '#{profile_url}'. Status code: #{response.code}"
    end

  rescue => e
    puts "ERROR: An error occurred while processing '#{profile_url}': #{e.message}"
  end
end
```

### 4. Potential Issues and Edge Cases

* **Corner Cases:**
    * Empty `lastUpdate` element: The server might return an empty string instead of a null value. The test should handle this case and report it as a failure.
    * Invalid `lastUpdate` format: The server might return a value that doesn't conform to the FHIR dateTime format. The test should validate the format and report a warning if it's invalid.
* **Performance Considerations:**
    * Retrieving multiple profiles in a loop might impact performance. Consider using asynchronous requests or batch operations for large numbers of profiles.
* **Security Considerations:**
    * Ensure that the test script uses appropriate authentication and authorization mechanisms to access the FHIR server.
    * Avoid storing sensitive information like access tokens directly in the script. Use environment variables or secure configuration files instead. 


---

<a id='req-27'></a>

### REQ-27: Support Organization Resource for Organization Information

**Description**: "Organization instances provide information about a specific organization and organizational hierarchies, including organization name, specialty, type, address and contact information."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-27: Support Organization Resource for Organization Information

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Moderate
* **Prerequisites:**
    * A running FHIR server that implements the Organization resource.
    * Test Organization data.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * **Create:** POST /Organization
    * **Read:** GET /Organization/{id}
    * **Search:** GET /Organization?parameter=value

* **Test Data Requirements:**
    * **Valid Organization data:**  Including name, type, address, telecom, etc.
    * **Invalid Organization data:** Missing required fields, incorrect data types, etc.
    * **Search parameters:**  Various combinations of search parameters to test search functionality.

* **Validation Criteria:**
    * **HTTP Status Codes:**
        * 200 (OK) for successful Read and Search operations.
        * 201 (Created) for successful Create operation.
        * 400 (Bad Request) for requests with invalid data.
        * Other relevant status codes based on server implementation.
    * **Response Content:**
        * Verify returned Organization resource conforms to FHIR specification.
        * Check for the presence and correctness of required elements (name, type, etc.).
        * Validate data types and formats of returned values.
        * Ensure search results match the specified criteria.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://your-fhir-server-url')

# Test Data
valid_organization = {
  resourceType: 'Organization',
  name: 'Test Hospital',
  type: [
    {
      coding: [
        {
          system: 'http://terminology.hl7.org/CodeSystem/organization-type',
          code: 'prov'
        }
      ]
    }
  ],
  address: [
    {
      line: ['123 Main St'],
      city: 'Anytown',
      state: 'CA',
      postalCode: '90210'
    }
  ],
  telecom: [
    {
      system: 'phone',
      value: '555-555-5555'
    }
  ]
}

# Test Case 1: Create Organization
begin
  response = client.create(resource: valid_organization)
  if response.code == 201
    puts 'Test Case 1: Create Organization - PASSED'
    created_organization_id = response.resource.id
  else
    puts "Test Case 1: Create Organization - FAILED. Status code: #{response.code}"
  end
rescue => e
  puts "Test Case 1: Create Organization - ERROR: #{e.message}"
end

# Test Case 2: Read Organization
begin
  response = client.read(resource: 'Organization', id: created_organization_id)
  if response.code == 200 && response.resource.name == 'Test Hospital'
    puts 'Test Case 2: Read Organization - PASSED'
  else
    puts "Test Case 2: Read Organization - FAILED. Status code: #{response.code}"
  end
rescue => e
  puts "Test Case 2: Read Organization - ERROR: #{e.message}"
end

# Test Case 3: Search Organization
begin
  response = client.search(resource: 'Organization', search: { parameters: { name: 'Test Hospital' } })
  if response.code == 200 && response.resource.entry.first.resource.name == 'Test Hospital'
    puts 'Test Case 3: Search Organization - PASSED'
  else
    puts "Test Case 3: Search Organization - FAILED. Status code: #{response.code}"
  end
rescue => e
  puts "Test Case 3: Search Organization - ERROR: #{e.message}"
end

# Additional test cases can be added for:
# - Creating an Organization with invalid data
# - Searching with different parameters and combinations
# - Testing edge cases like special characters in organization names
```

### 4. Potential Issues and Edge Cases

* **Data Validation:** Thoroughly test the server's validation of submitted data, including required fields, data types, and value sets.
* **Special Characters:** Test with organization names containing special characters, spaces, and different character encodings.
* **Edge Cases:** Consider edge cases like very long organization names, addresses with multiple lines, and international phone numbers.
* **Performance:**  Test with large datasets to assess the performance of create, read, and search operations.
* **Security:** Verify proper authentication and authorization mechanisms are in place to protect patient data.

This test specification provides a starting point for testing the "Support Organization Resource for Organization Information" requirement. It can be further expanded and customized based on the specific implementation and testing needs. 


---

<a id='req-28'></a>

### REQ-28: Support OrganizationAffiliation Resource for Role Descriptions

**Description**: "Organization Affiliation instances describe a role, and link a participating organization that provides or performs the role, with an organization where that role is available, and also links the participating organization to a HealthcareServices and networks."

**Actor**: Server

**Conformance**: SHALL

## Test Specification: OrganizationAffiliation Role Descriptions (REQ-28)

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Moderate
* **Prerequisites:**
    * A running FHIR server that implements the OrganizationAffiliation resource.
    * Pre-loaded test data including:
        * At least two Organization resources.
        * At least one HealthcareService resource.
        * At least one Network resource.

### 2. Test Implementation Strategy

#### 2.1 Required FHIR Operations

* **Create:** POST /OrganizationAffiliation
* **Read:** GET /OrganizationAffiliation/{id}
* **Search:** GET /OrganizationAffiliation?parameter=value

#### 2.2 Test Data Requirements

* **OrganizationAffiliation Resource:**
    * `participatingOrganization`: Reference to an Organization resource representing the organization providing the role.
    * `organization`: Reference to an Organization resource representing the organization where the role is available.
    * `code`: CodeableConcept describing the role.
    * `healthcareService`: Reference(s) to HealthcareService resource(s) associated with the role.
    * `network`: Reference(s) to Network resource(s) associated with the role.

#### 2.3 Validation Criteria

* **Positive Test Cases:**
    * Verify successful creation of OrganizationAffiliation resource with valid data.
    * Verify returned OrganizationAffiliation resource contains all expected data elements.
    * Verify ability to retrieve created OrganizationAffiliation resource by ID.
    * Verify ability to search for OrganizationAffiliation resources using relevant parameters (e.g., participatingOrganization, organization, code).

* **Negative Test Cases:**
    * Attempt to create an OrganizationAffiliation resource with missing mandatory fields (e.g., participatingOrganization, organization, code) and verify appropriate error response (e.g., HTTP 400 Bad Request).
    * Attempt to create an OrganizationAffiliation resource with invalid references and verify appropriate error response.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIRClient.new('https://your-fhir-server-url')

# Test Data
participating_org_id = 'org123'
organization_id = 'org456'
healthcare_service_id = 'hs789'
network_id = 'net012'
role_code = {
  "system": "http://terminology.hl7.org/CodeSystem/organization-role",
  "code": "provider"
}

# Positive Test Case: Create and Verify OrganizationAffiliation
def test_create_and_verify_organization_affiliation(client, participating_org_id, organization_id, healthcare_service_id, network_id, role_code)
  # Create OrganizationAffiliation resource
  org_affiliation = FHIR::OrganizationAffiliation.new(
    participatingOrganization: { reference: "Organization/#{participating_org_id}" },
    organization: { reference: "Organization/#{organization_id}" },
    code: [role_code],
    healthcareService: [{ reference: "HealthcareService/#{healthcare_service_id}" }],
    network: [{ reference: "Network/#{network_id}" }]
  )

  begin
    # Attempt to create the resource
    created_resource = client.create(org_affiliation)

    # Verify successful creation (HTTP 201 Created)
    assert_equal 201, created_resource.code

    # Verify returned resource data
    assert_equal participating_org_id, created_resource.resource.participatingOrganization.reference.split('/').last
    assert_equal organization_id, created_resource.resource.organization.reference.split('/').last
    assert_equal role_code[:code], created_resource.resource.code[0].code

    # Further assertions for other data elements...

  rescue => e
    puts "Error creating OrganizationAffiliation: #{e.message}"
    raise e
  end
end

# Negative Test Case: Missing Mandatory Field
def test_create_missing_field(client, participating_org_id, organization_id, role_code)
  # Create OrganizationAffiliation resource with missing 'organization' field
  org_affiliation = FHIR::OrganizationAffiliation.new(
    participatingOrganization: { reference: "Organization/#{participating_org_id}" },
    code: [role_code]
  )

  begin
    # Attempt to create the resource
    client.create(org_affiliation)
  rescue FHIR::ClientException => e
    # Verify HTTP 400 Bad Request error
    assert_equal 400, e.response[:code]
  end
end

# Run the tests
test_create_and_verify_organization_affiliation(client, participating_org_id, organization_id, healthcare_service_id, network_id, role_code)
test_create_missing_field(client, participating_org_id, organization_id, role_code)

# Add more test cases for searching, retrieving by ID, and other scenarios...
```

### 4. Potential Issues and Edge Cases

* **Data Consistency:** Ensure consistency of data across referenced resources (Organization, HealthcareService, Network).
* **Code System Validation:** Verify the server correctly validates the code and coding system used for the `code` element.
* **Performance:** Test with a large number of OrganizationAffiliation resources to assess performance impact.
* **Security:** Verify proper authorization and access control mechanisms are in place for creating, reading, and searching OrganizationAffiliation resources.
* **Edge Cases:**
    * Test with various combinations of optional elements present/absent.
    * Test with extremely long text values in string fields to check for truncation issues.
    * Test with different date formats to ensure proper handling. 


---

<a id='req-29'></a>

### REQ-29: Support HealthcareService Association with Networks via OrganizationAffiliation

**Description**: "OrganizationalAffiliation can also be used to associate a HealthcareService provided by an organization with networks."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-29: HealthcareService Association with Networks via OrganizationAffiliation

### 1. Requirement Analysis

* **Testability Assessment**: Automatic
* **Complexity**: Moderate
* **Prerequisites**:
    * A running FHIR server that implements the HealthcareService and OrganizationAffiliation resources.
    * Pre-existing or dynamically created test data:
        * A HealthcareService resource.
        * An Organization resource representing a network.
        * An OrganizationAffiliation resource linking the HealthcareService provider organization to the network organization.

### 2. Test Implementation Strategy

* **Required FHIR Operations**:
    * **Create**: Create the necessary HealthcareService, Organization, and OrganizationAffiliation resources.
    * **Read**: Retrieve the HealthcareService resource.
    * **Search**: Search for HealthcareService resources by the network organization.

* **Test Data Requirements**:
    * **HealthcareService**:
        * `name`: Test Healthcare Service
        * `type`: Relevant healthcare service type code
        * `providedBy`: Reference to the provider organization
    * **Organization (Network)**:
        * `name`: Test Network Organization
        * `type`: Network organization type code
    * **OrganizationAffiliation**:
        * `organization`: Reference to the provider organization
        * `participatingOrganization`: Reference to the network organization
        * `network`: Reference to the network organization

* **Validation Criteria**:
    * **Positive Test Case**:
        * Verify that the created HealthcareService resource can be retrieved successfully.
        * Verify that searching for HealthcareService resources by the network organization returns the created HealthcareService.
    * **Negative Test Case**:
        * Attempt to search for the HealthcareService using an invalid network organization reference. Verify that the search returns no results or an error.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# **Positive Test Case**

# Step 1: Create resources
client = FHIR::Client.new('https://your-fhir-server/fhir')

# Create Network Organization
network_org = FHIR::Organization.new(
  name: 'Test Network Organization',
  type: [
    {
      coding: [
        {
          system: 'http://terminology.hl7.org/CodeSystem/organization-type',
          code: 'prov'
        }
      ]
    }
  ]
)
created_network_org = client.create(network_org)

# Create Provider Organization (Assuming it doesn't already exist)
provider_org = FHIR::Organization.new(
  name: 'Test Provider Organization',
  type: [
    {
      coding: [
        {
          system: 'http://terminology.hl7.org/CodeSystem/organization-type',
          code: 'prov'
        }
      ]
    }
  ]
)
created_provider_org = client.create(provider_org)

# Create OrganizationAffiliation
org_affiliation = FHIR::OrganizationAffiliation.new(
  organization: { reference: "Organization/#{created_provider_org.id}" },
  participatingOrganization: { reference: "Organization/#{created_network_org.id}" },
  network: [
    { reference: "Organization/#{created_network_org.id}" }
  ]
)
created_org_affiliation = client.create(org_affiliation)

# Create HealthcareService
healthcare_service = FHIR::HealthcareService.new(
  name: 'Test Healthcare Service',
  type: [
    {
      coding: [
        {
          system: 'http://snomed.info/sct',
          code: '1234567890' # Replace with actual code
        }
      ]
    }
  ],
  providedBy: { reference: "Organization/#{created_provider_org.id}" }
)
created_healthcare_service = client.create(healthcare_service)

# Step 2 & 3: Read and Validate
retrieved_healthcare_service = client.read(FHIR::HealthcareService, created_healthcare_service.id)
assert retrieved_healthcare_service.id == created_healthcare_service.id, 'Failed to retrieve created HealthcareService'

# Step 4: Search and Validate
search_params = {
  'organization:OrganizationAffiliation.network': "Organization/#{created_network_org.id}"
}
search_result = client.search(FHIR::HealthcareService, search: { parameters: search_params })
assert search_result.resource.entry.first.resource.id == created_healthcare_service.id, 'Failed to find HealthcareService by network'

# **Negative Test Case**
invalid_network_id = 'invalid-id'
search_params = {
  'organization:OrganizationAffiliation.network': "Organization/#{invalid_network_id}"
}
search_result = client.search(FHIR::HealthcareService, search: { parameters: search_params })
assert search_result.resource.entry.nil? || search_result.resource.entry.empty?, 'Found HealthcareService with invalid network ID'

# Clean up resources (Optional)
# client.destroy(FHIR::HealthcareService, created_healthcare_service.id)
# client.destroy(FHIR::OrganizationAffiliation, created_org_affiliation.id)
# client.destroy(FHIR::Organization, created_network_org.id)
# client.destroy(FHIR::Organization, created_provider_org.id)

puts 'Test passed successfully!'
```

### 4. Potential Issues and Edge Cases

* **Multiple Networks**: Test with a HealthcareService associated with multiple networks.
* **Network Hierarchy**: Test with nested network organizations (e.g., regional network under a national network).
* **Inactive Affiliations**: Test with inactive OrganizationAffiliation resources to ensure they are not considered in the search.
* **Performance**: Evaluate the performance of searching for HealthcareServices by network, especially with a large number of resources.
* **Security**: Ensure that only authorized users can access the HealthcareService information based on their relationship with the provider and network organizations. 


---

<a id='req-30'></a>

### REQ-30: Support Endpoint Resource for Technical Details of Electronic Service Endpoints

**Description**: "An Endpoint instance provides  technical details of an endpoint that can be used for electronic services, such as a portal or FHIR REST services, messaging or operations, or DIRECT messaging."

**Actor**: Server

**Conformance**: SHALL

## FHIR Implementation Guide Test Specification: REQ-30

**Requirement:** REQ-30 - Support Endpoint Resource for Technical Details of Electronic Service Endpoints

**1. Requirement Analysis:**

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running FHIR server that implements the target FHIR version.
    * The server should be configured to allow access to the Endpoint resource.

**2. Test Implementation Strategy:**

* **Required FHIR Operations:**
    * `GET [base]/Endpoint` - Search for Endpoint resources
    * `GET [base]/Endpoint/{id}` - Read a specific Endpoint resource

* **Test Data Requirements:**
    * A valid Endpoint resource instance containing relevant technical details (e.g., address, connection type, payload type). This can be a minimal example for basic conformance or a more complex one for specific scenarios.

* **Validation Criteria:**
    * **Positive Test Case:**
        * The server SHALL return a 200 OK response for both search and read operations.
        * The returned Endpoint resource SHALL contain the expected technical details as defined in the test data.
        * The resource SHALL conform to the FHIR Endpoint resource structure and data types.
    * **Negative Test Case:**
        * Attempt to read a non-existent Endpoint resource. The server SHALL return a 404 Not Found response.

**3. Pseudocode Implementation (Ruby):**

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://your-fhir-server/base')

# Positive Test Case
def test_endpoint_resource_support(client)
  # Search for Endpoint resources
  search_response = client.search(FHIR::Endpoint)
  assert_equal 200, search_response.code, "Expected 200 OK, got #{search_response.code}"

  # Read a specific Endpoint resource
  endpoint_id = search_response.resource.entry.first.resource.id
  read_response = client.read(FHIR::Endpoint, endpoint_id)
  assert_equal 200, read_response.code, "Expected 200 OK, got #{read_response.code}"

  # Validate resource content
  endpoint = read_response.resource
  assert_equal 'example.com', endpoint.address, "Incorrect endpoint address"
  # Add more assertions for other required fields based on test data

  puts "Endpoint resource test passed!"
end

# Negative Test Case
def test_nonexistent_endpoint(client)
  response = client.read(FHIR::Endpoint, 'nonexistent-id')
  assert_equal 404, response.code, "Expected 404 Not Found, got #{response.code}"

  puts "Nonexistent Endpoint test passed!"
end

# Run the tests
test_endpoint_resource_support(client)
test_nonexistent_endpoint(client)
```

**4. Potential Issues and Edge Cases:**

* **Corner Cases:**
    * Test with different endpoint connection types (e.g., RESTful, messaging, DICOM).
    * Test with various payload types and security configurations.
    * Test with large datasets to assess performance implications.
* **Performance Considerations:**
    * Monitor response times for both search and read operations, especially with large datasets.
* **Security Considerations:**
    * Ensure that sensitive information within the Endpoint resource is properly secured and only accessible to authorized users.
    * Test for vulnerabilities like unauthorized access and data exposure.

This test specification provides a starting point for verifying REQ-30. It can be further expanded and customized based on specific implementation details and testing requirements. 


---

<a id='req-31'></a>

### REQ-31: Support all defined profiles

**Description**: "The Plan-Net Server **SHALL**:
1. Support all profiles defined in this Implementation Guide."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-31: Support all defined profiles

### 1. Requirement Analysis

* **Testability Assessment:** Hybrid (Automatic discovery, Manual validation)
* **Complexity:** Moderate
* **Prerequisites:**
    * Running instance of the Plan-Net Server
    * Access to the server's CapabilityStatement
    * Access to all profile definitions in the Implementation Guide

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    1. `GET /metadata` - Retrieve the server's CapabilityStatement
    2. `GET /StructureDefinition/<profile_url>` - Retrieve each profile definition

* **Test Data Requirements:**
    * List of all profile URLs defined in the Implementation Guide

* **Validation Criteria:**
    1. The CapabilityStatement **MUST** include all profile URLs from the Implementation Guide in the `rest.resource.profile` element.
    2. The server **MUST** return a successful response (HTTP 2xx) for each profile retrieval request.
    3. The returned profile definition **MUST** match the one defined in the Implementation Guide. (Manual verification)

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configuration
server_base_url = 'https://example.com/fhir'
implementation_guide_profiles = [
  'http://example.org/fhir/StructureDefinition/MyPatientProfile',
  'http://example.org/fhir/StructureDefinition/MyObservationProfile'
  # ... Add all profile URLs from the Implementation Guide
]

# Create a FHIR client
client = FHIR::Client.new(server_base_url)

# Test Case 1: Verify profiles in CapabilityStatement
def test_capability_statement(client, profiles)
  capability_statement = client.capability_statement
  supported_profiles = capability_statement.rest.first.resource.map(&:profile).flatten
  
  missing_profiles = profiles - supported_profiles
  
  if missing_profiles.empty?
    puts "PASS: All profiles found in CapabilityStatement."
  else
    puts "FAIL: Missing profiles in CapabilityStatement: #{missing_profiles}"
  end
end

# Test Case 2: Verify profile retrieval
def test_profile_retrieval(client, profiles)
  profiles.each do |profile_url|
    begin
      profile = client.read(FHIR::StructureDefinition, profile_url).resource
      puts "PASS: Successfully retrieved profile: #{profile_url}"

      # TODO: Add manual verification step to compare retrieved profile with the one defined in the Implementation Guide.

    rescue => e
      puts "FAIL: Error retrieving profile '#{profile_url}': #{e.message}"
    end
  end
end

# Run tests
test_capability_statement(client, implementation_guide_profiles)
test_profile_retrieval(client, implementation_guide_profiles)
```

### 4. Potential Issues and Edge Cases

* **Large number of profiles:**  Retrieving and comparing numerous profiles can impact performance. Consider optimizing the retrieval and comparison process.
* **Profile versioning:** Ensure the test accounts for potential version differences between the Implementation Guide and the server.
* **Manual verification limitations:** Manual comparison of complex profiles can be error-prone. Consider using automated schema validation tools for more robust verification.
* **Security considerations:** Authenticate with the server if necessary and handle sensitive data appropriately during testing. 


---

<a id='req-32'></a>

### REQ-32: Implement RESTful behavior according to FHIR specification

**Description**: "The Plan-Net Server **SHALL**:
2. Implement the RESTful behavior according to the FHIR specification."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-32: Implement RESTful behavior according to FHIR specification

### 1. Requirement Analysis

* **Testability Assessment:**  **Automatic** (can be automated with tools like Jest, Mocha, RSpec)
* **Complexity:** **Moderate** (requires understanding of RESTful principles and FHIR operations)
* **Prerequisites:**
    * A running instance of the Plan-Net Server.
    * Access credentials (if applicable) to interact with the server.
    * A FHIR client library or tool for making API requests (e.g., fhir-client, Postman).

### 2. Test Implementation Strategy

#### 2.1 Required FHIR Operations:

* **Read (GET):** Retrieve a FHIR resource using its logical ID.
* **Search (GET):** Search for FHIR resources using search parameters.
* **Create (POST):** Create a new FHIR resource.
* **Update (PUT):** Update an existing FHIR resource.
* **Delete (DELETE):** Delete a FHIR resource.
* **History (GET):** Retrieve the history of changes for a FHIR resource.
* **VRead (GET):** Retrieve a specific version of a FHIR resource.

#### 2.2 Test Data Requirements:

* **Valid FHIR Resources:**  Examples of valid FHIR resources in JSON format for different resource types (Patient, Observation, etc.).
* **Invalid FHIR Resources:**  Examples of FHIR resources with invalid data types, missing required elements, or other violations of the FHIR specification.
* **Search Parameters:**  A set of valid and invalid search parameters to test the search functionality.

#### 2.3 Validation Criteria:

* **HTTP Status Codes:** Verify that the server returns the correct HTTP status codes for each operation (e.g., 200 OK for successful retrieval, 201 Created for successful creation, 400 Bad Request for invalid input, etc.).
* **Response Headers:** Verify that the server includes appropriate response headers, such as `Content-Type` (application/fhir+json), `Location` (for newly created resources), and `ETag` or `Last-Modified` for caching.
* **Response Body:**
    * **Content:** Verify that the response body contains the expected FHIR resource or bundle in JSON format.
    * **Structure:** Validate the structure and data types of the returned FHIR resources against the FHIR specification.
    * **Errors:** Verify that error responses follow the FHIR OperationOutcome format, providing clear error codes and descriptions.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://plan-net-server.com/fhir') 

# Test Case: Create a new Patient resource
def test_create_patient(client)
  # Define a valid Patient resource
  patient = FHIR::Patient.new(
    name: [FHIR::HumanName.new(family: 'Doe', given: ['John'])]
  )

  # Attempt to create the resource
  response = client.create(patient)

  # Assertions
  assert_equal 201, response.code, "Expected 201 Created, got #{response.code}"
  assert_match /application\/fhir\+json/, response.headers['content-type'], "Incorrect Content-Type header"
  assert response.resource.is_a?(FHIR::Patient), "Response is not a FHIR::Patient"
  assert response.resource.id.present?, "Created resource should have an ID"

  # Return the created resource ID for potential cleanup
  response.resource.id
end

# Test Case: Read a Patient resource
def test_read_patient(client, patient_id)
  response = client.read(FHIR::Patient, patient_id)

  assert_equal 200, response.code, "Expected 200 OK, got #{response.code}"
  assert_match /application\/fhir\+json/, response.headers['content-type'], "Incorrect Content-Type header"
  assert response.resource.is_a?(FHIR::Patient), "Response is not a FHIR::Patient"
end

# Example usage
created_patient_id = test_create_patient(client)
test_read_patient(client, created_patient_id)

# ... Add more test cases for other operations (search, update, delete, etc.)
```

### 4. Potential Issues and Edge Cases

* **Resource Versioning:** Test scenarios involving concurrent updates to the same resource to ensure proper handling of versioning and optimistic locking (using ETags or If-Match headers).
* **Conditional Operations:** Test conditional create, update, and delete operations using the `If-None-Exist`, `If-Match`, and `If-None-Match` headers.
* **Transaction Bundles:** Test the server's ability to process transaction bundles containing multiple operations.
* **Error Handling:** Test various error scenarios, such as invalid resource IDs, unauthorized access attempts, and resource conflicts, to ensure that the server returns meaningful error messages in the OperationOutcome format.
* **Performance:** Consider performance testing for operations like search with large datasets or complex queries.
* **Security:** Verify that the server enforces appropriate authentication and authorization mechanisms to protect patient data.

This test specification provides a starting point for testing the RESTful behavior of the Plan-Net Server. You should expand these tests to cover all relevant FHIR operations, resource types, and edge cases specific to your implementation. Remember to use appropriate testing frameworks and tools to automate these tests and ensure the ongoing compliance of your server with the FHIR specification. 


---

<a id='req-33'></a>

### REQ-33: Return Status 400 for invalid parameter

**Description**: "The Plan-Net Server **SHALL**:
3. Return the following response classes:
* (Status 400): invalid parameter"

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-33: Return Status 400 for Invalid Parameter

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running instance of the Plan-Net Server.
    * A client capable of making FHIR API calls (e.g., REST client).
    * Knowledge of valid and invalid parameters for the specific FHIR resource and operation being tested.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * **HTTP GET** (or relevant operation based on the resource) with an invalid parameter.
* **Test Data Requirements:**
    * **Valid FHIR Resource:**  Choose a resource relevant to the Plan-Net Server implementation (e.g., Patient, Practitioner).
    * **Invalid Parameter:**  Identify a parameter that is not allowed or has an invalid format for the chosen resource and operation. For example:
        * Using an undefined search parameter.
        * Providing a parameter value in an incorrect data type.
* **Validation Criteria:**
    * **HTTP Status Code:** Verify the server returns a **400 Bad Request** status code.
    * **Response Body:** (Optional) The response body *may* contain an OperationOutcome resource with details about the error. This is not mandatory based on the requirement, but it's good practice.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'rest-client'
require 'json'

# **Test Case: Invalid Parameter**

def test_invalid_parameter(base_url, resource_type, invalid_parameter)
  begin
    # Construct the URL with the invalid parameter
    url = "#{base_url}/#{resource_type}?#{invalid_parameter}"

    # Make the GET request
    response = RestClient.get(url)

    # Check for unexpected success
    raise "Expected 400 Bad Request, but received #{response.code}" if response.code == 200

  rescue RestClient::BadRequest => e
    # Verify the error code
    puts "Test Passed (Invalid Parameter): Received expected 400 Bad Request"
    puts "Error Details: #{e.response.body}" # Optional: Log error details

  rescue => e
    puts "Test Failed: #{e.message}"
  end
end

# Example Usage
base_url = 'https://example.com/fhir' 
resource_type = 'Patient'
invalid_parameter = 'invalidparam=test' # Example invalid parameter

test_invalid_parameter(base_url, resource_type, invalid_parameter)
```

### 4. Potential Issues and Edge Cases

* **Specific Invalid Parameters:** The test should be repeated with various invalid parameters (different data types, undefined parameters, etc.) to ensure comprehensive coverage.
* **Error Message Content:** While the requirement doesn't mandate specific content for the error message, the server should ideally return a helpful message indicating the invalid parameter. This can be added as an optional validation.
* **Security Considerations:** Ensure that error messages don't expose sensitive information that could be exploited by attackers.
* **Performance:**  While not a primary concern for this specific test, consider the performance impact of processing invalid requests, especially under high load. The server should handle these gracefully without significant performance degradation. 


---

<a id='req-34'></a>

### REQ-34: Return Status 401/4xx for unauthorized request

**Description**: "The Plan-Net Server **SHALL**:
3. Return the following response classes:
* (Status 401/4xx): unauthorized request"

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-34: Return Status 401/4xx for unauthorized request

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running instance of the Plan-Net Server.
    * A valid FHIR endpoint on the server.
    * A mechanism to send requests with and without proper authorization (e.g., API token, OAuth2).

### 2. Test Implementation Strategy

* **Required FHIR Operations:** Any FHIR operation requiring authorization. For this example, we'll use `GET /Patient`.
* **Test Data Requirements:**
    * **Valid Request:** A valid FHIR GET request to `/Patient` with correct headers but missing or incorrect authorization.
    * **Expected Response (Positive Test):** HTTP Status code 401 (Unauthorized) or any 4xx code.
    * **Expected Response (Negative Test):**  Any HTTP Status code other than 401/4xx.
* **Validation Criteria:**
    * Verify the returned HTTP status code matches the expected response for both positive and negative tests.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'rest-client'
require 'json'

# Test Case: Unauthorized Request
def test_unauthorized_request(base_url)
  begin
    # Positive Test: Send request without authorization
    response = RestClient.get("#{base_url}/Patient")

    # Validation
    if response.code == 401 || (400..499).include?(response.code)
      puts "Positive Test Passed: Received expected status code #{response.code}"
    else
      raise "Positive Test Failed: Expected 401/4xx, got #{response.code}"
    end

    # Negative Test: Send request with valid authorization (implementation specific)
    # Example with Bearer token:
    response = RestClient.get("#{base_url}/Patient", authorization: "Bearer valid_token")

    # Validation
    if (400..499).include?(response.code)
      raise "Negative Test Failed: Received unexpected 4xx status code #{response.code}"
    else
      puts "Negative Test Passed: Did not receive 4xx status code"
    end

  rescue RestClient::ExceptionWithResponse => e
    puts "Request failed: #{e.message}"
    puts "Response Body: #{e.response.body}"
  end
end

# Example usage
base_url = 'https://your-fhir-server/api/v1'
test_unauthorized_request(base_url)
```

### 4. Potential Issues and Edge Cases

* **Specific 4xx codes:** The requirement is open to any 4xx code.  Consider testing with different invalid authorization scenarios (expired token, wrong credentials) and verifying the server returns the most appropriate 4xx code for each.
* **Authorization mechanism:**  The test implementation needs to be adapted to the specific authorization mechanism used by the Plan-Net server (e.g., Basic Auth, OAuth2, API keys).
* **Resource specific authorization:** The server might have different authorization policies for different resources.  Consider testing with various resources beyond just `/Patient`.
* **Performance:** While not the primary focus of this test, consider measuring response times for unauthorized requests to ensure they are within acceptable limits.
* **Security:** Ensure the test environment is secure and test data does not contain sensitive information. Do not commit actual authorization tokens to version control. 


---

<a id='req-35'></a>

### REQ-35: Return Status 403 for insufficient scope

**Description**: "The Plan-Net Server **SHALL**:
3. Return the following response classes:
* (Status 403): insufficient scope"

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-35: Return Status 403 for Insufficient Scope

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running instance of the Plan-Net Server.
    * A valid access token with insufficient scope to access the requested resource.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * Any FHIR operation requiring authorization (e.g., read, search, create, update, delete) on a protected resource.
* **Test Data Requirements:**
    * **Valid Access Token with Insufficient Scope:** An access token that grants access to the system but lacks the necessary scope for the specific resource or operation being tested.
    * **Target Resource:** A FHIR resource that requires the missing scope for access.
* **Validation Criteria:**
    * **HTTP Status Code:** Verify the server returns an HTTP status code of 403 (Forbidden).
    * **Response Body:** Optionally, verify the response body contains a clear and concise error message indicating "insufficient scope".

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'rest-client'
require 'json'

# Test Case: Insufficient Scope
def test_insufficient_scope(base_url, access_token, resource_type, resource_id = nil)
  begin
    headers = {
      'Authorization' => "Bearer #{access_token}",
      'Accept' => 'application/fhir+json'
    }

    # Construct the request URL based on resource type and optional ID
    url = if resource_id
            "#{base_url}/#{resource_type}/#{resource_id}"
          else
            "#{base_url}/#{resource_type}"
          end

    # Make the request (adjust method as needed: GET, POST, PUT, DELETE)
    response = RestClient.get(url, headers: headers)

    # Negative Test Case: Expecting 403 Forbidden
    if response.code == 403
      puts 'Test Passed: Insufficient scope resulted in 403 Forbidden.'
      # Optionally validate error message in response body
      error_message = JSON.parse(response.body)['issue'][0]['diagnostics']
      puts "Error Message: #{error_message}" if error_message == 'insufficient scope'
    else
      raise "Test Failed: Expected 403 Forbidden, got #{response.code}"
    end

  rescue RestClient::ExceptionWithResponse => e
    puts "Test Failed: #{e.message}"
    puts "Response Body: #{e.response.body}"
  end
end

# Example Usage:
base_url = 'https://example.com/fhir'
access_token = 'your_access_token_with_insufficient_scope'
resource_type = 'Patient' # Example resource type
resource_id = '12345' # Optional resource ID for specific resource access

test_insufficient_scope(base_url, access_token, resource_type, resource_id)
```

### 4. Potential Issues and Edge Cases

* **Scope Granularity:**  Ensure testing with different levels of scope granularity (e.g., read-only vs. read-write).
* **Resource Type Variations:** Test with various resource types requiring authorization to confirm consistent behavior.
* **Error Message Clarity:** Verify the error message in the response body is informative and helpful for developers debugging authorization issues.
* **Performance:** Consider the performance impact of authorization checks, especially with large datasets or complex authorization rules.
* **Security:** Avoid logging sensitive information like access tokens or detailed error messages in production environments. 


---

<a id='req-36'></a>

### REQ-36: Return Status 404 for unknown resource

**Description**: "The Plan-Net Server **SHALL**:
3. Return the following response classes:
* (Status 404): unknown resource"

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-36: Return Status 404 for unknown resource

### 1. Requirement Analysis

* **Testability Assessment**: Automatic
* **Complexity**: Simple
* **Prerequisites**: 
    * A running instance of the Plan-Net Server.
    * Knowledge of a resource type that is **not** supported by the server.

### 2. Test Implementation Strategy

* **Required FHIR Operations**: 
    * HTTP GET request to a resource endpoint with an invalid resource type.
* **Test Data Requirements**: 
    * An invalid resource type (e.g., "InvalidResource").
    * A valid base URL for the Plan-Net Server.
* **Validation Criteria**:
    * Verify the HTTP response status code is 404 (Not Found).
    * Optionally, verify the response body contains an appropriate error message indicating an unknown resource.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'rest-client'
require 'json'

# Test Case: REQ-36 - Return Status 404 for unknown resource

base_url = 'https://your-plan-net-server-base-url/fhir' # Replace with actual base URL
invalid_resource_type = 'InvalidResource'

begin
  response = RestClient.get("#{base_url}/#{invalid_resource_type}")

  # Test Failed
  puts "Test Failed: Expected 404 Not Found, received #{response.code}" 

rescue RestClient::NotFound => e
  # Test Passed
  puts "Test Passed: Received 404 Not Found as expected."
  puts "Response Body: #{e.response.body}" # Optional: Print response body for further inspection

rescue => e
  # Test Failed - Unexpected Error
  puts "Test Failed: Unexpected error occurred - #{e.message}"
end
```

### 4. Potential Issues and Edge Cases

* **Case Sensitivity**: Ensure the server consistently returns a 404 error for invalid resource types regardless of case sensitivity (e.g., "InvalidResource" vs. "invalidresource").
* **Trailing Slashes**: Test with and without trailing slashes in the URL to ensure consistent behavior.
* **Error Message Content**: While not explicitly required by the requirement, consider adding assertions to validate the content of the error message in the response body for better error handling and debugging.
* **Rate Limiting**: If the server implements rate limiting, consider incorporating appropriate delays in the test script to avoid triggering rate limits during testing.
* **Security**: Ensure the test script does not expose sensitive information (e.g., authentication credentials) in logs or error messages. 


---

<a id='req-37'></a>

### REQ-37: Return Status 410 for deleted resource

**Description**: "The Plan-Net Server **SHALL**:
3. Return the following response classes:
* (Status 410): deleted resource."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-37: Return Status 410 for Deleted Resource

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running instance of the Plan-Net Server.
    * A pre-existing resource on the server that can be deleted.
    * An API client capable of interacting with the FHIR server.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    1. **READ:** Attempt to retrieve a previously deleted resource using its ID.
* **Test Data Requirements:**
    * **Resource Type:** Any FHIR resource type supported by the server.
    * **Resource ID:** The ID of the deleted resource.
* **Validation Criteria:**
    * **HTTP Status Code:** Verify the server returns an HTTP status code of **410 Gone**.
    * **Response Body:** Optionally, check if the response body contains an OperationOutcome resource with appropriate error details.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure the FHIR client
client = FHIR::Client.new('https://plan-net-server.com/fhir')

# Test Case: Verify 410 Gone for deleted resource

def test_deleted_resource_returns_410(client, resource_type, resource_id)
  begin
    response = client.read(resource_type, resource_id)

    # Test failed, resource should not be accessible
    puts "Test Failed: Expected 410 Gone, received #{response.code}"
    puts "Response body: #{response.body}"
  rescue FHIR::ResourceNotFound => e
    # Verify the correct exception and status code
    if e.response[:code] == 410
      puts "Test Passed: Received 410 Gone for deleted resource."
    else
      puts "Test Failed: Expected 410 Gone, received #{e.response[:code]}"
      puts "Response body: #{e.response[:body]}"
    end
  end
end

# Example usage
resource_type = 'Patient'
resource_id = '12345'

test_deleted_resource_returns_410(client, resource_type, resource_id)
```

### 4. Potential Issues and Edge Cases

* **Resource Deletion Confirmation:** Ensure the test setup reliably deletes the resource before attempting to retrieve it. Consider using a separate test or mechanism to confirm deletion.
* **Caching:** Server-side caching could potentially serve a cached copy of the resource even after deletion. Consider cache invalidation mechanisms or test with a fresh server instance.
* **Resource History:** If the server supports resource history, retrieving a deleted resource might return its history instead of a 410 Gone. Clarify the requirement regarding resource history and adjust the test accordingly.
* **Security and Access Control:** Ensure the test user has appropriate permissions to access and delete the resource. Test with different user roles to verify consistent behavior. 


---

<a id='req-38'></a>

### REQ-38: Support JSON source formats

**Description**: "The Plan-Net Server **SHALL**:
4. Support json source formats for all Plan-Net interactions."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-38: Support JSON source formats

### 1. Requirement Analysis

* **Testability Assessment**: Automatic
* **Complexity**: Moderate
* **Prerequisites**:
    * A running instance of the Plan-Net Server.
    * Test client capable of making FHIR API calls with JSON payloads.
    * A set of valid FHIR resources in JSON format for various Plan-Net interactions.

### 2. Test Implementation Strategy

* **Required FHIR Operations**:
    * This requirement applies to all Plan-Net interactions, so the specific operations will depend on the resources and interactions defined in the Plan-Net implementation guide. For each interaction, the test should cover:
        * **Create**: `POST [base]/[resource]`
        * **Read**: `GET [base]/[resource]/[id]`
        * **Update**: `PUT [base]/[resource]/[id]`
        * **Delete**: `DELETE [base]/[resource]/[id]`
        * **Search**: `GET [base]/[resource]?parameter=value`
* **Test Data Requirements**:
    * Valid FHIR resources in JSON format representing different Plan-Net interactions.
    * Invalid JSON data to test error handling.
* **Validation Criteria**:
    * **Successful Response**: The server should respond with the appropriate HTTP status code (e.g., 200 OK, 201 Created) and a valid FHIR response in JSON format for successful interactions.
    * **Error Handling**: The server should respond with appropriate HTTP status codes (e.g., 400 Bad Request) and error messages in JSON format for invalid requests or data.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Define base URL for the Plan-Net server
base_url = 'https://plan-net-server.com/fhir'

# Create a FHIR client
client = FHIR::Client.new(base_url)

# Define test data for a Plan-Net interaction (e.g., creating a Coverage resource)
coverage_data = {
  "resourceType": "Coverage",
  "status": "active",
  # ... other required Coverage resource attributes
}

# Positive Test Case: Create a Coverage resource with JSON data
begin
  response = client.create(resource: coverage_data, format: :json)

  # Validate response code and format
  assert_equal 201, response.code
  assert_equal 'application/fhir+json', response.headers['content-type']

  # Validate returned resource
  created_coverage = FHIR::Coverage.from_json(response.body)
  # ... perform additional assertions on the created_coverage object

  puts "Positive Test Case: Create Coverage with JSON - PASSED"
rescue => e
  puts "Positive Test Case: Create Coverage with JSON - FAILED"
  puts e.message
end

# Negative Test Case: Create a Coverage resource with invalid JSON data
invalid_coverage_data = "{ 'invalid': 'json' }"

begin
  response = client.create(resource: invalid_coverage_data, format: :json)

  # This line should not be reached if error handling is correct
  puts "Negative Test Case: Create Coverage with invalid JSON - FAILED"
rescue FHIR::ClientException => e
  # Validate error response code and format
  assert_equal 400, e.response.code
  assert_equal 'application/fhir+json', e.response.headers['content-type']

  # Validate error message
  error_json = JSON.parse(e.response.body)
  assert_not_nil error_json['issue']

  puts "Negative Test Case: Create Coverage with invalid JSON - PASSED"
end

# Repeat similar test cases for other Plan-Net interactions (Read, Update, Delete, Search)
# ...
```

### 4. Potential Issues and Edge Cases

* **Large Resources**: Test with large FHIR resources to ensure the server can handle them efficiently.
* **Character Encoding**: Test with different character encodings in JSON data to ensure proper handling.
* **Invalid JSON Structures**: Test various invalid JSON structures to ensure robust error handling.
* **Security Considerations**: Ensure that the server properly validates and sanitizes incoming JSON data to prevent vulnerabilities like JSON injection attacks.
* **Performance Testing**: Conduct performance testing with a high volume of requests to assess the server's ability to handle JSON data efficiently under load. 


---

<a id='req-39'></a>

### REQ-39: Identify supported Plan-Net profiles in meta.profile attribute

**Description**: "The Plan-Net Server **SHALL**:
5. Identify the Plan-Net profiles supported as part of the FHIR `meta.profile` attribute for each instance."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-39: Identify supported Plan-Net profiles in meta.profile attribute

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running FHIR server that implements the Plan-Net profiles.
    * Access credentials for the FHIR server.
    * Knowledge of the specific Plan-Net profiles supported by the server.

### 2. Test Implementation Strategy

* **Required FHIR Operations:** 
    * `GET` request to a resource endpoint that supports Plan-Net profiles. 
    * Example: `/Coverage`
* **Test Data Requirements:**
    * No specific test data is required for this test case. The server should return the supported profiles for any valid resource instance.
* **Validation Criteria:**
    * The response `Content-Type` header MUST be `application/fhir+json`.
    * The response body MUST be a valid FHIR resource.
    * The resource MUST contain a `meta` element.
    * The `meta.profile` element MUST be present and contain a list of URLs.
    * Each URL in the `meta.profile` element MUST represent a supported Plan-Net profile.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://your-fhir-server-url')
client.set_bearer_token('your-bearer-token')

# Resource type to test
resource_type = 'Coverage'

# Expected Plan-Net profile URLs
expected_profiles = [
  'http://hl7.org/fhir/us/plan-net/StructureDefinition/plannet-Coverage-insuranceplan',
  # Add other expected Plan-Net profile URLs
]

begin
  # Make a GET request to the resource endpoint
  response = client.get(resource_type)

  # Check response status code
  if response.code == 200
    # Parse the response body
    resource = FHIR.from_json(response.body)

    # Check if meta.profile exists and is an array
    if resource.meta&.profile&.is_a?(Array)
      # Check if all expected profiles are present
      missing_profiles = expected_profiles - resource.meta.profile
      if missing_profiles.empty?
        puts "Test Passed: All expected Plan-Net profiles found in meta.profile."
      else
        puts "Test Failed: Missing expected Plan-Net profiles: #{missing_profiles}"
      end
    else
      puts "Test Failed: meta.profile is not an array or is missing."
    end
  else
    puts "Test Failed: Request failed with status code #{response.code}"
  end

rescue => e
  puts "Test Failed: An error occurred: #{e.message}"
end
```

### 4. Potential Issues and Edge Cases

* **Multiple profiles:** The server might support multiple Plan-Net profiles for the same resource type. The test should verify that all expected profiles are present in the `meta.profile` element.
* **Profile versions:** Ensure the test verifies the correct version of the Plan-Net profile URLs.
* **Performance:**  Repeatedly retrieving resources to check `meta.profile` can impact performance. Consider caching or other optimizations if this test is part of a larger suite.
* **Security:**  Ensure the test uses appropriate authentication and authorization mechanisms to access the FHIR server. 


---

<a id='req-40'></a>

### REQ-40: Support searchParameters individually and in combination

**Description**: "The Plan-Net Server **SHALL**:
6. Support the searchParameters on each profile individually and in combination."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-40: Support searchParameters individually and in combination

### 1. Requirement Analysis

- **Testability Assessment**: Automatic
- **Complexity**: Moderate
- **Prerequisites**:
    - A running FHIR server that implements the Plan-Net Implementation Guide.
    - At least two resources conforming to a profile defined in the Plan-Net IG, each with data populated for at least two different search parameters. 

### 2. Test Implementation Strategy

**2.1 Required FHIR Operations:**

- **Search Type**: GET /[resourceType]?searchParam1={value1}&searchParam2={value2}

**2.2 Test Data Requirements:**

- **Resource Type**:  The specific resource type from the Plan-Net IG being tested (e.g., `Patient`, `Observation`, etc.).
- **Search Parameter 1**: A valid search parameter defined for the chosen resource type in the Plan-Net IG.
- **Search Value 1**: A valid value for `searchParam1` present in a resource instance on the server.
- **Search Parameter 2**: A different valid search parameter defined for the chosen resource type in the Plan-Net IG.
- **Search Value 2**: A valid value for `searchParam2` present in a resource instance on the server.

**2.3 Validation Criteria:**

- **Individual Search Success**: A search using only `searchParam1` and `searchValue1` should return a `200 OK` response with a bundle containing the relevant resource(s).
- **Individual Search Success**: A search using only `searchParam2` and `searchValue2` should return a `200 OK` response with a bundle containing the relevant resource(s).
- **Combined Search Success**: A search using both `searchParam1=searchValue1` AND `searchParam2=searchValue2` should return a `200 OK` response with a bundle containing only the resource(s) matching both criteria.
- **No Match Handling**: Searches with invalid or non-matching values should return a `200 OK` response with an empty bundle.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# **Configuration**
base_url = 'https://your-fhir-server/fhir' # Replace with your server URL
resource_type = 'Patient' # Replace with the resource type you are testing
search_param1 = 'family' # Replace with the first search parameter
search_value1 = 'Doe' # Replace with a value for the first search parameter
search_param2 = 'given' # Replace with the second search parameter
search_value2 = 'John' # Replace with a value for the second search parameter

# **Create FHIR client**
client = FHIR::Client.new(base_url)

# **Test 1: Individual search with searchParam1**
search_response1 = client.search(resource_type, search: { search_param1 => search_value1 })
if search_response1.code == 200 && !search_response1.resource.entry.nil?
  puts "Test 1: PASS - Individual search with #{search_param1} successful."
else
  puts "Test 1: FAIL - Individual search with #{search_param1} failed."
  puts "Response code: #{search_response1.code}"
  puts "Response body: #{search_response1.body}"
end

# **Test 2: Individual search with searchParam2**
# ... (Similar implementation as Test 1, using search_param2 and search_value2)

# **Test 3: Combined search**
search_response_combined = client.search(resource_type, search: { search_param1 => search_value1, search_param2 => search_value2 })
if search_response_combined.code == 200 
  if !search_response_combined.resource.entry.nil? && search_response_combined.resource.entry.length > 0
    puts "Test 3: PASS - Combined search successful."
  else
    puts "Test 3: FAIL - Combined search returned no matching resources."
  end
else
  puts "Test 3: FAIL - Combined search failed."
  puts "Response code: #{search_response_combined.code}"
  puts "Response body: #{search_response_combined.body}"
end

# **Test 4: No match handling**
# ... (Implement tests with invalid or non-matching values and check for empty bundles)

```

### 4. Potential Issues and Edge Cases

- **Parameter Modifiers**: The test cases should be expanded to include different search parameter modifiers (e.g., `:exact`, `:contains`, etc.) as defined in the Plan-Net IG.
- **Chained Searches**: If the Plan-Net IG defines chained search parameters, specific test cases should be added to cover those scenarios.
- **Performance**: For large datasets, consider adding performance tests to ensure searches with multiple parameters are completed within acceptable timeframes.
- **Security**: Ensure that the test data used does not contain sensitive information and that the test environment is appropriately secured.
- **Resource Quantity**: The test should be run with varying quantities of resources to ensure consistent behavior. 
- **Parameter Combinations**:  Test various combinations of search parameters beyond just two to ensure comprehensive coverage. 


---

<a id='req-41'></a>

### REQ-41: Support forward and reverse chaining for search parameters with 'chain' property

**Description**: "The Plan-Net Server **SHALL**:
1.Support forward and reverse chaining on all search parameters that specify the 'chain' property"

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-41: Support Forward and Reverse Chaining

### 1. Requirement Analysis

**Testability Assessment:** Automatic
**Complexity:** Moderate
**Prerequisites:**
* A running FHIR server that implements the Plan-Net Implementation Guide.
* At least two resources with a search parameter that defines the 'chain' property. For this example, we'll use `Observation` and `Patient` resources, where `Observation.subject` can be chained to `Patient.identifier`.
* Test data loaded into the FHIR server, including Observations linked to Patients.

### 2. Test Implementation Strategy

**Required FHIR Operations:**

* **Forward Chaining:** `GET [base]/Observation?subject:identifier=[patient_identifier]`
* **Reverse Chaining:** `GET [base]/Patient?identifier=[patient_identifier]&link=Observation.subject`

**Test Data Requirements:**

* **Patient:**
    * `id`: patient-1
    * `identifier`: 
        * `system`: http://example.org/patient-identifier
        * `value`: patient-1-identifier
* **Observation:**
    * `id`: observation-1
    * `subject`: `Reference(Patient/patient-1)`

**Validation Criteria:**

* **Forward Chaining:**
    * Response status code should be 200 (OK).
    * The response bundle should contain the Observation with `id` = `observation-1`.
* **Reverse Chaining:**
    * Response status code should be 200 (OK).
    * The response bundle should contain the Patient with `id` = `patient-1`.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('http://[your-fhir-server]/[fhir-base]')

# Test Data
patient_identifier = 'http://example.org/patient-identifier|patient-1-identifier'

# Forward Chaining Test
def test_forward_chaining(client, patient_identifier)
  begin
    search_params = { 'subject:identifier': patient_identifier }
    response = client.search('Observation', search: { parameters: search_params })

    if response.code == 200 && response.resource.entry.first.resource.id == 'observation-1'
      puts "Forward Chaining Test: PASS"
    else
      puts "Forward Chaining Test: FAIL"
      puts "Expected Observation with id 'observation-1', but got #{response.body}"
    end
  rescue => e
    puts "Forward Chaining Test: ERROR - #{e.message}"
  end
end

# Reverse Chaining Test
def test_reverse_chaining(client, patient_identifier)
  begin
    search_params = { 'identifier': patient_identifier, 'link': 'Observation.subject' }
    response = client.search('Patient', search: { parameters: search_params })

    if response.code == 200 && response.resource.entry.first.resource.id == 'patient-1'
      puts "Reverse Chaining Test: PASS"
    else
      puts "Reverse Chaining Test: FAIL"
      puts "Expected Patient with id 'patient-1', but got #{response.body}"
    end
  rescue => e
    puts "Reverse Chaining Test: ERROR - #{e.message}"
  end
end

# Run Tests
test_forward_chaining(client, patient_identifier)
test_reverse_chaining(client, patient_identifier)
```

### 4. Potential Issues and Edge Cases

* **Multiple matches:** The test data assumes a single Observation linked to the Patient.  Tests should be expanded to handle cases with multiple matching resources.
* **Chaining depth:** The requirement doesn't specify a maximum chaining depth.  Tests should explore chaining beyond two levels to identify potential issues.
* **Performance:** Chained searches can be resource-intensive.  Performance testing should be conducted with large datasets and complex chaining scenarios.
* **Security:** Ensure that chained searches respect authorization rules and don't expose sensitive data unintentionally.
* **Circular references:**  The implementation should gracefully handle circular references in chained searches to avoid infinite loops. 


---

<a id='req-42'></a>

### REQ-42: Support XML source formats

**Description**: "The Plan-Net Server **SHOULD**:
1. Support xml source formats for all Plan-Net interactions."

**Actor**: Server

**Conformance**: SHOULD

## Test Specification for REQ-42: Support XML Source Formats

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running instance of the Plan-Net Server.
    * Test client capable of sending FHIR resources in XML format.
    * A set of valid FHIR resources in XML format representing different Plan-Net interactions.

### 2. Test Implementation Strategy

* **Required FHIR Operations:** 
    * This will depend on the specific Plan-Net interactions. For each interaction, the relevant FHIR operation (e.g., `read`, `create`, `update`, `search`) needs to be tested with an XML payload.
* **Test Data Requirements:**
    * **Valid XML FHIR Resources:**  A set of valid FHIR resources representing different Plan-Net interactions, serialized in XML format. These resources should cover various data types and edge cases.
    * **Invalid XML FHIR Resources:**  A set of intentionally malformed XML FHIR resources to test error handling.
* **Validation Criteria:**
    * **HTTP Status Code:** The server should return a `200 OK` status code for valid requests with XML payloads.
    * **Response Format:** The server should return a valid FHIR response in the requested format (XML or JSON if specified in the request headers).
    * **Response Content:** The content of the response should accurately reflect the outcome of the operation performed (e.g., successful resource creation, retrieval, update).
    * **Error Handling:** The server should gracefully handle invalid XML payloads and return appropriate error codes and messages (e.g., `400 Bad Request` with details about the XML parsing error).

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://plan-net-server.com/fhir')
client.use_format = :xml

# Define test data
test_resources = [
  { interaction: 'create', resource_type: 'Patient', path: 'Patient', data: File.read('test_patient.xml') },
  # ... add more test resources for different interactions
]

# Iterate through test resources and perform tests
test_resources.each do |resource|
  begin
    response = case resource[:interaction]
               when 'create'
                 client.create(FHIR.from_xml(resource[:data]))
               when 'read'
                 client.read(resource[:resource_type], resource[:id])
               # ... add other interactions as needed
               end

    # Validate response
    assert_equal 200, response.code, "Expected 200 OK, got #{response.code} for #{resource[:interaction]} #{resource[:resource_type]}"
    assert_equal 'xml', response.format, "Expected XML response format, got #{response.format}"
    # ... add more specific validations based on the interaction and resource type

  rescue => e
    puts "Error during test: #{e.message}"
    # Handle specific error cases, e.g., check for expected error codes and messages
  end
end
```

### 4. Potential Issues and Edge Cases

* **Large XML Payloads:** Test with large XML resources to assess performance impact and potential timeouts.
* **Special Characters:** Include special characters and Unicode characters in the XML data to ensure proper handling and encoding.
* **XML Schema Validation:** Verify that the server performs strict XML schema validation against the FHIR specification to prevent vulnerabilities related to malformed XML.
* **Security Considerations:** Test for XML External Entity (XXE) vulnerabilities by including malicious external entities in the XML payloads. Ensure the server is configured to prevent XXE attacks.
* **Resource Versioning:** If the Plan-Net Server supports different FHIR versions, test compatibility with XML payloads conforming to those versions.


---

<a id='req-43'></a>

### REQ-43: Reject unauthorized requests with HTTP 401

**Description**: "A server **SHALL** reject any unauthorized requests by returning an `HTTP 401` unauthorized response code."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-43: Reject unauthorized requests with HTTP 401

### 1. Requirement Analysis

* **Testability Assessment**: Automatic
* **Complexity**: Simple
* **Prerequisites**:
    * A running FHIR server that implements the specification being tested.
    * A test client capable of making FHIR API requests.
    * A known valid resource endpoint on the FHIR server (e.g., `Patient`).
    * A means to send requests without proper authorization (e.g., missing or invalid authentication token).

### 2. Test Implementation Strategy

* **Required FHIR Operations**: 
    * `READ` (or any other operation requiring authorization) on a protected resource.
* **Test Data Requirements**:
    * No specific test data is required for this test case.
* **Validation Criteria**:
    * **Positive Test Case**: A request without proper authorization **MUST** result in an `HTTP 401 Unauthorized` response code.
    * **Negative Test Case**: A request with proper authorization **MUST NOT** result in an `HTTP 401 Unauthorized` response code.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://your-fhir-server-url')

# Positive Test Case: Unauthorized Request
begin
  response = client.read(FHIR::Patient, '12345')
  # Test fails if this line is reached without exception
  raise "Expected HTTP 401 Unauthorized, but received #{response.code}"
rescue => e
  # Verify HTTP 401 response code
  assert_equal(401, e.response[:code], "Expected HTTP 401 Unauthorized")
end

# Negative Test Case: Authorized Request (Assuming Bearer Token Authorization)
begin
  # Set authorization header with valid token
  client.set_bearer_token('your-valid-auth-token') 
  response = client.read(FHIR::Patient, '12345')
  # Test passes if request is successful (e.g., 200 OK)
  assert_includes([200, 201], response.code, "Expected successful response code")
rescue => e
  # Test fails if an exception occurs with authorized request
  raise "Unexpected error with authorized request: #{e.message}"
end
```

### 4. Potential Issues and Edge Cases

* **Different Authentication Methods**: The test case assumes a specific authorization method (Bearer Token).  The implementation should be adapted for other mechanisms like Basic Authentication or OAuth2.
* **Custom Error Responses**: The server might return a custom error response body with more details even with a 401 status code. The test case could be extended to validate the content of the error response if needed.
* **Rate Limiting**: Continuous unauthorized requests might trigger rate limiting, interfering with the test results. Implement appropriate delays or use test accounts excluded from rate limiting.
* **Security Considerations**: 
    * Never hardcode sensitive information like authentication tokens in test scripts. Use environment variables or secure configuration mechanisms.
    * Ensure the test environment is isolated and does not impact production data or systems. 


---

<a id='req-44'></a>

### REQ-44: Support Plan-Net Endpoint profile

**Description**: "Supported Profiles: [Plan-Net Endpoint](StructureDefinition-plannet-Endpoint.html)"

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-44: Support Plan-Net Endpoint profile

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:** 
    * A running FHIR server under test that implements the Plan-Net Implementation Guide.
    * Access credentials (if applicable) for the FHIR server.

### 2. Test Implementation Strategy

* **Required FHIR Operations:** 
    * `GET [base]/Endpoint` - Retrieve all Endpoints.
    * `GET [base]/Endpoint/$validate` - Validate an Endpoint resource against the Plan-Net profile.

* **Test Data Requirements:**
    * A valid FHIR Endpoint resource conforming to the Plan-Net Endpoint profile ([StructureDefinition-plannet-Endpoint.html](StructureDefinition-plannet-Endpoint.html)). 

* **Validation Criteria:**
    * The server **SHALL** return a 200 OK status code for both `GET` requests.
    * The `GET [base]/Endpoint` response **SHALL** include the Plan-Net Endpoint profile in the `meta.profile` element of returned Endpoint resources.
    * The `GET [base]/Endpoint/$validate` operation **SHALL** return an OperationOutcome resource with a successful outcome (issue.severity != "error") when validating the provided Plan-Net Endpoint resource.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://[FHIR-server-base-url]')
client.use_r4

# Test Case 1: Retrieve Endpoints and check for Plan-Net profile
def test_endpoint_profile(client)
  begin
    response = client.search(FHIR::Endpoint).resource
    # Check if any Endpoint resources were returned
    if response.entry.present?
      response.entry.each do |entry|
        # Check if Plan-Net profile is present in meta.profile
        if entry.resource.meta.profile.include?('http://hl7.org/fhir/StructureDefinition/plannet-Endpoint')
          puts 'Test Passed: Plan-Net Endpoint profile found in returned resources.'
        else
          raise 'Test Failed: Plan-Net Endpoint profile not found in returned resources.'
        end
      end
    else
      puts 'Test Warning: No Endpoint resources found.'
    end
  rescue => e
    puts "Test Failed: Error retrieving or processing Endpoint resources: #{e.message}"
  end
end

# Test Case 2: Validate Endpoint resource against Plan-Net profile
def test_endpoint_validation(client)
  begin
    # Load Plan-Net Endpoint resource from file or create a new instance
    endpoint_resource = FHIR::Endpoint.new(
      # ... your Plan-Net Endpoint resource data ...
    )

    # Validate the resource
    validation_outcome = client.validate(endpoint_resource)

    # Check for any errors in the validation outcome
    if validation_outcome.issue.any? { |issue| issue.severity == 'error' }
      raise "Test Failed: Endpoint validation failed: #{validation_outcome.to_json}"
    else
      puts 'Test Passed: Plan-Net Endpoint resource validated successfully.'
    end
  rescue => e
    puts "Test Failed: Error validating Endpoint resource: #{e.message}"
  end
end

# Run the test cases
test_endpoint_profile(client)
test_endpoint_validation(client)
```

### 4. Potential Issues and Edge Cases

* **Server returns no Endpoint resources:** The test should handle cases where no Endpoint resources are found and provide a warning instead of failing.
* **Invalid Plan-Net Endpoint resource:** The test data should be thoroughly validated to ensure it conforms to the Plan-Net Endpoint profile. 
* **Performance:** Consider testing with a large number of Endpoint resources to assess performance impact.
* **Security:** Ensure the test client authenticates appropriately with the FHIR server if required. 

This test specification provides a starting point for testing the Plan-Net Endpoint profile requirement. You may need to adapt it based on the specific implementation and testing environment. 


---

<a id='req-45'></a>

### REQ-45: Support search-type and read interactions for Endpoint

**Description**: "**SHALL** support `search-type`, `read`."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-45: Endpoint Search and Read Support

### 1. Requirement Analysis

**Testability Assessment:** Automatic
**Complexity:** Simple
**Prerequisites:** 
* A running FHIR server that implements the Endpoint resource.
* At least one Endpoint resource instance loaded on the server.

### 2. Test Implementation Strategy

**Required FHIR Operations:**
* **Search-type:** `GET [base]/Endpoint`
* **Read:** `GET [base]/Endpoint/[id]`

**Test Data Requirements:**
* **Valid Endpoint ID:**  A known, existing Endpoint ID on the server.

**Validation Criteria:**
* **HTTP Status Code:** 
    * **Search-type:** 200 (OK)
    * **Read:** 200 (OK) if the resource exists, 404 (Not Found) if it doesn't.
* **Response Content-Type:** `application/fhir+json`
* **Response Body:**
    * **Search-type:** A valid Bundle resource containing matching Endpoint resources.
    * **Read:** A valid Endpoint resource with the requested ID.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://your-fhir-server/base')

# Test Case 1: Search-type interaction
def test_endpoint_search(client)
  begin
    response = client.search('Endpoint')
    
    # Assertions
    assert_equal 200, response.code, "Expected 200 OK, got #{response.code}"
    assert_equal 'application/fhir+json', response.headers['content-type']
    assert_not_nil response.resource, "Response body should not be empty"
    assert_equal 'Bundle', response.resource.resourceType, "Expected Bundle resource type"

    puts "Test Case 1: Endpoint search PASSED"
  rescue => e
    puts "Test Case 1: Endpoint search FAILED - #{e.message}"
  end
end

# Test Case 2: Read interaction (successful)
def test_endpoint_read_success(client, endpoint_id)
  begin
    response = client.read('Endpoint', endpoint_id)

    # Assertions
    assert_equal 200, response.code, "Expected 200 OK, got #{response.code}"
    assert_equal 'application/fhir+json', response.headers['content-type']
    assert_not_nil response.resource, "Response body should not be empty"
    assert_equal 'Endpoint', response.resource.resourceType, "Expected Endpoint resource type"
    assert_equal endpoint_id, response.resource.id, "Resource ID mismatch"

    puts "Test Case 2: Endpoint read (success) PASSED"
  rescue => e
    puts "Test Case 2: Endpoint read (success) FAILED - #{e.message}"
  end
end

# Test Case 3: Read interaction (not found)
def test_endpoint_read_not_found(client, invalid_endpoint_id)
  begin
    response = client.read('Endpoint', invalid_endpoint_id)

    # Assertions
    assert_equal 404, response.code, "Expected 404 Not Found, got #{response.code}"

    puts "Test Case 3: Endpoint read (not found) PASSED"
  rescue => e
    puts "Test Case 3: Endpoint read (not found) FAILED - #{e.message}"
  end
end

# Execute test cases
test_endpoint_search(client)
test_endpoint_read_success(client, 'valid_endpoint_id')
test_endpoint_read_not_found(client, 'invalid_endpoint_id')
```

### 4. Potential Issues and Edge Cases

* **Large Result Sets:** Test how the server handles searches that return a large number of Endpoint resources. Consider pagination and performance implications.
* **Filtering and Sorting:** Test various search parameters to ensure accurate filtering and sorting of results.
* **Invalid Search Parameters:** Test the server's behavior when provided with invalid or unsupported search parameters.
* **Security:** Ensure appropriate authorization is required for both search and read operations, especially if dealing with sensitive endpoint data.
* **Data Types and Constraints:** Test with Endpoint resources containing various data types and edge-case values to ensure compliance with FHIR data types and constraints. 


---

<a id='req-46'></a>

### REQ-46: Support vread interaction for Endpoint

**Description**: "**SHOULD** support `vread`."

**Actor**: Server

**Conformance**: SHOULD

## Test Specification for REQ-46: Support vread interaction for Endpoint

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running FHIR server under test.
    * At least one `Endpoint` resource instance available on the server.
    * The `Endpoint` resource instance should have a version history (i.e., it has been updated at least once).

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * `GET [base]/Endpoint/[id]/_history/[versionId]`
* **Test Data Requirements:**
    * `[base]`: The base URL of the FHIR server.
    * `[id]`: The logical ID of the `Endpoint` resource.
    * `[versionId]`: The version ID of the `Endpoint` resource to retrieve.
* **Validation Criteria:**
    * **Positive Test Case:**
        * **HTTP Status Code:** 200 OK
        * **Response Body:** A valid FHIR `Endpoint` resource representing the requested version.
    * **Negative Test Case:**
        * **HTTP Status Code:** 404 Not Found (if the specified version does not exist).

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# **Test Case: Successful vread operation**

def test_vread_success(client, endpoint_id, version_id)
  begin
    response = client.read(FHIR::Endpoint, endpoint_id, version_id)

    assert_response_ok(response)
    assert_resource_type(response, FHIR::Endpoint)

    puts "Test Passed: Successfully retrieved Endpoint version #{version_id}"
  rescue => e
    handle_error("Error during vread operation: #{e.message}")
  end
end

# **Test Case: vread operation for non-existent version**

def test_vread_not_found(client, endpoint_id, invalid_version_id)
  begin
    response = client.read(FHIR::Endpoint, endpoint_id, invalid_version_id)

    assert_response_status_code(response, 404)

    puts "Test Passed: Correctly received 404 for non-existent Endpoint version"
  rescue => e
    handle_error("Error during vread operation: #{e.message}")
  end
end

# **Helper Functions**

def assert_response_ok(response)
  raise "Unexpected HTTP Status Code: #{response.code}" unless response.code == 200
end

def assert_response_status_code(response, expected_code)
  raise "Unexpected HTTP Status Code: #{response.code}, Expected: #{expected_code}" unless response.code == expected_code
end

def assert_resource_type(response, resource_type)
  raise "Unexpected Resource Type: #{response.resource.resourceType}" unless response.resource.instance_of?(resource_type)
end

def handle_error(message)
  puts "Test Failed: #{message}"
end

# **Example Usage**

client = FHIR::Client.new('[base]')
client.use_r4
endpoint_id = '[endpoint_id]'
version_id = '[version_id]'
invalid_version_id = '[invalid_version_id]'

test_vread_success(client, endpoint_id, version_id)
test_vread_not_found(client, endpoint_id, invalid_version_id)
```

### 4. Potential Issues and Edge Cases

* **Large Resource Versions:**  Test with `Endpoint` resources that have a significant number of versions to ensure performance is not negatively impacted.
* **Concurrent Updates:**  Consider testing scenarios where the `Endpoint` resource is updated concurrently by another process to ensure versioning consistency.
* **Security Considerations:**  Verify that appropriate authorization mechanisms are in place to restrict access to specific versions of the `Endpoint` resource based on user roles and permissions. 


---

<a id='req-47'></a>

### REQ-47: Return Endpoint resource using ID

**Description**: "A Server **SHALL** be capable of returning a Endpoint resource using: `GET [base]/Endpoint/[id]`"

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-47: Return Endpoint resource using ID

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running FHIR server that implements the Endpoint resource.
    * At least one Endpoint resource must exist on the server.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * `GET [base]/Endpoint/[id]`
* **Test Data Requirements:**
    * `[base]` - The base URL of the FHIR server.
    * `[id]` - The logical ID of an existing Endpoint resource.
* **Validation Criteria:**
    * **HTTP Status Code:** 200 OK
    * **Response Content-Type:** application/fhir+json
    * **Response Body:** A valid FHIR Endpoint resource with the requested ID.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Test Case 1: Successful retrieval of Endpoint resource

def test_get_endpoint_success(base_url, endpoint_id)
  client = FHIR::Client.new(base_url)
  response = client.read(FHIR::Endpoint, endpoint_id)

  assert_equal 200, response.code, "Expected HTTP 200 OK, but got #{response.code}"
  assert_equal 'application/fhir+json', response.headers['content-type'], "Expected Content-Type 'application/fhir+json', but got #{response.headers['content-type']}"

  endpoint = FHIR::Endpoint.from_json(response.body)
  assert_equal endpoint_id, endpoint.id, "Returned Endpoint ID does not match requested ID"

  puts "Test Case 1: Successful retrieval of Endpoint resource - PASSED"
end

# Test Case 2: Endpoint resource not found

def test_get_endpoint_not_found(base_url, invalid_endpoint_id)
  client = FHIR::Client.new(base_url)
  begin
    client.read(FHIR::Endpoint, invalid_endpoint_id)
  rescue FHIR::ResourceNotFound => e
    assert_equal 404, e.response.code, "Expected HTTP 404 Not Found, but got #{e.response.code}"
    puts "Test Case 2: Endpoint resource not found - PASSED"
    return
  end
  assert_fail "Expected FHIR::ResourceNotFound exception, but no exception was raised"
end

# Example usage
base_url = 'https://example.com/fhir'
endpoint_id = '12345'
invalid_endpoint_id = 'invalid_id'

test_get_endpoint_success(base_url, endpoint_id)
test_get_endpoint_not_found(base_url, invalid_endpoint_id)
```

### 4. Potential Issues and Edge Cases

* **Invalid Endpoint ID:** The server should return a 404 Not Found error if the provided ID does not exist.
* **Unauthorized Access:** The test should consider scenarios where access to the Endpoint resource is restricted and verify appropriate authorization mechanisms are in place.
* **Data Conformance:** The returned Endpoint resource should be validated against the FHIR specification to ensure data integrity.
* **Performance:** Consider testing with a large number of Endpoint resources to assess performance impact.
* **Character Encoding:** Ensure the server correctly handles different character encodings in the request and response.
* **Trailing Slashes:** Test with and without trailing slashes in the URL to ensure consistent behavior.


---

<a id='req-48'></a>

### REQ-48: Return Endpoint resource using ID and version ID

**Description**: "A Server **SHOULD** be capable of returning a Endpoint resource using: `GET [base]/Endpoint/[id]/_history/vid`"

**Actor**: Server

**Conformance**: SHOULD

## Test Specification for REQ-48: Return Endpoint resource using ID and version ID

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running FHIR server that implements the Endpoint resource.
    * At least one Endpoint resource loaded into the server with at least one previous version.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * `GET [base]/Endpoint/[id]/_history/[vid]`

* **Test Data Requirements:**
    * `[base]`: The base URL of the FHIR server.
    * `[id]`: The ID of an existing Endpoint resource.
    * `[vid]`: The version ID of a previous version of the Endpoint resource.

* **Validation Criteria:**
    * **Positive Test Case:**
        * **HTTP Status Code:** 200 OK
        * **Response Body:** The response body should contain the Endpoint resource representation corresponding to the specified `[id]` and `[vid]`.
        * **Response Headers:**
            * `Content-Type`: `application/fhir+json` or `application/fhir+xml` (depending on the request headers).
    * **Negative Test Cases:**
        * **Invalid Endpoint ID:**
            * **HTTP Status Code:** 404 Not Found
        * **Invalid Version ID:**
            * **HTTP Status Code:** 404 Not Found
        * **Unauthorized Request:**
            * **HTTP Status Code:** 401 Unauthorized (or other relevant authentication/authorization error code)

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Test Setup
base_url = 'https://your-fhir-server/fhir'
endpoint_id = 'example-endpoint-id'
endpoint_vid = '1'

# Create FHIR client
client = FHIR::Client.new(base_url)

# Positive Test Case
begin
  response = client.read(FHIR::Endpoint, endpoint_id, vid: endpoint_vid)

  if response.code == 200
    puts "Positive Test Case Passed: Successfully retrieved Endpoint with ID '#{endpoint_id}' and version ID '#{endpoint_vid}'."
    puts "Response Body:\n#{response.body}"
  else
    raise "Unexpected HTTP status code: #{response.code}"
  end

rescue => e
  puts "Positive Test Case Failed: #{e.message}"
end

# Negative Test Case - Invalid Endpoint ID
begin
  invalid_endpoint_id = 'invalid-id'
  response = client.read(FHIR::Endpoint, invalid_endpoint_id, vid: endpoint_vid)

  raise "Expected 404 Not Found, but received #{response.code}"

rescue RestClient::ResourceNotFound
  puts "Negative Test Case (Invalid Endpoint ID) Passed: Received expected 404 Not Found."
rescue => e
  puts "Negative Test Case (Invalid Endpoint ID) Failed: #{e.message}"
end

# Negative Test Case - Invalid Version ID
begin
  invalid_endpoint_vid = '999'
  response = client.read(FHIR::Endpoint, endpoint_id, vid: invalid_endpoint_vid)

  raise "Expected 404 Not Found, but received #{response.code}"

rescue RestClient::ResourceNotFound
  puts "Negative Test Case (Invalid Version ID) Passed: Received expected 404 Not Found."
rescue => e
  puts "Negative Test Case (Invalid Version ID) Failed: #{e.message}"
end
```

### 4. Potential Issues and Edge Cases

* **Deleted Resources:** The server might handle requests for deleted resources differently. Test cases should cover scenarios where the requested version belongs to a deleted resource.
* **Resource Access Control:** The test cases should consider different authorization levels and ensure appropriate error codes are returned for unauthorized requests.
* **Performance:** For systems with a large number of resource versions, retrieving specific versions might impact performance. Consider adding performance tests to measure the response time for this operation.
* **Data Format:** The test cases should verify the server correctly returns the requested data format (JSON or XML) based on the request headers. 


---

<a id='req-49'></a>

### REQ-49: Support _include for Endpoint:organization

**Description**: "A Server **SHALL** be capable of supporting the following _includes: Endpoint:organization - `GET [base]/Endpoint?[parameter=value]&_include=Endpoint:organization`"

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-49: Support _include for Endpoint:organization

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running FHIR server that implements the Endpoint resource.
    * At least one Endpoint resource with a reference to an Organization resource.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * `GET [base]/Endpoint?_include=Endpoint:organization`
* **Test Data Requirements:**
    * An Endpoint resource with a valid `organization` reference.
* **Validation Criteria:**
    * **HTTP Status Code:** 200 OK
    * **Content-Type:** application/fhir+json
    * **Response Body:**
        * The response bundle should contain the requested Endpoint resource.
        * The response bundle should contain the Organization resource referenced by the Endpoint's `organization` element.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# Configure FHIR client
client = FHIR::Client.new('https://your-fhir-server/fhir')

# Test Case 1: Successful _include

def test_endpoint_include_success(client)
  begin
    response = client.search(FHIR::Endpoint, search: { parameters: { _include: 'Endpoint:organization' } })

    # Assertions
    assert_equal 200, response.code, "Expected HTTP 200 OK, but got #{response.code}"
    assert_equal 'application/fhir+json', response.response[:headers]['content-type'], "Unexpected Content-Type: #{response.response[:headers]['content-type']}"

    bundle = FHIR::Bundle.from_contents(response.body)
    assert bundle.present?, "Response body is empty"

    endpoint_entry = bundle.entry.find { |e| e.resource.resourceType == 'Endpoint' }
    assert endpoint_entry.present?, "No Endpoint resource found in the response bundle"

    organization_entry = bundle.entry.find { |e| e.resource.resourceType == 'Organization' }
    assert organization_entry.present?, "No Organization resource found in the response bundle"

    puts "Test Case 1: Successful _include - PASSED"
  rescue => e
    puts "Test Case 1: Successful _include - FAILED: #{e.message}"
  end
end

# Test Case 2: Invalid _include parameter (negative test)

def test_endpoint_include_invalid_parameter(client)
  begin
    response = client.search(FHIR::Endpoint, search: { parameters: { _include: 'Endpoint:invalid' } })

    # Assertions
    assert_equal 400, response.code, "Expected HTTP 400 Bad Request, but got #{response.code}"

    puts "Test Case 2: Invalid _include parameter - PASSED"
  rescue => e
    puts "Test Case 2: Invalid _include parameter - FAILED: #{e.message}"
  end
end

# Run the test cases
test_endpoint_include_success(client)
test_endpoint_include_invalid_parameter(client)
```

### 4. Potential Issues and Edge Cases

* **Circular References:** Ensure the server handles circular references gracefully (e.g., Endpoint references Organization, which references back to Endpoint).
* **Performance:** Test with a large number of Endpoint resources to assess performance impact of the _include parameter.
* **Security:** Verify that the _include parameter doesn't expose sensitive information from the referenced Organization resource if access control is implemented.
* **Missing Organization:** Test with an Endpoint resource that has a missing or invalid `organization` reference. The server should still return the Endpoint resource but might return an OperationOutcome with an error about the missing reference. 


---

<a id='req-50'></a>

### REQ-50: Support organization search parameter for Endpoint

**Description**: "**SHALL**   [organization](SearchParameter-endpoint-organization.html)   reference   `GET [base]/Endpoint?organization=[organization]`"

**Actor**: Server

**Conformance**: SHALL

## Test Specification for FHIR Implementation Guide Requirement REQ-50

### 1. Requirement Analysis

* **Testability Assessment:** Automatic
* **Complexity:** Simple
* **Prerequisites:**
    * A running FHIR server that implements the Endpoint resource.
    * At least one Endpoint resource loaded with an 'organization' reference.

### 2. Test Implementation Strategy

* **Required FHIR Operations:**
    * `GET [base]/Endpoint?organization=[organization]`
* **Test Data Requirements:**
    * **Organization Resource:** A pre-existing Organization resource with a known ID.
    * **Endpoint Resource:** An Endpoint resource that references the above Organization resource in its `organization` field.
* **Validation Criteria:**
    * **HTTP Status Code:** 200 OK
    * **Content-Type:** application/fhir+json
    * **Response Body:**
        * The response bundle should contain at least one Endpoint resource.
        * The returned Endpoint resource(s) should have the `organization` field matching the provided `[organization]` search parameter value.

### 3. Pseudocode Implementation (Ruby)

```ruby
require 'fhir_client'

# **Test Case 1: Successful Search**

def test_endpoint_search_by_organization_success(fhir_client, organization_id)
  response = fhir_client.search(FHIR::Endpoint, search: { parameters: { 'organization': organization_id } })

  assert_equal 200, response.code, "Expected HTTP 200 OK, got #{response.code}"
  assert_equal 'application/fhir+json', response.headers['content-type'], "Expected 'application/fhir+json', got #{response.headers['content-type']}"

  bundle = FHIR::Bundle.from_json(response.body)
  assert bundle.entry.length > 0, "Expected at least one Endpoint resource in the response bundle"

  bundle.entry.each do |entry|
    assert_equal organization_id, entry.resource.organization.reference, "Expected Endpoint resource to have organization reference matching '#{organization_id}'"
  end
end

# **Test Case 2: No Match**

def test_endpoint_search_by_organization_no_match(fhir_client, non_existent_organization_id)
  response = fhir_client.search(FHIR::Endpoint, search: { parameters: { 'organization': non_existent_organization_id } })

  assert_equal 200, response.code, "Expected HTTP 200 OK, got #{response.code}"
  assert_equal 'application/fhir+json', response.headers['content-type'], "Expected 'application/fhir+json', got #{response.headers['content-type']}"

  bundle = FHIR::Bundle.from_json(response.body)
  assert_equal 0, bundle.entry.length, "Expected no Endpoint resources in the response bundle"
end

# **Example Usage**

fhir_client = FHIR::Client.new('https://your-fhir-server-url')
organization_id = 'Organization/12345'
non_existent_organization_id = 'Organization/99999'

test_endpoint_search_by_organization_success(fhir_client, organization_id)
test_endpoint_search_by_organization_no_match(fhir_client, non_existent_organization_id)
```

### 4. Potential Issues and Edge Cases

* **Multiple Organizations:** Test with an Endpoint referencing multiple organizations.
* **Invalid Organization ID:** Test with an invalid or malformed organization ID.
* **Large Datasets:** Evaluate performance with a large number of Endpoint and Organization resources.
* **Security:** Ensure proper authorization is required to access Endpoint resources based on the associated organization.
* **Pagination:** Test scenarios with large result sets requiring pagination.
* **Search Parameter Modifiers:** Test the use of supported search parameter modifiers like `:missing`, `:above`, `:below`, etc. (if applicable). 


---



