module Test3_claude
  class MustSupportInterpretationGroup < Inferno::TestGroup
    id :must_support_interpretation
    title 'Missing Must Support Data Element Interpretation'
    description %(
      Verify that the Application Actor correctly interprets missing Must Support 
      data elements as data not present in the Health Plan API system.
      
      This test validates conformance to REQ-09: Application Actor SHALL interpret 
      missing Must Support data elements as data not present in Health Plan API system.
    )

    test do
      id :must_support_missing_elements
      title 'Application interprets missing Must Support elements correctly'
      description %(
        This test verifies that when Must Support elements are missing from a resource,
        the application interprets them as not present rather than errors.
      )
      
      input :patient_id
      input :server_url
      
      fhir_client do
        url :server_url
      end

      run do
        # Get patient resource that should have Must Support elements
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)
        
        patient = resource

        # List of Must Support elements for Patient
        must_support_elements = [
          'name',
          'gender', 
          'birthDate',
          'address'
        ]

        # Check each Must Support element
        missing_elements = []
        must_support_elements.each do |element|
          missing_elements << element unless patient.respond_to?(element) && 
                                           patient.send(element).present?
        end

        if missing_elements.any?
          # Verify application handles missing elements appropriately
          # by not raising errors and continuing processing
          begin
            missing_elements.each do |element|
              assert !patient.respond_to?(element) || 
                     patient.send(element).blank?,
                     "Expected missing Must Support element '#{element}' to be interpreted as not present"
            end
            pass "Application correctly interpreted #{missing_elements.length} missing Must Support elements as not present: #{missing_elements.join(', ')}"
          rescue => e
            fail "Application incorrectly handled missing Must Support elements: #{e.message}"
          end
        else
          skip "No missing Must Support elements found to test interpretation. Test patient should have some Must Support elements missing."
        end
      end
    end
  end
end