# frozen_string_literal: true

module Test5_gemini
  class Req22ReverseChainingSupportTest < Inferno::Test
    id :req_22_reverse_chaining_support
    title 'Support reverse chaining on all search parameters that specify the \'chain\' property'
    description %(
      This test verifies that the server supports reverse chaining on all search parameters that specify the 'chain' property.
    )

    def self.metadata
      @metadata ||= YAML.load_file(File.join(__dir__, 'metadata.yml'))
    end

    def data_for_assertion(search_param)
      {
        search_param_url: search_param[:url],
        search_param_name: search_param[:name],
        resource_type: search_param[:resource]
      }
    end

    test 'Reverse chaining support' do
      metadata[:searches].each do |resource_type, search_params|
        search_params.each do |search_param_name, search_param|
          skip_if search_param[:chain].blank?, "Search parameter #{search_param_name} for resource type #{resource_type} does not specify 'chain' property."

          search_param[:chain].each do |chain_name|
            begin
              fhir_search_interaction(
                resource_type: resource_type,
                search_params: { chain_name => 'example' }
              )

              assert_response_status(200), "Failed to search resource type #{resource_type} with chain #{chain_name}."
            rescue Inferno::AssertionException => e
              assert false, e.message, data: data_for_assertion(search_param)
            end
          end
        end
      end
    end
  end
end