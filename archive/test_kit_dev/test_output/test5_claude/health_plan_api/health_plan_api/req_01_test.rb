module Test5_claude
  class NoPiiRequirementGroup < Inferno::TestGroup
    id :no_pii_requirement_query
    title 'No PII Required for Directory Queries'
    description %(
      Validates that a Plan-Net service does not require consumer identifying 
      information when performing directory queries.

      Requirement: A conformant Plan-Net service SHALL NOT require a directory
      mobile application to send consumer identifying information in order to
      query content.
    )

    test do
      id :basic_practitioner_search_no_pii
      title 'Basic Practitioner search succeeds without PII'
      description %(
        Performs a basic Practitioner search without providing any PII to verify
        the server allows directory queries without consumer information.
      )

      # Input server URL defined at group level
      input :server_url

      run do
        # Setup FHIR client
        fhir_client do
          url server_url
        end

        # Perform basic Practitioner search without any PII parameters
        fhir_search(:practitioner)

        # Assert search was successful
        assert_response_status(200)
        assert_resource_type(:bundle)

        # Verify bundle contains valid Practitioner resources
        bundle = resource
        assert bundle.entry.length.positive?, 'No Practitioner resources returned'
        
        bundle.entry.each do |entry|
          assert entry.resource.resourceType == 'Practitioner', 
                'Non-Practitioner resource found in bundle'
        end

        # Verify no error indicating missing required PII
        assert bundle.total != 0, 'Search failed - server may require PII'
        assert !response[:body].include?('require'), 
               'Response suggests PII requirements'
      end
    end

    test do
      id :organization_search_no_pii  
      title 'Organization search succeeds without PII'
      description %(
        Performs a basic Organization search without providing any PII to verify
        the server allows directory queries without consumer information.
      )

      input :server_url

      run do
        fhir_client do
          url server_url
        end

        fhir_search(:organization)

        assert_response_status(200)
        assert_resource_type(:bundle)

        bundle = resource
        assert bundle.entry.length.positive?, 'No Organization resources returned'
        
        bundle.entry.each do |entry|
          assert entry.resource.resourceType == 'Organization',
                'Non-Organization resource found in bundle'
        end

        assert bundle.total != 0, 'Search failed - server may require PII'
        assert !response[:body].include?('require'),
               'Response suggests PII requirements'
      end
    end
  end
end