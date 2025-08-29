module Test5_claude
  class IndividualSearchParameterSupportGroup < Inferno::TestGroup
    id :individual_search_parameter_support
    title 'Individual Search Parameter Support'
    description %(
      This test group verifies conformance to REQ-19: Support the searchParameters 
      on each profile individually.
      
      The test will attempt searches using each valid search parameter defined for
      the supported profiles to ensure they can be used independently.
    )

    SUPPORTED_RESOURCES = ['Coverage', 'Patient', 'Practitioner', 'Organization']

    def get_search_params(resource_type)
      case resource_type
      when 'Coverage'
        ['beneficiary', 'identifier', 'patient', 'payor', 'status', 'subscriber']
      when 'Patient' 
        ['identifier', 'name', 'birthdate', 'gender', 'address', 'telecom']
      when 'Practitioner'
        ['identifier', 'name', 'specialty', 'role', 'organization']
      when 'Organization'
        ['identifier', 'name', 'address', 'type', 'partof']
      end
    end

    SUPPORTED_RESOURCES.each do |resource_type|
      test do
        id "search_#{resource_type.downcase}_parameters"
        title "Server supports individual search parameters for #{resource_type}"
        description "Verify that each search parameter for #{resource_type} can be used independently"

        run do
          search_params = get_search_params(resource_type)

          skip_if search_params.nil?, "No search parameters defined for #{resource_type}"

          search_params.each do |param|
            fhir_search(resource_type.to_sym, params: { param => 'test' })
            
            assert_response_status([200, 404], 
              "Server returned #{response.code} for #{resource_type} search with parameter: #{param}")

            if response.code == 200
              assert_resource_type(:bundle)
              assert_valid_bundle_entries(resource_type)
            end

            # Verify search response has proper structure even if no results
            if response.code == 404
              assert_response_content_type('application/fhir+json')
              assert_valid_json(response.body)
            end
          end

          pass "Successfully tested all search parameters for #{resource_type}"
        end
      end
    end

    def assert_valid_bundle_entries(resource_type)
      bundle = FHIR.from_contents(response.body)
      assert bundle.entry.all? { |entry| entry.resource.resourceType == resource_type },
        "Bundle contains resources other than #{resource_type}"
      
      bundle.entry.each do |entry|
        assert_valid_resource(entry.resource)
      end
    end
  end
end