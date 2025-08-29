module Test5_claude
  class ForwardChainingTestGroup < Inferno::TestGroup
    id :forward_chaining_support
    title 'Forward Chaining Support'
    description %(
      This test suite verifies the server supports forward chaining on all search parameters 
      that specify the 'chain' property as required by REQ-21.
      
      Forward chaining allows clients to search for resources based on properties of referenced resources.
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    test do
      id :forward_chain_patient_organization
      title 'Server supports chaining Patient.organization to Organization.name'
      description %(
        Verify that the server properly handles a forward chained search from 
        Patient.organization to Organization.name
      )
      
      run do
        # Search for patients by organization name using forward chaining
        search_params = { 'organization.name': 'Hospital' }
        fhir_search(:patient, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource

        assert bundle.entry.present?, 'No resources returned from chained search'
        assert bundle.entry.all? { |e| e.resource.resourceType == 'Patient' }, 
          'All returned resources must be Patients'
      end
    end

    test do
      id :forward_chain_observation_patient 
      title 'Server supports chaining Observation.patient to Patient.name'
      description %(
        Verify that the server properly handles a forward chained search from
        Observation.patient to Patient.name
      )

      run do
        search_params = { 'patient.name': 'Smith' }
        fhir_search(:observation, params: search_params)

        assert_response_status(200)
        assert_resource_type(:bundle)

        bundle = resource
        
        assert bundle.entry.present?, 'No resources returned from chained search'
        assert bundle.entry.all? { |e| e.resource.resourceType == 'Observation' },
          'All returned resources must be Observations'
      end
    end

    test do
      id :forward_chain_error_handling
      title 'Server handles invalid chain parameters appropriately'
      description %(
        Verify the server returns an appropriate error when an invalid 
        chain parameter is specified
      )

      run do
        # Search with invalid chain parameter
        search_params = { 'invalid.chain': 'value' }
        fhir_search(:patient, params: search_params)

        assert_response_status(400)
        assert_resource_type(:operationoutcome)
        
        outcome = resource
        assert outcome.issue.present?, 'OperationOutcome should contain error details'
      end
    end
  end
end