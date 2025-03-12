# Resource Profile: PlannetEndpoint - Detailed Descriptions

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plan-Net Endpoint**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-plannet-Endpoint.html)
* [Detailed Descriptions](#)
* [Mappings](StructureDefinition-plannet-Endpoint-mappings.html)
* [Examples](StructureDefinition-plannet-Endpoint-examples.html)

## Resource Profile: PlannetEndpoint - Detailed Descriptions

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Definitions for the plannet-Endpoint resource profile.

|  |  |
| --- | --- |
| 1. **Endpoint** | |
| Definition | The technical details of an endpoint that can be used for electronic services, such as for web services providing XDS.b or a REST endpoint for another FHIR server. This may include any security context information. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| Invariants | **Defined on this element**  **dom-2**: If the resource is contained in another resource, it SHALL NOT contain nested Resources (: contained.contained.empty()) **dom-3**: If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource (: contained.where((('#'+id in (%resource.descendants().reference | %resource.descendants().as(canonical) | %resource.descendants().as(uri) | %resource.descendants().as(url))) or descendants().where(reference = '#').exists() or descendants().where(as(canonical) = '#').exists() or descendants().where(as(canonical) = '#').exists()).not()).trace('unmatched', id).empty()) **dom-4**: If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated (: contained.meta.versionId.empty() and contained.meta.lastUpdated.empty()) **dom-5**: If a resource is contained in another resource, it SHALL NOT have a security label (: contained.meta.security.empty()) **dom-6**: A resource should have narrative for robust management (: text.`div`.exists()) |
| 2. **Endpoint.id** | |
| Definition | The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Comments | The only time that a resource does not have an id is when it is being submitted to the server using a create operation. |
| 3. **Endpoint.meta** | |
| Definition | The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 4. **Endpoint.meta.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 5. **Endpoint.meta.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Endpoint.meta.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 6. **Endpoint.meta.versionId** | |
| Definition | The version specific identifier, as it appears in the version portion of the URL. This value changes when the resource is created, updated, or deleted. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [id](http://hl7.org/fhir/R4/datatypes.html#id) |
| Comments | The server assigns this value, and ignores what the client specifies, except in the case that the server is imposing version integrity on updates/deletes. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 7. **Endpoint.meta.lastUpdated** | |
| Definition | When the resource last changed - e.g. when the version changed. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [instant](http://hl7.org/fhir/R4/datatypes.html#instant) |
| Comments | This value is always populated except when the resource is first being created. The server / resource manager sets this value; what a client provides is irrelevant. This is equivalent to the HTTP Last-Modified and SHOULD have the same value on a [read](http://hl7.org/fhir/R4/http.html#read) interaction. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 8. **Endpoint.meta.source** | |
| Definition | A uri that identifies the source system of the resource. This provides a minimal amount of [Provenance](http://hl7.org/fhir/R4/provenance.html#) information that can be used to track or differentiate the source of information in the resource. The source may identify another FHIR server, document, message, database, etc. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | In the provenance resource, this corresponds to Provenance.entity.what[x]. The exact use of the source (and the implied Provenance.entity.role) is left to implementer discretion. Only one nominated source is allowed; for additional provenance details, a full Provenance resource should be used.  This element can be used to indicate where the current master source of a resource that has a canonical URL if the resource is no longer hosted at the canonical URL. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 9. **Endpoint.meta.profile** | |
| Definition | A list of profiles (references to [StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html#) resources) that this resource claims to conform to. The URL is a reference to [StructureDefinition.url](http://hl7.org/fhir/R4/structuredefinition-definitions.html#StructureDefinition.url). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [canonical](http://hl7.org/fhir/R4/datatypes.html#canonical)([StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html "http://hl7.org/fhir/StructureDefinition/StructureDefinition")) |
| Comments | It is up to the server and/or other infrastructure of policy to determine whether/how these claims are verified and/or updated over time. The list of profile URLs is a set. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 10. **Endpoint.meta.security** | |
| Definition | Security labels applied to this resource. These tags connect specific resources to the overall security policy and infrastructure. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [All Security Labels](http://hl7.org/fhir/R4/valueset-security-labels.html); other codes may be used where these codes are not suitable Security Labels from the Healthcare Privacy and Security Classification System. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) |
| Comments | The security labels can be updated without changing the stated version of the resource. The list of security labels is a set. Uniqueness is based the system/code, and version and display are ignored. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 11. **Endpoint.meta.tag** | |
| Definition | Tags applied to this resource. Tags are intended to be used to identify and relate resources to process and workflow, and applications are not required to consider the tags when interpreting the meaning of a resource. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | For example codes, see [CommonTags](http://hl7.org/fhir/R4/valueset-common-tags.html) Codes that represent various types of tags, commonly workflow-related; e.g. "Needs review by Dr. Jones". |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) |
| Comments | The tags can be updated without changing the stated version of the resource. The list of tags is a set. Uniqueness is based the system/code, and version and display are ignored. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 12. **Endpoint.implicitRules** | |
| Definition | A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Comments | Asserting this rule set restricts the content to be only understood by a limited set of trading partners. This inherently limits the usefulness of the data in the long term. However, the existing health eco-system is highly fractured, and not yet ready to define, collect, and exchange data in a generally computable sense. Wherever possible, implementers and/or specification writers should avoid using this element. Often, when used, the URL is a reference to an implementation guide that defines these special rules as part of it's narrative along with other profiles, value sets, etc. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 13. **Endpoint.language** | |
| Definition | The base language in which the resource is written. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHOULD be taken from [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html) [Max Binding](http://hl7.org/fhir/R4/extension-elementdefinition-maxvalueset.html "Max Value Set Extension"): [AllLanguages](http://hl7.org/fhir/R4/valueset-all-languages.html) A human language. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| Comments | Language is provided to support indexing and accessibility (typically, services such as text to speech use the language tag). The html language tag in the narrative applies to the narrative. The language tag on the resource may be used to specify the language of other presentations generated from the data in the resource. Not all the content has to be in the base language. The Resource.language should not be assumed to apply to the narrative automatically. If a language is specified, it should it also be specified on the div element in the html (see rules in HTML5 for information about the relationship between xml:lang and the html lang attribute). |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 14. **Endpoint.text** | |
| Definition | A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Narrative](http://hl7.org/fhir/R4/datatypes.html#Narrative) |
| Alternate Names | narrative, html, xhtml, display |
| Comments | Contained resources do not have narrative. Resources that are not contained SHOULD have a narrative. In some cases, a resource may only have text with little or no additional discrete data (as long as all minOccurs=1 elements are satisfied). This may be necessary for data from legacy systems where information is captured as a "text blob" or where text is additionally entered raw or narrated and encoded information is added later. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 15. **Endpoint.contained** | |
| Definition | These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Resource](http://hl7.org/fhir/R4/resource.html) |
| Alternate Names | inline resources, anonymous resources, contained resources |
| Comments | This should never be done when the content can be identified properly, as once identification is lost, it is extremely difficult (and context dependent) to restore it again. Contained resources may have profiles and tags In their meta elements, but SHALL NOT have security labels. |
| 16. **Endpoint.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Endpoint.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 17. **Endpoint.extension:endpoint-usecase** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | endpoint-usecase |
| Definition | EndpointUseCase is an enumeration of the specific use cases (service descriptions) supported by the endpoint |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* This element is affected by the following invariants: ele-1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)([EndpointUsecase](StructureDefinition-endpoint-usecase.html "[CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/endpoint-usecase]]")) (Complex Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 18. **Endpoint.modifierExtension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Modifier extensions allow for extensions that *cannot* be safely ignored to be clearly distinguished from the vast majority of extensions which can be safely ignored. This promotes interoperability by eliminating the need for implementers to prohibit the presence of extensions. For further information, see the [definition of modifier extensions](http://hl7.org/fhir/R4/extensibility.html#modifierExtension). |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 19. **Endpoint.identifier** | |
| Definition | Identifier for the organization that is used to identify the endpoint across multiple disparate systems. |
| Note | This is a business identifier, not a resource identifier (see [discussion](http://hl7.org/fhir/R4/resource.html#identifiers)) |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 20. **Endpoint.status** | |
| Definition | active | suspended | error | off | test. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [EndpointStatus](http://hl7.org/fhir/R4/valueset-endpoint-status.html) The status of the endpoint. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | This element is labeled as a modifier because the status contains codes that mark the endpoint as not currently valid. |
| Fixed Value | active |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 21. **Endpoint.connectionType** | |
| Definition | A coded value that represents the technical details of the usage of this endpoint, such as what WSDLs should be used in what way. (e.g. XDS.b/DICOM/cds-hook). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [Endpoint Connection Types VS](ValueSet-EndpointConnectionTypeVS.html); other codes may be used where these codes are not suitable [Min Binding](http://hl7.org/fhir/R4/extension-elementdefinition-minvalueset.html "Min Value Set Extension"): [Minimum Endpoint Connection Types VS](ValueSet-MinEndpointConnectionTypeVS.html) |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | For additional connectivity details for the protocol, extensions will be used at this point, as in the XDS example. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 22. **Endpoint.name** | |
| Definition | A friendly name that this endpoint can be referred to with. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 23. **Endpoint.managingOrganization** | |
| Definition | The organization that manages this endpoint (even if technically another organization is hosting this in the cloud, it is the organization associated with the data). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetOrganization](StructureDefinition-plannet-Organization.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | This property is not typically used when searching for Endpoint resources for usage. The typical usage is via the reference from an applicable Organization/Location/Practitioner resource, which is where the context is provided. Multiple Locations may reference a single endpoint, and don't have to be within the same organization resource, but most likely within the same organizational hierarchy. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 24. **Endpoint.contact** | |
| Definition | Contact details for a human to contact about the subscription. The primary use of this for system administrator troubleshooting. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 25. **Endpoint.contact.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 26. **Endpoint.contact.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Endpoint.contact.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 27. **Endpoint.contact.system** | |
| Definition | Telecommunications form for contact point - what communications system is required to make use of the contact. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 This element is affected by the following invariants: cpt-2 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [ContactPointSystem](http://hl7.org/fhir/R4/valueset-contact-point-system.html) Telecommunications form for contact point. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 28. **Endpoint.contact.value** | |
| Definition | The actual contact point details, in a form that is meaningful to the designated communication system (i.e. phone number or email address). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Need to support legacy numbers that are not in a tightly controlled format. |
| Comments | Additional text data such as phone extension numbers, or notes about use of the contact are sometimes included in the value. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 29. **Endpoint.contact.use** | |
| Definition | Identifies the purpose for the contact point. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [ContactPointUse](http://hl7.org/fhir/R4/valueset-contact-point-use.html) Use of contact point. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Need to track the way a person uses this contact, so a user can choose which is appropriate for their purpose. |
| Comments | Applications can assume that a contact is current unless it explicitly says that it is temporary or old. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 30. **Endpoint.contact.rank** | |
| Definition | Specifies a preferred order in which to use a set of contacts. ContactPoints with lower rank values are more preferred than those with higher rank values. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [positiveInt](http://hl7.org/fhir/R4/datatypes.html#positiveInt) |
| Comments | Note that rank does not necessarily follow the order in which the contacts are represented in the instance. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 31. **Endpoint.contact.period** | |
| Definition | Time period when the contact point was/is in use. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 32. **Endpoint.period** | |
| Definition | The interval during which the endpoint is expected to be operational. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 33. **Endpoint.payloadType** | |
| Definition | The payload type describes the acceptable content that can be communicated on the endpoint. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [Endpoint Payload Types VS](ValueSet-EndpointPayloadTypeVS.html); other codes may be used where these codes are not suitable |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | The payloadFormat describes the serialization format of the data, where the payloadType indicates the specific document/schema that is being transferred; e.g. DischargeSummary or CarePlan. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 34. **Endpoint.payloadMimeType** | |
| Definition | The mime type to send the payload in - e.g. application/fhir+xml, application/fhir+json. If the mime type is not specified, then the sender could send any content (including no content depending on the connectionType). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [Mime Types](http://hl7.org/fhir/R4/valueset-mimetypes.html) The mime type of an attachment. Any valid mime type is allowed. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | Sending the payload has obvious security consequences. The server is responsible for ensuring that the content is appropriately secured. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 35. **Endpoint.address** | |
| Definition | The uri that describes the actual end-point to connect to. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [url](http://hl7.org/fhir/R4/datatypes.html#url) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | For rest-hook, and websocket, the end-point must be an http: or https: URL; for email, a mailto: url, for sms, a tel: url, and for message the endpoint can be in any form of url the server understands (usually, http: or mllp:). The URI is allowed to be relative; in which case, it is relative to the server end-point (since there may be more than one, clients should avoid using relative URIs)  This address will be to the service base, without any parameters, or sub-services or resources tacked on.  E.g. for a WADO-RS endpoint, the url should be "https://pacs.hospital.org/wado-rs"  and not "https://pacs.hospital.org/wado-rs/studies/1.2.250.1.59.40211.12345678.678910/series/1.2.250.1.59.40211.789001276.14556172.67789/instances/...". |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 36. **Endpoint.header** | |
| Definition | Additional headers / information to send as part of the notification. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Comments | Exactly what these mean depends on the channel type. The can convey additional information to the recipient and/or meet security requirements. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |