module Test6_claude
  class IncludesTest < Inferno::TestGroup
    id :req_27_includes_support
    title 'Support for _includes'
    description %(
      Verify that the server supports the _include parameter for each resource type.
      This test validates that resources can be retrieved with included references
      according to the required include paths.
    )

    test do
      id :patient_include_test
      title 'Server supports _include parameter for Patient'
      description %(
        Verify that Patient resources can be retrieved with included references.
        Tests _include=Patient:organization to include referenced Organization resources.
      )
      
      fhir_client do
        url :url
        bearer_token :bearer
      end

      run do
        # Search with _include parameter
        fhir_search(:patient, params: {
          _include: 'Patient:organization'
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource

        # Verify bundle contains both Patient and Organization resources
        resource_types = bundle.entry.map { |e| e.resource.resourceType }.uniq
        assert resource_types.include?('Patient'), 
          'Bundle must contain Patient resources'
        assert resource_types.include?('Organization'),
          'Bundle must contain included Organization resources'

        # Verify included resources match references
        patient_entries = bundle.entry.select { |e| e.resource.resourceType == 'Patient' }
        org_entries = bundle.entry.select { |e| e.resource.resourceType == 'Organization' }
        
        patient_entries.each do |entry|
          patient = entry.resource
          if patient.organization&.reference
            org_id = patient.organization.reference.split('/').last
            assert org_entries.any? { |org_entry| org_entry.resource.id == org_id },
              "Referenced Organization #{org_id} must be included in bundle"
          end
        end
      end
    end

    test do
      id :practitioner_include_test 
      title 'Server supports _include parameter for Practitioner'
      description %(
        Verify that Practitioner resources can be retrieved with included references.
        Tests _include=Practitioner:organization to include referenced Organization resources.
      )

      fhir_client do
        url :url
        bearer_token :bearer
      end

      run do
        fhir_search(:practitioner, params: {
          _include: 'Practitioner:organization'
        })

        assert_response_status(200)
        assert_resource_type(:bundle)

        bundle = resource

        resource_types = bundle.entry.map { |e| e.resource.resourceType }.uniq
        assert resource_types.include?('Practitioner'),
          'Bundle must contain Practitioner resources'
        assert resource_types.include?('Organization'),
          'Bundle must contain included Organization resources'

        practitioner_entries = bundle.entry.select { |e| e.resource.resourceType == 'Practitioner' }
        org_entries = bundle.entry.select { |e| e.resource.resourceType == 'Organization' }

        practitioner_entries.each do |entry|
          practitioner = entry.resource
          if practitioner.organization&.reference
            org_id = practitioner.organization.reference.split('/').last
            assert org_entries.any? { |org_entry| org_entry.resource.id == org_id },
              "Referenced Organization #{org_id} must be included in bundle"
          end
        end
      end
    end
  end
end