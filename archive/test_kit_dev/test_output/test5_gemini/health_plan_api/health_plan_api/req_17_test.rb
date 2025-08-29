# frozen_string_literal: true

module Test5_gemini
  class Req17DeletedResourceResponseTest < Inferno::Test
    id :req_17_deleted_resource_response
    title 'Deleted resource returns HTTP 410 (Gone)'
    description %(
      This test verifies that the server returns an HTTP 410 status code when
      attempting to read a resource that has been deleted.
    )

    input :deleted_resource_id,
          title: 'Deleted Resource ID',
          description: 'The ID of a resource that has been deleted.',
          required: true

    run do
      fhir_read(:patient, deleted_resource_id)
      assert_response_status(410)
    end
  end
end