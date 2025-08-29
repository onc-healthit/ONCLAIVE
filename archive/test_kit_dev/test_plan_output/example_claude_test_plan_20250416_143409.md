# Consolidated Test Plan for Plan Net

## Generated on: 2025-04-16 14:34:35

## Capability Statement

This test plan incorporates constraints and requirements from the Plan Net Capability Statement.

## Table of Contents

- [Application-Level Requirements](#application-level-requirements)
  - [REQ-08: Must Support elements display](#req-08)
- [Authentication](#authentication)
  - [REQ-01: No authentication requirement](#req-01)
- [Base Requirements](#base-requirements)
  - [REQ-09: Missing Must Support interpretation](#req-09)
- [CORE Conformance](#core-conformance)
  - [REQ-07: Must Support elements processing](#req-07)
- [Cross-Resource](#cross-resource)
  - [REQ-06: Required Must Support elements handling](#req-06)
- [General Requirements](#general-requirements)
  - [REQ-04: Must Support elements population](#req-04)
- [Global](#global)
  - [REQ-05: Optional Must Support elements handling](#req-05)
- [OrganizationAffiliation](#organizationaffiliation)
  - [REQ-11: Network documentation for organizations](#req-11)
- [Plan-Net API Security](#plan-net-api-security)
  - [REQ-02: No consumer identification requirement](#req-02)
- [PractitionerRole](#practitionerrole)
  - [REQ-10: Network documentation for practitioners](#req-10)
- [Security](#security)
  - [REQ-03: No consumer information in queries](#req-03)

## Test Specifications

<a id='application-level-requirements'></a>

## Application-Level Requirements

<a id='req-08'></a>

### REQ-08: Must Support elements display

**Description**: "Application Actor SHOULD display Must Support data elements for human use or store for other purposes"

**Actor**: Application Actor

**Conformance**: SHOULD

# Test Specification for REQ-08

## 1. Requirement ID
REQ-08: Must Support Elements Display

## 2. Requirement Analysis

### Testability Assessment
- Semi-automated testable with manual verification components
- Requires both automated testing of Must Support element presence and manual verification of display/storage

### Complexity
Moderate

### Prerequisites
- Test system with Application Actor implementation
- Access to test data containing Must Support elements
- Documentation of all Must Support elements defined in the IG
- Sample FHIR resources containing Must Support elements
- Test client capable of making FHIR API calls
- System capable of displaying or storing FHIR data

## 3. Test Implementation Strategy

### Required Inputs
1. FHIR Resources:
   - Set of test resources containing all defined Must Support elements
   - Resources should be available in both XML and JSON formats (per Capability Statement)
   - Minimum one instance of each Must Support element type

### Required FHIR Operations
1. READ operations to retrieve test resources
2. SEARCH operations to query for resources containing Must Support elements

### Test Scenarios

#### Scenario 1: Display Verification
1. **Setup**:
   - Prepare test resources containing Must Support elements
   - Configure test client to access Application Actor system

2. **Test Steps**:
   ```
   a. Load test resources into Application Actor system
   b. For each Must Support element:
      - Retrieve resource containing the element
      - Verify element is accessible via UI or storage
      - Document display/storage method
   c. Test with both XML and JSON formats
   ```

3. **Validation Criteria**:
   - Must Support elements are accessible via UI or queryable in storage
   - Elements maintain semantic meaning when displayed/stored
   - System handles both XML and JSON formats appropriately

### Validation Assertions

1. Technical Validation:
   ```
   - All Must Support elements can be retrieved
   - No errors occur during processing
   - Data integrity is maintained
   ```

2. Display/Storage Validation:
   ```
   - Must Support elements are visible in UI or retrievable from storage
   - Elements are presented in human-readable format (if displayed)
   - Storage mechanism preserves all required data elements
   ```

3. Format Handling:
   ```
   - System properly handles XML format (SHOULD requirement)
   - System properly handles JSON format (implied default)
   ```

### Test Data Requirements
1. Sample Resources:
   ```
   - Minimum one instance of each Must Support element
   - Both valid and edge case scenarios
   - XML and JSON formatted versions
   ```

### Pass/Fail Criteria
- PASS: System successfully displays or stores all Must Support elements while maintaining data integrity
- PARTIAL PASS: System handles most Must Support elements but has minor display/storage issues
- FAIL: System fails to display or store Must Support elements appropriately

### Test Documentation Requirements
1. Record for each Must Support element:
   - Display method or storage location
   - Any display/storage limitations
   - Format handling capabilities
   - Screenshots or storage queries as evidence

---



<a id='authentication'></a>

## Authentication

<a id='req-01'></a>

### REQ-01: No authentication requirement

**Description**: "Health Plan API SHALL NOT require authentication for Plan-Net service access"

**Actor**: Health Plan API

**Conformance**: SHALL NOT

# Test Specification for REQ-01

## 1. Requirement ID
REQ-01: Health Plan API SHALL NOT require authentication for Plan-Net service access

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically Testable
- **Complexity**: Simple
- **Impact**: High (affects all API access)

### Prerequisites
- Health Plan API endpoint is available and operational
- Test environment with the ability to make HTTP requests without authentication credentials
- List of supported Plan-Net endpoints to test (e.g., Organization, Practitioner, PractitionerRole, etc.)

## 3. Test Implementation Strategy

### Required Inputs
- Base URL of the Health Plan API
- Set of Plan-Net resource endpoints to test
- Sample valid resource IDs for read operations

### Required FHIR Operations
Test the following FHIR interactions without authentication:
1. READ operations (GET {base}/[resource-type]/[id])
2. SEARCH operations (GET {base}/[resource-type]?[parameters])
3. Instance level operations if supported

### Test Cases

#### TC-01: Basic Unauthenticated Access
1. Execute GET requests without any authentication headers to:
   - `GET {base}/Organization`
   - `GET {base}/Practitioner`
   - `GET {base}/PractitionerRole`
   - `GET {base}/HealthcareService`
   - `GET {base}/Location`
   - `GET {base}/Network`

#### TC-02: XML Format Testing (SHOULD Support)
1. Execute GET requests with Accept header "application/fhir+xml" to test XML support:
   - `GET {base}/Organization` with `Accept: application/fhir+xml`

### Validation Criteria

#### Success Criteria
1. All requests without authentication should return:
   - HTTP Status Code 200 (OK) for successful requests
   - HTTP Status Code 404 for non-existent resources
   - No HTTP Status Code 401 (Unauthorized) or 403 (Forbidden)

2. Response headers should:
   - Not contain WWW-Authenticate header
   - Not redirect to authentication endpoints

#### Failure Criteria
The test fails if:
- Any Plan-Net endpoint returns 401 (Unauthorized) or 403 (Forbidden)
- System requires authentication tokens or credentials
- System redirects to authentication/login pages

### Test Data Requirements
- Minimum of one valid resource ID for each resource type
- List of valid search parameters for each resource type

### Implementation Notes
1. Test both valid and invalid resource IDs to ensure authentication is not required in either case
2. Document any endpoints that do require authentication (these would be non-conformant)
3. Consider testing with various HTTP methods (GET, POST, PUT, DELETE) to ensure consistent behavior
4. For XML support testing, verify proper content negotiation

### Limitations and Assumptions
1. Tests assume the API is operational and accessible
2. Network connectivity is available and stable
3. The API implements the required Plan-Net resources
4. Firewall and network security allow unauthenticated access

---



<a id='base-requirements'></a>

## Base Requirements

<a id='req-09'></a>

### REQ-09: Missing Must Support interpretation

**Description**: "Application Actor SHALL interpret missing Must Support data elements as data not present in Health Plan API system"

**Actor**: Application Actor

**Conformance**: SHALL

# Test Specification for REQ-09

## 1. Requirement ID
REQ-09: Missing Must Support interpretation

## 2. Requirement Analysis

### Testability Assessment
Semi-automatically testable - Requires both automated testing and manual verification of application behavior

### Complexity
Moderate - Involves testing multiple Must Support elements across different scenarios

### Prerequisites
- Application Actor implementation with UI or logging capability to verify interpretation of missing data
- Test environment with FHIR server supporting Plan-Net resources
- Sample resources with deliberately missing Must Support elements
- Documentation of all Must Support elements for relevant resources

## 3. Test Implementation Strategy

### Required Inputs
1. FHIR Resources:
   - Set of test resources with deliberately omitted Must Support elements
   - Corresponding complete resources with Must Support elements present
   - Must include both required and optional Must Support elements

### Required FHIR Operations
1. READ operations on resources containing Must Support elements
2. SEARCH operations returning resources with missing Must Support elements

### Test Scenarios

#### Scenario 1: Direct Resource Retrieval
1. Setup:
   - Configure test resources missing various Must Support elements
   - Document expected application behavior for each missing element

2. Test Steps:
   a. Perform READ operations on resources
   b. Verify application correctly interprets missing Must Support elements
   c. Compare behavior with complete resources

#### Scenario 2: Search Results Processing
1. Setup:
   - Configure search responses returning resources with missing Must Support elements
   
2. Test Steps:
   a. Execute search operations
   b. Verify application handling of missing elements in search results

### Validation Criteria

#### Automated Checks
1. Verify application does not generate errors when Must Support elements are missing
2. Confirm application can process resources with missing Must Support elements
3. Validate that application maintains functionality with incomplete data

#### Manual Verification
1. UI Display:
   - Verify appropriate display/handling of missing Must Support elements
   - Confirm no misleading default values are shown
   
2. Application Behavior:
   - Validate application continues normal operation
   - Ensure no incorrect assumptions about missing data

#### Documentation Requirements
1. Test report should include:
   - List of tested Must Support elements
   - Screenshot/logs showing application interpretation
   - Verification of consistent behavior across multiple resources

### Pass/Fail Criteria
- PASS: Application correctly interprets missing Must Support elements as "data not present"
- FAIL: Application:
  - Crashes or errors when Must Support elements are missing
  - Makes incorrect assumptions about missing data
  - Displays misleading default values
  - Fails to process resources with missing Must Support elements

### Additional Considerations
1. Test both xml and json formats (capability statement indicates xml support)
2. Include edge cases:
   - Resources with all Must Support elements missing
   - Resources with combination of present and missing Must Support elements
3. Consider impact on workflow and downstream processing

---



<a id='core-conformance'></a>

## CORE Conformance

<a id='req-07'></a>

### REQ-07: Must Support elements processing

**Description**: "Application Actor SHALL process resource instances containing Must Support data elements without errors or application failure"

**Actor**: Application Actor

**Conformance**: SHALL

# Test Specification: REQ-07

## 1. Requirement ID
REQ-07: Must Support Elements Processing

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically Testable
- **Rationale**: Can be tested through systematic resource submissions containing Must Support elements to verify system handling

### Complexity
- **Level**: Complex
- **Rationale**: Requires testing multiple resources and combinations of Must Support elements, including edge cases and boundary conditions

### Prerequisites
- Complete list of Must Support elements for all relevant resources in the IG
- Test system with Application Actor role configured
- Access to test environment with FHIR server endpoints
- Sample data sets containing Must Support elements
- Configuration to support XML format (based on Capability Statement)

## 3. Test Implementation Strategy

### Required Inputs
1. **Test Resources**:
   - Resource instances for each resource type defined in the IG
   - Each resource should contain:
     - All Must Support elements populated with valid data
     - Minimum Must Support elements populated
     - Maximum allowed Must Support elements populated
     - Must Support elements with boundary values

2. **Test Data Variations**:
   - Valid data within Must Support elements
   - Empty but present Must Support elements
   - Maximum length strings in Must Support elements
   - Special characters in Must Support text elements

### Required FHIR Operations
1. **CREATE Operations**:
   ```
   POST [base]/[resource-type]
   ```
2. **READ Operations**:
   ```
   GET [base]/[resource-type]/[id]
   ```
3. **SEARCH Operations**:
   ```
   GET [base]/[resource-type]?[must-support-element]=[value]
   ```

### Validation Criteria

#### Primary Success Criteria
1. System processes resources without errors when:
   - All Must Support elements are present and populated
   - Only required Must Support elements are present
   - Must Support elements contain maximum allowed values
   - Must Support elements contain special characters

#### Specific Test Cases

1. **Basic Processing Test**
   - Submit resource with all Must Support elements
   - Expected: 200 OK response, resource successfully processed

2. **Minimal Must Support Test**
   - Submit resource with only required Must Support elements
   - Expected: 200 OK response, resource successfully processed

3. **Maximum Values Test**
   - Submit resource with maximum allowed values in Must Support elements
   - Expected: 200 OK response, resource successfully processed

4. **Special Characters Test**
   - Submit resource with special characters in Must Support text elements
   - Expected: 200 OK response, resource successfully processed

5. **XML Format Test** (based on Capability Statement)
   - Submit resources in XML format
   - Expected: 200 OK response, resource successfully processed

#### Error Conditions to Test
1. System should not fail when:
   - Non-Must Support elements are missing
   - Must Support elements contain valid but unusual values
   - Must Support elements are present but empty (where allowed)

#### Test Pass/Fail Criteria
Test passes if:
1. All test cases execute without system errors or application failures
2. System returns appropriate HTTP status codes (200-range for success)
3. System successfully processes XML formatted resources
4. System maintains data integrity for Must Support elements
5. System can retrieve and display Must Support elements after processing

Test fails if:
1. System generates errors or crashes during processing
2. System fails to process valid Must Support elements
3. System cannot handle XML formatted resources
4. System loses or corrupts Must Support element data
5. System becomes unresponsive during processing

---



<a id='cross-resource'></a>

## Cross-Resource

<a id='req-06'></a>

### REQ-06: Required Must Support elements handling

**Description**: "Health Plan API SHALL provide reason for missing information using nullFlavors or dataAbsentReason extension when Must Support element is absent and minimum cardinality is >0"

**Actor**: Health Plan API

**Conformance**: SHALL

# Test Specification for REQ-06

## 1. Requirement ID
REQ-06: Must Support Elements Handling with Data Absent Reason

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically Testable
- **Complexity**: Moderate
- **Impact**: High - This is a fundamental requirement for handling required Must Support elements

### Prerequisites
1. Access to Health Plan API endpoint
2. Test data with Must Support elements intentionally omitted
3. List of all Must Support elements defined in the IG with cardinality >0
4. Valid authentication credentials for API access

## 3. Test Implementation Strategy

### Required Inputs
1. FHIR Resources with Must Support elements having min cardinality >0
2. Sample requests for each relevant resource type

### Required FHIR Operations
- GET operations on resources containing Must Support elements
- Based on Capability Statement, both JSON and XML formats should be tested

### Test Scenarios

#### Scenario 1: Basic Must Support Element Absence Validation
**Purpose**: Verify proper handling of missing Must Support elements

**Steps**:
1. Identify a resource instance where a Must Support element with min cardinality >0 is absent
2. Send GET request for this resource
3. Validate response contains either:
   - dataAbsentReason extension
   - appropriate nullFlavor value

#### Scenario 2: Multiple Must Support Elements
**Purpose**: Verify handling when multiple Must Support elements are absent

**Steps**:
1. Create test cases with multiple absent Must Support elements
2. Verify each absent element has appropriate documentation

### Validation Criteria

#### Technical Validations
1. Response Status:
   - SHALL return 200 OK for successful requests

2. Response Content:
   - SHALL contain dataAbsentReason extension or nullFlavor for each missing Must Support element
   - Extension SHALL conform to http://hl7.org/fhir/StructureDefinition/data-absent-reason
   - NullFlavor values SHALL be from valid ValueSet

#### Data Validation
1. For each absent Must Support element:
   - Verify presence of dataAbsentReason extension or nullFlavor
   - Verify reason code is appropriate for the context
   - Verify extension or nullFlavor syntax is correct

### Error Conditions
1. Missing dataAbsentReason/nullFlavor when required
2. Invalid dataAbsentReason/nullFlavor codes
3. Incorrect placement of extensions

### Test Data Requirements
1. Sample resources with:
   - Single missing Must Support element
   - Multiple missing Must Support elements
   - Complete set of valid dataAbsentReason codes
   - Complete set of valid nullFlavor values

### Expected Results
- All missing Must Support elements (min cardinality >0) SHALL have either:
  - dataAbsentReason extension with valid reason code
  - Valid nullFlavor value
- Documentation SHALL be syntactically correct
- Reason codes SHALL be appropriate for the clinical context

### Notes
- XML format support should be tested as per Capability Statement
- Consider bulk testing for multiple resources
- Document specific Must Support elements being tested
- Consider performance implications of extension validation

---



<a id='general-requirements'></a>

## General Requirements

<a id='req-04'></a>

### REQ-04: Must Support elements population

**Description**: "Health Plan API SHALL populate all Must Support data elements in query results"

**Actor**: Health Plan API

**Conformance**: SHALL

# Test Specification for REQ-04

## 1. Requirement ID
REQ-04: Must Support Elements Population

## 2. Requirement Analysis

### Testability Assessment
Automatically testable through API verification

### Complexity
Moderate
- Requires testing across multiple resource types
- Needs verification of all Must Support elements
- May require multiple test scenarios

### Prerequisites
- Complete list of all Must Support elements from the IG for each applicable resource type
- Test data that includes valid values for all Must Support elements
- Access to Health Plan API endpoints
- Authentication credentials if required
- Capability to parse and validate XML responses (based on SHOULD support for XML)

## 3. Test Implementation Strategy

### Required Inputs
1. Test Data:
   - Sample resources with all Must Support elements populated
   - Resource instances missing some Must Support elements for negative testing

### Required FHIR Operations
1. READ operations for individual resources
2. SEARCH operations with various parameters to retrieve resources
3. Specific resource endpoints defined in the IG

### Validation Criteria

#### Positive Tests
1. For each resource type that contains Must Support elements:
   - Execute appropriate SEARCH/READ operations
   - Verify all Must Support elements are present in responses
   - Verify Must Support elements contain valid values according to IG specifications
   
2. Format Validation:
   - Test both JSON and XML formats (XML is SHOULD support)
   - Verify Must Support elements are correctly represented in both formats

#### Negative Tests
1. Error Handling:
   - Verify appropriate error responses when mandatory Must Support elements are missing
   - Validate error message format and content

### Test Steps
1. Setup Phase:
   ```
   - Configure test environment
   - Prepare test data
   - Establish API connectivity
   ```

2. Execution Phase:
   ```
   For each resource type:
     For each Must Support element:
       Execute appropriate FHIR operation
       Validate response contains Must Support element
       Validate element content matches specifications
       Verify XML representation (if supported)
   ```

3. Validation Phase:
   ```
   - Compare actual vs expected results
   - Document any missing Must Support elements
   - Verify error handling for missing mandatory elements
   ```

### Success Criteria
- All Must Support elements are present in API responses
- Elements contain valid values as defined in the IG
- XML representation is correct (when supported)
- Appropriate error handling for missing mandatory elements

### Test Data Requirements
1. Sample Resources:
   ```
   {
     "resourceType": "[Resource]",
     "id": "test-resource-1",
     "mustSupportElement1": "value",
     "mustSupportElement2": "value"
     // ... all other Must Support elements
   }
   ```

2. Expected Results:
   ```
   - List of all Must Support elements per resource
   - Expected values or value ranges
   - Expected error responses
   ```

### Error Conditions
1. Missing Must Support Elements:
   - Document expected behavior
   - Verify error responses
   - Log validation results

2. Invalid Values:
   - Test boundary conditions
   - Verify error handling
   - Document responses

---



<a id='global'></a>

## Global

<a id='req-05'></a>

### REQ-05: Optional Must Support elements handling

**Description**: "Health Plan API SHALL NOT include Must Support data elements in resource instances when information is not present and minimum cardinality is 0"

**Actor**: Health Plan API

**Conformance**: SHALL NOT

# Test Specification for REQ-05

## 1. Requirement ID
REQ-05: Optional Must Support elements handling

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically testable
- **Justification**: Can be verified through automated inspection of resource instances for Must Support elements with minimum cardinality of 0

### Complexity
Moderate
- Requires analysis of IG profiles to identify Must Support elements
- Needs verification across multiple resource types
- Requires understanding of cardinality rules

### Prerequisites
1. Access to Health Plan API endpoints
2. List of all applicable FHIR profiles defined in the IG
3. Inventory of Must Support elements with minimum cardinality of 0 for each profile
4. Test data that intentionally excludes optional Must Support elements
5. Valid authentication credentials for API access

## 3. Test Implementation Strategy

### Required Inputs
1. **FHIR Resources**:
   - Sample instances of each resource type defined in the IG
   - Resources should be configured to exclude optional Must Support elements
   
2. **Profile Definitions**:
   - StructureDefinition resources for all profiles in the IG
   - Documentation of Must Support elements and their cardinality

### Required FHIR Operations
1. READ operations on resource instances
2. SEARCH operations to retrieve resources
   - Both xml and json formats should be tested (per Capability Statement)

### Test Cases

#### Test Case 1: Basic Validation
1. **Purpose**: Verify absence of optional Must Support elements
2. **Steps**:
   - For each profile:
     a. Create resource instance excluding optional Must Support elements
     b. Submit to server
     c. Retrieve resource
     d. Verify excluded elements are not present

#### Test Case 2: Format Verification
1. **Purpose**: Verify behavior across formats
2. **Steps**:
   - Repeat Test Case 1 with both XML and JSON formats
   - Verify consistent behavior across formats

### Validation Criteria

#### Success Criteria
1. Resource instances MUST NOT contain Must Support elements when:
   - Element's minimum cardinality is 0
   - No data is available for the element
2. Server responses MUST be valid against profile definitions
3. Behavior MUST be consistent across supported formats

#### Failure Conditions
1. Presence of any Must Support element with:
   - Minimum cardinality of 0
   - No meaningful data content
2. Invalid resource instances
3. Inconsistent behavior between formats

### Test Data Requirements
1. Sample resource instances for each profile
2. Test cases covering:
   - All Must Support elements with min cardinality 0
   - Various combinations of optional elements
3. Both valid and invalid scenarios

### Implementation Notes
- Implement automated validation using FHIR validator
- Consider edge cases where elements might be present but empty
- Document any assumptions about what constitutes "information not present"
- Include checks for both primitive and complex data types

---



<a id='organizationaffiliation'></a>

## OrganizationAffiliation

<a id='req-11'></a>

### REQ-11: Network documentation for organizations

**Description**: "Health Plan API SHALL document organization network participation using OrganizationAffiliation instances linked to Networks"

**Actor**: Health Plan API

**Conformance**: SHALL

# Test Specification: Network Documentation for Organizations

## 1. Requirement ID
REQ-11

## 2. Requirement Analysis

### Testability Assessment
- Automatically Testable
- The requirement can be verified through API interactions and resource validation

### Complexity
Moderate
- Requires verification of multiple linked resources
- Multiple search operations and relationship validations needed

### Prerequisites
1. Health Plan API must be operational and accessible
2. Test data must include:
   - Network Organizations
   - Organizations participating in networks
   - Valid OrganizationAffiliation resources
   - Valid Organization resources representing networks

## 3. Test Implementation Strategy

### Required Resources
1. Organization resources representing:
   - Networks
   - Participating healthcare organizations
2. OrganizationAffiliation resources linking organizations to networks
3. Valid endpoints and references between resources

### Required FHIR Operations
Based on Capability Statement, the following operations are supported and needed:

1. Search OrganizationAffiliation resources:
   ```
   GET [base]/OrganizationAffiliation?network=[reference]
   GET [base]/OrganizationAffiliation?participating-organization=[reference]
   ```

2. Search Organization resources:
   ```
   GET [base]/Organization?_id=[id]
   GET [base]/Organization?type=ntwk
   ```

### Validation Criteria

#### Test Case 1: Basic Network Documentation
1. Verify Organization resources exist for networks
   - Assert Organization.type includes "ntwk" code
   - Assert Organization resources are properly formed

2. Verify OrganizationAffiliation resources exist linking organizations to networks
   - Assert OrganizationAffiliation.network references valid network Organization
   - Assert OrganizationAffiliation.participatingOrganization references valid Organization

#### Test Case 2: Network Search and Retrieval
1. Search for all network-type organizations
   ```
   GET [base]/Organization?type=ntwk
   ```
   - Assert response contains expected network organizations
   - Assert HTTP 200 status code

2. For each network, search for affiliated organizations
   ```
   GET [base]/OrganizationAffiliation?network=[network-reference]
   ```
   - Assert response contains expected OrganizationAffiliation resources
   - Assert each OrganizationAffiliation has valid participating organization reference

#### Test Case 3: Reference Integrity
1. For each OrganizationAffiliation:
   - Verify network reference resolves to valid Organization resource
   - Verify participating organization reference resolves to valid Organization resource
   - Assert all mandatory fields are present

### Testing Notes
1. All search parameters used in tests are verified as supported in Capability Statement
2. XML format should be tested as noted in Capability Statement (SHOULD support)
3. Test data should include:
   - Multiple networks
   - Multiple organizations affiliated with each network
   - Edge cases such as organizations affiliated with multiple networks

### Pass/Fail Criteria
Test passes if:
1. All Organization resources representing networks are properly documented
2. All OrganizationAffiliation resources correctly link organizations to networks
3. All references resolve to valid resources
4. All search operations return expected results
5. No HTTP errors occur during normal operations
6. All mandatory fields are present and valid

---



<a id='plan-net-api-security'></a>

## Plan-Net API Security

<a id='req-02'></a>

### REQ-02: No consumer identification requirement

**Description**: "Health Plan API SHALL NOT require directory mobile applications to send consumer identifying information in queries"

**Actor**: Health Plan API

**Conformance**: SHALL NOT

# Test Specification for REQ-02

## 1. Requirement ID
REQ-02: Health Plan API SHALL NOT require directory mobile applications to send consumer identifying information in queries

## 2. Requirement Analysis

### Testability Assessment
Automatically testable through API interaction testing

### Complexity
Moderate - Requires testing multiple API endpoints and verifying absence of required consumer identification fields

### Prerequisites
- Health Plan API endpoint must be available and accessible
- Test client capable of making FHIR API requests
- Sample valid queries for directory information
- Documentation of all supported search parameters

## 3. Test Implementation Strategy

### Required Inputs
- Set of valid FHIR search queries without consumer identification
- Test data covering various directory resources:
  - PractitionerRole
  - Practitioner
  - Organization
  - Location
  - HealthcareService
  - InsurancePlan

### Required FHIR Operations
- GET operations on supported directory resources
- Search operations with various permitted parameters
Example endpoints to test:
```
GET [base]/PractitionerRole
GET [base]/Organization
GET [base]/Location
GET [base]/HealthcareService
GET [base]/InsurancePlan
```

### Validation Criteria

#### Positive Tests
1. Execute valid searches without consumer identification
   - Assert: Returns 200 OK
   - Assert: Returns valid FHIR Bundle
   - Assert: No error messages about missing consumer identification

#### Negative Tests
2. Check for absence of required consumer identification fields in API documentation
   - Assert: No required parameters related to consumer identification in capability statement
   - Assert: No required headers related to consumer identification

3. Test error handling
   - Assert: Server does not return 401 Unauthorized or 403 Forbidden due to missing consumer identification
   - Assert: Server does not return 400 Bad Request due to missing consumer identification parameters

#### Documentation Tests
4. Review API documentation
   - Assert: No documentation indicating requirement for consumer identification
   - Assert: No OAuth2 scopes or security requirements related to consumer identification

### Test Data Requirements
- Valid search queries for each resource type
- Various combinations of valid search parameters
- Sample responses to verify correct processing

### Additional Considerations
1. Test both XML and JSON formats (since XML is mentioned in Capability Statement)
2. Include tests for various search parameter combinations
3. Verify behavior remains consistent across all supported directory resources
4. Document any observed security mechanisms that don't involve consumer identification

### Expected Results
For a conformant implementation:
- All API calls should succeed without consumer identification
- No error responses related to missing consumer identification
- Documentation should not mention consumer identification requirements
- Security mechanisms should not depend on consumer identification

---



<a id='practitionerrole'></a>

## PractitionerRole

<a id='req-10'></a>

### REQ-10: Network documentation for practitioners

**Description**: "Health Plan API SHALL document practitioner network participation using PractitionerRole instances linked to Networks"

**Actor**: Health Plan API

**Conformance**: SHALL

# Test Specification for REQ-10

## 1. Requirement ID
REQ-10: Network documentation for practitioners

## 2. Requirement Analysis

### Testability Assessment
- **Classification**: Automatically Testable
- **Reason**: The requirement can be verified through API interactions and resource validation

### Complexity
- **Level**: Moderate
- **Rationale**: Requires verification of multiple linked resources and proper network documentation structure

### Prerequisites
1. Health Plan API endpoint must be available and accessible
2. Test data must include:
   - At least one Network resource
   - At least one Practitioner resource
   - Associated PractitionerRole resources
3. Authentication/authorization credentials if required
4. Test environment capable of making FHIR API calls

## 3. Test Implementation Strategy

### Required Resources
1. **Input Resources**:
   - Network resource(s)
   - Practitioner resource(s)
   - PractitionerRole resource(s)

2. **Expected Output**:
   - PractitionerRole resources with valid network references

### Required FHIR Operations
1. Search for PractitionerRole resources:
   ```
   GET [base]/PractitionerRole?network=[network-id]
   GET [base]/PractitionerRole?practitioner=[practitioner-id]
   ```
2. Read individual resources:
   ```
   GET [base]/PractitionerRole/[id]
   GET [base]/Practitioner/[id]
   GET [base]/Network/[id]
   ```

### Test Cases

#### Test Case 1: Basic Network Documentation
1. **Setup**:
   - Create test Practitioner
   - Create test Network
   - Create PractitionerRole linking both

2. **Actions**:
   - Retrieve PractitionerRole using network search parameter
   - Verify linked resources exist and are accessible

3. **Assertions**:
   - PractitionerRole.network reference exists
   - Referenced Network resource is retrievable
   - PractitionerRole.practitioner reference exists
   - Referenced Practitioner resource is retrievable

#### Test Case 2: Multiple Network Associations
1. **Setup**:
   - Create test Practitioner
   - Create multiple Networks
   - Create PractitionerRole instances for each network

2. **Actions**:
   - Search PractitionerRole by practitioner
   - Verify all network associations

3. **Assertions**:
   - Multiple PractitionerRole resources returned
   - Each PractitionerRole has valid network reference
   - All referenced resources are retrievable

### Validation Criteria

#### Resource Validation
1. PractitionerRole resources must contain:
   - Valid network reference
   - Valid practitioner reference
   - Proper cardinality of references

#### Reference Integrity
1. All referenced resources must be retrievable:
   - Network references must resolve
   - Practitioner references must resolve

#### Search Functionality
1. PractitionerRole search by network must work:
   - Returns appropriate resources
   - Supports valid network references
   - Returns empty bundle for invalid networks

### Error Conditions to Test
1. Invalid network references
2. Missing practitioner references
3. Malformed PractitionerRole resources
4. Non-existent network searches

### Success Criteria
Test passes if:
1. All PractitionerRole resources contain valid network references
2. All referenced resources are retrievable
3. Search operations return expected results
4. No broken references are found in production data

## Notes
- The test implementation aligns with the Capability Statement's supported search parameters
- XML support should be tested as per the SHOULD requirement in the Capability Statement
- Implementation should verify both JSON and XML formats if supported

---



<a id='security'></a>

## Security

<a id='req-03'></a>

### REQ-03: No consumer information in queries

**Description**: "Application Actor SHALL NOT send consumer identifiable information when querying a Plan-Net service"

**Actor**: Application Actor

**Conformance**: SHALL NOT

# Test Specification for REQ-03

## 1. Requirement ID
REQ-03: No consumer information in queries

## 2. Requirement Analysis

### Testability Assessment
- Automatically testable through API request inspection
- Requires monitoring of query parameters and request payloads

### Complexity
Moderate
- Requires checking multiple possible query parameters
- Needs analysis of different resource types and search parameters
- Must account for various ways PII could be transmitted

### Prerequisites
- Test environment with Plan-Net service endpoint
- Sample non-PII search parameters for valid queries
- List of prohibited PII fields/parameters
- Access to request logging or monitoring capability

## 3. Test Implementation Strategy

### Required Inputs
1. Collection of test queries containing:
   - Valid non-PII queries
   - Invalid queries containing PII elements like:
     - Patient identifiers
     - Member IDs
     - Social Security numbers
     - Personal contact information
     - Names of consumers

2. Test Resources:
   - Healthcare Service
   - Organization
   - Practitioner
   - PractitionerRole
   - Location
   - Network

### Required FHIR Operations
- GET requests with search parameters for supported resources
- Examples:
  ```
  GET [base]/Organization?name=GeneralHospital
  GET [base]/Practitioner?specialty=101Y00000X
  GET [base]/Location?address-state=MA
  ```

### Validation Criteria

#### Test Cases

1. **Basic Parameter Validation**
   - Assert no parameters contain:
     - patient references
     - subscriber IDs
     - member identifiers
     - SSN
     - personal email addresses
     - personal phone numbers

2. **Header Inspection**
   - Assert no PII in custom headers
   - Check Authorization headers contain only valid tokens/credentials

3. **Query Parameter Testing**
   ```
   POSITIVE TEST:
   GET [base]/Organization?name=CityHospital
   Expected: 200 OK
   
   NEGATIVE TEST:
   GET [base]/Organization?patient=12345
   Expected: 400 Bad Request
   ```

4. **Resource-Specific Tests**
   - Test each supported resource type ensuring queries only contain:
     - Provider identifiers
     - Facility identifiers
     - Standard healthcare coding systems
     - Geographic location data
     - Network identifiers

#### Success Criteria
- All queries containing PII are rejected
- Only queries with approved non-PII parameters succeed
- System logs show no PII transmission in requests

#### Test Data Requirements
- Create test data sets with:
  - Valid provider/facility identifiers
  - Standard healthcare taxonomy codes
  - Geographic search parameters
  - Network identification codes
  - Sample PII data (for negative testing)

### Notes
- Tests should consider both direct and encoded PII transmission
- Consider implementing automated request scanning for PII patterns
- Document any exceptions or allowed identifiers that might resemble PII
- Consider privacy regulation compliance (HIPAA, GDPR) in test design

---



