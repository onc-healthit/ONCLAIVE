module Test4_gemini
  class OptionalMustSupportElementsHandlingTest < Inferno::Test
    id :req_05_optional_must_support_elements_handling
    title 'Optional Must Support elements are not included when information is not present'
    description %(
      Health Plan API SHALL NOT include Must Support data elements in resource instances when information is not present and minimum cardinality is 0.
    )
    
    input :resource_type,
          title: 'Resource Type',
          description: 'The type of resource to test',
          required: true,
          default: 'Patient'
    
    run do
      skip_if resource_type.blank?, 'Must specify a resource type for this test.'
      
      resource_definition = FHIR::StructureDefinition.new(resourceType: resource_type)
      
      # Find all MustSupport elements with cardinality 0..1 or 0..*
      must_support_elements = resource_definition.snapshot.element.select do |element|
        element.mustSupport && ['0..1', '0..*'].include?(element.min.to_s + '..' + element.max)
      end
      
      skip_if must_support_elements.empty?, "No MustSupport elements found with minimum cardinality 0 in resource #{resource_type}."
      
      # Create a minimal resource instance
      resource = FHIR.from_contents('{"resourceType": "' + resource_type + '"}')
      
      # Attempt to create the resource
      response = fhir_create(resource)
      
      # Assert that the server accepted the resource creation
      assert_response_status(201, response)
      
      # Retrieve the created resource
      created_resource = fhir_read(resource_type, response.response[:id]).resource
      
      # Check that no MustSupport elements with minimum cardinality 0 are present
      must_support_elements.each do |element|
        element_path = element.path.gsub("#{resource_type}.", '')
        assert !created_resource.has_value?(element_path),
               "MustSupport element '#{element_path}' is present in the created #{resource_type} resource, but it should not be included when information is not present and minimum cardinality is 0."
      end
    end
  end
end