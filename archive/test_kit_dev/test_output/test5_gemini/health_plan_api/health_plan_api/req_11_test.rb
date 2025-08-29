# frozen_string_literal: true

module Test5_gemini
  class RestfulBehaviorTest < Inferno::TestGroup
    id :req_11_restful_behavior_implementation
    title 'RESTful Behavior Implementation'
    description %(
      Verify that the Health Plan API implements RESTful behavior according to the FHIR specification.
    )

    test do
      id :req_11_restful_behavior_implementation_test
      title 'Server conforms to RESTful behavior'
      description %(
        This test verifies that the server adheres to the RESTful behavior defined in the FHIR specification.
        It will perform a series of basic CRUD operations on a Patient resource and validate the responses.
      )
      input :patient_id

      run do
        skip_if patient_id.blank?, 'Patient ID is required'

        # Read operation
        fhir_read(:patient, patient_id)
        assert_response_status(200)
        assert_resource_type(:patient)

        # Update operation
        updated_name = { family: 'Updated Family Name' }
        fhir_update(resource.body.merge(name: [updated_name]))
        assert_response_status(200)
        assert_resource_type(:patient)
        assert_equal updated_name, resource.body[:name]&.first, 'Updated name does not match'

        # Delete operation
        fhir_delete(:patient, patient_id)
        assert_response_status(204)

        # Attempt to read deleted resource
        fhir_read(:patient, patient_id)
        assert_response_status(404)
      end
    end
  end
end
