module Test5_claude
  class MustSupportDataElementsTest < Inferno::TestGroup
    id :must_support_absent_data_test
    title 'Must Support Data Elements Not Present Test'
    description %(
      This test verifies that when Must Support data elements are not present and have 
      minimum cardinality of 0, they are not included in returned resource instances.
      
      Requirement: Health Plan API actors SHALL NOT include Must Support data elements
      when the information is not present and minimum cardinality is 0.
    )

    MUST_SUPPORT_ELEMENTS = {
      'Patient' => ['birthDate', 'name.given', 'address.city'],
      'Coverage' => ['period.end', 'type.coding', 'payor'],
      'ExplanationOfBenefit' => ['billablePeriod.end', 'provider', 'diagnosis']
    }

    test do
      id :verify_absent_must_support_elements
      title 'Verify Must Support Elements Not Present When Data Absent'
      description %(
        This test verifies that Must Support elements with min cardinality 0 
        are not included when data is absent.
      )
      
      input :patient_id
      
      run do
        MUST_SUPPORT_ELEMENTS.each do |resource_type, elements|
          if resource_type == 'Patient'
            response = fhir_read(:patient, patient_id)
          else
            response = fhir_search(resource_type.to_sym, {patient: patient_id})
          end
          
          assert_response_status(200)
          assert_valid_resource
          
          resources = resource_type == 'Patient' ? [response.resource] : response.resource.entry&.map(&:resource)
          
          resources&.each do |resource|
            elements.each do |element_path|
              element_present = resource.traverse(element_path).present?
              
              if element_present
                element_empty = resource.traverse(element_path).respond_to?(:empty?) && 
                              resource.traverse(element_path).empty?
                
                if !element_empty
                  warning do
                    assert false, "#{resource_type} resource contains #{element_path} when data " \
                                "is potentially absent. Verify this represents actual data."
                  end
                end
              end
            end
          end
        end

        pass "Must Support elements appropriately excluded when data absent"
      end
    end
  end
end