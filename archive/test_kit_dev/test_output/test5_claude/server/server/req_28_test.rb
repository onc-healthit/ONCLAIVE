module Test5_claude
  class RevincludesSupportTest < Inferno::TestGroup
    id :revinclude_support_test
    title 'Support for _revinclude Parameters'
    description %(
      Verify that the server supports _revinclude parameters for retrieving 
      resources that reference the target resource.
      
      This test focuses on requirement REQ-28:
      "For each resource, a Server SHALL be capable of supporting _revincludes"
    )

    fhir_client do
      url :url
      bearer_token :bearer_token
    end

    # Test base _revinclude support
    test do
      id :basic_revinclude_support
      title 'Server supports basic _revinclude parameter'
      description %(
        This test verifies that the server properly handles a basic _revinclude
        parameter by returning both the target resource and referenced resources.
      )
      
      input :patient_id
      
      run do
        # Search for Patient with _revinclude for related Observations
        fhir_search(:patient, 
          params: {
            _id: patient_id,
            _revinclude: 'Observation:subject'
          }
        )

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource

        assert bundle.entry.length > 1, 
          'Expected bundle to contain Patient and related Observations'

        # Verify bundle contains the target Patient
        patient_entry = bundle.entry.find { |e| e.resource.resourceType == 'Patient' }
        assert !patient_entry.nil?, 'Bundle must contain the target Patient'
        assert patient_entry.resource.id == patient_id, 
          'Bundle Patient must match requested ID'

        # Verify bundle contains Observations referencing the Patient
        obs_entries = bundle.entry.select { |e| e.resource.resourceType == 'Observation' }
        assert !obs_entries.empty?, 'Bundle must contain related Observations'
        
        obs_entries.each do |entry|
          assert entry.resource.subject&.reference&.include?(patient_id),
            'All returned Observations must reference the target Patient'
        end
      end
    end

    # Test multiple _revinclude parameters
    test do
      id :multiple_revinclude_support
      title 'Server supports multiple _revinclude parameters'
      description %(
        This test verifies that the server properly handles multiple _revinclude
        parameters by returning the target resource and all referenced resource types.
      )

      input :patient_id
      
      run do
        # Search with multiple _revinclude parameters
        fhir_search(:patient,
          params: {
            _id: patient_id,
            _revinclude: [
              'Observation:subject',
              'Condition:patient',
              'Procedure:patient'
            ]
          }
        )

        assert_response_status(200)
        assert_resource_type(:bundle)

        bundle = resource
        
        # Verify bundle contains target Patient
        assert bundle.entry.any? { |e| e.resource.resourceType == 'Patient' },
          'Bundle must contain the target Patient'

        # Check for presence of each referenced resource type
        ['Observation', 'Condition', 'Procedure'].each do |type|
          matching_entries = bundle.entry.select { |e| e.resource.resourceType == type }
          
          if matching_entries.any?
            matching_entries.each do |entry|
              reference = case type
              when 'Observation'
                entry.resource.subject&.reference
              when 'Condition', 'Procedure'  
                entry.resource.patient&.reference
              end

              assert reference&.include?(patient_id),
                "#{type} resources must reference the target Patient"
            end
          end
        end
      end
    end

    # Test _revinclude with search parameters
    test do
      id :revinclude_with_search
      title 'Server supports _revinclude with additional search parameters'
      description %(
        This test verifies that the server properly handles _revinclude parameters
        when combined with other search parameters.
      )

      input :patient_id
      
      run do
        # Search with _revinclude and additional parameters
        fhir_search(:patient,
          params: {
            _id: patient_id,
            _revinclude: 'Observation:subject',
            _count: 5
          }
        )

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource

        assert bundle.entry.length <= 6, # Patient + max 5 Observations
          'Server must respect _count parameter with _revinclude'

        assert bundle.entry.any? { |e| e.resource.resourceType == 'Patient' },
          'Bundle must contain the target Patient'

        obs_entries = bundle.entry.select { |e| e.resource.resourceType == 'Observation' }
        obs_entries.each do |entry|
          assert entry.resource.subject&.reference&.include?(patient_id),
            'All Observations must reference the target Patient'
        end
      end
    end
  end
end