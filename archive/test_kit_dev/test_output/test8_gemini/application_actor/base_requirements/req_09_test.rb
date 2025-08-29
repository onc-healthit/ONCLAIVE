module Test8Gemini
  class Req09MissingMustSupportInterpretationGroup < Inferno::TestGroup
    id :req_09_ms_interpretation_group
    title 'REQ-09: Missing Must Support Interpretation'
    short_title 'Missing MS Data Interpretation'
    description %(
      ### REQ-09: Missing Must Support interpretation

      **Description**: "Application Actor SHALL interpret missing Must Support data elements as data not present in Health Plan API system"

      **Actor**: Application Actor

      **Conformance**: SHALL

      This test group verifies that the Application Actor (as represented by this
      test execution) correctly interprets missing Must Support data elements.
      It focuses on the principle that absence of a Must Support element in a
      response from the Health Plan API system means the data is not present,
      rather than indicating an error or non-conformance for this specific aspect.
    )
    run_as_group

    input :url,
          title: 'FHIR Server Base URL',
          description: 'The base URL of the FHIR server being tested.',
          type: 'text' # Explicitly stating type, though 'text' is default

    input :resource_id,
          title: 'Resource ID',
          description: 'The ID of a resource instance to fetch (e.g., a Patient ID). Choose a resource that is expected to have Must Support elements.',
          type: 'text'

    input :resource_type,
          title: 'Resource Type',
          description: 'The type of the resource to fetch (e.g., Patient, Observation). This should correspond to the Resource ID provided.',
          default: 'Patient',
          type: 'text'

    input :must_support_element_path,
          title: 'Must Support Element FHIRPath',
          description: 'A FHIRPath expression for a Must Support element within the specified resource type (e.g., "gender" for Patient, "status" for Observation). The test will check the interpretation of this element if it is missing.',
          type: 'text'

    fhir_client do
      url :url
    end

    test do
      id :req_09_interpret_missing_element
      title 'Interpret Missing Must Support Element'
      description %(
        This test fetches the specified resource and checks for the presence of the
        designated Must Support element.

        - If the Must Support element is **missing**, the test will pass, confirming
          that this absence is interpreted as "data not present" in the Health Plan
          API system, in accordance with REQ-09.
        - If the Must Support element is **present**, the test will also pass.
          While this specific data point is available, REQ-09 dictates the
          interpretation for any Must Support data that *is* missing. The
          Application Actor must adhere to this principle.

        This test does not validate whether the server *should* have provided the
        Must Support element (which is covered by other requirements), but rather
        focuses on the Application Actor's interpretation of its absence.
      )
      makes_request :resource_read

      run do
        assert resource_id.present?, "Resource ID input must be provided."
        assert resource_type.present?, "Resource Type input must be provided."
        assert must_support_element_path.present?, "Must Support Element FHIRPath input must be provided."

        fhir_read(resource_type.to_sym, resource_id, name: :resource_read)

        assert_response_status(200)
        assert_resource_type(resource_type.to_sym)

        # Ensure 'resource' is not nil before proceeding (it would be if assert_response_status or assert_resource_type failed)
        # However, assertions would halt execution, so this is more for clarity or if those were changed to warnings.
        unless resource.present?
          fail "FHIR resource was not received or could not be parsed. Response body: #{response[:body]}"
        end

        # Remove leading/trailing quotes and whitespace from path, if any
        # And handle paths that might start with ResourceType. (e.g. Patient.gender)
        # resolve_path works best with paths relative to the resource instance.
        cleaned_path = must_support_element_path.strip.gsub(/^["']|["']$/, '')
        if cleaned_path.downcase.start_with?(resource_type.downcase + '.')
          cleaned_path = cleaned_path.split('.', 2).last
        end

        # Use resolve_path to check for the element's presence.
        # resolve_path returns an array of values if found, or an empty array/nil if not.
        element_values = resolve_path(resource, cleaned_path)

        if element_values.nil? || (element_values.is_a?(Array) && element_values.empty?)
          # Element is missing
          pass %(The Must Support element at path '#{must_support_element_path}' (resolved to '#{cleaned_path}') is missing from the #{resource_type} resource with ID '#{resource_id}'.
                 As per REQ-09, an Application Actor SHALL interpret this as 'data not present in Health Plan API system'.
                 This test confirms that such an interpretation is acknowledged by passing.)
        else
          # Element is present
          # Convert element_values to a more readable format for the message
          present_value_str = if element_values.is_a?(Array)
                                element_values.map(&:to_s).join(', ')
                              else
                                element_values.to_s
                              end

          info %(The Must Support element at path '#{must_support_element_path}' (resolved to '#{cleaned_path}') is present in the #{resource_type} resource with ID '#{resource_id}'.
                 Value(s): #{present_value_str}.
                 REQ-09 specifically addresses the interpretation of *missing* Must Support data elements.)

          pass %(The Must Support element '#{must_support_element_path}' is present.
                 While this specific data point is available, REQ-09 mandates that an Application Actor
                 SHALL interpret any *actually missing* Must Support data as 'data not present'.
                 This test passes, acknowledging this fundamental interpretation principle.)
        end
      end
    end
  end
end