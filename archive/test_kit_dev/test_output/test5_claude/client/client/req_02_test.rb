module Test5_claude
  class NoPiiSendingGroup < Inferno::TestGroup
    id :no_pii_sending_test
    title 'No PII Sending by Clients'
    description %(
      Verify that directory mobile applications do not send consumer identifiable 
      information when querying a Plan-Net service.

      Requirement: A directory mobile application SHALL NOT send consumer 
      identifiable information when querying a Plan-Net service.
    )

    test do
      id :check_no_pii_in_search
      title 'Search requests do not contain PII'
      description %(
        This test verifies that search requests do not contain any personally 
        identifiable information in the parameters or headers.
      )

      # Define inputs needed for test
      input :server_url
      input :bearer_token, optional: true

      run do
        # Setup FHIR client
        fhir_client do
          url :server_url
          bearer_token :bearer_token if bearer_token.present?
        end

        # Make sample search requests that could potentially contain PII
        searches = [
          [:practitioner, {}],
          [:organization, {}],
          [:practitionerrole, {}],
          [:location, {}]
        ]

        searches.each do |resource_type, params|
          fhir_search(resource_type, params: params)

          # Get the request that was made
          request = request_details

          # Check query parameters
          request.query_parameters&.each do |param, value|
            assert !contains_pii?(value), 
              "Search parameter '#{param}' contains PII: #{value}"
          end

          # Check headers
          request.headers&.each do |header, value|
            next if ['authorization', 'content-type'].include?(header.downcase)
            assert !contains_pii?(value),
              "Request header '#{header}' contains PII: #{value}"
          end
        end

        pass 'No PII found in search requests'
      end

      # Helper method to check for PII patterns
      def contains_pii?(value)
        return false if value.nil?
        
        pii_patterns = [
          /\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b/i,  # Email
          /\b\d{3}[-.]?\d{2}[-.]?\d{4}\b/,               # SSN
          /\b\d{3}[-.]?\d{3}[-.]?\d{4}\b/,               # Phone
          /\b\d{5}(?:[-\s]\d{4})?\b/,                    # ZIP
          /\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2},\s+\d{4}\b/i # Dates
        ]

        value = value.to_s
        pii_patterns.any? { |pattern| value.match?(pattern) }
      end
    end
  end
end