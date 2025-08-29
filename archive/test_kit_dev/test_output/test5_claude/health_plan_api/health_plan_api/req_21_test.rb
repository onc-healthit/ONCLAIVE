module Test5_claude
  class ForwardChainingTest < Inferno::TestGroup
    id :forward_chaining_support
    title 'Forward Chaining Support'
    description %(
      Verify that the server supports forward chaining on all search parameters 
      that specify the 'chain' property.

      This test checks that:
      * The server properly handles chained search parameters
      * Results are filtered correctly based on the chained criteria
      * Error responses are handled appropriately
    )

    test do
      id :patient_organization_chaining
      title 'Patient-Organization forward chaining'
      description 'Verify forward chaining from Patient to Organization works correctly'
      
      input :patient_id
      input :organization_name
      
      run do
        # Search for patients with chained organization name
        fhir_search(:patient, params: {
          'organization.name': organization_name
        })

        assert_response_status(200)
        assert_resource_type(:bundle) 
        
        bundle = resource

        assert bundle.entry.present?, 'No results returned for chained search'
        
        # Verify each result is a Patient linked to an org with matching name
        bundle.entry.each do |entry|
          assert entry.resource.is_a?(FHIR::Patient), 'Result is not a Patient resource'
          
          org_reference = entry.resource.managingOrganization
          assert org_reference.present?, 'Patient has no organization reference'

          # Read referenced organization 
          fhir_read(:organization, org_reference.reference.split('/').last)
          assert_response_status(200)
          
          org = resource
          assert org.name == organization_name, 
            "Organization name '#{org.name}' does not match search criteria '#{organization_name}'"
        end
      end
    end

    test do
      id :observation_patient_chaining 
      title 'Observation-Patient forward chaining'
      description 'Verify forward chaining from Observation to Patient works correctly'
      
      input :patient_family_name
      
      run do
        # Search observations with chained patient name
        fhir_search(:observation, params: {
          'subject:Patient.family': patient_family_name
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource
        
        assert bundle.entry.present?, 'No results returned for chained search'

        # Verify each result is properly chained
        bundle.entry.each do |entry|
          assert entry.resource.is_a?(FHIR::Observation), 'Result is not an Observation resource'
          
          patient_reference = entry.resource.subject
          assert patient_reference.present?, 'Observation has no patient reference'

          # Read referenced patient
          fhir_read(:patient, patient_reference.reference.split('/').last)
          assert_response_status(200)
          
          patient = resource
          assert patient.name.any? { |name| name.family == patient_family_name },
            "Patient family name does not match search criteria '#{patient_family_name}'"
        end
      end
    end

    test do
      id :invalid_chain_parameter
      title 'Invalid chain parameter handling'
      description 'Verify server handles invalid chain parameters appropriately'
      
      run do
        # Try searching with invalid chain
        fhir_search(:patient, params: {
          'invalid.chain': 'value'
        })

        assert_response_status(400)
      end
    end
  end
end