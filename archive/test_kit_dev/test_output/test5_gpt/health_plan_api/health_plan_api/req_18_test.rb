module Test5Gpt
  class ProfileIdentificationTestGroup < Inferno::TestGroup
    id :req_18_profile_identification
    title 'Profile Identification in Meta Attribute'
    description %(
      Verify that each FHIR resource instance from the Health Plan API
      includes the Plan-Net profiles in the meta.profile attribute.
    )

    input :resource_type, :resource_id

    fhir_client do
      url :server_url
      bearer_token :access_token
    end

    test do
      id :check_meta_profile
      title 'Check meta.profile for Plan-Net profiles'
      description %(
        Ensure that the meta.profile attribute of the resource includes
        the Plan-Net profiles.
      )

      run do
        fhir_read(resource_type.to_sym, resource_id)
        assert_response_status(200)
        assert_valid_resource

        profiles = resource.meta&.profile
        assert profiles.present?, 'meta.profile is missing from the resource'

        plan_net_profiles = [
          'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-organization',
          'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-practitioner',
          'http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-location'
        ]

        profile_found = profiles.any? { |profile| plan_net_profiles.include?(profile) }
        assert profile_found, 'None of the Plan-Net profiles are present in the meta.profile attribute'
      end
    end
  end
end