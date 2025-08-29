module Test5_claude
  class LastUpdateTimestampGroup < Inferno::TestGroup
    id :last_update_timestamp_requirement
    title 'Last Update Timestamp Requirement'
    description %(
      Validates that each profile includes a lastUpdate timestamp as part of its data content.
      
      Requirement REQ-30: Each profile in this guide requires that the lastUpdate timestamp 
      be provided as part of the profile's data content.
    )

    test do
      id :check_last_update_patient
      title 'Patient Profile Last Update Timestamp'
      description 'Verify Patient profile contains lastUpdate timestamp'
      
      run do
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)
        
        patient = resource
        assert !patient.meta.nil?, 'Patient resource must contain meta element'
        assert !patient.meta.lastUpdated.nil?, 'Patient resource must contain lastUpdated timestamp'
        assert patient.meta.lastUpdated.is_a?(Time), 'lastUpdated must be a valid timestamp'
      end
    end

    test do
      id :check_last_update_practitioner
      title 'Practitioner Profile Last Update Timestamp' 
      description 'Verify Practitioner profile contains lastUpdate timestamp'

      run do
        fhir_read(:practitioner, practitioner_id)
        assert_response_status(200)
        assert_resource_type(:practitioner)

        practitioner = resource
        assert !practitioner.meta.nil?, 'Practitioner resource must contain meta element'
        assert !practitioner.meta.lastUpdated.nil?, 'Practitioner resource must contain lastUpdated timestamp'
        assert practitioner.meta.lastUpdated.is_a?(Time), 'lastUpdated must be a valid timestamp'
      end
    end

    test do
      id :check_last_update_organization
      title 'Organization Profile Last Update Timestamp'
      description 'Verify Organization profile contains lastUpdate timestamp'

      run do
        fhir_read(:organization, organization_id)
        assert_response_status(200)
        assert_resource_type(:organization)

        organization = resource
        assert !organization.meta.nil?, 'Organization resource must contain meta element'
        assert !organization.meta.lastUpdated.nil?, 'Organization resource must contain lastUpdated timestamp'
        assert organization.meta.lastUpdated.is_a?(Time), 'lastUpdated must be a valid timestamp'
      end
    end

    test do
      id :check_last_update_location
      title 'Location Profile Last Update Timestamp'
      description 'Verify Location profile contains lastUpdate timestamp'

      run do
        fhir_read(:location, location_id)
        assert_response_status(200)
        assert_resource_type(:location)

        location = resource
        assert !location.meta.nil?, 'Location resource must contain meta element'
        assert !location.meta.lastUpdated.nil?, 'Location resource must contain lastUpdated timestamp'
        assert location.meta.lastUpdated.is_a?(Time), 'lastUpdated must be a valid timestamp'
      end
    end
  end
end