xml version="1.0" encoding="UTF-8"?

HL7.FHIR.UV.SUBSCRIPTIONS-BACKPORT\Topic-Based Subscription Components - FHIR v4.3.0

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
* **Topic-Based Subscription Components**
[<prev](actors.html) |
[bottom](#bottom)
| [next>](workflow.html)

This page is part of the Subscriptions R5 Backport (v1.1.0: [STU](https://confluence.hl7.org/display/HL7/HL7+Balloting "Standard for Trial-Use") 1.1) based on [FHIR v4.3.0](http://hl7.org/fhir/4.3.0). This is the current published version in its permanent home (it will always be available at this URL). For a full list of available versions, see the [Directory of published versions ![](external.png)](http://hl7.org/fhir/uv/subscriptions-backport/history.html)

## Topic-Based Subscription Components

* [Subscription Topics](#subscription-topics)
* [Subscriptions](#subscriptions)
* [Subscription Notifications](#subscription-notifications)

The FHIR Topic-Based Subscription Model is composed of three parts:

* [Subscription Topic](#subscription-topics)
  + What is it?
    - Defines the **what** is used to trigger notifications
    - Defines the **filters** allowed to clients
    - Defines the **shape** of the notification
    - Always referenced by canonical URL
  + How is it defined?
    - FHIR R4: [out of scope](#subscription-topics-in-r4)
    - FHIR R4B: [SubscriptionTopic](http://hl7.org/fhir/R4B/subscriptiontopic.html) resource
* [Subscription](#subscriptions)
  + What is it?
    - Describes a request to be notified about events defined by a `SubscriptionTopic`
      * Canonical URL reference to a `SubscriptionTopic`
      * Set **filters** on events (as allowed in the referenced `SubscriptionTopic`)
    - Describe the `channel` and `endpoint` used to send notifications
    - Describe the **payload** included in notifications (MIME type, content level, etc.)
  + How is it defined?
    - FHIR R4: A [Subscription](http://hl7.org/fhir/R4/subscription.html) resource with extensions
    - FHIR R4B: A [Subscription](http://hl7.org/fhir/R4B/subscription.html) resource with extensions
* [Notification Bundle](#subscription-notifications)
  + What is it?
    - Describes the contents of a notification
    - Contains zero or more notification **payloads**
  + How is it defined?
    - FHIR R4:
      * A [Bundle](http://hl7.org/fhir/R4/bundle.html) resource with type `history`,
      * a [Parameters](http://hl7.org/fhir/R4/parameters.html) resource using the [Backport SubscriptionStatus Profile](StructureDefinition-backport-subscription-status-r4.html), and
      * zero or more additional entries, with either URLs or resources representing contents.
    - FHIR R4B:
      * A [Bundle](http://hl7.org/fhir/R4B/bundle.html) resource with type `history`,
      * a [SubscriptionStatus](http://hl7.org/fhir/subscriptionstatus.html) resource, and
      * zero or more additional entries, with either URLs or resources representing contents.

### Subscription Topics

In FHIR R4B and later, the `SubscriptionTopic` resource is used to define conceptual or computable events for `Subscription` resources. Conceptually, subscription topics specify an event or change in data that is used to trigger a notification. Topic definitions also include the boundaries around what a Subscription can filter for and additional resources that MAY be included with notifications.

For example, a topic may define that notifications should be sent when an `Encounter` is created or updated to have the specific value of `status=in-progress`. The topic may also specify that filters may only be applied to the Patient (`Encounter.subject` where subject is a Patient) referenced by the Encounter, and that notifications may include the relevant Patient resource.

Detailed information about the [SubscriptionTopic](http://hl7.org/fhir/subscriptiontopic.html) resource can be found on the HL7 FHIR website.

In order to make subscription topics more widely available, support for `SubscriptionTopic` resources is available via the [FHIR Registry](http://registry.fhir.org).

#### Subscription Topics in R4

`SubscriptionTopic` resources contain information that is difficult to model without an appropriate resource to start from. There was an attempt to profile the `Basic` resource with extensions, but the complexity resulted in very low usability. Combined with use-case evaluation indicated that the most urgent and likely support of topic-based subscriptions would be relying on pre-defined topics with fixed canonical URLs (e.g., topics defined by an Implementation Guide), it was decided to leave topic definitions out-of-scope in R4.

In order to allow for discovery of supported subscription topics, this guide defines the [CapabilityStatement SubscriptionTopic Canonical](StructureDefinition-capabilitystatement-subscriptiontopic-canonical.html) extension. The extension allows server implementers to advertise the canonical URLs of topics available to clients and allows clients to see the list of supported topics on a server. The extension is expected to appear, if supported, on the `Subscription` resource entry. Note that servers are NOT required to advertise supported topics via this extension. Supported topics can also be advertised, for example, by the `CapabilityStatement.instantiates` or `CapabilityStatement.implementationGuide` elements of a CapabilityStatement, as defined by another Implementation Guide. Finally, FHIR R4 servers MAY choose to leave topic discovery completely out-of-band and part of other steps, such as registration or integration.

Full definitions of subscription topics are considered out-of-scope for FHIR R4 implementations. Since the full topic definitions are out-of-scope, FHIR R4 servers are not able to support custom topics submitted by clients. If that functionality is required, a server may choose to expose a limited R4B endpoint to enable such support.

Implementers adding server-side support for topic-based subscriptions are encouraged (but not required) to use the R4B or R5 definitions internally, in order to ease the transition to future versions.

### Subscriptions

The `Subscription` resource is used to request notifications for a specific client about a specific topic. Conceptually, a subscription is a concrete request for a single client to receive notifications per a single topic.

For example, a subscription may ask for notifications based on an ‘Encounter in-progress’ topic, such as the one briefly described as an example in [Subscription Topics](#subscription-topics). The subscription requires a link to the canonical URL of the topic, such as `http://server.example.org/fhir/subscriptiontopics/encounter-in-progress`, information about the channel, such as requesting notifications via `rest-hook` to the endpoint at `http://client.example.org/notification-endpoint/abc`), and payload configuration, such as requesting that bundles are encoded as `application/fhir+json` and include only identifiers (`id-only`). Additionally, a subscription sets the filters which are applied to determine when notifications should be sent, such as indicating that only notifications for `Patient/123` should be sent. More details about filters can be found in the [Subscription Filters](#subscription-filters) section.

In order to support topic-based subscriptions in R4, this guide defines several extensions for use on the [R4 Subscription](http://hl7.org/fhir/subscription.html) resource. A list of extensions defined by this guide can be found on the [Artifacts](artifacts.html#3) page. Note that the future FHIR R5 publication may define capabilities included in this specification as cross-version extensions. Since the FHIR R5 is currently under development, there are no guarantees these extensions will meet the requirements of this guide. In order to promote widespread compatibility, cross version extensions SHOULD NOT be used on R4 subscriptions to describe any elements also described by this guide

In order to link a `Subscription` to a `SubscriptionTopic` and prevent any confusion between the R4 query-based and topic-based implementations, the link to a `SubscriptionTopic` is specified in the `Subscription.criteria` field. For more details, please see the [Subscription Profile](StructureDefinition-backport-subscription.html) in this guide.

#### Subscription Filters

While Subscription Topics are responsible for declaring the triggers for notifications (e.g., a new observation has been created, a medication dispense has occurred, etc.), the subscription itself MAY contain filters to further refine results. For example, a topic could trigger all new observations, while a filter could indicate interest in only lab results or observations relating to a specific patient.

Information about defining filters can be found on the [R4B SubscriptionTopicResource](https://hl7.org/fhir/R4B/subscriptiontopic.html#filters).

In FHIR R5, the usage of filters matches the definition structure - i.e., elements for the `resourceType`, `filterParameter`, `modifier`, and `value`. However, modeling that number of elements in extensions is cumbersome and a relevant syntax already exists. The [R5 FilterBy Criteria](StructureDefinition-backport-filter-criteria.html) extension contains filter information, formatted according to the search syntax defined by the FHIR core specification.

In filter criteria strings, a `filterParameter`, as defined by the relevant `SubscriptionTopic` is used in the place of a search parameter. A server MAY support search parameters not listed by a topic definition (e.g., if filtering is applied to a `Patient`, the server can honor filters for `Patient.name` even if the topic does not expose them), however topic authors are encouraged to explicitly list any parameters for best interoperability.

The valid formats for criteria are:

* `[filterParameter]=[value]`
* `[filterParameter]:[modifier]=[value]`
* `[resourceType].[filterParameter]=[value]`
* `[resourceType].[filterParameter]:[modifier]=[value]`

Note that `resourceType` is only necessary for disambiguation in the case where there are filter parameters with the same code exposed for multiple resources available for filtering within a specific topic. Even in the cases where this is true (e.g., hoisting existing search parameters), it is preferable for the topic definition to assign unique names for simplicity.

#### Subscriptions and FHIR Versions

Note that subscription notifications, by default, are made using the same FHIR version as the server. The `Subscription.channel.payload` element can be used to specify a different FHIR version, using syntax and values defined by the [MIME Type Parameter](https://hl7.org/fhir/versioning.html#mt-version). Servers SHALL look for this parameter during subscription negotiation and SHALL not accept requests for notification FHIR versions it cannot support (servers MAY reject or coerce, according to their policies).

For example, a request for notifications encoded as `application/fhir+json; fhirVersion=4.3` explicitly asks for notifications conforming to the FHIR R4B notification format, while a request for `application/fhir+json; fhirVersion=4.0` explicitly asks for notifications conformant to FHIR R4. This mechanism allows for more flexibility during upgrades, ensuring that servers and clients can continue to operate across version changes.

More information about the differences in notifications can be found on the [Notifications](notifications.html) page.

#### Accepting Subscription Requests

When a FHIR Server accepts a request to create a `Subscription`, the server is indicating to the client that the server:

* is capable of detecting when events covered by the requested SubscriptionTopic occur, and
* is willing to make a simple best effort attempt at delivering a notification for each occurrence of a matching event.

When processing a request for a `Subscription`, following are *some* checks that a server SHOULD validate:

* that the `SubscriptionTopic` is valid and implemented by the server
* that all requested filters are defined in the requested topic and are implemented in the server
* that the channel type is known and implemented by the server
* that the channel endpoint is valid for the channel provided (e.g., is it a valid URL of the expected type)
* that the payload configuration is known and implemented by the server
* that the payload configuration is valid for the channel type requested (e.g., complies with the server’s security policy)

### Subscription Notifications

In FHIR R5, a new type of `Bundle` has been introduced, which uses the new `SubscriptionStatus` resource to convey status information in notifications. Support for earlier FHIR versions has been designed to offer similar functionality and serialized data.

In both FHIR R4 and R4B, notifications are based on a [history Bundle](http://hl7.org/fhir/bundle.html#history). The first entry always contains `SubscriptionStatus` information, encoded as either a [Parameters](http://hl7.org/fhir/R4/parameters.html) resource using the [Backport SubscriptionStatus Profile](StructureDefinition-backport-subscription-status-r4.html) in FHIR R4 or a [SubscriptionStatus](http://hl7.org/fhir/subscriptionstatus.html) resource in FHIR R4B.

Note that since notifications use `history` type Bundles, all notifications need to comply with the requirements for that bundle type. Specifically, there are two invariants on Bundle (`bdl-3` and `bdl-4`) that require a `Bundle.entry.request` element for *every* `Bundle.entry`.

* For the status resource (`entry[0]`), the request SHALL be filled out to match a request to the `$status` operation.
* For additional entries, the request SHOULD be filled out in a way that makes sense given the subscription (e.g., a `POST` or `PUT` operation on the resource, etc.). However, a server MAY choose to simply include a `GET` to the relevant resource instead.

Detailed information about notifications, including the differences between FHIR R4 and R4B, can be found on the [Notifications](notifications.html) page.

#### Scoping Responsibilities

Unless otherwise specified by a server implementation and channel, the Subscriptions Framework does not involve guaranteed delivery of notifications. While the Subscriptions Framework is able to support such mechanisms, defining them are beyond the scope of the standard or this guide.

Servers SHOULD detect errors and take appropriate action where possible. In general, this boundary is when the notification is delivered. For example, during a REST-hook notification, the subscription server can detect errors up until the REST endpoint returns a HTTP status code (e.g., 200). This does not imply that a client successfully processed (or even received) a notification - simply that the server has sent the notification successfully.

Therefore, clients SHOULD be aware of some limitations regarding delivery. In particular:

* Some notifications might not be delivered.
* Some notifications might be delivered multiple times.

In order to mitigate the impact from the above issues, the Subscriptions Framework includes mechanisms to detect both scenarios. Details can be found on the [Errors Page](errors.html).

#### Cross Version Analysis

This is an R4B IG. None of the features it uses are changed in R4, so it can be used as is with R4 systems. Packages for both [R4 (hl7.fhir.uv.subscriptions-backport.r4)](package.r4.tgz) and [R4B (hl7.fhir.uv.subscriptions-backport.r4b)](package.r4b.tgz) are available.

The following resources are not in the R4 version:

* [Bundle/r4b-notification-empty](Bundle-r4b-notification-empty.html)
* [Bundle/r4b-notification-error](Bundle-r4b-notification-error.html)
* [Bundle/r4b-notification-full-resource](Bundle-r4b-notification-full-resource.html)
* [Bundle/r4b-notification-handshake](Bundle-r4b-notification-handshake.html)
* [Bundle/r4b-notification-heartbeat](Bundle-r4b-notification-heartbeat.html)
* [Bundle/r4b-notification-id-only](Bundle-r4b-notification-id-only.html)
* [Bundle/r4b-notification-multi-resource](Bundle-r4b-notification-multi-resource.html)
* [CapabilityStatement/backport-subscription-server](CapabilityStatement-backport-subscription-server.html)
* [SubscriptionStatus/r4b-notification-status](SubscriptionStatus-r4b-notification-status.html)
* [R4B Topic-Based Subscription Notification Bundle](StructureDefinition-backport-subscription-notification.html)

| [<prev](actors.html) | [top](#top) | [next>](workflow.html) |
| --- | --- | --- |

IG © 2020+ [HL7 FHIR Infrastructure WG](https://hl7.org/Special/committees/fiwg). Package hl7.fhir.uv.subscriptions-backport#1.1.0 based on [FHIR 4.3.0](http://build.fhir.org/). Generated 2023-01-11

Links: [Table of Contents](toc.html) |
[QA Report](qa.html)
| [Version History](http://hl7.org/fhir/uv/subscriptions-backport/history.html) |
[![CC0](cc0.png)](http://build.fhir.org/license.html) |

[Propose a change](http://hl7.org/fhir-issues)