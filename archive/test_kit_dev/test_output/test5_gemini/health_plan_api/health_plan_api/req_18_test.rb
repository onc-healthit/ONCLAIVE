module Test5_gemini
  class Req18ProfileIdentification < Inferno::TestGroup
    id :req_18_profile_identification
    title 'REQ-18: Profile Identification in Meta Attribute'
    description %(
      Verify that the Plan-Net profiles supported are identified in the FHIR meta.profile attribute for each instance.
    )

    test do
      id :req_18_profile_present
      title 'Meta.profile attribute contains at least one Plan-Net profile'
      description %(
        Each resource instance SHALL have a meta.profile attribute that lists all profiles the resource instance claims conformance to.
      )
      input :resource_type,
            title: 'Resource Type',
            description: 'The type of resource to read',
            default: 'Patient'
      input :resource_id,
            title: 'Resource ID',
            description: 'The ID of the resource to read'

      run do
        fhir_read(resource_type, resource_id)
        assert_response_status(200)
        assert_valid_resource

        assert resource.meta&.profile&.present?, 'Resource does not contain a meta.profile attribute'
        assert resource.meta.profile.any? { |profile| profile.start_with?('http://hl7.org/fhir/us/plannet') }, 'Resource meta.profile does not contain any Plan-Net profiles'
      end
    end
  end
end