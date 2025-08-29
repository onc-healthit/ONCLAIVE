require 'fhir_models' # Ensure FHIR models are available
require 'fhir_client' # Ensure FHIR client is available

module Test3
  # Test Group for REQ-08: Must Support Element Display
  # This group contains tests related to the requirement that an Application Actor
  # SHOULD display Must Support data elements for human use or store them for other purposes.
  class MustSupportDisplayGroup < Inferno::TestGroup
    id :req_08_must_support_display_group
    title 'REQ-08: Must Support Element Display'
    description %(
      ### Requirement REQ-08
      **Description**: "Application Actor SHOULD display Must Support data elements for human use or store for other purposes"
      **Actor**: Application Actor
      **Conformance**: SHOULD

      ### Test Description
      Since Inferno tests the FHIR server and not the Application Actor's user interface
      or internal storage directly, this test verifies a necessary precondition for the
      application to meet the requirement.

      The test fetches a specified resource (e.g., Patient) known to contain Must Support elements
      and checks if those elements are present in the data returned by the server.

      If the required Must Support elements are present in the server's response, the test
      will pass and provide an informational message reminding the tester to manually
      verify that their application appropriately displays or stores these elements.

      If the resource cannot be fetched or if the relevant Must Support elements are not
      present in the fetched resource, the test will be skipped, as the application
      cannot display or store data that is not available.

      **Note**: The specific Must Support elements checked by this test are based on
      common examples (e.g., for Patient). In a real-world scenario, these would be
      derived from the specific Implementation Guide profiles being tested against.
    )
    # Define input for the patient ID needed to fetch a resource
    # This assumes we are checking Must Support elements on a Patient resource.
    # This could be generalized to other resource types if needed.
    input :patient_id,
          title: 'Patient ID',
          description: 'ID of a Patient resource expected to contain Must Support elements.'

    # FHIR client setup is typically handled in a parent group or TestSuite
    # fhir_client do
    #   url :server_url
    #   bearer_token :access_token # Or other auth mechanism
    # end

    # Test implementation for REQ-08
    test do
      # Unique ID for this specific test
      id :req_08_must_support_element_check
      title 'Check for Presence of Must Support Elements in Patient Resource'
      description %(
        Fetches the specified Patient resource using `read` interaction.
        Checks if common Must Support elements (e.g., `name`, `identifier`, `gender`, `birthDate`)
        are present in the resource data returned by the server.

        If elements are present, the test passes with a reminder for manual application verification (REQ-08).
        If the resource is not found or required elements are absent, the test is skipped.
      )
      # Link this test to the requirement ID
      links [
        {
          label: 'Requirement REQ-08',
          url: 'https://example.com/fhir/requirements#REQ-08' # Replace with actual link if available
        }
      ]

      # Mark the request this test makes for potential debugging or logging
      makes_request :patient_read_for_must_support

      # Define the Must Support elements to check for the Patient resource.
      # In a production Test Kit, this list would ideally be generated from
      # the Implementation Guide's StructureDefinitions.
      # Using simple paths for demonstration. FHIRPath would be more robust for complex elements.
      MUST_SUPPORT_PATIENT_ELEMENTS = [
        { path: 'name', description: 'Patient Name' },
        { path: 'identifier', description: 'Patient Identifier' },
        { path: 'gender', description: 'Patient Gender' },
        { path: 'birthDate', description: 'Patient Birth Date' }
        # Add other relevant Must Support elements as needed based on the IG
      ].freeze

      run do
        # Step 1: Attempt to read the specified Patient resource
        fhir_read(:patient, patient_id, name: :patient_read_for_must_support)

        # Step 2: Check if the read was successful (HTTP 200 OK)
        # If not found (404) or other error, assert_response_status will fail the test here.
        # We could alternatively catch 404 and skip, but failing on read error is often desired.
        assert_response_status(200)

        # Step 3: Verify the resource returned is of the expected type
        assert_resource_type(:patient)

        # Step 4: Optionally, validate the resource against base FHIR specs or a profile
        # assert_valid_resource(profile_url: 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient') # Example profile validation
        assert_valid_resource # Basic validation

        # Store the fetched resource for inspection
        patient_resource = resource

        # Step 5: Check for the presence of defined Must Support elements
        must_support_elements_present = []
        must_support_elements_missing = []

        MUST_SUPPORT_PATIENT_ELEMENTS.each do |ms_element|
          path = ms_element[:path]
          element_data = nil
          begin
            # Access the element data using the path (assumes simple direct properties)
            element_data = patient_resource.send(path)
          rescue NoMethodError
            # The property doesn't exist on the FHIR model instance
            element_data = nil
          end

          # Determine if the element has a meaningful value
          # Checks for nil, empty arrays, and blank strings.
          is_present = case element_data
                       when nil
                         false
                       when Array
                         !element_data.empty? # True if array has items
                       when String
                         !element_data.strip.empty? # True if string is not blank
                       else
                         true # Assume other types (Boolean, Date, Integer etc.) are present if not nil
                       end

          if is_present
            must_support_elements_present << ms_element[:description] # Store description for readability
          else
            must_support_elements_missing << ms_element[:description]
          end
        end

        # Step 6: Determine test outcome based on element presence

        # If no Must Support elements were found in *this specific resource*,
        # we cannot verify the application's behavior for this requirement with this data.
        # Skip the test, indicating why.
        skip_if must_support_elements_present.empty?, %(
          No common Must Support elements (#{MUST_SUPPORT_PATIENT_ELEMENTS.map { |e| e[:description] }.join(', ')})
          were found with present values in the fetched Patient resource with ID '#{patient_id}'.
          Therefore, the application's display/storage behavior (REQ-08) cannot be
          verified using this specific resource.
          Missing or empty elements: #{must_support_elements_missing.join(', ')}.
        )

        # If at least one Must Support element is present, the precondition is met.
        # Pass the test, but include an informational message guiding the user
        # to perform the manual verification step required by REQ-08.
        pass %(
          Successfully fetched Patient resource '#{patient_id}' containing Must Support data.

          **Found Must Support Elements**:
          * #{must_support_elements_present.join("\n* ")}

          **Action Required (REQ-08 - SHOULD)**:
          Please manually verify that your application displays the found Must Support
          element(s) listed above for human use, or stores them for other purposes.

          (Elements checked but not found or empty: #{must_support_elements_missing.join(', ')})
        )
      end
    end
  end
end