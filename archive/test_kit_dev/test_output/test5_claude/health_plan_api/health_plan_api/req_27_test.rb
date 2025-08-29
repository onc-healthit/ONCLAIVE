module Test5_claude
  class IncludesValidationGroup < Inferno::TestGroup
    id :includes_validation
    title 'Support for _includes Parameter'
    description %(
      Validate that the server properly supports the _include parameter
      for searching related resources, as required by the implementation guide.
      The server SHALL support specified _include parameters for each resource type.
    )

    test do
      id :patient_include_organization
      title 'Patient _include Organization support'
      description %(
        Verify that the server supports _include=Patient:organization when 
        searching Patient resources to include referenced Organization resources.
      )
      
      input :patient_id
      
      run do
        fhir_search(:patient, params: {
          '_id': patient_id,
          '_include': 'Patient:organization'
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource

        assert bundle.entry.length > 1, 
          'Expected Bundle to contain both Patient and included Organization resources'

        patient = bundle.entry.find { |e| e.resource.resourceType == 'Patient' }&.resource
        assert patient.present?, 'Bundle must contain the requested Patient'

        org = bundle.entry.find { |e| e.resource.resourceType == 'Organization' }&.resource
        assert org.present?, 'Bundle must contain the included Organization'

        assert patient.organization&.reference&.include?(org.id), 
          'Included Organization must match Patient.organization reference'
      end
    end

    test do
      id :coverage_include_payor
      title 'Coverage _include Payor support' 
      description %(
        Verify that the server supports _include=Coverage:payor when
        searching Coverage resources to include referenced Organization resources.
      )

      input :coverage_id
      
      run do
        fhir_search(:coverage, params: {
          '_id': coverage_id,
          '_include': 'Coverage:payor'
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource

        assert bundle.entry.length > 1,
          'Expected Bundle to contain both Coverage and included Organization resources'

        coverage = bundle.entry.find { |e| e.resource.resourceType == 'Coverage' }&.resource
        assert coverage.present?, 'Bundle must contain the requested Coverage'

        payor = bundle.entry.find { |e| e.resource.resourceType == 'Organization' }&.resource
        assert payor.present?, 'Bundle must contain the included Payor Organization'

        assert coverage.payor.any? { |p| p.reference.include?(payor.id) },
          'Included Organization must match Coverage.payor reference'
      end
    end

    test do
      id :practitioner_include_location
      title 'PractitionerRole _include Location support'
      description %(
        Verify that the server supports _include=PractitionerRole:location when
        searching PractitionerRole resources to include referenced Location resources.
      )

      input :practitioner_role_id
      
      run do
        fhir_search(:practitionerrole, params: {
          '_id': practitioner_role_id,
          '_include': 'PractitionerRole:location'
        })

        assert_response_status(200)
        assert_resource_type(:bundle)
        
        bundle = resource

        assert bundle.entry.length > 1,
          'Expected Bundle to contain both PractitionerRole and included Location resources'

        role = bundle.entry.find { |e| e.resource.resourceType == 'PractitionerRole' }&.resource
        assert role.present?, 'Bundle must contain the requested PractitionerRole'

        location = bundle.entry.find { |e| e.resource.resourceType == 'Location' }&.resource
        assert location.present?, 'Bundle must contain the included Location'

        assert role.location.any? { |l| l.reference.include?(location.id) },
          'Included Location must match PractitionerRole.location reference'
      end
    end
  end
end