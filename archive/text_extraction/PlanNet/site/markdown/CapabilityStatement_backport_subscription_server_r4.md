xml version="1.0" encoding="UTF-8"?

HL7.FHIR.UV.SUBSCRIPTIONS-BACKPORT\R4 Topic-Based Subscription Server Capability Statement - FHIR v4.3.0

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
* **R4 Topic-Based Subscription Server Capability Statement**
[<prev](CapabilityStatement-backport-subscription-server.ttl.html) |
[bottom](#bottom)
| [next>](CapabilityStatement-backport-subscription-server-r4-testing.html)

This page is part of the Subscriptions R5 Backport (v1.1.0: [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use") 1.1) based on [FHIR v4.3.0](http://hl7.org/fhir/4.3.0). This is the current published version in its permanent home (it will always be available at this URL). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/uv/subscriptions-backport/history.html)

* [Narrative Content](#)
* [XML](CapabilityStatement-backport-subscription-server-r4.xml.html)
* [JSON](CapabilityStatement-backport-subscription-server-r4.json.html)
* [TTL](CapabilityStatement-backport-subscription-server-r4.ttl.html)

## CapabilityStatement: R4 Topic-Based Subscription Server Capability Statement

| *Official URL*: http://hl7.org/fhir/uv/subscriptions-backport/CapabilityStatement/backport-subscription-server-r4 | | | | *Version*: 1.1.0 |
| --- | --- | --- | --- | --- |
| Active as of 2020-11-30 | | | | *Computable Name*: BackportSubscriptionCapabilityStatementR4 |

CapabilityStatement describing the required and optional capabilities of a FHIR Server supporting backported R5 Subscriptions in R4.

This `CapabilityStatement` describes the expected capabilities of a FHIR R4 server supporting this Implementation Guide.

[Raw OpenAPI-Swagger Definition file](backport-subscription-server-r4.openapi.json) | [Download](backport-subscription-server-r4.openapi.json)

### FHIR RESTful Capabilities by Resource/Profile:

#### Summary

| Resource Type | Supported Profiles | Supported Searches | Supported `_includes` | Supported `_revincludes` | Supported Operations |
| --- | --- | --- | --- | --- | --- |
| [Subscription](#subscription) | [Backported R5 Subscription](StructureDefinition-backport-subscription.html) | url, status | - | - | $status, $events, $get-ws-binding-token |

#### Subscription

Conformance Expectation: **SHALL**

Supported Profiles:

* **SHALL** support: [Backported R5 Subscription](StructureDefinition-backport-subscription.html)

Operation Summary:

* **SHALL** support the [$status](OperationDefinition-backport-subscription-status.html) operation
* **MAY** support the [$events](OperationDefinition-backport-subscription-events.html) operation , [$get-ws-binding-token](OperationDefinition-backport-subscription-get-ws-binding-token.html) operation

Fetch and Search Criteria:

* A Server **SHALL** be capable of returning a Subscription resource using: `GET [base]/Subscription/[id]`
* A Server **SHOULD** be capable of creating a Subscription resource using either: `POST [base]/Subscription` or `PUT [base]/Subscription/[id]`
* A Server **SHOULD** be capable of modifying a Subscription resource using either: `PUT [base]/Subscription/[id]` or `PATCH [base]/Subscription/[id]`
* A Server **SHOULD** be capable of deleting a Subscription resource using: `DELETE [base]/Subscription/[id]`
* A Server **SHOULD** be capable of searching for Subscription resources using: `GET [base]/Subscription/?[parameters]`

Search Parameter Summary:

| Conformance | Parameter | Type |
| --- | --- | --- |
| **SHOULD** | [url](http://hl7.org/fhir/subscription.html#search) | uri |
| **SHOULD** | [status](http://hl7.org/fhir/subscription.html#search) | token |

---

| [<prev](CapabilityStatement-backport-subscription-server.ttl.html) | [top](#top) | [next>](CapabilityStatement-backport-subscription-server-r4-testing.html) |
| --- | --- | --- |

IG © 2020+ [HL7 FHIR Infrastructure WG](https://hl7.org/Special/committees/fiwg). Package hl7.fhir.uv.subscriptions-backport#1.1.0 based on [FHIR 4.3.0](http://build.fhir.org/). Generated 2023-01-11

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/uv/subscriptions-backport/history.html) |
[![CC0](cc0.png)](http://build.fhir.org/license.html) |

[Propose a change](http://hl7.org/fhir-issues)