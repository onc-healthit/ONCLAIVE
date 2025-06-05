xml version="1.0" encoding="UTF-8"?

HL7.FHIR.UV.SUBSCRIPTIONS-BACKPORT\R4 Notification: Empty - FHIR v4.3.0

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
* **R4 Notification: Empty**
[<prev](CapabilityStatement-r4-capabilitystatement-example-server.ttl.html) |
[bottom](#bottom)
| [next>](Bundle-r4-notification-empty.xml.html)

This page is part of the Subscriptions R5 Backport (v1.1.0: [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use") 1.1) based on [FHIR v4.3.0](http://hl7.org/fhir/4.3.0). This is the current published version in its permanent home (it will always be available at this URL). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/uv/subscriptions-backport/history.html)

* [Narrative Content](#)
* [XML](Bundle-r4-notification-empty.xml.html)
* [JSON](Bundle-r4-notification-empty.json.html)
* [TTL](Bundle-r4-notification-empty.ttl.html)

## Example Bundle: R4 Notification: Empty

|  | |
| --- | --- |

This Bundle provides an example of an `empty` notification. This `Bundle` is typical of what may be posted to a notification endpoint (e.g., a listening HTTP server, etc.).

Bundle r4-notification-empty of type history

---

Entry 1 - fullUrl = urn:uuid:9e41ff6d-5be6-4e6a-8b85-abd4e7f58400

Request:

```
GET https://example.org/fhir/Subscription/admission/$status

```

Response:

```
200

```

Resource Parameters:

> ## Parameters
> 
> | subscription | https://example.org/fhir/Subscription/admission |
> | --- | --- |
> | topic | <http://hl7.org/SubscriptionTopic/admission> |
> | status | active |
> | type | event-notification |
> | events-since-subscription-start | 2 |
> | notification-event |  |
> | event-number | 2 |
> | timestamp | 2020-05-29 11:44:13-0500 |

### Notes:

In order to satisfy the requirements of a `history` Bundle (specifically `bdl-3` and `bdl-4`), note that `Bundle.entry.request` must exist.

For the status resource (`entry[0]`), the request is filled out to match a request to the `$status` operation.

Since this is an `empty` notification and does not include additional entries, no additional constraints are imposed by `Bundle` requirements.

| [<prev](CapabilityStatement-r4-capabilitystatement-example-server.ttl.html) | [top](#top) | [next>](Bundle-r4-notification-empty.xml.html) |
| --- | --- | --- |

IG © 2020+ [HL7 FHIR Infrastructure WG](https://hl7.org/Special/committees/fiwg). Package hl7.fhir.uv.subscriptions-backport#1.1.0 based on [FHIR 4.3.0](http://build.fhir.org/). Generated 2023-01-11

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/uv/subscriptions-backport/history.html) |
[![CC0](cc0.png)](http://build.fhir.org/license.html) |

[Propose a change](http://hl7.org/fhir-issues)