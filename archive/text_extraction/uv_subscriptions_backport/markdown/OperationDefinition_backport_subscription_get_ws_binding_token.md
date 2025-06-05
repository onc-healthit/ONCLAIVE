xml version="1.0" encoding="UTF-8"?

HL7.FHIR.UV.SUBSCRIPTIONS-BACKPORT\Get WS Binding Token for Subscription Operation - FHIR v4.3.0

[![Visit the HL7 website](assets/images/hl7-logo-header.png)](http://hl7.org)

[![Visit the FHIR website](assets/images/fhir-logo-www.png)](http://hl7.org/fhir) 

[![Search FHIR](assets/images/search.png)](searchform.html)

Subscriptions R5 Backport

1.1.0 - Standard for Trial Use
![International flag](assets/images/001.svg "International")

[FHIR](http://build.fhir.org/index.html)

* [Contents](toc.html)
* [Home](index.html)
* [Specification](#)
  + [Actors](actors.html)
  + [Topic-Based Subscription Components](components.html)
  + [Workflow](workflow.html)
  + [Channels](channels.html)
  + [Notifications](notifications.html)
  + [Payload Types](payloads.html)
  + [Conformance](conformance.html)
  + [Handling Errors](errors.html)
* [Safety and Security](safety_security.html)
* [Artifacts](#)
  + [Capability Statements](artifacts.html#1)
  + [Operations](artifacts.html#2)
  + [Search Parameters](artifacts.html#3)
  + [Profiles](artifacts.html#4)
  + [Extensions](artifacts.html#5)
  + [Value Sets](artifacts.html#6)
  + [Examples](artifacts.html#8)
* [Support](#)
  + [Downloads](downloads.html)
  + [Known Implementations](https://confluence.hl7.org/display/FHIRI/FHIR+Subscriptions)

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Get WS Binding Token for Subscription Operation**
[<prev](OperationDefinition-backport-subscription-events.ttl.html) |
[bottom](#bottom)
| [next>](OperationDefinition-backport-subscription-get-ws-binding-token-testing.html)

This page is part of the Subscriptions R5 Backport (v1.1.0: [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use") 1.1) based on [FHIR v4.3.0](http://hl7.org/fhir/4.3.0). This is the current published version in its permanent home (it will always be available at this URL). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/uv/subscriptions-backport/history.html)

* [Narrative Content](#)
* [XML](OperationDefinition-backport-subscription-get-ws-binding-token.xml.html)
* [JSON](OperationDefinition-backport-subscription-get-ws-binding-token.json.html)
* [TTL](OperationDefinition-backport-subscription-get-ws-binding-token.ttl.html)

## OperationDefinition: Get WS Binding Token for Subscription Operation

| *Official URL*: http://hl7.org/fhir/uv/subscriptions-backport/OperationDefinition/backport-subscription-get-ws-binding-token | | | | *Version*: 1.1.0 |
| --- | --- | --- | --- | --- |
| *Standards status:* [Trial-use](http://build.fhir.org/versions.html#std-process "Standard Status") | | | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 0 | *Computable Name*: R5SubscriptionGetWsBindingToken |

This operation is used to get a token for a websocket client to use in order to bind to one or more subscriptions.

URL: [base]/Subscription/$get-ws-binding-token

URL: [base]/Subscription/[id]/$get-ws-binding-token

Parameters

| **Use** | **Name** | **Cardinality** | **Type** | **Binding** | **Documentation** |
| --- | --- | --- | --- | --- | --- |
| IN | id | 0..\* | [id](http://hl7.org/fhir/R4B/datatypes.html#id) |  | At the Instance level, this parameter is ignored. At the Resource level, one or more parameters containing a FHIR id for a Subscription to get a token for. In the absense of any specified ids, the server may either return a token for all Subscriptions available to the caller with a channel-type of websocket or fail the request. |
| OUT | token | 1..1 | [string](http://hl7.org/fhir/R4B/datatypes.html#string) |  | An access token that a client may use to show authorization during a websocket connection. |
| OUT | expiration | 1..1 | [dateTime](http://hl7.org/fhir/R4B/datatypes.html#dateTime) |  | The date and time this token is valid until. |
| OUT | subscription | 0..\* | [string](http://hl7.org/fhir/R4B/datatypes.html#string) |  | The subscriptions this token is valid for. |
| OUT | websocket-url | 1..1 | [url](http://hl7.org/fhir/R4B/datatypes.html#url) |  | The URL the client should use to connect to Websockets. |

| [<prev](OperationDefinition-backport-subscription-events.ttl.html) | [top](#top) | [next>](OperationDefinition-backport-subscription-get-ws-binding-token-testing.html) |
| --- | --- | --- |

IG © 2020+ [HL7 FHIR Infrastructure WG](https://hl7.org/Special/committees/fiwg). Package hl7.fhir.uv.subscriptions-backport#1.1.0 based on [FHIR 4.3.0](http://build.fhir.org/). Generated 2023-01-11

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/uv/subscriptions-backport/history.html) |
[![CC0](cc0.png)](http://build.fhir.org/license.html) |

[Propose a change](http://hl7.org/fhir-issues)