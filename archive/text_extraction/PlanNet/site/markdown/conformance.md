xml version="1.0" encoding="UTF-8"?

HL7.FHIR.UV.SUBSCRIPTIONS-BACKPORT\Conformance - FHIR v4.3.0

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
* [**Specification**](specification.html)
* **Conformance**
[<prev](payloads.html) |
[bottom](#bottom)
| [next>](errors.html)

This page is part of the Subscriptions R5 Backport (v1.1.0: [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use") 1.1) based on [FHIR v4.3.0](http://hl7.org/fhir/4.3.0). This is the current published version in its permanent home (it will always be available at this URL). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/uv/subscriptions-backport/history.html)

## Conformance

* [Conformance in FHIR R4B](#conformance-in-fhir-r4b)
* [Conformance in FHIR R4](#conformance-in-fhir-r4)

This page defines how CapabilityStatements are used and the expectations for mandatory and must support elements. A conformant system SHALL support the resources as profiled by this guide.

Note that the conformance verbs - SHALL, SHOULD, MAY - used in this guide are defined by the [FHIR Conformance Rules](http://hl7.org/fhir/conformance-rules.html).

### Conformance in FHIR R4B

In order to claim conformance with this guide, a server:

* SHALL support the `Subscription` resource (read/write).
* SHALL support the `$status` operation on the `Subscription` resource.
* SHALL support the `SubscriptionTopic` resource (read/search).
* SHALL support at least one channel type, and SHOULD include one from this guide
* SHALL support at least one Payload Type

#### Conformance Artifacts

FHIR Servers claiming conformance to this Implementation Guide must conform to the expectations described in the Capability Statement appropriate to the implemented FHIR version. For FHIR R4B servers, this guide defines the [R4B Server CapabilityStatement](CapabilityStatement-backport-subscription-server.html).

Some options of the Subscriptions Framework are not easily expressed in a `CapabilityStatement`. In addition to the basic support in the CapabilityStatement (e.g., resources, interactions, and operations), a conformant server SHALL support at least one [Payload Type](payloads.html) and SHOULD support one [Channel Type](channels.html) listed in this IG.

Note that the future publication of FHIR R5 may define capabilities included in this specification as cross-version extensions. Since FHIR R5 is currently under development, there are no guarantees these extensions will meet the requirements of this guide. In order to promote widespread compatibility, cross version extensions SHOULD NOT be used on R4 subscriptions to describe any elements described by this guide.

##### Profile Support

Profile Support refers to the support of the profiles defined in this guide in a system exposing FHIR resources. Specifically, a conformant server:

* SHALL communicate all profile data elements that are mandatory by that profile’s StructureDefinition.
* SHOULD declare conformance with the Backport Subscription Server Capability Statement by including its official URL in the server’s `CapabilityStatement.instantiates` element: `http://hl7.org/fhir/uv/subscriptions-backport/CapabilityStatement/CapabilitySubscriptionServer`.
* SHALL specify the full capability details from the CapabilityStatement it claims to implement, including declaring support for the Backport Subscription Profile by including its official URL in the server’s `CapabilityStatement.rest.resource.supportedProfile` element: `http://hl7.org/fhir/uv/subscriptions-backport/StructureDefinition/backport-subscription`

#### Must-support

In this guide, some elements are marked as [Must Support](https://www.hl7.org/fhir/conformance-rules.html#mustSupport). Elements that are flagged as MS are enumerated below, with details on what support means.

##### backport-channel-type

The [backport-channel-type](StructureDefinition-backport-channel-type.html) extension is used to allow for custom channels not described in this guide.

* Server Support

Servers supporting this guide SHALL be able to read values present in this element. A server SHALL reject the subscription request if a client requests an unsupported channel via this element.

* Client Support

Clients supporting this guide MAY support this extension, as necessary for their use case.

##### backport-filter-criteria

The [backport-filter-criteria](StructureDefinition-backport-filter-criteria.html) extension is used to describe the actual filters used in a specific instance of a subscription.

* Server Support

Servers supporting this guide SHALL be able to read values in this extension and SHALL be able to apply filters as described by any Subscription Topics the server advertises support for.

If a server is capable of supporting filter criteria in general but unable to support criteria requested in a subscription, the server SHALL reject the subscription.

* Client Support

Clients supporting this guide SHALL be able to write values in this extension.

##### backport-payload-content

The [backport-payload-content](StructureDefinition-backport-payload-content.html) extension is used to describe the amount of detail included in notification payloads.

* Server Support

Servers supporting this guide SHALL be able to read values from this extension. A server SHALL reject the subscription request if a client asks for a content level the server does not intend to support (e.g., does not meet security requirements). Servers SHALL include information in notifications as described in this guide based on this value.

* Client Support

Clients supporting this guide SHALL be able to write values in this extension.

##### Notification entry: SubscriptionStatus

Notification bundles SHALL contain a FHIR R4B [SubscriptionStatus](http://hl7.org/fhir/R4B/subscriptionstatus.html) as the first entry.

* Server Support

Servers supporting this guide SHALL be able to generate a valid and correct `SubscriptionStatus` resource for each notification. The status entry SHALL be the first entry of each notification bundle.

* Client Support

Clients supporting this guide SHALL be able to process a valid `SubscriptionStatus` resource without errors.

##### Subscription.criteria

The `Subscription.criteria` element is required (cardinality of 1..1), so any compatible implementation SHALL be able to read and/or write as necessary. Compared with the core specification, this guide specifies that the element SHALL contain the canonical URL for the Subscription Topic.

* Server Support

Servers supporting this guide SHALL be able to read values in this element and process requests for subscription topics referenced by it. If a server does not support a requested topic or will not honor the subscription otherwise, a server SHALL reject the subscription request.

* Client Support

Clients supporting this guide SHALL be able to write subscription topic URLs into this element.

### Conformance in FHIR R4

In order to claim conformance with this guide, a server:

* SHALL support the `Subscription` resource (read/write).
* SHALL support the `$status` operation on the `Subscription` resource.
* SHOULD support topic discovery via the [CapabilityStatement SubscriptionTopic Canonical](StructureDefinition-capabilitystatement-subscriptiontopic-canonical.html) extension
* SHALL support at least one channel type, and SHOULD include one from this guide
* SHALL support at least one Payload Type

Note that in FHIR R4, there is no representation of Subscription Topics. Detailed discussion can be found on the [Topic-Based Subscription Components](components.html#subscription-topics-in-r4) page.

#### Conformance Artifacts

FHIR Servers claiming conformance to this Implementation Guide must conform to the expectations described in the Capability Statement appropriate to the implemented FHIR version. For FHIR R4 servers, this guide defines the [R4 Server CapabilityStatement](CapabilityStatement-backport-subscription-server-r4.html).

Some options of the Subscriptions Framework are not easily expressed in a `CapabilityStatement`. In addition to the basic support in the CapabilityStatement (e.g., resources, interactions, and operations), a conformant server SHALL support at least one [Payload Type](payloads.html) and SHOULD support one [Channel Type](channels.html) listed in this IG.

Note that the future publication of FHIR R5 may define capabilities included in this specification as cross-version extensions. Since FHIR R5 is currently under development, there are no guarantees these extensions will meet the requirements of this guide. In order to promote widespread compatibility, cross version extensions SHOULD NOT be used on R4 subscriptions to describe any elements described by this guide.

##### Profile Support

Profile Support refers to the support of the profiles defined in this guide in a system exposing FHIR resources. Specifically, a conformant server:

* SHALL communicate all profile data elements that are mandatory by that profile’s StructureDefinition.
* SHOULD declare conformance with the Backport Subscription Server Capability Statement by including its official URL in the server’s `CapabilityStatement.instantiates` element: `http://hl7.org/fhir/uv/subscriptions-backport/CapabilityStatement/backport-subscription-server-r4`.
* SHALL specify the full capability details from the CapabilityStatement it claims to implement, including declaring support for the Backport Subscription Profile by including its official URL in the server’s `CapabilityStatement.rest.resource.supportedProfile` element: `http://hl7.org/fhir/uv/subscriptions-backport/StructureDefinition/backport-subscription`

#### Must-support

In this guide, some elements are marked as [Must Support](https://www.hl7.org/fhir/conformance-rules.html#mustSupport). Elements that are flagged as MS are enumerated below, with details on what support means.

##### backport-channel-type

The [backport-channel-type](StructureDefinition-backport-channel-type.html) extension is used to allow for custom channels not described in this guide.

* Server Support

Servers supporting this guide SHALL be able to read values present in this element. A server SHALL reject the subscription request if a client requests an unsupported channel via this element.

* Client Support
  Clients supporting this guide MAY support this extension, as necessary for their use case.

##### backport-filter-criteria

The [backport-filter-criteria](StructureDefinition-backport-filter-criteria.html) extension is used to describe the actual filters used in a specific instance of a subscription.

* Server Support

Servers supporting this guide SHALL be able to read values in this extension and SHALL be able to apply filters as described by any Subscription Topics the server advertises support for.

If a server is capable of supporting filter criteria in general but unable to support criteria requested in a subscription, the server SHALL reject the subscription.

* Client Support

Clients supporting this guide SHALL be able to write values in this extension.

##### backport-payload-content

The [backport-payload-content](StructureDefinition-backport-payload-content.html) extension is used to describe the amount of detail included in notification payloads.

* Server Support

Servers supporting this guide SHALL be able to read values from this extension. A server SHALL reject the subscription request if a client asks for a content level the server does not intend to support (e.g., does not meet security requirements). Servers SHALL include information in notifications as described in this guide based on this value.

* Client Support

Clients supporting this guide SHALL be able to write values in this extension.

##### Notification entry: SubscriptionStatus

Notification bundles SHALL contain a FHIR R4 [Parameters](http://hl7.org/fhir/R4/parameters.html) resource, conforming to the [R4 Backported R5 SubscriptionStatus](StructureDefinition-backport-subscription-status-r4.html) profile, as the first entry.

* Server Support

Servers supporting this guide SHALL be able to generate a valid and correct `R4 Backported R5 SubscriptionStatus` resource for each notification. The status entry SHALL be the first entry of each notification bundle.

* Client Support

Clients supporting this guide SHALL be able to process a valid `R4 Backported R5 SubscriptionStatus` resource without errors.

##### Subscription.criteria

The `Subscription.criteria` element is required (cardinality of 1..1), so any compatible implementation SHALL be able to read and/or write as necessary. Compared with the core specification, this guide specifies that the element SHALL contain the canonical URL for the Subscription Topic.

* Server Support

Servers supporting this guide SHALL be able to read values in this element and process requests for subscription topics referenced by it. If a server does not support a requested topic or will not honor the subscription otherwise, a server SHALL reject the subscription request.

* Client Support

Clients supporting this guide SHALL be able to write subscription topic URLs into this element.

| [<prev](payloads.html) | [top](#top) | [next>](errors.html) |
| --- | --- | --- |

IG © 2020+ [HL7 FHIR Infrastructure WG](https://hl7.org/Special/committees/fiwg). Package hl7.fhir.uv.subscriptions-backport#1.1.0 based on [FHIR 4.3.0](http://build.fhir.org/). Generated 2023-01-11

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/uv/subscriptions-backport/history.html) |
[![CC0](cc0.png)](http://build.fhir.org/license.html) |

[Propose a change](http://hl7.org/fhir-issues)