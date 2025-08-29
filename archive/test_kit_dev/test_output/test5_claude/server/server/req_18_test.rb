module Test5_claude
  class ProfileIdentificationGroup < Inferno::TestGroup
    id :profile_identification_meta
    title 'Plan-Net Profile Identification in Meta Attribute'
    description %(
      Verify that Plan-Net profiles are properly identified in the meta.profile 
      attribute for each resource instance.

      Requirement: REQ-18
      Conformance: SHALL
    )

    PLAN_NET_PROFILES = [
      'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization',
      'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Practitioner',
      'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location',
      'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole',
      'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Network',
      'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-InsurancePlan',
      'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Endpoint',
      'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-HealthcareService'
    ].freeze

    test do
      id :verify_organization_profile
      title 'Organization resource declares Plan-Net profile'
      description 'Verify Organization instances include Plan-Net profile in meta.profile'
      
      run do
        fhir_search(:organization)
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        skip_if resource.entry.empty?, 'No Organization resources found'
        
        resource.entry.each do |entry|
          org = entry.resource
          assert org.meta&.profile&.include?(PLAN_NET_PROFILES[0]),
                "Organization resource does not declare Plan-Net profile in meta.profile"
        end
      end
    end

    test do
      id :verify_practitioner_profile  
      title 'Practitioner resource declares Plan-Net profile'
      description 'Verify Practitioner instances include Plan-Net profile in meta.profile'

      run do
        fhir_search(:practitioner)
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        skip_if resource.entry.empty?, 'No Practitioner resources found'
        
        resource.entry.each do |entry|
          pract = entry.resource
          assert pract.meta&.profile&.include?(PLAN_NET_PROFILES[1]),
                "Practitioner resource does not declare Plan-Net profile in meta.profile"
        end
      end
    end

    test do
      id :verify_location_profile
      title 'Location resource declares Plan-Net profile'
      description 'Verify Location instances include Plan-Net profile in meta.profile'
      
      run do
        fhir_search(:location)
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        skip_if resource.entry.empty?, 'No Location resources found'
        
        resource.entry.each do |entry|
          loc = entry.resource
          assert loc.meta&.profile&.include?(PLAN_NET_PROFILES[2]),
                "Location resource does not declare Plan-Net profile in meta.profile"
        end
      end
    end

    test do
      id :verify_practitioner_role_profile
      title 'PractitionerRole resource declares Plan-Net profile'
      description 'Verify PractitionerRole instances include Plan-Net profile in meta.profile'
      
      run do
        fhir_search(:practitionerrole)
        assert_response_status(200)
        assert_resource_type(:bundle)
        
        skip_if resource.entry.empty?, 'No PractitionerRole resources found'
        
        resource.entry.each do |entry|
          role = entry.resource
          assert role.meta&.profile&.include?(PLAN_NET_PROFILES[3]),
                "PractitionerRole resource does not declare Plan-Net profile in meta.profile"
        end
      end
    end
  end
end