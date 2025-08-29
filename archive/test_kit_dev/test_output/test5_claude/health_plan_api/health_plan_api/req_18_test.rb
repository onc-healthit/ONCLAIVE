module Test5_claude
  class ProfileIdentificationGroup < Inferno::TestGroup
    id :plan_net_profile_identification
    title 'Plan-Net Profile Identification'
    description %(
      Verify that Plan-Net profiles are correctly identified in the meta.profile 
      attribute for each resource instance. Each resource instance SHALL include
      the appropriate Plan-Net profile URL in its meta.profile array.
    )

    test do
      id :meta_profile_practitioner
      title 'Practitioner resource includes Plan-Net profile'
      description %(
        Verify that Practitioner resources include the Plan-Net Practitioner
        profile URL in their meta.profile attribute.
      )
      
      input :practitioner_id

      run do
        fhir_read(:practitioner, practitioner_id)

        assert_response_status(200)
        assert_resource_type(:practitioner)

        practitioner = resource
        
        assert practitioner.meta&.profile&.any?, 
          'Practitioner resource must have meta.profile defined'

        plan_net_profile = 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Practitioner'
        
        assert practitioner.meta.profile.include?(plan_net_profile),
          "Practitioner meta.profile must contain Plan-Net profile URL: #{plan_net_profile}"
      end
    end

    test do
      id :meta_profile_organization
      title 'Organization resource includes Plan-Net profile' 
      description %(
        Verify that Organization resources include the Plan-Net Organization
        profile URL in their meta.profile attribute.
      )

      input :organization_id

      run do
        fhir_read(:organization, organization_id)

        assert_response_status(200)
        assert_resource_type(:organization)

        organization = resource

        assert organization.meta&.profile&.any?,
          'Organization resource must have meta.profile defined'

        plan_net_profile = 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization'

        assert organization.meta.profile.include?(plan_net_profile),
          "Organization meta.profile must contain Plan-Net profile URL: #{plan_net_profile}"
      end
    end

    test do
      id :meta_profile_location
      title 'Location resource includes Plan-Net profile'
      description %(
        Verify that Location resources include the Plan-Net Location 
        profile URL in their meta.profile attribute.
      )

      input :location_id

      run do
        fhir_read(:location, location_id)

        assert_response_status(200)
        assert_resource_type(:location)

        location = resource

        assert location.meta&.profile&.any?,
          'Location resource must have meta.profile defined'

        plan_net_profile = 'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location'

        assert location.meta.profile.include?(plan_net_profile),
          "Location meta.profile must contain Plan-Net profile URL: #{plan_net_profile}"
      end
    end
  end
end