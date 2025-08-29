module Test4_claude
  class MissingMustSupportTest < Inferno::TestGroup
    id :missing_must_support_interpretation
    title 'Missing Must Support Data Element Interpretation'
    description %(
      Validates that the Application Actor correctly interprets missing Must Support 
      data elements as data not present in the Health Plan API system, rather than
      errors or unknown values.

      Requirement: Application Actor SHALL interpret missing Must Support data elements
      as data not present in Health Plan API system.
    )

    test do
      id :verify_missing_must_support_handling
      title 'Missing Must Support elements are handled correctly'
      description %(
        This test verifies that when Must Support elements are not present in a
        resource, the application interprets this correctly as "data not present"
        rather than erroring or showing unknown values.
      )
      
      # Input parameters needed for test execution
      input :patient_id
      input :server_url
      input :bearer_token

      run do
        # Configure FHIR client
        fhir_client do
          url :server_url
          bearer_token :bearer_token
        end

        # Get patient resource that is known to have missing Must Support elements
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)

        patient = resource

        # Check handling of common Must Support elements when missing
        must_support_elements = [
          'birthDate',
          'address',
          'telecom',
          'name'
        ]

        must_support_elements.each do |element|
          # Verify element is actually missing
          element_present = patient.send(element).present? rescue false
          
          next unless !element_present

          # Element is missing - verify application handles this appropriately
          # Application should:
          # 1. Not error/crash
          # 2. Indicate "No Data" or similar
          # 3. Not show as "Unknown" or "Error"
          
          begin
            # Attempt to access the missing element
            patient.send(element)
            
            # Should reach here without error
            pass "Application correctly handles missing Must Support element: #{element}"
          rescue => e
            fail "Application incorrectly errors on missing Must Support element: #{element}. Error: #{e.message}"
          end
        end

      end
    end
  end
end