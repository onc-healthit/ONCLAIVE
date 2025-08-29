# frozen_string_literal: true

module Test5_gemini
  class Req16UnknownResourceResponseTest < Inferno::Test
    id :req_16_unknown_resource_response
    title 'Health Plan API returns 404 status for unknown resource'
    description %(
      This test verifies that the server returns a 404 (Not Found) status code
      when attempting to access an unknown resource.
    )

    run do
      fhir_get(resource_type: 'ThisIsNotARealResource')

      assert_response_status(404)
    end
  end
end