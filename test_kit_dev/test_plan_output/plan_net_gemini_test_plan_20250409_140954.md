# Consolidated Test Plan for Plan Net

## Generated on: 2025-04-09 14:10:14

## Capability Statement

This test plan incorporates constraints and requirements from the Plan Net Capability Statement.

## Table of Contents

- [Client](#client)
  - [REQ-02: No PII sending by clients](#req-02)
  - [REQ-06: Client handling of Must Support data elements](#req-06)
  - [REQ-07: Client display of data elements](#req-07)
  - [REQ-08: Client interpretation of missing Must Support data](#req-08)
  - [REQ-09: Client processing of missing information indicators](#req-09)
  - [REQ-31: Client tracking of directory content updates](#req-31)
- [Server](#server)
  - [REQ-01: No PII requirement for directory queries](#req-01)
  - [REQ-03: Population of Must Support data elements](#req-03)
  - [REQ-04: Not including absent data elements](#req-04)
  - [REQ-05: Using dataAbsentReason for missing required information](#req-05)
  - [REQ-10: JSON format support](#req-10)
  - [REQ-11: RESTful behavior implementation](#req-11)
  - [REQ-12: Support for all Implementation Guide profiles](#req-12)
  - [REQ-13: Unauthorized request response](#req-13)
  - [REQ-14: Insufficient scope response](#req-14)
  - [REQ-15: Invalid parameter response](#req-15)
  - [REQ-16: Unknown resource response](#req-16)
  - [REQ-17: Deleted resource response](#req-17)
  - [REQ-18: Profile identification in meta attribute](#req-18)
  - [REQ-19: Individual search parameter support](#req-19)
  - [REQ-20: Combination search parameter support](#req-20)
  - [REQ-21: Forward chaining support](#req-21)
  - [REQ-22: Reverse chaining support](#req-22)
  - [REQ-23: XML format support](#req-23)
  - [REQ-24: Rejection of unauthorized requests](#req-24)
  - [REQ-25: Support for read interaction](#req-25)
  - [REQ-26: Support for vread interaction](#req-26)
  - [REQ-27: Support for _includes](#req-27)
  - [REQ-28: Support for _revincludes](#req-28)
  - [REQ-29: Network profile NPI handling](#req-29)
  - [REQ-30: lastUpdate timestamp requirement](#req-30)
  - [REQ-32: General Search for Pharmacy](#req-32)
  - [REQ-33: Provider search by name](#req-33)
  - [REQ-34: Organization search by name](#req-34)
  - [REQ-35: Provider search by specialty](#req-35)
  - [REQ-36: Organization search by specialty](#req-36)
  - [REQ-37: Search for active practitioners and organizations](#req-37)
  - [REQ-38: Network contact handling for departments](#req-38)
  - [REQ-39: Organization contact handling for departments](#req-39)
  - [REQ-40: Practitioner qualification coding](#req-40)

## Test Specifications

<a id='client'></a>

## Client

<a id='req-02'></a>

### REQ-02: No PII sending by clients

**Description**: "A directory mobile application SHALL NOT send consumer identifiable information when querying a Plan-Net service."

**Actor**: Client

**Conformance**: SHALL NOT

## Test Specification for REQ-02: No PII Sending by Clients

**1. Requirement ID:** REQ-02

**2. Requirement Analysis:**

   - **Testability Assessment:**  **Not Testable (Too Vague)** 
     - The requirement lacks specific definitions of "consumer identifiable information" and "Plan-Net service." Without clear definitions, it's impossible to create an objective test.
   - **Complexity:** N/A (due to not being testable)
   - **Prerequisites:** N/A (due to not being testable)

**3. Test Implementation Strategy:**

   - **Not Applicable** -  This requirement needs further refinement before a test can be designed. 

**Explanation and Recommendations:**

This requirement, as written, is not directly testable. Here's why and how to improve it:

* **Lack of Concrete Definitions:**
    * **"Consumer identifiable information"** is too broad.  A testable requirement would explicitly list the FHIR elements considered PII (e.g., `Patient.name`, `Patient.birthDate`, `Address.line`, etc.).
    * **"Plan-Net service"** is unclear.  What specific FHIR endpoint or operation does this refer to?  The Capability Statement should identify the relevant interaction.

* **Reliance on Inspection:**  "Inspection" as a verification method is subjective. Automated tests are preferable for consistency and repeatability.

**To make this requirement testable:**

1. **Define PII:** Create a clear, unambiguous list of FHIR resource elements that constitute PII within the scope of this implementation guide.
2. **Specify the Target:** Precisely identify the FHIR endpoint(s) or operation(s) that the client application is prohibited from sending PII to.
3. **Consider Data Profiles:**  Develop FHIR profiles that specifically exclude or mask PII fields for use in this context.
4. **Automated Testing:** Once the above are defined, design tests that send requests to the specified endpoint(s) with and without the defined PII elements. The test should verify:
    * **Requests with PII:** The server should reject these requests (e.g., with an HTTP 400 Bad Request or similar error).
    * **Requests without PII:** The server should process these requests successfully.

By addressing these points, you can transform REQ-02 into a testable requirement that ensures the privacy and security of consumer data. 


---

<a id='req-06'></a>

### REQ-06: Client handling of Must Support data elements

**Description**: "Application actors SHALL be capable of processing resource instances containing the Must Support data elements without generating an error or causing the application to fail."

**Actor**: Client

**Conformance**: SHALL

## Test Specification for REQ-06: Client Handling of Must Support Data Elements

**1. Requirement ID:** REQ-06

**2. Requirement Analysis:**

   - **Testability Assessment:** Automatically Testable
   - **Complexity:** Moderate 
   - **Prerequisites:** 
      - Identify a list of resources and "Must Support" data elements within those resources relevant to the tested client's interactions (e.g., if the client only reads `Patient` resources, focus on those).
      - Access to a FHIR server capable of serving resources with the identified "Must Support" elements.

**3. Test Implementation Strategy:**

   **3.1 Required Inputs:**

   * **FHIR Resources:** Create a set of FHIR resources containing the identified "Must Support" data elements. These resources should be valid according to the base FHIR specification and any applicable profiles. 
     * Example: A `Patient` resource with the `birthDate` element populated (assuming `birthDate` is a "Must Support" element for this client).
   * **Expected Outputs:** Define the expected successful responses from the client for each test case. This could include:
     * HTTP Status Code: `200 OK` (for read operations), `201 Created` (for create operations), etc.
     * Absence of error messages in the response body related to the "Must Support" elements.

   **3.2 Required FHIR Operations:**

   * **Read (GET):** Retrieve a resource containing "Must Support" elements.
   * **Create (POST):** Send a new resource containing "Must Support" elements to the server.
   * **Update (PUT):** Update an existing resource, ensuring the "Must Support" elements are handled correctly.
   * **Search (GET with parameters):** Search for resources using parameters that might involve "Must Support" elements.

   **Note:** The specific operations to test will depend on the client's capabilities as declared in the Capability Statement.

   **3.3 Validation Criteria:**

   * **Successful Response:** Verify that the client returns the expected HTTP status code (e.g., 200, 201) for each operation without generating errors related to the "Must Support" elements.
   * **Data Integrity:** For operations involving data retrieval (Read, Search), ensure the client correctly processes and returns the values of the "Must Support" elements.
   * **Error Handling:** If the client receives a resource with invalid data types or values within the "Must Support" elements, it should handle the error gracefully according to the FHIR specification (e.g., return a `400 Bad Request` with an OperationOutcome resource explaining the issue).

**Example Test Case:**

**Test Case ID:** TC-REQ-06-001

**Test Case Description:** Verify the client can successfully read a `Patient` resource containing the "Must Support" element `birthDate`.

**Test Steps:**

1. Prepare a `Patient` resource with a valid `birthDate` element.
2. Send a GET request to the appropriate endpoint to retrieve the `Patient` resource.

**Expected Results:**

1. The client returns an HTTP status code of `200 OK`.
2. The response body contains the `Patient` resource with the `birthDate` element and its value correctly populated.
3. No errors related to the `birthDate` element are present in the response. 


---

<a id='req-07'></a>

### REQ-07: Client display of data elements

**Description**: "Application actors SHOULD be capable of displaying the data elements for human use or storing the information for other purposes."

**Actor**: Client

**Conformance**: SHOULD

## Test Specification for REQ-07: Client Display of Data Elements

**1. Requirement ID:** REQ-07

**2. Requirement Analysis:**

   - **Testability Assessment:** Not Testable (Too Vague)
   - **Complexity:** N/A
   - **Prerequisites:** N/A

**Rationale for Testability Assessment:**

This requirement is too vague for automated testing or objective verification through inspection.  The requirement states applications "SHOULD be capable of displaying the data elements for human use or storing the information for other purposes." This lacks specific criteria for:

* **"Data elements":**  Which specific data elements from which resources are in scope?
* **"Displaying for human use":** What constitutes acceptable display?  Are there formatting, accessibility, or usability requirements?
* **"Storing for other purposes":**  What are the acceptable storage mechanisms and data retention policies?

**3. Test Implementation Strategy:**

Due to the vagueness of the requirement, a formal test implementation strategy is not feasible. 

**Recommendations:**

* **Requirement Refinement:**  Revise REQ-07 to include concrete, testable criteria. For example:
    * Specify the exact FHIR resources and data elements in scope.
    * Define acceptable display formats or provide examples (e.g., tabular view, human-readable text).
    * If storage is relevant, outline minimum requirements for data security and retention.
* **Alternative Verification:** Consider these options if automated testing isn't possible:
    * **User Acceptance Testing (UAT):**  Involve end-users in testing the display and usability of data elements within the application's intended workflow.
    * **Documentation Review:** Require vendors to provide documentation (e.g., user manuals, implementation guides) that clearly demonstrate how their application meets the requirement. This documentation should include screenshots or examples of data element display and explanations of storage mechanisms if applicable. 
* **Capability Statement Alignment:** While this requirement is not directly testable via the Capability Statement, ensure the Capability Statement accurately reflects the system's ability to READ the relevant resources containing the data elements. 

By refining the requirement and considering alternative verification methods, you can gain more confidence in the client application's ability to handle data elements appropriately. 


---

<a id='req-08'></a>

### REQ-08: Client interpretation of missing Must Support data

**Description**: "When querying Health Plan API actors, Application actors SHALL interpret missing Must Support data elements within resource instances as data not present in the Health Plan API actors system."

**Actor**: Client

**Conformance**: SHALL

## Test Specification for REQ-08: Client Interpretation of Missing Must Support Data

### 1. Requirement ID

REQ-08

### 2. Requirement Analysis

* **Testability Assessment:** Automatically Testable
* **Complexity:** Moderate
* **Prerequisites:**
    * A running FHIR server (Health Plan API actor) with known resources.
    * A client application capable of making FHIR API requests.
    * At least one resource type on the server should have a "Must Support" element defined in the Implementation Guide, which is not marked as required in the base FHIR specification.
    * This resource instance on the server should be missing the "Must Support" data element.

### 3. Test Implementation Strategy

#### 3.1 Required Inputs

* **FHIR Resource:**  A resource instance on the server that is missing the defined "Must Support" data element.
* **Capability Statement:** The server's Capability Statement, confirming support for the required FHIR operation.

#### 3.2 Required FHIR Operations

* **READ Operation:** The client SHALL perform a READ operation on the pre-determined resource instance.

#### 3.3 Validation Criteria

1. **Response Code:** The client SHALL receive a successful HTTP status code (e.g., 200 OK) in response to the READ operation. This confirms the server operates as expected despite the missing "Must Support" data.
2. **Missing Element:** The returned resource instance SHALL NOT contain the "Must Support" data element that was intentionally omitted.
3. **Client Interpretation:** The client application SHALL interpret the absence of the "Must Support" data element as "data not present" in the Health Plan API actor's system. This step may involve logging, specific UI behavior, or another form of demonstrable action by the client.

**Note:** This test case focuses on the client's behavior. To ensure robustness, consider additional negative test cases where the server returns an error when a "Must Support" element is missing. This would highlight incorrect server behavior. 


---

<a id='req-09'></a>

### REQ-09: Client processing of missing information indicators

**Description**: "Consumer App actors SHALL be able to process resource instances containing Must Support data elements asserting missing information."

**Actor**: Client

**Conformance**: SHALL

## Test Specification for REQ-09: Client Processing of Missing Information Indicators

### 1. Requirement ID

REQ-09

### 2. Requirement Analysis

* **Testability Assessment:** Automatically Testable
* **Complexity:** Moderate
* **Prerequisites:**
    * A running FHIR server with the implemented Implementation Guide.
    * A test client capable of making FHIR API calls and interpreting responses.
    * Pre-loaded resources on the FHIR server containing Must Support data elements with missing information indicators (e.g., dataAbsentReason extensions).

### 3. Test Implementation Strategy

#### 3.1 Required Inputs

* **Resource Type:**  Specify the resource type(s) relevant for testing (e.g., Patient, Observation).
* **Must Support Element:** Identify the specific Must Support data element within the chosen resource type that will be tested with missing information.
* **Missing Information Indicator:** Define the specific code/value used to represent missing information (e.g., "unknown", "asked-but-unknown", as defined in the dataAbsentReason extension).

#### 3.2 Required FHIR Operations

1. **Read Operation:**
    * **Method:** GET
    * **URL:** `[FHIR Server Base URL]/[Resource Type]/[Resource ID]`
    * **Headers:**  Accept: application/fhir+json (or desired format)

#### 3.3 Validation Criteria

1. **Response Status Code:** Verify that the server returns a successful read response (HTTP status code 200).
2. **Resource Content:** 
    * Assert that the returned resource contains the specified Must Support data element.
    * Confirm that the Must Support data element contains the pre-defined missing information indicator (e.g., dataAbsentReason extension with the correct code).
3. **Client Behavior:** (This step requires observation or client-side logging)
    * **Successful Processing:** The client application should successfully process the resource without errors, recognizing the missing information indicator.
    * **Appropriate Handling:**  The client should handle the missing information appropriately based on the specific indicator and application logic. This could involve:
        * Displaying a user-friendly message indicating missing information.
        * Disabling specific functionalities dependent on the missing data.
        * Prompting the user for the missing information.

**Note:** The specific validation criteria for "Appropriate Handling" will depend on the client application's intended behavior as defined in its own requirements or design specifications. 


---

<a id='req-31'></a>

### REQ-31: Client tracking of directory content updates

**Description**: "Clients that cache query results can track additions or modifications to directory content through queries that filter content using the _lastUpdated search parameter."

**Actor**: Client

**Conformance**: None (Implementation guidance)

## Test Specification for REQ-31: Client Tracking of Directory Content Updates

**1. Requirement ID:** REQ-31

**2. Requirement Analysis:**

   - **Testability Assessment:** Automatically Testable
   - **Complexity:** Moderate
   - **Prerequisites:** 
      - A FHIR server with resources that support the `_lastUpdated` search parameter.
      - The ability to create, update, and search for resources on the server.

**3. Test Implementation Strategy:**

   **3.1 Required Inputs:**

     - **Resource Type:**  (Specify the resource type to be tested, e.g., Patient, Practitioner)
     - **Initial Resource Count:** Number of resources of the specified type present on the server before testing.

   **3.2 Test Steps:**

     **Step 1: Record Initial Time**
       - Record the current timestamp (T1).

     **Step 2: Create/Update a Resource**
       - Create a new resource of the specified type or update an existing one.

     **Step 3: Record Update Time**
       - Record the current timestamp (T2).

     **Step 4: Execute Search with _lastUpdated Parameter**
       - Perform a search for the specified resource type using the `_lastUpdated` parameter with a value range from T1 to T2. 
         - Example: `GET [base]/[resource type]?_lastUpdated=ge[T1]& _lastUpdated=le[T2]`

   **3.3 Expected Outputs:**

     - **HTTP Status Code:** 200 (OK)
     - **Response Content:** A Bundle resource containing the newly created or updated resource.

   **3.4 Validation Criteria:**

     - **Assertion 1:** Verify that the returned Bundle contains only resources that were created or updated within the specified time range (T1 to T2).
     - **Assertion 2:** Verify that the number of resources returned in the Bundle matches the number of resources created or updated in Step 2. 

**4. Additional Notes:**

   - This test specification focuses on the functional aspect of the requirement. 
   - Performance testing (e.g., response times for queries with `_lastUpdated`) might be necessary depending on the specific implementation and use case.
   - The test can be repeated with different resource types that support the `_lastUpdated` parameter to ensure broader coverage. 


---



<a id='server'></a>

## Server

<a id='req-01'></a>

### REQ-01: No PII requirement for directory queries

**Description**: "A conformant Plan-Net service SHALL NOT require a directory mobile application to send consumer identifying information in order to query content."

**Actor**: Server

**Conformance**: SHALL NOT

## Test Specification for REQ-01: No PII Requirement for Directory Queries

### 1. Requirement ID

REQ-01

### 2. Requirement Analysis

- **Testability Assessment:**  **Attestation** (While technically possible to test by intercepting traffic, it's more reliable to obtain confirmation from the server implementer)
- **Complexity:** **Simple**
- **Prerequisites:** 
    - Access to the server's Capability Statement.
    - A communication channel with the server implementer to obtain attestation.

### 3. Test Implementation Strategy

#### 3.1 Required Inputs

- **Capability Statement:** The server's published Capability Statement.
- **Attestation Request:** A formal request to the server implementer seeking confirmation about REQ-01 compliance. This request should clearly state the requirement and ask for explicit confirmation that the server does not require PII for directory queries.

#### 3.2 Required FHIR Operations

- N/A (This test relies on inspection and attestation, not direct API interaction)

#### 3.3 Validation Criteria

1. **Capability Statement Review:** Examine the Capability Statement for any indications that contradict REQ-01. For example, if the Capability Statement explicitly mentions requiring patient identifiers for directory searches, this would flag a potential non-conformance. 
2. **Attestation Confirmation:**  The server implementer must provide a clear and unambiguous statement confirming that their Plan-Net service does NOT require consumer identifying information for directory queries. This could be in the form of:
    - A signed document.
    - An email response.
    - An entry in the server's conformance documentation explicitly addressing REQ-01.

**Passing Criteria:** The test is considered passed if:

- The Capability Statement does not contradict REQ-01.
- The server implementer provides explicit attestation confirming compliance with REQ-01.

**Failing Criteria:** The test fails if either:

- The Capability Statement indicates a requirement for PII in directory queries.
- The server implementer cannot provide satisfactory attestation of compliance. 


---

<a id='req-03'></a>

### REQ-03: Population of Must Support data elements

**Description**: "Health Plan API actors SHALL be capable of populating all Must Support data elements as part of the query results."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-03: Population of Must Support Data Elements

### 1. Requirement ID

REQ-03

### 2. Requirement Analysis

**Testability Assessment:** Automatically Testable

**Complexity:** Moderate

**Prerequisites:**

* A list of all "Must Support" data elements for the relevant FHIR resources used in the Health Plan API.
* Access to a test environment with the Health Plan API server running.
* Ability to send API requests and receive responses in FHIR format.

### 3. Test Implementation Strategy

#### 3.1. Required Inputs

* **FHIR Resources:**  A set of test FHIR resources relevant to the Health Plan API (e.g., Patient, Coverage, Claim) containing a mix of "Must Support" and optional data elements.
* **Must Support Data Elements List:** A comprehensive list identifying all "Must Support" data elements within the resources used in the test.

#### 3.2. Required FHIR Operations

* **Read Operation:**  Execute a read operation (e.g., GET /Patient/{id}) for each test FHIR resource. 
* **Search Operation:** Execute search operations (e.g., GET /Patient?family=Smith) with relevant search parameters to retrieve resources.

**Note:** The Capability Statement should confirm the server supports the Read and Search operations for the tested resources.

#### 3.3. Validation Criteria

1. **Presence of Must Support Data Elements:** For each returned resource in both Read and Search operations, verify that all data elements marked as "Must Support" in the provided list are present in the response.
2. **Data Type Validation:** Validate that the data type of each "Must Support" data element in the response matches the data type defined in the respective FHIR resource profile.
3. **Cardinality Validation:** Ensure that the cardinality of each "Must Support" data element in the response adheres to the minimum and maximum occurrences specified in the FHIR resource profile.

**Passing Criteria:** The test is considered passed if all "Must Support" data elements are present, with the correct data type and cardinality, in the responses for all tested resources and operations.

**Failure Criteria:** The test fails if any "Must Support" data element is:

* Missing from the response.
* Of an incorrect data type.
* Does not adhere to the defined cardinality. 


---

<a id='req-04'></a>

### REQ-04: Not including absent data elements

**Description**: "In situations where information on a particular Must Support data element is not present and the minimum cardinality is 0, the Health Plan API actors SHALL NOT include the data elements in the resource instance returned as part of the query results."

**Actor**: Server

**Conformance**: SHALL NOT

## Test Specification for REQ-04: Not Including Absent Data Elements

### 1. Requirement ID

REQ-04

### 2. Requirement Analysis

* **Testability Assessment:** Automatically Testable
* **Complexity:** Simple
* **Prerequisites:**
    * A FHIR server instance with the implemented API.
    * At least one resource type with optional (minimum cardinality 0) and Must Support data elements as defined in the Implementation Guide.
    * Test data with known absent optional data elements for the chosen resource type.

### 3. Test Implementation Strategy

#### 3.1. Test Case 1: Absent Optional Data Element Not Included

* **Test Objective:** Verify that the server does not include optional Must Support data elements with absent values in the returned resource instance.

* **Required Inputs:**
    * **FHIR Resource:** A resource instance of the chosen type with a known optional Must Support data element absent. 
    * **Example:** 
        ```json
        {
          "resourceType": "Patient",
          "id": "patient-example",
          "name": [
            {
              "family": "Doe",
              "given": [
                "John"
              ]
            }
          ]
          // "birthDate" element is missing and is optional with MustSupport
        }
        ```

* **Required FHIR Operations:**
    * `GET` request to the appropriate resource endpoint to retrieve the resource instance.
    * **Example:** `GET [base]/Patient/patient-example`

* **Validation Criteria:**
    * **Assertion:** The response body MUST NOT contain the absent optional data element ("birthDate" in the example).
    * **Status Code:** 200 (OK)

#### 3.2. Test Case 2:  Present Optional Data Element Included

* **Test Objective:** Verify that the server includes optional Must Support data elements with present values in the returned resource instance.

* **Required Inputs:**
    * **FHIR Resource:** A resource instance of the chosen type with a known optional Must Support data element present. 
    * **Example:** 
        ```json
        {
          "resourceType": "Patient",
          "id": "patient-example",
          "name": [
            {
              "family": "Doe",
              "given": [
                "John"
              ]
            }
          ],
          "birthDate": "1970-01-01" 
        }
        ```

* **Required FHIR Operations:**
    * `GET` request to the appropriate resource endpoint to retrieve the resource instance.
    * **Example:** `GET [base]/Patient/patient-example`

* **Validation Criteria:**
    * **Assertion:** The response body MUST contain the present optional data element ("birthDate" in the example) with the correct value.
    * **Status Code:** 200 (OK)

**Note:** These test cases should be repeated for different resource types and optional Must Support data elements as defined in the Implementation Guide. The Capability Statement should be consulted to ensure the chosen resources and operations are supported. 


---

<a id='req-05'></a>

### REQ-05: Using dataAbsentReason for missing required information

**Description**: "In situations where information on a particular data element is not present and the minimum cardinality is >0, SHALL send the reason for the missing information using values (such as nullFlavors) from the value set where they exist or use the dataAbsentReason extension."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-05: Using dataAbsentReason for Missing Required Information

### 1. Requirement ID

REQ-05

### 2. Requirement Analysis

* **Testability Assessment:** Automatically Testable
* **Complexity:** Moderate
* **Prerequisites:** 
    * A FHIR server with the capability to create resources relevant to the test.
    * Knowledge of at least one resource type and data element within that resource type where the minimum cardinality is > 0 on the server. This information should be available in the CapabilityStatement. 
    * The server should support the `dataAbsentReason` extension ([http://hl7.org/fhir/StructureDefinition/data-absent-reason](http://hl7.org/fhir/StructureDefinition/data-absent-reason): [http://hl7.org/fhir/StructureDefinition/data-absent-reason](http://hl7.org/fhir/StructureDefinition/data-absent-reason)).

### 3. Test Implementation Strategy

#### 3.1. Required Inputs

* **Resource Type:**  [Specify the resource type to be used for testing, e.g., Patient].
* **Data Element:** [Specify the required data element within the chosen resource type, e.g., Patient.birthDate].
* **Test Data:** A FHIR resource of the chosen type with the specified data element intentionally missing.

**Example:**

```json
{
  "resourceType": "Patient",
  "name": [
    {
      "family": "Doe",
      "given": ["John"]
    }
  ]
  // birthDate element intentionally missing
}
```

#### 3.2. Required FHIR Operations

* **HTTP POST:** To create the resource with the missing required data element. The specific endpoint will depend on the base URL of the FHIR server and the chosen resource type (e.g., `[FHIR Server Base URL]/Patient`).

#### 3.3. Validation Criteria

1. **HTTP Status Code:** The server SHALL return an HTTP status code of `201 Created` (or `200 OK` if using conditional create) indicating successful resource creation.
2. **Data Absent Reason:** The response SHALL include the created resource with the missing data element populated with either:
    * A `nullFlavor` code from the element's value set if applicable.
    * The `dataAbsentReason` extension with a valid code from the `DataAbsentReason` value set ([http://hl7.org/fhir/ValueSet/data-absent-reason](http://hl7.org/fhir/ValueSet/data-absent-reason)).

**Example of Successful Response:**

```json
{
  "resourceType": "Patient",
  "id": "12345",
  "name": [
    {
      "family": "Doe",
      "given": ["John"]
    }
  ],
  "birthDate": {
    "extension": [
      {
        "url": "http://hl7.org/fhir/StructureDefinition/data-absent-reason",
        "valueCode": "unknown"
      }
    ]
  }
}
```

**Passing the Test:** The test is considered passed if both validation criteria are met. This confirms the server correctly handles missing required information by providing a reason for the absence. 


---

<a id='req-10'></a>

### REQ-10: JSON format support

**Description**: "Support json source formats for all Plan-Net interactions."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-10: JSON Format Support

**1. Requirement ID:** REQ-10

**2. Requirement Analysis:**

   - **Testability Assessment:** Automatically Testable
   - **Complexity:** Simple
   - **Prerequisites:**
      - A running FHIR server that implements the Plan-Net interactions. 
      - Test Plan-Net resources in JSON format.

**3. Test Implementation Strategy:**

   **3.1 Test Case 1: Create PlanDefinition Resource (JSON)**

      - **Description:** Verify the server can successfully process a create request for a PlanDefinition resource with JSON payload.
      - **Required Inputs:**
         - A valid FHIR PlanDefinition resource in JSON format.
      - **Required FHIR Operation:**
         - `POST [base]/PlanDefinition` 
      - **Validation Criteria:**
         - **HTTP Status Code:** 201 (Created)
         - **Response Body:** The server should return the created PlanDefinition resource in JSON format, including a newly assigned logical ID.

   **3.2 Test Case 2: Update PlanDefinition Resource (JSON)**

      - **Description:** Verify the server can successfully process an update request for an existing PlanDefinition resource with JSON payload.
      - **Required Inputs:**
         - The logical ID of an existing PlanDefinition resource.
         - A valid FHIR PlanDefinition resource in JSON format containing updates.
      - **Required FHIR Operation:**
         - `PUT [base]/PlanDefinition/{id}`
      - **Validation Criteria:**
         - **HTTP Status Code:** 200 (OK) or 204 (No Content) 
         - **Response Body (if applicable):** The server may return the updated PlanDefinition resource in JSON format.

   **3.3 Test Case 3: Read PlanDefinition Resource (Accept Header)**

      - **Description:** Verify the server can return a PlanDefinition resource in JSON format when specified in the Accept header.
      - **Required Inputs:**
         - The logical ID of an existing PlanDefinition resource.
      - **Required FHIR Operation:**
         - `GET [base]/PlanDefinition/{id}` with header `Accept: application/fhir+json`
      - **Validation Criteria:**
         - **HTTP Status Code:** 200 (OK)
         - **Response Body:** The server should return the requested PlanDefinition resource in JSON format.

   **Note:** These test cases should be repeated for all relevant Plan-Net interaction resources (e.g., Task, DeviceRequest) to ensure comprehensive coverage of the requirement. 


---

<a id='req-11'></a>

### REQ-11: RESTful behavior implementation

**Description**: "Implement the RESTful behavior according to the FHIR specification."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-11: RESTful Behavior Implementation

### 1. Requirement ID

REQ-11

### 2. Requirement Analysis

- **Testability Assessment:** Not Testable (Too Vague)
- **Complexity:** N/A
- **Prerequisites:** N/A

**Rationale:**

The requirement "Implement the RESTful behavior according to the FHIR specification" is too broad to be directly testable. The FHIR specification encompasses a wide range of RESTful principles and behaviors, making it difficult to define specific, measurable test cases without further clarification. 

This requirement is better addressed through a combination of:

* **Conformance to FHIR Validator:**  Ensuring the server passes validation against the official FHIR validator for the chosen FHIR version already covers a significant portion of RESTful behavior expectations.
* **Targeted Tests for Specific Behaviors:**  Break down this high-level requirement into smaller, more concrete requirements focusing on specific RESTful aspects like HTTP methods, status codes, resource retrieval, etc. These specific requirements can then be tested individually.

### 3. Test Implementation Strategy

**Not Applicable:** Due to the vagueness of the requirement, a specific test implementation strategy cannot be defined. 

**Recommendations:**

1. **Rely on FHIR Validator:** Utilize the official FHIR validator as the primary means of verifying general RESTful conformance.
2. **Define Specific Requirements:**  Decompose REQ-11 into more granular requirements that address specific aspects of RESTful behavior relevant to the implementation. For example:
    - **REQ-11.1:** The server SHALL support HTTP GET for resource retrieval.
    - **REQ-11.2:** The server SHALL return appropriate HTTP status codes (e.g., 200 OK, 404 Not Found) based on the outcome of the request.
    - **REQ-11.3:** The server SHALL support content negotiation for different resource representations (e.g., XML, JSON).

By creating these specific requirements, you can then develop targeted test cases with clear inputs, outputs, and validation criteria. Each test case would focus on verifying a particular aspect of RESTful behavior, making the testing process more manageable and effective. 


---

<a id='req-12'></a>

### REQ-12: Support for all Implementation Guide profiles

**Description**: "Support all profiles defined in this Implementation Guide."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-12: Support for all Implementation Guide profiles

### 1. Requirement ID

REQ-12

### 2. Requirement Analysis

* **Testability Assessment:** Automatically Testable
* **Complexity:** Moderate
* **Prerequisites:** 
    * A list of all profiles defined in the Implementation Guide.
    * Access to the server's Capability Statement.

### 3. Test Implementation Strategy

#### 3.1 Test Case 1: Validate Profile Declarations in CapabilityStatement

This test case verifies that the server's CapabilityStatement declares support for all profiles defined in the Implementation Guide.

* **Required Inputs:**
    * **Implementation Guide:** The FHIR Implementation Guide under test.
    * **Capability Statement:** The server's Capability Statement resource.
* **Required FHIR Operations:**
    * `GET [base]/metadata` - To retrieve the server's CapabilityStatement.
* **Validation Criteria:**
    1. **Extract Profile URLs:** Obtain a list of all profile URLs defined in the Implementation Guide.
    2. **Check Resource Types:** For each resource type mentioned in the CapabilityStatement's `rest.resource` array:
        * **Iterate through `supportedProfile`:** Verify that every profile URL extracted from the Implementation Guide is present in the `supportedProfile` array for that resource type.
    3. **Pass/Fail:** The test passes if all profile URLs from the Implementation Guide are found within the corresponding `supportedProfile` arrays in the CapabilityStatement. Otherwise, the test fails.

#### 3.2 Test Case 2: Validate Resource Conformance to Profiles (Data-Driven)

This test case validates that the server can process resources conforming to the profiles defined in the Implementation Guide.

* **Required Inputs:**
    * **Implementation Guide:** The FHIR Implementation Guide under test.
    * **Test Data Set:** A set of FHIR resources, each conforming to one of the profiles defined in the Implementation Guide. This data set should cover a representative sample of resources and use cases relevant to the Implementation Guide.
* **Required FHIR Operations:**
    * Resource-specific operations (e.g., `CREATE`, `UPDATE`, `READ`) based on the test data set and the operations supported by the server as declared in the CapabilityStatement.
* **Validation Criteria:**
    1. **For each resource in the test data set:**
        * **Send the resource to the server** using the appropriate FHIR operation (CREATE, UPDATE, or READ).
        * **Verify HTTP Status Code:**  
            * For `CREATE`: Expect a `201 Created` response.
            * For `UPDATE`: Expect a `200 OK` or `201 Created` response.
            * For `READ`: Expect a `200 OK` response.
        * **Validate Response Resource:** If applicable, validate that the returned resource conforms to the expected profile and contains the expected data.
    2. **Pass/Fail:** The test passes if all resource interactions are successful and meet the validation criteria. Otherwise, the test fails.


**Note:**  These test cases provide a starting point for validating REQ-12. Depending on the specific profiles and their complexity, additional test cases might be necessary to ensure comprehensive coverage. 


---

<a id='req-13'></a>

### REQ-13: Unauthorized request response

**Description**: "Return the following response classes: (Status 401/4xx): unauthorized request."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-13: Unauthorized Request Response

### 1. Requirement ID

REQ-13

### 2. Requirement Analysis

**Testability Assessment:** Automatically Testable

**Complexity:** Simple

**Prerequisites:**

* A running FHIR server that implements the Implementation Guide.
* A test client capable of making authenticated and unauthenticated FHIR API requests.

### 3. Test Implementation Strategy

#### 3.1 Test Case 1: Unauthorized Access to Protected Resource

**Objective:** Verify that the server returns a 401 Unauthorized response when an unauthenticated request is made to a protected resource.

**Inputs:**

* **Request Type:** GET, POST, PUT, DELETE (any operation requiring authorization)
* **Resource:** Any resource defined as protected in the Implementation Guide.
* **Authentication:** None (simulate an unauthenticated request)

**Expected Outputs:**

* **HTTP Status Code:** 401 Unauthorized
* **FHIR OperationOutcome Resource:** (Optional) The response MAY include an OperationOutcome resource with details about the authorization failure.

**Validation Criteria:**

1. Assert that the HTTP status code of the response is 401 Unauthorized.
2. (Optional) If an OperationOutcome resource is returned, assert that its `issue.code` element contains a relevant code indicating an authentication error (e.g., `login`, `security`, `processing`).

#### 3.2 Test Case 2: Unauthorized Access with Invalid Credentials

**Objective:** Verify that the server returns a 401 Unauthorized response when a request is made with invalid credentials.

**Inputs:**

* **Request Type:** GET, POST, PUT, DELETE (any operation requiring authorization)
* **Resource:** Any resource defined as protected in the Implementation Guide.
* **Authentication:** Provide invalid credentials (e.g., incorrect username/password, expired token).

**Expected Outputs:**

* **HTTP Status Code:** 401 Unauthorized
* **FHIR OperationOutcome Resource:** (Optional) The response MAY include an OperationOutcome resource with details about the authorization failure.

**Validation Criteria:**

1. Assert that the HTTP status code of the response is 401 Unauthorized.
2. (Optional) If an OperationOutcome resource is returned, assert that its `issue.code` element contains a relevant code indicating an authentication error (e.g., `login`, `security`, `processing`).

**Note:**

* These test cases assume that the Capability Statement confirms the server requires authorization for accessing the specified resources.
* The specific resources and authentication mechanisms used in the test cases should be tailored to the specific Implementation Guide and server implementation. 


---

<a id='req-14'></a>

### REQ-14: Insufficient scope response

**Description**: "Return the following response classes: (Status 403): insufficient scope."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-14: Insufficient Scope Response

### 1. Requirement ID

REQ-14

### 2. Requirement Analysis

- **Testability Assessment:** Automatically Testable
- **Complexity:** Simple
- **Prerequisites:** 
    - A valid OAuth2 token with insufficient scope to access the requested resource or operation. 

### 3. Test Implementation Strategy

#### 3.1. Test Case 1: Insufficient Scope for Read Operation

**3.1.1. Inputs:**

- **FHIR Resource:** Any resource the test token has insufficient scope to read (e.g., Patient).
- **FHIR Operation:** `read` (e.g., GET request to `/Patient/{id}`)
- **Authorization:** OAuth2 token with insufficient scope.

**3.1.2. Expected Outputs:**

- **HTTP Status Code:** 403 Forbidden
- **FHIR OperationOutcome:**
    - `OperationOutcome.issue.severity`:  "error"
    - `OperationOutcome.issue.code`: "security"
    - `OperationOutcome.issue.details.coding.system`: "http://terminology.hl7.org/CodeSystem/fhir-issue"
    - `OperationOutcome.issue.details.coding.code`: "insufficient-scope"
    - `OperationOutcome.issue.diagnostics`:  A human-readable explanation of the insufficient scope error.

**3.1.3. Validation Criteria:**

- **Assert:** The HTTP status code is 403 Forbidden.
- **Assert:** The response body is a valid FHIR OperationOutcome resource.
- **Assert:** The OperationOutcome resource contains the expected error codes and diagnostics message.

#### 3.2. Test Case 2: Insufficient Scope for Write Operation

**3.2.1. Inputs:**

- **FHIR Resource:** Any resource the test token has insufficient scope to write (e.g., Patient).
- **FHIR Operation:** `create` (e.g., POST request to `/Patient`)
- **Authorization:** OAuth2 token with insufficient scope.

**3.2.2. Expected Outputs:**

- **HTTP Status Code:** 403 Forbidden
- **FHIR OperationOutcome:** (Same structure and content as in Test Case 1)

**3.2.3. Validation Criteria:**

- **Assert:** The HTTP status code is 403 Forbidden.
- **Assert:** The response body is a valid FHIR OperationOutcome resource.
- **Assert:** The OperationOutcome resource contains the expected error codes and diagnostics message.

**Note:** These test cases can be adapted for other FHIR operations like `update`, `delete`, `search`, etc., by adjusting the input resource, operation, and expected output accordingly. 


---

<a id='req-15'></a>

### REQ-15: Invalid parameter response

**Description**: "Return the following response classes: (Status 400): invalid parameter."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-15: Invalid Parameter Response

### 1. Requirement ID

REQ-15

### 2. Requirement Analysis

* **Testability Assessment:** Automatically Testable
* **Complexity:** Simple
* **Prerequisites:** 
    * A running FHIR server that implements the relevant resources and operations.
    * Knowledge of a valid resource and operation supported by the server (as per Capability Statement).
    * Ability to send requests with intentionally invalid parameters.

### 3. Test Implementation Strategy

#### 3.1 Test Case 1: Invalid Parameter in Search Operation

**Objective:** Verify that the server returns a status code 400 (Bad Request) with an "invalid parameter" message when an invalid parameter is used in a search operation.

**Inputs:**

* **FHIR Resource:**  Any resource supported for search operations by the server (refer to Capability Statement).
* **FHIR Operation:** Search (e.g., `GET [base]/[resource]?parameter=value`)
* **Invalid Parameter:** 
    * Use a non-existent search parameter.
    * Use an invalid format for an existing search parameter (e.g., incorrect date format).

**Expected Outputs:**

* **HTTP Status Code:** 400 (Bad Request)
* **Response Body:** OperationOutcome resource with an issue of severity "error" and a diagnostic message indicating "invalid parameter" or a similar message that clearly conveys the reason for the error.

**Validation Criteria:**

* Assert that the HTTP status code is 400.
* Assert that the response body is a valid OperationOutcome resource.
* Assert that the OperationOutcome resource contains an issue with severity "error".
* Assert that the OperationOutcome's diagnostic message indicates an "invalid parameter" or a similar clear message.

#### 3.2 Test Case 2: Invalid Parameter in Create Operation

**Objective:** Verify that the server returns a status code 400 (Bad Request) with an "invalid parameter" message when an invalid parameter is used in a create operation.

**Inputs:**

* **FHIR Resource:** Any resource supported for create operations by the server (refer to Capability Statement).
* **FHIR Operation:** Create (e.g., `POST [base]/[resource]`)
* **Invalid Parameter:** Include an invalid or non-existent element/field in the resource being created.

**Expected Outputs:**

* **HTTP Status Code:** 400 (Bad Request)
* **Response Body:** OperationOutcome resource with an issue of severity "error" and a diagnostic message indicating "invalid parameter" or a similar message that clearly conveys the reason for the error.

**Validation Criteria:**

* Assert that the HTTP status code is 400.
* Assert that the response body is a valid OperationOutcome resource.
* Assert that the OperationOutcome resource contains an issue with severity "error".
* Assert that the OperationOutcome's diagnostic message indicates an "invalid parameter" or a similar clear message.

**Note:** 

* These test cases provide a starting point. You can create additional test cases by varying the resource type, operation, and specific invalid parameters used.
* Refer to the FHIR specification and the server's Capability Statement to determine valid and invalid parameter formats and values. 


---

<a id='req-16'></a>

### REQ-16: Unknown resource response

**Description**: "Return the following response classes: (Status 404): unknown resource."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-16: Unknown Resource Response

**1. Requirement ID:** REQ-16

**2. Requirement Analysis:**

   - **Testability Assessment:** Automatically Testable
   - **Complexity:** Simple
   - **Prerequisites:** 
      - A running FHIR server that implements the target Implementation Guide.
      - Knowledge of a resource type **not** supported by the server (this information can be derived from the CapabilityStatement).

**3. Test Implementation Strategy:**

   **3.1. Test Case 1: Requesting an Unknown Resource**

     - **Description:** This test case verifies that the server returns a 404 (Not Found) status code when a request is made for a resource type that is not supported.

     - **Required Inputs:**
        - **HTTP Method:** GET
        - **URL:** `[base]/[unknownResource]` where `[base]` is the base URL of the FHIR server and `[unknownResource]` is a resource type not listed in the CapabilityStatement's `rest.[mode].resource` array.

     - **Expected Outputs:**
        - **HTTP Status Code:** 404 Not Found
        - **Response Body:**  The response body SHOULD be a valid OperationOutcome resource indicating the reason for the error (unknown resource).

     - **Validation Criteria:**
        - Verify that the HTTP status code is 404 Not Found.
        - Verify that the response body is a valid OperationOutcome resource (optional, but recommended).
        - Verify that the OperationOutcome resource (if present) describes the reason for the error as an unknown resource.

   **3.2. Test Case 2: Requesting an Unknown Resource with an ID**

     - **Description:** This test case verifies that the server returns a 404 (Not Found) status code when a request is made for a specific resource instance using an unsupported resource type.

     - **Required Inputs:**
        - **HTTP Method:** GET
        - **URL:** `[base]/[unknownResource]/[someId]` where `[base]` is the base URL of the FHIR server, `[unknownResource]` is a resource type not listed in the CapabilityStatement's `rest.[mode].resource` array, and `[someId]` is an arbitrary ID.

     - **Expected Outputs:**
        - **HTTP Status Code:** 404 Not Found
        - **Response Body:**  The response body SHOULD be a valid OperationOutcome resource indicating the reason for the error (unknown resource).

     - **Validation Criteria:**
        - Verify that the HTTP status code is 404 Not Found.
        - Verify that the response body is a valid OperationOutcome resource (optional, but recommended).
        - Verify that the OperationOutcome resource (if present) describes the reason for the error as an unknown resource. 

**Note:** These test cases can be automated using testing frameworks like Jest (with a library like `node-fhir-client`) or Postman. 


---

<a id='req-17'></a>

### REQ-17: Deleted resource response

**Description**: "Return the following response classes: (Status 410): deleted resource."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-17: Deleted Resource Response

**1. Requirement ID:** REQ-17

**2. Requirement Analysis:**

   - **Testability Assessment:** Automatically Testable
   - **Complexity:** Simple
   - **Prerequisites:**
     - A FHIR server instance under test.
     - A pre-existing resource on the server that can be deleted.

**3. Test Implementation Strategy:**

   **3.1 Test Case 1: Successful Deletion and 410 Response**

     **3.1.1 Required Inputs:**

       - **Resource Type:** Any resource type supported by the server (e.g., Patient, Observation).
       - **Valid Resource ID:** The ID of the pre-existing resource to be deleted.

     **3.1.2 Required FHIR Operations:**

       1. **DELETE:** `/fhir/[resourceType]/[resourceId]` 
          - This operation should delete the specified resource.

       2. **READ:** `/fhir/[resourceType]/[resourceId]`
          - This operation should be attempted after the DELETE to verify the response code.

     **3.1.3 Validation Criteria:**

       1. **Response Code (DELETE):** Verify the server returns an HTTP status code `204 (No Content)` or `202 (Accepted)` for the DELETE request, indicating successful deletion.
       2. **Response Code (READ):** Verify the server returns an HTTP status code `410 (Gone)` for the subsequent READ request, indicating the resource has been deleted.
       3. **Response Body (READ):** Verify the response body for the READ request adheres to the FHIR specification for OperationOutcome and includes a relevant message indicating the resource was deleted.

   **3.2 Test Case 2: Attempting to Delete Non-Existent Resource**

     **3.2.1 Required Inputs:**

       - **Resource Type:** Any resource type supported by the server.
       - **Non-Existent Resource ID:** An ID that does not correspond to an existing resource.

     **3.2.2 Required FHIR Operations:**

       1. **DELETE:** `/fhir/[resourceType]/[nonExistentResourceId]`

     **3.2.3 Validation Criteria:**

       1. **Response Code (DELETE):** Verify the server returns an HTTP status code `404 (Not Found)` for the DELETE request, indicating the resource does not exist.

**Note:** These test cases assume the Capability Statement confirms support for the DELETE and READ operations for the chosen resource type. 


---

<a id='req-18'></a>

### REQ-18: Profile identification in meta attribute

**Description**: "Identify the Plan-Net profiles supported as part of the FHIR meta.profile attribute for each instance."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-18: Profile Identification in meta Attribute

### 1. Requirement ID

REQ-18

### 2. Requirement Analysis

* **Testability Assessment:** Automatically Testable
* **Complexity:** Simple
* **Prerequisites:** 
    * A running FHIR server that implements the Plan-Net Implementation Guide.
    * Access to at least one FHIR resource instance that should be profiled according to the Plan-Net IG.

### 3. Test Implementation Strategy

#### 3.1 Required Inputs

* **FHIR Resource:** Any resource instance conforming to the Plan-Net IG. 
* **Plan-Net Profile URL:** The canonical URL of the Plan-Net profile that the resource instance should conform to. This information should be provided in the Implementation Guide's documentation.

#### 3.2 Required FHIR Operations

* **Read Operation:** A standard FHIR read operation will be performed to retrieve the desired resource instance from the server. 

#### 3.3 Validation Criteria

1. **Profile URL Presence:** The `meta.profile` element of the returned resource instance MUST contain the provided Plan-Net Profile URL.
2. **Valid URL:** The provided Plan-Net Profile URL in the `meta.profile` element MUST be a valid URL.

#### 3.4 Test Steps

1. **Retrieve Resource:** Perform a FHIR Read operation to retrieve the target resource instance from the server.
2. **Extract Profile URL:** Parse the returned resource instance and extract the value(s) within the `meta.profile` element.
3. **Validate Profile URL Presence:** Assert that the extracted `meta.profile` value(s) include the expected Plan-Net Profile URL.
4. **Validate URL Format:** Assert that the extracted Plan-Net Profile URL is a syntactically valid URL.

#### 3.5 Example using Python and the `requests` library

```python
import requests

# Define the base URL of your FHIR server and the resource type
base_url = "https://your-fhir-server/fhir"
resource_type = "Patient"
resource_id = "12345"

# Define the expected Plan-Net profile URL
expected_profile_url = "http://hl7.org/fhir/us/plannet/StructureDefinition/plannet-patient"

# Construct the full URL for the read operation
url = f"{base_url}/{resource_type}/{resource_id}"

# Perform the read operation
response = requests.get(url)

# Check for successful response
response.raise_for_status()

# Parse the response as JSON
resource = response.json()

# Extract the profile URLs from the meta.profile element
profile_urls = resource.get("meta", {}).get("profile", [])

# Assert that the expected profile URL is present
assert expected_profile_url in profile_urls, f"Expected profile URL '{expected_profile_url}' not found in resource meta.profile"

# Print a success message
print(f"Successfully validated presence of profile URL '{expected_profile_url}' in resource meta.profile")
```

This test specification provides a clear and structured approach to verifying the "Profile identification in meta attribute" requirement (REQ-18). It outlines the necessary steps, inputs, validation criteria, and even provides a simple example implementation. This ensures consistent and reliable testing of this critical aspect of the Plan-Net Implementation Guide. 


---

<a id='req-19'></a>

### REQ-19: Individual search parameter support

**Description**: "Support the searchParameters on each profile individually."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-19: Individual Search Parameter Support

### 1. Requirement ID

REQ-19

### 2. Requirement Analysis

- **Testability Assessment**: Automatically Testable
- **Complexity**: Moderate
- **Prerequisites**: 
    - A list of all FHIR resources with custom profiles defined in the Implementation Guide.
    - For each profile, a list of supported search parameters. This information should be available in the Implementation Guide itself.
    - A running FHIR server that implements the Implementation Guide.

### 3. Test Implementation Strategy

#### 3.1 Required Inputs

1. **FHIR Server Endpoint**: Base URL of the FHIR server under test.
2. **List of Resources**: An array of FHIR resource types with custom profiles defined in the Implementation Guide (e.g., ["Patient", "Observation"]).
3. **Search Parameter Mapping**: A JSON object mapping each resource type to an array of its supported search parameters according to the Implementation Guide. 
    Example:
    ```json
    {
      "Patient": ["identifier", "name", "birthdate", "custom-parameter"],
      "Observation": ["subject", "code", "value-quantity", "another-custom-parameter"]
    }
    ```

#### 3.2 Required FHIR Operations

- **GET /[resourceType]?{searchParameter}={searchValue}**: This operation will be used to test each search parameter for each resource type.

#### 3.3 Validation Criteria

1. **HTTP Status Code**: Each request should return a 200 (OK) status code if the search parameter is supported and valid search criteria are provided.
2. **Content-Type**: The response Content-Type header should be "application/fhir+json" or "application/fhir+xml" depending on the request headers.
3. **Resource Type**: The returned resource should be a Bundle with the type "searchset".
4. **Search Parameter Presence**: Verify that the "parameter" element in the Bundle entry reflects the search parameter used in the request.
5. **Number of Results**: The number of returned resources in the Bundle should be greater than zero if data exists matching the search criteria. This assumes the server has data populated for testing. If not, at minimum, the server should respond without error.

#### 3.4 Test Procedure

1. For each resource type in the "List of Resources":
    - Retrieve the list of supported search parameters from the "Search Parameter Mapping".
    - For each search parameter:
        - Construct a valid search URL using the FHIR server endpoint, resource type, search parameter, and a valid search value (if applicable).
        - Execute a GET request to the constructed URL.
        - Validate the response based on the criteria outlined in section 3.3.

#### 3.5 Example Test Case

**Resource Type**: Patient

**Search Parameter**: identifier

**Test URL**: [FHIR Server Endpoint]/Patient?identifier=12345

**Expected Results**:

- HTTP Status Code: 200 (OK)
- Content-Type: application/fhir+json
- Resource Type: Bundle with type "searchset"
- Search Parameter Presence: "parameter" element in Bundle entry includes "identifier"
- Number of Results: Greater than zero (assuming data exists for a patient with identifier "12345")

This test specification provides a structured approach to automatically test the "Individual search parameter support" requirement. By iterating through each resource and its supported search parameters, we can ensure that the FHIR server correctly implements the search functionality defined in the Implementation Guide. 


---

<a id='req-20'></a>

### REQ-20: Combination search parameter support

**Description**: "Support the searchParameters on each profile in combination."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-20: Combination Search Parameter Support

### 1. Requirement ID

REQ-20

### 2. Requirement Analysis

* **Testability Assessment:** Automatically Testable
* **Complexity:** Moderate
* **Prerequisites:**
    * The FHIR server under test must support the search parameters defined in the profiles mentioned in the requirement.
    * The FHIR server should have data populated for the resources relevant to the profiles mentioned in the requirement. 

### 3. Test Implementation Strategy

This test specification focuses on verifying the server's ability to handle combined search parameters effectively. It's crucial to select combinations relevant to real-world use cases and representative of the complexity expected in the implementation.

#### 3.1 Test Case 1: Simple Combination

* **Description:**  This test case verifies if the server can handle a simple combination of two search parameters.
* **Required Inputs:**
    * **Resource Type:**  (Specify the resource type relevant to the profile)
    * **Search Parameter 1:** (Specify the first search parameter and its value)
    * **Search Parameter 2:** (Specify the second search parameter and its value)
* **Required FHIR Operation:**  
    * `GET [base]/[resource type]?{searchParameter1}={value}&{searchParameter2}={value}`
* **Validation Criteria:**
    * **HTTP Status Code:** 200 (OK)
    * **Response Content:** The response bundle SHOULD contain only resources that match BOTH search criteria.
    * **Response Bundle:** Validate the 'total' element in the bundle to ensure it accurately reflects the number of matching resources.

#### 3.2 Test Case 2:  Combination with Different Search Parameter Types

* **Description:** This test case verifies if the server can handle a combination of search parameters with different types (e.g., string, date, token).
* **Required Inputs:**
    * **Resource Type:** (Specify the resource type relevant to the profile)
    * **Search Parameter 1:** (Specify the first search parameter with its type and value)
    * **Search Parameter 2:** (Specify the second search parameter with its type and value)
* **Required FHIR Operation:**  
    * `GET [base]/[resource type]?{searchParameter1}={value}&{searchParameter2}={value}`
* **Validation Criteria:**
    * **HTTP Status Code:** 200 (OK)
    * **Response Content:** The response bundle SHOULD contain only resources that match BOTH search criteria, considering their respective types.
    * **Response Bundle:** Validate the 'total' element in the bundle to ensure it accurately reflects the number of matching resources.

#### 3.3 Test Case 3: Combination with Chained Search Parameters (If Applicable)

* **Description:** This test case verifies if the server can handle a combination that includes chained search parameters.
* **Required Inputs:**
    * **Resource Type:** (Specify the resource type relevant to the profile)
    * **Search Parameter 1:** (Specify the first search parameter, which is a chained parameter, and its value)
    * **Search Parameter 2:** (Specify the second search parameter and its value)
* **Required FHIR Operation:**  
    * `GET [base]/[resource type]?{searchParameter1}={value}&{searchParameter2}={value}`
* **Validation Criteria:**
    * **HTTP Status Code:** 200 (OK)
    * **Response Content:** The response bundle SHOULD contain only resources that match BOTH search criteria, including the chained parameter resolution.
    * **Response Bundle:** Validate the 'total' element in the bundle to ensure it accurately reflects the number of matching resources.

**Note:**

* Replace the placeholders like `{resource type}`, `{searchParameter1}`, `{value}`, etc., with actual values from the FHIR Implementation Guide and the CapabilityStatement.
* These test cases provide a starting point. You should expand them based on the specific search parameters and profiles defined in your implementation guide and the complexity of the combinations you need to support. 
* Consider edge cases and invalid combinations to ensure robust error handling. 


---

<a id='req-21'></a>

### REQ-21: Forward chaining support

**Description**: "Support forward chaining on all search parameters that specify the 'chain' property."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-21: Forward Chaining Support

### 1. Requirement ID

REQ-21

### 2. Requirement Analysis

* **Testability Assessment:** Automatically Testable
* **Complexity:** Moderate
* **Prerequisites:**
    * The Capability Statement MUST advertise support for at least one search parameter with the `chain` property defined.
    * Test data MUST include resources that establish a chain based on the supported search parameters with the `chain` property. For example, if the `Patient.general-practitioner` search parameter supports chaining, test data should include a Patient resource linked to a Practitioner resource.

### 3. Test Implementation Strategy

#### 3.1. Required Inputs

* **Capability Statement:** The server's Capability Statement.
* **Test Data:** A set of FHIR resources that establish a chain based on a supported search parameter with the `chain` property.

#### 3.2. Required FHIR Operations

* **Read (GET) Operation:** To retrieve the Capability Statement.
* **Search (GET) Operation:** To execute searches using chained parameters.

#### 3.3. Validation Criteria

1. **Capability Statement Validation:**
    * Verify that the Capability Statement advertises support for at least one search parameter with the `chain` property defined. This involves inspecting the `rest`, `resource`, `searchParam` elements within the Capability Statement.

2. **Forward Chaining Test:**
    * **Step 1:** Identify a search parameter with the `chain` property from the Capability Statement.
    * **Step 2:** Construct a search URL that utilizes the identified chained parameter. For example, if `Patient.general-practitioner` supports chaining and we want to find all patients of a specific organization, the search URL might look like this: `[base]/Patient?general-practitioner:Organization=123`.
    * **Step 3:** Execute the search request.
    * **Step 4:** Verify that the server returns the correct resources based on the chained search. This means the server should traverse the chain defined by the search parameter and return resources that ultimately match the final criteria. For the example above, the server should return all Patient resources linked to a Practitioner who belongs to the organization with ID `123`.

3. **Error Handling:**
    * **Invalid Chain:** If the search URL contains an invalid chain (e.g., a chain that is not supported or a chain with incorrect syntax), the server should return an appropriate error code (e.g., 400 Bad Request) with a clear error message indicating the issue.

#### 3.4. Test Outcome

The test is considered **successful** if all the validation criteria are met. This indicates that the server correctly implements forward chaining for the tested search parameters. If any validation criteria fail, the test is considered **failed**, and the specific failure points should be documented for remediation. 


---

<a id='req-22'></a>

### REQ-22: Reverse chaining support

**Description**: "Support reverse chaining on all search parameters that specify the 'chain' property."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-22: Reverse Chaining Support

### 1. Requirement ID

REQ-22

### 2. Requirement Analysis

* **Testability Assessment:** Automatically Testable
* **Complexity:** Moderate
* **Prerequisites:** 
    * The server under test MUST advertise support for the search parameters with the `chain` property in its CapabilityStatement.
    * Test data MUST include resources that establish chained relationships relevant to the search parameters being tested.

### 3. Test Implementation Strategy

This test specification outlines a general approach. Specific test cases should be created for each search parameter with the `chain` property advertised in the server's CapabilityStatement.

#### 3.1 Required Inputs

* **CapabilityStatement:** The server's CapabilityStatement.
* **Test Data:** FHIR resources with established chained relationships relevant to the search parameter under test.  For example, if testing reverse chaining on `Observation.subject:Patient`, the test data should include Observations linked to Patients, potentially through Encounters.

#### 3.2 Required FHIR Operations

* **Read (GET):** To retrieve the CapabilityStatement.
* **Search (GET):** To execute searches using the search parameters with the `chain` property.

#### 3.3 Validation Criteria

1. **CapabilityStatement Validation:**
    * Verify that the CapabilityStatement advertises support for the search parameter being tested and that it includes the `chain` property.

2. **Reverse Chaining Search Validation:**
    * **Positive Test:** Execute a search using the search parameter with the `chain` property. 
        * **Expected Output:** The search results MUST include resources that match the search criteria through the chained relationship.
    * **Negative Test:** Execute a search using the search parameter without the `chain` property, but with criteria that would only match through reverse chaining.
        * **Expected Output:** The search results MUST NOT include resources that only match through the chained relationship. This confirms that chaining is not implicitly enabled.

#### 3.4 Example Test Case (for `Observation.subject:Patient`)

1. **Retrieve the server's CapabilityStatement.**
2. **Verify that the `Observation.subject` search parameter is supported and includes the `chain` property.**
3. **Populate the server with test data:**
    * Create a Patient resource (e.g., Patient/123).
    * Create an Encounter resource linked to the Patient (e.g., Encounter/456, with `subject` referencing Patient/123).
    * Create an Observation resource linked to the Encounter (e.g., Observation/789, with `encounter` referencing Encounter/456).
4. **Execute a search:**
    * **Positive Test:** Search for Observations with `subject:Patient/123` (using the chained search parameter).
        * **Expected Result:** Observation/789 is returned in the search results.
    * **Negative Test:** Search for Observations with `subject:Patient/123` (without using the chained search parameter).
        * **Expected Result:** Observation/789 is NOT returned in the search results.

This approach ensures that the server correctly implements reverse chaining only for search parameters explicitly defined with the `chain` property, enhancing data retrieval accuracy and preventing unintended data exposure. 


---

<a id='req-23'></a>

### REQ-23: XML format support

**Description**: "Support xml source formats for all Plan-Net interactions."

**Actor**: Server

**Conformance**: SHOULD

## Test Specification for REQ-23: XML Format Support

**1. Requirement ID:** REQ-23

**2. Requirement Analysis:**

   - **Testability Assessment:** Automatically Testable
   - **Complexity:** Simple
   - **Prerequisites:**
     - A running FHIR server that implements the Plan-Net interactions.
     - Test Plan-Net resources in XML format.

**3. Test Implementation Strategy:**

   **3.1 Test Case 1: Create a Plan-Net Resource (XML)**

     - **Description:** Verify the server can successfully process a create request for a Plan-Net resource with the payload in XML format.
     - **Required Inputs:**
       - A valid Plan-Net resource instance in XML format.
     - **Required FHIR Operations:**
       - `POST [base]/[Plan-Net Resource Type]` (e.g., `POST [base]/Coverage`)
     - **Validation Criteria:**
       - **HTTP Status Code:** 201 Created
       - **Response Body:** The server should return the newly created resource in XML format (if requested via `Accept` header) or a format specified in the `Content-Location` header.

   **3.2 Test Case 2: Read a Plan-Net Resource (XML)**

     - **Description:** Verify the server can return a Plan-Net resource in XML format when requested.
     - **Required Inputs:**
       - The logical ID of an existing Plan-Net resource.
     - **Required FHIR Operations:**
       - `GET [base]/[Plan-Net Resource Type]/[id]?_format=xml` (e.g., `GET [base]/Coverage/123?_format=xml`)
     - **Validation Criteria:**
       - **HTTP Status Code:** 200 OK
       - **Response Headers:** `Content-Type: application/fhir+xml`
       - **Response Body:** The server should return the requested resource in XML format.

   **3.3 Test Case 3: Update a Plan-Net Resource (XML)**

     - **Description:** Verify the server can successfully process an update request for a Plan-Net resource with the payload in XML format.
     - **Required Inputs:**
       - The logical ID of an existing Plan-Net resource.
       - A valid Plan-Net resource instance in XML format containing updates.
     - **Required FHIR Operations:**
       - `PUT [base]/[Plan-Net Resource Type]/[id]` (e.g., `PUT [base]/Coverage/123`)
     - **Validation Criteria:**
       - **HTTP Status Code:** 200 OK or 204 No Content
       - **Response Body:** The server may return the updated resource in XML format (if requested via `Accept` header) or a format specified in the `Content-Location` header.

   **3.4 Test Case 4: Search for a Plan-Net Resource (XML)**

     - **Description:** Verify the server can return search results for Plan-Net resources in XML format when requested.
     - **Required Inputs:**
       - Valid search parameters for the Plan-Net resource.
     - **Required FHIR Operations:**
       - `GET [base]/[Plan-Net Resource Type]?_format=xml&[search parameters]` (e.g., `GET [base]/Coverage?_format=xml&status=active`)
     - **Validation Criteria:**
       - **HTTP Status Code:** 200 OK
       - **Response Headers:** `Content-Type: application/fhir+xml`
       - **Response Body:** The server should return the Bundle resource containing matching resources in XML format.

**Note:** 

* These test cases cover the basic CRUD operations. Additional tests may be needed depending on the specific Plan-Net interactions supported by the server.
* The Capability Statement should be consulted to identify the supported Plan-Net resource types and interactions.
* The "SHOULD" conformance level implies that the server is not required to support XML, but it is highly recommended. Therefore, the test results should be interpreted accordingly. 


---

<a id='req-24'></a>

### REQ-24: Rejection of unauthorized requests

**Description**: "A server SHALL reject any unauthorized requests by returning an HTTP 401 unauthorized response code."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-24: Rejection of Unauthorized Requests

**1. Requirement ID:** REQ-24

**2. Requirement Analysis:**

   - **Testability Assessment:** Automatically Testable
   - **Complexity:** Simple
   - **Prerequisites:**
     - A FHIR server endpoint is operational.
     - A protected resource exists on the server that requires authorization to access.
     - The Capability Statement indicates support for the required FHIR operation on the chosen resource. 

**3. Test Implementation Strategy:**

   **3.1. Test Case 1: Unauthorized Access Attempt**

     - **Description:**  Attempt to access a protected resource without providing any authorization credentials.
     - **Required Inputs:**
       - **FHIR Resource:**  Any protected resource on the server (e.g., Patient, Observation).
       - **Authorization:** None (Do not include an Authorization header in the request).
     - **Required FHIR Operation:**  
       - `READ` operation (or any other operation supported by the server for the chosen resource) on the chosen protected resource.
     - **Expected Output:**
       - **HTTP Status Code:** 401 Unauthorized
       - **Optional:** The response body MAY include an `OperationOutcome` resource with details about the authorization failure.
     - **Validation Criteria:**
       - Verify that the server returns an HTTP 401 Unauthorized status code.
       - Optionally, verify the content of the `OperationOutcome` resource if provided.

   **3.2. Test Case 2: Invalid Authorization Credentials**

     - **Description:** Attempt to access a protected resource with invalid authorization credentials.
     - **Required Inputs:**
       - **FHIR Resource:** Any protected resource on the server.
       - **Authorization:** Include an Authorization header with an invalid or expired token.
     - **Required FHIR Operation:** 
       - `READ` operation (or any other operation supported by the server for the chosen resource) on the chosen protected resource.
     - **Expected Output:**
       - **HTTP Status Code:** 401 Unauthorized
       - **Optional:** The response body MAY include an `OperationOutcome` resource with details about the authorization failure.
     - **Validation Criteria:**
       - Verify that the server returns an HTTP 401 Unauthorized status code.
       - Optionally, verify the content of the `OperationOutcome` resource if provided. 

**Note:**

- These test cases should be repeated for different protected resources and FHIR operations to ensure comprehensive coverage.
- The specific format of the authorization credentials (e.g., Bearer token) will depend on the authentication mechanism implemented by the server.
- The Capability Statement should be consulted to determine the supported authentication mechanisms and the expected format of authorization credentials. 


---

<a id='req-25'></a>

### REQ-25: Support for read interaction

**Description**: "For each resource type and profile, a Plan Net server SHALL support the read interaction."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-25: Support for Read Interaction

### 1. Requirement ID

REQ-25

### 2. Requirement Analysis

* **Testability Assessment:** Automatically Testable
* **Complexity:** Simple 
* **Prerequisites:**
    * A running FHIR server compliant with the Implementation Guide.
    * At least one instance of each resource type and profile defined in the Implementation Guide must be available on the server.

### 3. Test Implementation Strategy

#### 3.1 Test Case 1: Read Resource Instance

This test case verifies that the server can successfully return a resource instance using the `read` interaction.

* **Required Inputs:**
    * **Resource Type:**  A valid resource type defined in the Implementation Guide (e.g., `Patient`, `Observation`, etc.).
    * **Resource ID:** A valid logical ID of an existing resource of the specified type.

* **Required FHIR Operations:**
    * `GET [base]/[resourceType]/[id]`

* **Validation Criteria:**
    * **HTTP Status Code:** 200 (OK)
    * **Response Body:** The response body MUST contain a valid FHIR resource of the requested type and ID.
    * **Response Headers:**
        * `Content-Type`:  `application/fhir+json` or `application/fhir+xml` based on request headers.

#### 3.2 Test Case 2: Read Resource Instance with Profile

This test case verifies that the server can successfully return a resource instance that conforms to a specific profile using the `read` interaction.

* **Required Inputs:**
    * **Resource Type:** A valid resource type defined in the Implementation Guide.
    * **Resource ID:** A valid logical ID of an existing resource of the specified type that conforms to the specified profile.
    * **Profile URL:** A valid canonical URL of a profile defined in the Implementation Guide.

* **Required FHIR Operations:**
    * `GET [base]/[resourceType]/[id]`

* **Validation Criteria:**
    * **HTTP Status Code:** 200 (OK)
    * **Response Body:**
        * The response body MUST contain a valid FHIR resource of the requested type and ID.
        * The returned resource MUST conform to the specified profile. This can be validated using a FHIR validator.

#### 3.3 Negative Test Case: Read Non-Existing Resource

This test case verifies that the server returns the appropriate error code when attempting to read a non-existing resource.

* **Required Inputs:**
    * **Resource Type:** A valid resource type defined in the Implementation Guide.
    * **Resource ID:** A non-existing logical ID.

* **Required FHIR Operations:**
    * `GET [base]/[resourceType]/[id]`

* **Validation Criteria:**
    * **HTTP Status Code:** 404 (Not Found)


**Note:** These test cases should be repeated for each resource type and profile defined in the Implementation Guide. The CapabilityStatement can be used to dynamically generate test cases for each supported resource type. 


---

<a id='req-26'></a>

### REQ-26: Support for vread interaction

**Description**: "For each resource type and profile, a Plan Net server SHOULD support the vread interaction."

**Actor**: Server

**Conformance**: SHOULD

## Test Specification for REQ-26: Support for vread interaction

### 1. Requirement ID

REQ-26

### 2. Requirement Analysis

- **Testability Assessment:** Automatically Testable
- **Complexity:** Simple
- **Prerequisites:** 
    - A running FHIR server that implements the Plan Net Implementation Guide.
    - At least one resource instance of each supported resource type and profile exists on the server.

### 3. Test Implementation Strategy

#### 3.1 Required Inputs

- **Resource Type:** Any resource type supported by the server as per the CapabilityStatement.
- **Resource ID:** A valid logical ID of an existing resource of the chosen type.
- **Version ID:** A valid version ID of the chosen resource.

#### 3.2 Required FHIR Operations

- **HTTP GET Request:**  A GET request to the vread endpoint for the chosen resource.
    - **URL Format:** `[base]/[resourceType]/[id]/_history/[versionId]`
    - **Example:** `https://example.com/fhir/PlanDefinition/123/_history/4`

#### 3.3 Validation Criteria

1. **HTTP Status Code:** The server MUST return a **200 (OK)** HTTP status code if the vread interaction is successful.
2. **Resource Type:** The returned resource MUST be of the same type as the requested resource type.
3. **Resource Content:** 
    - The returned resource MUST represent the state of the resource at the specified version.
    - All required elements for the resource type and profile MUST be present and populated with valid data.
4. **ETag Header:** The response MUST include an ETag header containing the version specific ETag for the returned resource.

#### 3.4 Example Test Case

**Resource Type:** PlanDefinition
**Resource ID:** 123
**Version ID:** 4

**Request:**

```
GET https://example.com/fhir/PlanDefinition/123/_history/4
```

**Expected Response:**

```
HTTP/1.1 200 OK
Content-Type: application/fhir+json
ETag: W/"4"

{
  "resourceType": "PlanDefinition",
  "id": "123",
  "meta": {
    "versionId": "4",
    // ... other metadata elements
  },
  // ... other PlanDefinition resource content
}
```

**Assertions:**

- Verify the HTTP status code is 200 (OK).
- Verify the returned resource type is "PlanDefinition".
- Verify the content of the returned resource matches the expected content for version 4 of the PlanDefinition with ID 123.
- Verify the ETag header is present and contains the expected version specific ETag. 


---

<a id='req-27'></a>

### REQ-27: Support for _includes

**Description**: "[For each resource] A Server SHALL be capable of supporting the following _includes [list]."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-27: Support for _includes

**1. Requirement ID:** REQ-27

**2. Requirement Analysis:**

   **- Testability Assessment:** Automatically Testable
   **- Complexity:** Moderate 
   **- Prerequisites:**
     - A running FHIR server that implements the target Implementation Guide.
     - A list of supported _includes from the Implementation Guide requirement.
     - Test resources available on the server that have the potential to return related resources via the supported _includes. 

**3. Test Implementation Strategy:**

   **- Required Inputs:**
     - **Resource Type:** The specific FHIR resource type to test (e.g., Patient, Observation).
     - **_include Parameter:** The specific _include parameter value to test (e.g., Patient:general-practitioner, Observation:patient).

   **- Required FHIR Operations:**
     - **READ:**  To retrieve the base resource (e.g., GET [base]/Patient/123).

   **- Validation Criteria:**
     1. **HTTP Status Code:** The server MUST return a 200 (OK) status code, indicating a successful read operation.
     2. **Resource Validation:** The returned resource(s) MUST be valid FHIR resources according to the specified FHIR version.
     3. **_include Content:** The response bundle SHOULD contain the related resources specified by the _include parameter.
        - **Example:** If the request is `GET [base]/Patient/123?_include=Patient:general-practitioner` and the patient resource has a general practitioner, the response bundle should include both the Patient resource and the related Practitioner resource.
     4. **CapabilityStatement Conformance:** Verify that the tested _includes are listed as supported in the server's CapabilityStatement.

**Example Test Case:**

**Test Case ID:** TC_REQ-27_Patient_GeneralPractitioner

**Description:** Verify that the server supports the `_include=Patient:general-practitioner` parameter when retrieving a Patient resource.

**Steps:**

1. **Send a READ request:** `GET [base]/Patient/123?_include=Patient:general-practitioner`
2. **Verify the HTTP status code is 200 (OK).**
3. **Validate the returned resource is a valid FHIR Bundle.**
4. **Verify the bundle contains the requested Patient resource.**
5. **Verify the bundle contains the related Practitioner resource linked through the `generalPractitioner` element of the Patient resource.**
6. **Check if `_include=Patient:general-practitioner` is listed as supported in the server's CapabilityStatement.**

**Expected Result:**  The test passes if all verification criteria are met.

**Notes:**

* This test specification provides a general framework. Specific test cases should be created for each supported _include defined in the Implementation Guide.
* Negative testing can also be performed to ensure the server handles invalid _include parameters gracefully. 
* Automated testing tools can be used to streamline the execution and validation of these tests. 


---

<a id='req-28'></a>

### REQ-28: Support for _revincludes

**Description**: "[For each resource] A Server SHALL be capable of supporting the following _revincludes: [list]."

**Actor**: Server

**Conformance**: SHALL

## Test Specification for REQ-28: Support for _revincludes

### 1. Requirement ID

REQ-28

### 2. Requirement Analysis

- **Testability Assessment:** Automatically Testable
- **Complexity:** Moderate
- **Prerequisites:**
    - A running FHIR server that implements the target Implementation Guide.
    - A list of supported resources from the CapabilityStatement.
    - The specific list of _revincludes stated in the "Description" section of REQ-28.

### 3. Test Implementation Strategy

This test specification will iterate through each supported resource and its defined _revincludes, constructing and executing search requests.

#### 3.1 Required Inputs

- **CapabilityStatement:** The server's CapabilityStatement to identify supported resources and their interactions.
- **Resource List:** A list of resources supported by the server, extracted from the CapabilityStatement.
- **_revincludes List:** The specific list of _revincludes required by REQ-28 for each resource.

#### 3.2 Required FHIR Operations

- **read (GET):** To retrieve the CapabilityStatement.
- **search (GET):** To execute search operations on each resource type with the specified _revincludes.

#### 3.3 Validation Criteria

For each supported resource and its defined _revincludes:

1. **Successful Response:** Verify that the server returns a successful HTTP status code (2xx) for the search request.
2. **Valid Bundle:** Verify that the response body is a valid FHIR Bundle resource.
3. **Included Resources:** Verify that the Bundle includes resources matching the specified _revincludes. This can be achieved by:
    - Checking the `type` of included resources against the expected _revincludes.
    - Verifying the presence and correctness of references between the primary resource(s) and the included resources.
4. **Error Handling:** If a specified _revinclude is not supported for a particular resource, verify that the server:
    - Returns a successful HTTP status code (2xx).
    - Does not include resources of the unsupported _revincludes type in the Bundle.
    - Optionally, includes an OperationOutcome resource in the Bundle with an appropriate warning message indicating the unsupported _revincludes.

**Example:**

If REQ-28 specifies that the `Patient` resource SHALL support the `_revinclude=Provenance:target` _revinclude, the test would:

1. Construct a search request for `Patient` resources, including the `_revinclude=Provenance:target` parameter.
2. Verify that the server returns a 2xx status code.
3. Verify that the response is a valid Bundle.
4. Verify that the Bundle includes any Provenance resources referenced as `target` by the returned Patient resources.

This process would be repeated for each supported resource and its defined _revincludes. 


---

<a id='req-29'></a>

### REQ-29: Network profile NPI handling

**Description**: "The NPI and CLIA identifier types, which are Must-Support, are clearly intended for provider organizations only and are not expected to be populated for other organization types."

**Actor**: Server

**Conformance**: None (Clarification)

## Test Specification for REQ-29: Network profile NPI handling

**1. Requirement ID:** REQ-29

**2. Requirement Analysis:**

   - **Testability Assessment:**  Attestation (The requirement is a clarification of intent and cannot be directly tested against the CapabilityStatement.)
   - **Complexity:** Simple
   - **Prerequisites:** None

**3. Test Implementation Strategy:**

   - **Required inputs:** 
     - FHIR CapabilityStatement of the server under test.
   - **Required FHIR Operations:** None
   - **Validation Criteria:** 
     - **Attestation:** The implementer MUST attest that NPI and CLIA identifiers are ONLY populated for provider organization resources and NOT for other organization types. This attestation should be documented and provided as part of the implementation guide conformance statement.

**Rationale:**

This requirement focuses on clarifying the intended use of NPI and CLIA identifiers within the specific implementation guide context. It is not a testable assertion against the server's capabilities but rather a constraint on how those capabilities are utilized when creating resources. 

Directly testing this requirement would necessitate creating various organization resources with different identifier types and then validating if the server rejects those not adhering to the rule. However, this approach is flawed:

* **CapabilityStatement Limitation:** The CapabilityStatement doesn't provide granularity to express such specific data element constraints within different resource types.
* **Potential Overlap:** Enforcing this rule likely falls under the purview of the server's internal validation logic or profile validation against the implementation guide's specific Organization profile, which is outside the scope of basic CapabilityStatement testing.

Therefore, an attestation from the implementer confirming their adherence to this data population constraint is the most appropriate and practical approach for this requirement. 


---

<a id='req-30'></a>

### REQ-30: lastUpdate timestamp requirement

**Description**: "Each profile in this guide requires that the lastUpdate timestamp be provided as part of the profile's data content."

**Actor**: Server

**Conformance**: None (Requirement)

## Test Specification for REQ-30: lastUpdate Timestamp Requirement

### 1. Requirement ID

REQ-30

### 2. Requirement Analysis

- **Testability Assessment:** Automatically Testable
- **Complexity:** Simple
- **Prerequisites:**
    - A list of all FHIR profiles defined in the Implementation Guide.
    - Access to an instance of the FHIR server under test.

### 3. Test Implementation Strategy

#### 3.1 Test Case 1: Verify lastUpdate Presence

This test case verifies that the `lastUpdate` element is present in all resources conforming to the profiles defined in the Implementation Guide.

**3.1.1 Required Inputs:**

- **FHIR Resources:** Any resource instance conforming to a profile defined in the Implementation Guide.

**3.1.2 Required FHIR Operations:**

- **READ:** Retrieve resource instances of various profiles defined in the Implementation Guide.

**3.1.3 Validation Criteria:**

- **Assertion:** The returned resource instance MUST contain a non-empty `lastUpdate` element.

#### 3.2 Test Case 2: Verify lastUpdate Data Type

This test case verifies that the `lastUpdate` element conforms to the FHIR data type specification.

**3.2.1 Required Inputs:**

- **FHIR Resources:** Any resource instance conforming to a profile defined in the Implementation Guide.

**3.2.2 Required FHIR Operations:**

- **READ:** Retrieve resource instances of various profiles defined in the Implementation Guide.

**3.2.3 Validation Criteria:**

- **Assertion:** The `lastUpdate` element MUST conform to the `instant` data type as defined in the FHIR specification. This includes:
    - The value MUST be a valid date and time representation in the format YYYY-MM-DDThh:mm:ss.sss+zz:zz.
    - The timezone offset MUST be present and valid.

#### 3.3 Test Automation Considerations

- These test cases can be easily automated using a testing framework like Jest, Mocha, or pytest.
- A test script can be written to:
    - Iterate through the list of profiles defined in the Implementation Guide.
    - For each profile, retrieve a sample resource instance from the FHIR server.
    - Validate the presence and data type of the `lastUpdate` element in the retrieved resource.
- The test script should include assertions to verify the expected behavior and report any failures.

**Note:** This test specification focuses on the technical aspects of the requirement. Additional tests might be necessary to cover specific business rules or edge cases related to the `lastUpdate` timestamp. 


---

<a id='req-32'></a>

### REQ-32: General Search for Pharmacy

**Description**: "The Plan-Net design is based around the following types of searches: General Search - Example: Pharmacy - Focal Resource and Field: HealthcareService.category, HealthcareService.specialty - Qualifications of Search: Location, network."

**Actor**: Server

**Conformance**: None (Design requirement)

## Test Specification

### 1. Requirement ID

REQ-32

### 2. Requirement Analysis

**Testability Assessment:** Automatically Testable

**Complexity:** Moderate

**Prerequisites:**

- A FHIR server instance with the Plan-Net implementation.
- The server should be populated with at least one HealthcareService resource representing a Pharmacy.
- The Pharmacy HealthcareService resource should have at least one associated Location resource.
- The Location resource should have data populated for the search parameters used in the test cases.

### 3. Test Implementation Strategy

#### Test Case 1: Search for Pharmacy by Service Category and Location

**Required Inputs:**

- **FHIR Resource:** None (search operation)
- **Search Parameters:**
    - `service-category`: `http://terminology.hl7.org/CodeSystem/service-category|pharmacy`
    - `location`: (Logical ID of a Location resource associated with a Pharmacy HealthcareService)
- **Expected Output:**
    - HTTP Status Code: 200 (OK)
    - Bundle Type: searchset
    - Bundle Contains: At least one HealthcareService resource with `category` matching the search parameter and associated with the specified `location`.

**Required FHIR Operations:**

- `GET /HealthcareService?service-category=http://terminology.hl7.org/CodeSystem/service-category|pharmacy&location=[Location-Logical-ID]`

**Validation Criteria:**

- Verify the HTTP status code is 200 (OK).
- Verify the returned resource is a Bundle with type 'searchset'.
- Verify the Bundle contains at least one HealthcareService resource.
- Verify the `category` element in the returned HealthcareService resource matches the search parameter.
- Verify the returned HealthcareService resource is associated with the specified `location` through the `location` reference.

#### Test Case 2: Search for Pharmacy by Specialty and Location (Network simulation)

**Required Inputs:**

- **FHIR Resource:** None (search operation)
- **Search Parameters:**
    - `specialty`: (Code from a relevant ValueSet representing a Pharmacy specialty)
    - `location-address`: (Partial or complete address information of the Location associated with a Pharmacy HealthcareService)
- **Expected Output:**
    - HTTP Status Code: 200 (OK)
    - Bundle Type: searchset
    - Bundle Contains: At least one HealthcareService resource with `specialty` matching the search parameter and associated with a Location matching the provided address information.

**Required FHIR Operations:**

- `GET /HealthcareService?specialty=[Specialty-Code]&location-address=[Location-Address-Information]`

**Validation Criteria:**

- Verify the HTTP status code is 200 (OK).
- Verify the returned resource is a Bundle with type 'searchset'.
- Verify the Bundle contains at least one HealthcareService resource.
- Verify the `specialty` element in the returned HealthcareService resource matches the search parameter.
- Verify the returned HealthcareService resource is associated with a Location that matches the provided address information through the `location` reference and corresponding Location resource.

**Note:** These test cases demonstrate searching for Pharmacy resources using a combination of service category/specialty and location parameters. The specific codes and values used in the search parameters should be aligned with the Plan-Net implementation and the data populated in the FHIR server. 


---

<a id='req-33'></a>

### REQ-33: Provider search by name

**Description**: "The Plan-Net design is based around the following types of searches: Provider by Name - Example: Joe Smith - Focal Resource and Field: Practitioner.name - Qualifications of Search: Location, network, specialty, role/privileges."

**Actor**: Server

**Conformance**: None (Design requirement)

## Test Specification

### 1. Requirement ID

REQ-33: Provider search by name

### 2. Requirement Analysis

* **Testability Assessment:** Automatically Testable
* **Complexity:** Moderate
* **Prerequisites:**
    * A FHIR server instance is running and accessible.
    * The server has Practitioner resources loaded with at least one practitioner having a name matching the search criteria.
    * The server has Location resources loaded, potentially linked to Practitioners.

### 3. Test Implementation Strategy

#### 3.1 Required Inputs

* **Search String:** "Joe Smith" (or any other test name)

#### 3.2 Required FHIR Operations

* **Search Practitioner Resource:** `GET [base]/Practitioner?name=[search string]`
* **Optional - Search Location Resource:** `GET [base]/Location?[search parameters]` (if location filtering is included in the test case)

#### 3.3 Validation Criteria

1. **HTTP Status Code:** The server SHALL return a status code of 200 (OK) for a successful search.
2. **Resource Type:** The response SHALL be a Bundle with a type of 'searchset'.
3. **Resource Content:** 
    * The Bundle SHALL contain at least one Practitioner resource where the `name` element matches the provided search string (e.g., "Joe Smith").
    * **Optional:** If location, network, specialty, or role/privileges are included in the search criteria, the returned Practitioner resources SHALL match those criteria as well. This will require additional search parameters on the Practitioner search or subsequent filtering of results. 
4. **Capability Conformance:** Verify that the server's CapabilityStatement correctly advertises support for the `name` search parameter on the Practitioner resource and any other used search parameters.

**Example Test Cases:**

* **Test Case 1: Simple Name Search**
    * Input: "Joe Smith"
    * Expected Output: Bundle with at least one Practitioner resource where name matches "Joe Smith".
* **Test Case 2: Name Search with Location Filtering**
    * Input: "Joe Smith", "New York" (city)
    * Expected Output: Bundle with at least one Practitioner resource where name matches "Joe Smith" AND the practitioner is associated with a location in "New York". This might involve additional logic to check Location resources linked to the returned Practitioners. 

**Note:** This test specification provides a framework. Specific test cases should be developed to cover various search scenarios and edge cases, including different name formats, partial matches, and combinations of search criteria. 


---

<a id='req-34'></a>

### REQ-34: Organization search by name

**Description**: "The Plan-Net design is based around the following types of searches: Organization by Name - Example: Montgomery Cardiology or CVS - Focal Resource and Field: Organization.name - Qualifications of Search: Location, network, specialty."

**Actor**: Server

**Conformance**: None (Design requirement)

## Test Specification

### 1. Requirement ID

REQ-34: Organization search by name

### 2. Requirement Analysis

- **Testability Assessment:** Automatically Testable
- **Complexity:** Simple
- **Prerequisites:** 
    - A FHIR server instance is running and accessible.
    - The FHIR server has Organization resources loaded.
    - At least one Organization resource has a 'name' element populated.

### 3. Test Implementation Strategy

#### 3.1 Required Inputs

- **FHIR Resource:** N/A (Test will search existing resources)
- **Search Parameters:**
    - `name`:  A string representing the name or partial name of an organization (e.g., "Montgomery Cardiology", "CVS").

#### 3.2 Required FHIR Operations

- **HTTP GET Request:**  Search for Organization resources using the `name` search parameter.
    - Example: `GET [base]/Organization?name=[search-string]`

#### 3.3 Validation Criteria

1. **HTTP Status Code:** The server SHALL return a `200 OK` status code if the search is successful.
2. **Resource Type:** The response SHALL be a Bundle with a type of `searchset`.
3. **Search Results:** The Bundle SHALL contain only `Organization` resources that match the provided `name` search parameter.
4. **Partial Match:** The server SHOULD support partial name matching (e.g., searching for "Cardiology" returns "Montgomery Cardiology").
5. **Case-Insensitivity:** The search SHOULD be case-insensitive (e.g., searching for "montgomery" returns "Montgomery Cardiology").

**Additional Considerations:**

- The test cases should include a variety of search strings, including full names, partial names, and names with different capitalization to ensure comprehensive coverage.
- The test cases should also include searches that are expected to return no results to verify that the server correctly handles empty search results.
- While not explicitly stated in the requirement, consider adding test cases to verify the functionality of combining the `name` search parameter with other supported search parameters like `address`, `type`, or `coverage-area` to ensure they function as expected in combination. 


---

<a id='req-35'></a>

### REQ-35: Provider search by specialty

**Description**: "The Plan-Net design is based around the following types of searches: Provider by Specialty - Example: Cardiologist - Focal Resource and Field: PractitionerRole.specialty - Qualifications of Search: Location, network, name."

**Actor**: Server

**Conformance**: None (Design requirement)

## Test Specification

### 1. Requirement ID

REQ-35

### 2. Requirement Analysis

**Testability Assessment:** Automatically Testable

**Complexity:** Moderate

**Prerequisites:**

* The FHIR server must have Practitioner, PractitionerRole, and Location resources populated with data that includes specialties, locations, and network information.
* The test client must be able to send search requests to the FHIR server and interpret the responses.

### 3. Test Implementation Strategy

#### 3.1 Test Case 1: Search by Specialty Only

**Description:** This test case verifies that the system can successfully search for PractitionerRoles by specialty.

**Required Inputs:**

* **FHIR Resource:** N/A
* **Search Parameters:**
    * `specialty`: {system}|{code} (e.g.,  http://hl7.org/fhir/us/core/ValueSet/us-core-provider-taxonomy|2084P0803X)

**Required FHIR Operations:**

* `GET [base]/PractitionerRole?specialty={system}|{code}`

**Validation Criteria:**

* **Response Code:** 200 OK
* **Response Body:**
    * The response bundle SHOULD contain only PractitionerRole resources that match the specified specialty.
    * The response bundle SHOULD include the total number of matching PractitionerRoles.

#### 3.2 Test Case 2: Search by Specialty and Location

**Description:** This test case verifies that the system can successfully search for PractitionerRoles by specialty and location.

**Required Inputs:**

* **FHIR Resource:** N/A
* **Search Parameters:**
    * `specialty`: {system}|{code}
    * `location`: {Location resource ID} 

**Required FHIR Operations:**

* `GET [base]/PractitionerRole?specialty={system}|{code}&location={Location resource ID}`

**Validation Criteria:**

* **Response Code:** 200 OK
* **Response Body:**
    * The response bundle SHOULD contain only PractitionerRole resources that match the specified specialty and location.
    * The response bundle SHOULD include the total number of matching PractitionerRoles.

#### 3.3 Test Case 3: Search by Specialty and Network

**Description:** This test case verifies that the system can successfully search for PractitionerRoles by specialty and network.

**Required Inputs:**

* **FHIR Resource:** N/A
* **Search Parameters:**
    * `specialty`: {system}|{code}
    * `network`: {Organization resource ID} 

**Required FHIR Operations:**

* `GET [base]/PractitionerRole?specialty={system}|{code}&network={Organization resource ID}`

**Validation Criteria:**

* **Response Code:** 200 OK
* **Response Body:**
    * The response bundle SHOULD contain only PractitionerRole resources that match the specified specialty and network.
    * The response bundle SHOULD include the total number of matching PractitionerRoles.

#### 3.4 Test Case 4: Search by Specialty and Name

**Description:** This test case verifies that the system can successfully search for PractitionerRoles by specialty and practitioner name.

**Required Inputs:**

* **FHIR Resource:** N/A
* **Search Parameters:**
    * `specialty`: {system}|{code}
    * `practitioner:name`: {Practitioner name} 

**Required FHIR Operations:**

* `GET [base]/PractitionerRole?specialty={system}|{code}&practitioner:name={Practitioner name}`

**Validation Criteria:**

* **Response Code:** 200 OK
* **Response Body:**
    * The response bundle SHOULD contain only PractitionerRole resources that match the specified specialty and practitioner name.
    * The response bundle SHOULD include the total number of matching PractitionerRoles.

**Note:** This test specification assumes that "name" in the requirement refers to the practitioner's name. If it refers to another field, the test case should be adjusted accordingly. 


---

<a id='req-36'></a>

### REQ-36: Organization search by specialty

**Description**: "The Plan-Net design is based around the following types of searches: Organization by specialty - Example: Compounding Pharmacy - Focal Resource and Field: OrganizationAffiliation.specialty - Qualifications of Search: Location, network, name."

**Actor**: Server

**Conformance**: None (Design requirement)

## Test Specification

### 1. Requirement ID

REQ-36

### 2. Requirement Analysis

**Testability Assessment:** Automatically Testable

**Complexity:** Moderate

**Prerequisites:**

* The FHIR server must have Organization, OrganizationAffiliation, and Location resources populated with data representing various specialties, locations, and networks.
* At least one Organization should have an OrganizationAffiliation with the specialty "Compounding Pharmacy."

### 3. Test Implementation Strategy

#### 3.1 Test Case 1: Search for Organizations by Specialty

**Test Objective:** Verify that the system can successfully search for Organizations by the `specialty` search parameter on the OrganizationAffiliation resource.

**Required Inputs:**

* **FHIR Operation:** GET `/OrganizationAffiliation?specialty=http://terminology.hl7.org/CodeSystem/c80-practice-codes|3336F004` (assuming "Compounding Pharmacy" maps to this code)

**Expected Outputs:**

* **HTTP Status Code:** 200 (OK)
* **Response Body:** A Bundle resource containing a list of OrganizationAffiliation resources where the `specialty` field matches the search criteria ("Compounding Pharmacy").
* **Validation Criteria:**
    * The Bundle should contain at least one entry.
    * Each entry in the Bundle should be an OrganizationAffiliation resource.
    * The `specialty` field in each OrganizationAffiliation resource should match the search criteria.

#### 3.2 Test Case 2: Search for Organizations by Specialty with Location

**Test Objective:** Verify that the system can successfully search for Organizations by `specialty` and `location` search parameters.

**Required Inputs:**

* **FHIR Operation:** GET `/OrganizationAffiliation?specialty=http://terminology.hl7.org/CodeSystem/c80-practice-codes|3336F004&location=[Location-ID]` (replace `[Location-ID]` with the actual Location resource ID)

**Expected Outputs:**

* **HTTP Status Code:** 200 (OK)
* **Response Body:** A Bundle resource containing a list of OrganizationAffiliation resources matching the search criteria.
* **Validation Criteria:**
    * The Bundle should contain only entries that match both the `specialty` and `location` criteria.

#### 3.3 Test Case 3: Search for Organizations by Specialty with Network

**Test Objective:** Verify that the system can successfully search for Organizations by `specialty` and `network` search parameters.

**Required Inputs:**

* **FHIR Operation:** GET `/OrganizationAffiliation?specialty=http://terminology.hl7.org/CodeSystem/c80-practice-codes|3336F004&network=[Network-ID]` (replace `[Network-ID]` with the actual Organization resource ID representing the network)

**Expected Outputs:**

* **HTTP Status Code:** 200 (OK)
* **Response Body:** A Bundle resource containing a list of OrganizationAffiliation resources matching the search criteria.
* **Validation Criteria:**
    * The Bundle should contain only entries that match both the `specialty` and `network` criteria.

#### 3.4 Test Case 4: Search for Organizations by Specialty with Name

**Test Objective:** Verify that the system can successfully search for Organizations by `specialty` and the organization's `name` search parameter.

**Required Inputs:**

* **FHIR Operation:** 
    1. GET `/OrganizationAffiliation?specialty=http://terminology.hl7.org/CodeSystem/c80-practice-codes|3336F004` 
    2. Extract the `participating-organization` reference from each returned OrganizationAffiliation resource.
    3. For each extracted reference, perform a GET request to `/Organization?name=[Organization-Name]` (replace `[Organization-Name]` with the display value from the extracted reference).

**Expected Outputs:**

* **HTTP Status Code:** 200 (OK) for all requests.
* **Response Body:** 
    * For the first request, a Bundle resource containing a list of OrganizationAffiliation resources matching the `specialty` criteria.
    * For subsequent requests, an Organization resource matching the provided `name`.
* **Validation Criteria:**
    * The final set of Organization resources should only include those that have an OrganizationAffiliation with the specified `specialty` and match the provided `name`.

**Note:** These test cases assume that the system uses a standard code system for specialties. If a custom code system is used, the test cases will need to be updated accordingly. 


---

<a id='req-37'></a>

### REQ-37: Search for active practitioners and organizations

**Description**: "Sample query to search for currently active Practitioners (replace date in query with current date): http://davinci-plan-net-ri.logicahealth.org/fhir/PractitionerRole?_include=PractitionerRole:date=ge2021-10-25. Sample query to search for currently active Organizations (replace date in query with current date): http://davinci-plan-net-ri.logicahealth.org/fhir/OrganizationAffiliation?_include=OrganizationAffiliation:date=ge2021-10-25."

**Actor**: Server

**Conformance**: None (Implementation example)

## Test Specification

### 1. Requirement ID

REQ-37: Search for active practitioners and organizations

### 2. Requirement Analysis

**Testability Assessment**: Automatically Testable

**Complexity**: Moderate

**Prerequisites**:

* The FHIR server must be populated with at least one Practitioner and one Organization resource, each with at least one associated PractitionerRole and OrganizationAffiliation resource respectively.
* The PractitionerRole and OrganizationAffiliation resources must have a `date` element populated with a date in the past. 

### 3. Test Implementation Strategy

#### 3.1 Test Case 1: Search for Active Practitioners

**Required Inputs**:

* **FHIR Operation**: GET 
* **Resource**: PractitionerRole
* **Search Parameters**:
    * `_include=PractitionerRole:date`:  Include the Practitioner resource referenced in the `practitioner` element of the PractitionerRole.
    * `date=ge[CurrentDate]`:  Filter for PractitionerRoles with a `date` element greater than or equal to the current date.

**Expected Outputs**:

* **HTTP Status Code**: 200 (OK)
* **Response Body**: A Bundle resource containing PractitionerRole resources that meet the search criteria.
* **Validation Criteria**:
    * The Bundle should contain only PractitionerRole resources where the `date` element is greater than or equal to the current date.
    * Each returned PractitionerRole resource should include the associated Practitioner resource as specified by the `_include` parameter.

#### 3.2 Test Case 2: Search for Active Organizations

**Required Inputs**:

* **FHIR Operation**: GET
* **Resource**: OrganizationAffiliation
* **Search Parameters**:
    * `_include=OrganizationAffiliation:date`: Include the Organization resource referenced in the `participating-organization` element of the OrganizationAffiliation.
    * `date=ge[CurrentDate]`: Filter for OrganizationAffiliations with a `date` element greater than or equal to the current date.

**Expected Outputs**:

* **HTTP Status Code**: 200 (OK)
* **Response Body**: A Bundle resource containing OrganizationAffiliation resources that meet the search criteria.
* **Validation Criteria**:
    * The Bundle should contain only OrganizationAffiliation resources where the `date` element is greater than or equal to the current date.
    * Each returned OrganizationAffiliation resource should include the associated Organization resource as specified by the `_include` parameter.

**Notes**:

* The `[CurrentDate]` in the search parameters should be replaced with the actual current date in YYYY-MM-DD format at the time of test execution.
* These test cases assume that the `date` element in both PractitionerRole and OrganizationAffiliation resources represents the active period. If a different element is used to determine active status, the test cases need to be adjusted accordingly. 
* The Capability Statement confirms the server supports the required search parameters for both PractitionerRole and OrganizationAffiliation resources. 


---

<a id='req-38'></a>

### REQ-38: Network contact handling for departments

**Description**: "When the contact is a department name, rather than a human (e.g., patient help line), include a blank family and given name, and provide the department name in contact.name.text."

**Actor**: Server

**Conformance**: None (Implementation guidance)

## Test Specification for REQ-38: Network Contact Handling for Departments

### 1. Requirement ID

REQ-38

### 2. Requirement Analysis

* **Testability Assessment:** Automatically Testable
* **Complexity:** Simple
* **Prerequisites:**
    * The system under test must support the creation and retrieval of `Organization` resources with `Contact` components.
    * The Capability Statement must indicate support for `create` and `read` operations on the `Organization` resource.

### 3. Test Implementation Strategy

#### 3.1 Test Case 1: Create Organization with Department Contact

**Objective:** Verify that the system correctly handles the creation of an `Organization` resource where a contact represents a department, with a blank family and given name, and the department name in `contact.name.text`.

**Inputs:**

* **FHIR Resource:** `Organization`
    ```json
    {
      "resourceType": "Organization",
      "name": "Test Hospital",
      "contact": [
        {
          "purpose": {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/contactentity-type",
                "code": "ADMIN"
              }
            ]
          },
          "name": {
            "text": "Patient Help Line"
          },
          "telecom": [
            {
              "system": "phone",
              "value": "555-123-4567"
            }
          ]
        }
      ]
    }
    ```

**Operations:**

1. `POST` the `Organization` resource to the `/Organization` endpoint.

**Validation Criteria:**

1. **Response Code:** The server should return a `201 Created` HTTP status code.
2. **Resource Retrieval:** Retrieve the created `Organization` resource using the returned `Location` header.
3. **Data Validation:** Verify the following:
    * The `contact.name.text` element contains the value "Patient Help Line".
    * The `contact.name.family` and `contact.name.given` elements are absent or empty.

#### 3.2 Test Case 2: Retrieve Organization with Department Contact

**Objective:** Verify that the system correctly returns an `Organization` resource where a contact represents a department, with a blank family and given name, and the department name in `contact.name.text`.

**Inputs:**

* **Organization ID:** The ID of an existing `Organization` resource containing a department contact as defined in Test Case 1.

**Operations:**

1. `GET` the `Organization` resource using the ID: `/Organization/{id}`.

**Validation Criteria:**

1. **Response Code:** The server should return a `200 OK` HTTP status code.
2. **Data Validation:** Verify the following:
    * The `contact.name.text` element contains the expected department name.
    * The `contact.name.family` and `contact.name.given` elements are absent or empty.

**Note:** These test cases assume that the Capability Statement confirms the server's ability to handle the required FHIR resources and operations. 


---

<a id='req-39'></a>

### REQ-39: Organization contact handling for departments

**Description**: "When the contact is a department name, rather than a human (e.g., patient help line), include a blank family and given name, and provide the department name in contact.name.text."

**Actor**: Server

**Conformance**: None (Implementation guidance)

## Test Specification for REQ-39: Organization Contact Handling for Departments

**1. Requirement ID:** REQ-39

**2. Requirement Analysis:**

   - **Testability Assessment:** Automatically Testable
   - **Complexity:** Simple
   - **Prerequisites:**
     - A FHIR server instance capable of handling Organization resources and supporting the required search parameters.
     - Test data: An Organization resource with a contact element representing a department.

**3. Test Implementation Strategy:**

   **3.1. Required Inputs:**

   **3.1.1. FHIR Resource:**

   ```json
   {
     "resourceType": "Organization",
     "id": "test-org-dept-contact",
     "name": "Test Hospital",
     "contact": [
       {
         "purpose": {
           "coding": [
             {
               "system": "http://terminology.hl7.org/CodeSystem/contactentity-type",
               "code": "ADMIN",
               "display": "Administrative"
             }
           ]
         },
         "name": {
           "text": "Patient Help Line"
         },
         "telecom": [
           {
             "system": "phone",
             "value": "555-555-1212"
           }
         ]
       }
     ]
   }
   ```

   **3.1.2. Expected Output:**

   A successful response (HTTP 200 OK) with the created Organization resource containing the department contact information as specified in the requirement:

   ```json
   {
     "resourceType": "Organization",
     "id": "test-org-dept-contact",
     "name": "Test Hospital",
     "contact": [
       {
         "purpose": {
           "coding": [
             {
               "system": "http://terminology.hl7.org/CodeSystem/contactentity-type",
               "code": "ADMIN",
               "display": "Administrative"
             }
           ]
         },
         "name": {
           "text": "Patient Help Line"
         },
         "telecom": [
           {
             "system": "phone",
             "value": "555-555-1212"
           }
         ]
       }
     ]
   }
   ```

   **3.2. Required FHIR Operations:**

   1. **Create:** Send a POST request to the `/Organization` endpoint with the test Organization resource as the payload.

   2. **Read:** Send a GET request to the `/Organization/{id}` endpoint, replacing `{id}` with the ID of the created Organization resource.

   **3.3. Validation Criteria:**

   1. **Response Status Code:** Verify that the response status code for both the Create and Read operations is 200 OK.

   2. **Contact Information:** Verify that the returned Organization resource in the Read response contains the contact element with the following:
      - `name.text` is populated with the department name ("Patient Help Line" in this example).
      - `name.family` and `name.given` are absent or empty. 
      - Other contact details like `purpose` and `telecom` are populated as needed.

   **3.4. Test Steps:**

   1. **Setup:** Ensure the FHIR server is running and accessible.
   2. **Execute:** Perform the Create operation to create the Organization resource with the department contact.
   3. **Verify:** 
      - Check the response status code of the Create operation (should be 200 OK).
      - Extract the ID of the created resource from the response.
   4. **Execute:** Perform the Read operation using the extracted ID.
   5. **Verify:**
      - Check the response status code of the Read operation (should be 200 OK).
      - Validate the contact information within the returned Organization resource against the expected output.

   **3.5. Notes:**

   - This test case focuses on the specific requirement of handling department names in the contact element. 
   - Additional test cases can be created to cover different contact types, purposes, and variations in data. 
   - This test leverages the Capability Statement information to ensure the required search parameters are supported, but it does not explicitly test them. Separate tests can be designed for that purpose. 


---

<a id='req-40'></a>

### REQ-40: Practitioner qualification coding

**Description**: "When the value set for the coded concept in qualification is insufficient, the qualification can be provided in the text field of the codeableConcept."

**Actor**: Server

**Conformance**: None (Implementation guidance)

## Test Specification for REQ-40: Practitioner qualification coding

### 1. Requirement ID

REQ-40

### 2. Requirement Analysis

**Testability Assessment:**  Attestation (partially testable)

**Rationale:** While we can automatically test if a Practitioner resource allows both coded and text representations within the `qualification.code` field, determining if the text field is used "when the value set is insufficient" requires human judgment. 

**Complexity:** Moderate

**Prerequisites:**

* A FHIR server capable of handling Practitioner resources.
* At least one pre-loaded Practitioner resource with a `qualification` element. This resource should ideally have a case where the coded concept is deemed "insufficient" and the text field is used to provide additional qualification information.

### 3. Test Implementation Strategy

#### 3.1 Required Inputs

* **FHIR Resource:** Practitioner resource with at least one `qualification` element.
    * **Scenario 1:** `qualification.code` contains a code from a value set, and the `qualification.text` is empty.
    * **Scenario 2:** `qualification.code` contains a code from a value set, and the `qualification.text` provides additional information because the coded concept alone is not sufficient.

#### 3.2 Required FHIR Operations

* **Read Operation:** Retrieve the Practitioner resource using the `GET /Practitioner/[id]` operation (supported based on Capability Statement).

#### 3.3 Validation Criteria

**Automated Tests:**

1. **Structure Validation:** Validate the Practitioner resource conforms to the FHIR specification and any applicable profiles using a FHIR validator.
2. **Codeable Concept Structure:** Verify that the `qualification.code` element allows both `coding` and `text` fields as per the FHIR data type definition.

**Manual Inspection (Attestation):**

1. **Scenario 1:**  Verify that when `qualification.code` is sufficient, the `qualification.text` field is appropriately left empty.
2. **Scenario 2:** Examine the Practitioner resource instances where `qualification.text` is used. Assess:
    * **Justification:** Is there clear evidence within the data or context that the coded concept alone was insufficient, justifying the use of the text field?
    * **Clarity and Completeness:** Is the information provided in the `qualification.text` field clear, concise, and sufficient to supplement the coded concept?

**Passing Criteria:**

* All automated tests pass.
* Manual inspection confirms that the use of `qualification.text` aligns with the requirement, providing supplemental information only when the coded concept is insufficient.

**Notes:**

* This test specification focuses on the server's ability to handle and represent the data as specified by the requirement. It does not directly test the client's ability to interpret or utilize the information in the `qualification.text` field.
* Clear documentation and examples of "insufficient coded concepts" and appropriate use of the text field will be crucial for implementers and testers. 


---



