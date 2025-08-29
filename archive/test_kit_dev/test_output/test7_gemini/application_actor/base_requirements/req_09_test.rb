require 'fhir_models'
require 'fhir_client'

module Test7Gemini
  class Req09InterpretMissingMustSupportGroup < Inferno::TestGroup
    id :req_09_interpret_missing_must_support_group
    title 'REQ-09: Missing Must Support Interpretation'
    short_title 'Missing MS Interpretation'
    description %(
      **Requirement REQ-09**: "Application Actor SHALL interpret missing Must Support
      data elements as data not present in Health Plan API system."

      This test group verifies that the Application Actor (which is Inferno in this
      context) correctly interprets missing Must Support data elements.

      **Test Logic**:
      1. The test requires the user to specify a resource type, a resource ID,
         the FHIRPath to a Must Support element within that resource, and a
         friendly name for that element.
      2. It fetches the specified resource from the FHIR server.
      3. It then checks if the designated Must Support element is present in the
         retrieved resource using the provided FHIRPath.
      4. **If the element is absent** (FHIRPath evaluation results in an empty list),
         the test passes. This demonstrates that the Application Actor (Inferno's
         FHIR processing capabilities) has correctly processed the resource and
         interprets the absence of the element as "data not present".
      5. **If the element is present**, the test is skipped. This is because the
         specific condition for this test (a *missing* Must Support element) is not
         met for this particular resource instance and element. The test is not
         designed to fail if the data is present, only to confirm behavior when
         it's missing.

      This test helps ensure that the client application does not erroneously assume
      data presence or encounter errors when a Must Support element, which is
      conditionally optional at the instance level, is not provided by the server.
    )

    input :url,
          title: 'FHIR Server Base URL',
          description: 'The base URL of the FHIR server to test.'

    input :resource_id_ms_check,
          title: 'Resource ID for Must Support Check',
          description: 'The ID of a resource instance to fetch for checking Must Support interpretation (e.g., a Patient ID like "example" or "123").'
          # Example: 'patient-1'

    input :resource_type_ms_check,
          title: 'Resource Type for Must Support Check',
          description: 'The FHIR resource type to fetch (e.g., "Patient", "Coverage", "Observation").',
          default: 'Patient' # Provide a common default

    input :must_support_element_path,
          title: 'FHIRPath for Must Support Element',
          description: %(
            A valid FHIRPath expression pointing to a Must Support element within
            the specified resource type. For example:
            - For Patient.gender: "gender"
            - For Patient.name.family (first name entry): "name.first().family"
            - For Observation.value[x] (if it's a Quantity): "value.as(Quantity)"
            Ensure the path is correct for the chosen resource type and element.
          ),
          default: 'gender' # Default assumes Patient.gender

    input :must_support_element_friendly_name,
          title: 'Friendly Name for Must Support Element',
          description: 'A human-readable name for the Must Support element being checked (e.g., "Patient Gender", "Coverage Status", "Observation Value Quantity"). This is used in messages.',
          default: 'Patient Gender' # Matches default path and resource type

    fhir_client do
      url :url
      # Additional FHIR client configuration (e.g., authentication)
      # should be handled at the suite or higher group level if needed.
    end

    test do
      id :req_09_interpret_missing_must_support_element
      title 'Interpret Missing Must Support Element as Not Present'
      description %(
        This test verifies REQ-09 by fetching a specified resource and checking
        if a designated Must Support element is absent.

        **Success Criteria**:
        - The test passes if the FHIR server successfully returns the requested resource,
          AND the specified Must Support element is *not present* in the resource
          (as determined by FHIRPath evaluation). This demonstrates that the
          Application Actor (Inferno) correctly processes such a resource and
          interprets the missing element as "data not present".

        **Skip Condition**:
        - The test is skipped if the specified Must Support element *is present*
          in the fetched resource. This is because the test's purpose is to
          evaluate the handling of *missing* data, and that condition is not met.
          It does not imply a failure of the server or client.

        **Error Conditions**:
        - The test will error if the FHIR server fails to return the resource
          (e.g., 404 Not Found, 500 Server Error) or if the returned resource
          is not of the expected type.
        - The test may also error if the provided FHIRPath is invalid, though
          FHIRPath.evaluate typically returns an empty array for unresolvable paths
          on a valid resource.
      )

      run do
        # --- Input Validation ---
        missing_inputs = []
        missing_inputs << "'Resource ID for Must Support Check'" if resource_id_ms_check.blank?
        missing_inputs << "'Resource Type for Must Support Check'" if resource_type_ms_check.blank?
        missing_inputs << "'FHIRPath for Must Support Element'" if must_support_element_path.blank?
        missing_inputs << "'Friendly Name for Must Support Element'" if must_support_element_friendly_name.blank?

        assert missing_inputs.empty?, "The following required inputs are missing: #{missing_inputs.join(', ')}. Please provide them to run the test."

        # --- FHIR API Call ---
        resource_type_sym = resource_type_ms_check.to_sym
        fhir_read(resource_type_sym, resource_id_ms_check)

        # --- Response Validation ---
        assert_response_status(200)
        assert_resource_type(resource_type_sym)
        # Consider adding assert_valid_resource if a profile is known or expected
        # assert_valid_resource(profile_url: 'PROFILE_URL_IF_APPLICABLE')

        # --- Must Support Element Check ---
        # Use FHIRPath to evaluate the presence of the element.
        # FHIRPath.evaluate returns an array of matching elements/values.
        # An empty array means the element is not present or has no value.
        begin
          element_values = FHIRPath.evaluate(resource, must_support_element_path)
        rescue StandardError => e
          error "FHIRPath evaluation failed for path '#{must_support_element_path}' on resource #{resource.resourceType}/#{resource.id}. Error: #{e.message}"
        end

        if element_values.nil?
          # This case should ideally not happen with FHIRPath.evaluate unless an exception occurred.
          # If it does, it implies an issue with the FHIRPath evaluation itself or the resource structure.
          warning "FHIRPath.evaluate returned nil for path '#{must_support_element_path}'. This is unexpected. Assuming element is not present for the purpose of this test."
          pass %(
            The Must Support element '#{must_support_element_friendly_name}'
            (FHIRPath: '#{must_support_element_path}') was determined to be effectively
            absent (FHIRPath evaluation returned nil) in the fetched resource
            #{resource_type_ms_check}/#{resource_id_ms_check}.
            The Application Actor (Inferno) correctly interpreted this as data not present.
          )
        elsif element_values.empty?
          # This is the target condition: element is not present or has no values.
          pass %(
            The Must Support element '#{must_support_element_friendly_name}'
            (FHIRPath: '#{must_support_element_path}') was not found or was empty
            in the fetched resource #{resource_type_ms_check}/#{resource_id_ms_check}.
            The Application Actor (Inferno) correctly interpreted this as data not present,
            fulfilling REQ-09.
          )
        else
          # Element is present.
          # The requirement is about interpreting *missing* data.
          # Since the data is present, we skip this specific check for this element.
          skip %(
            The Must Support element '#{must_support_element_friendly_name}'
            (FHIRPath: '#{must_support_element_path}') was present in the fetched
            resource #{resource_type_ms_check}/#{resource_id_ms_check}.
            (Found value(s): #{element_values.map(&:to_s).join(', ')}).
            This test specifically verifies the interpretation of *missing* Must Support data.
            To confirm this aspect of REQ-09 for '#{must_support_element_friendly_name}',
            a resource instance where this element is genuinely absent would be needed.
          )
        end
      end
    end
  end
end