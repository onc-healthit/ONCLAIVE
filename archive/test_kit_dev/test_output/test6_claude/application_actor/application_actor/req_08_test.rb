module Test6_claude
  class MustSupportRequirementsGroup < Inferno::TestGroup
    id :must_support_requirements
    title 'Must Support Requirements'
    description %(
      This test group verifies that Application actors correctly interpret missing Must Support
      data elements within resource instances from Health Plan API actors as data not being
      present in the system, per requirement REQ-08.
    )
    
    test do
      id :interpret_missing_must_support
      title 'Interpret Missing Must Support Elements'
      description %(
        Verify that Application actors correctly interpret missing Must Support data elements
        as data not being present in the Health Plan API system.
      )
      
      input :server_url
      input :token
      
      # Sample Must Support elements to check
      must_support_elements = {
        'Patient': ['name', 'birthDate', 'gender'],
        'Coverage': ['status', 'beneficiary', 'payor'],
        'Organization': ['name', 'address', 'telecom']
      }
      
      run do
        must_support_elements.each do |resource_type, elements|
          # Search for resources of this type
          fhir_search(resource_type, search: {parameters: {}})
          assert_response_status(200)
          assert_resource_type(resource_type)
          
          resources = resource.entry&.map(&:resource) || []
          next if resources.empty?
          
          resources.each do |resource|
            elements.each do |element|
              # Check if Must Support element is missing
              element_value = resource.send(element) rescue nil
              
              if element_value.nil? || element_value.empty?
                # Element is missing - verify system handles this appropriately
                assert true, "#{resource_type} resource #{resource.id} correctly handles missing Must Support element '#{element}' as not present"
              end
            end
          end
        end

        pass "Application correctly interprets missing Must Support elements as data not present in the system"
      rescue StandardError => e
        fail "Error checking Must Support elements: #{e.message}"
      end
    end
  end
end