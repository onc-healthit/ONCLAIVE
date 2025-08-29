module Test5_gemini
  class Req02NoPiiSending < Inferno::TestGroup
    id :req_02_no_pii_sending
    title 'REQ-02: No PII Sending by Clients'
    description %(
      A directory mobile application SHALL NOT send consumer identifiable information when querying a Plan-Net service.
    )

    test do
      id :req_02_no_pii_sending_test
      title 'Directory mobile application does not send PII in Plan-Net queries'
      description %(
        Verify that the application does not send consumer identifiable information (PII) when making requests to the Plan-Net service.
      )

      run do
        skip 'Test not implemented. Please manually verify that the application does not send PII in Plan-Net queries.'
      end
    end
  end
end
