xml version="1.0" encoding="UTF-8"?

HL7.FHIR.UV.SUBSCRIPTIONS-BACKPORT\Subscription Events Operation - FHIR v4.3.0

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
* **Subscription Events Operation**
[<prev](CapabilityStatement-backport-subscription-server-r4.ttl.html) |
[bottom](#bottom)
| [next>](OperationDefinition-backport-subscription-events-testing.html)

This page is part of the Subscriptions R5 Backport (v1.1.0: [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use") 1.1) based on [FHIR v4.3.0](http://hl7.org/fhir/4.3.0). This is the current published version in its permanent home (it will always be available at this URL). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/uv/subscriptions-backport/history.html)

* [Narrative Content](#)
* [XML](OperationDefinition-backport-subscription-events.xml.html)
* [JSON](OperationDefinition-backport-subscription-events.json.html)
* [TTL](OperationDefinition-backport-subscription-events.ttl.html)

## OperationDefinition: Subscription Events Operation

| *Official URL*: http://hl7.org/fhir/uv/subscriptions-backport/OperationDefinition/backport-subscription-events | | | | *Version*: 1.1.0 |
| --- | --- | --- | --- | --- |
| *Standards status:* [Trial-use](http://build.fhir.org/versions.html#std-process "Standard Status") | | | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 0 | *Computable Name*: R5SubscriptionEvents |

This operation is used to search for and return notifications that have been previously triggered by a topic-based Subscription in R4.

URL: [base]/Subscription/[id]/$events

Parameters

| **Use** | **Name** | **Cardinality** | **Type** | **Binding** | **Documentation** |
| --- | --- | --- | --- | --- | --- |
| IN | eventsSinceNumber | 0..1 | [string](http://hl7.org/fhir/R4B/datatypes.html#string) |  | The starting event number, inclusive of this event (lower bound). |
| IN | eventsUntilNumber | 0..1 | [string](http://hl7.org/fhir/R4B/datatypes.html#string) |  | The ending event number, inclusive of this event (upper bound). |
| IN | content | 0..1 | [code](http://hl7.org/fhir/R4B/datatypes.html#code) |  | Requested content style of returned data. Codes from backport-content-value-set (e.g., empty, id-only, full-resource). This is a hint to the server what a client would prefer, and MAY be ignored. |
| OUT | return | 1..1 | [Bundle](http://hl7.org/fhir/R4B/bundle.html) |  | The operation returns a valid notification bundle, with the first entry being the subscription status information resource. The bundle type is "history". |

| [<prev](CapabilityStatement-backport-subscription-server-r4.ttl.html) | [top](#top) | [next>](OperationDefinition-backport-subscription-events-testing.html) |
| --- | --- | --- |

IG © 2020+ [HL7 FHIR Infrastructure WG](https://hl7.org/Special/committees/fiwg). Package hl7.fhir.uv.subscriptions-backport#1.1.0 based on [FHIR 4.3.0](http://build.fhir.org/). Generated 2023-01-11

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/uv/subscriptions-backport/history.html) |
[![CC0](cc0.png)](http://build.fhir.org/license.html) |

[Propose a change](http://hl7.org/fhir-issues)