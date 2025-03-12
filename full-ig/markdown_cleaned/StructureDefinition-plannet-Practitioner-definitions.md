# Resource Profile: PlannetPractitioner - Detailed Descriptions

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plan-Net Practitioner**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-plannet-Practitioner.html)
* [Detailed Descriptions](#)
* [Mappings](StructureDefinition-plannet-Practitioner-mappings.html)
* [Examples](StructureDefinition-plannet-Practitioner-examples.html)

## Resource Profile: PlannetPractitioner - Detailed Descriptions

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Definitions for the plannet-Practitioner resource profile.

|  |  |
| --- | --- |
| 1. **Practitioner** | |
| Definition | This is basic constraint on provider for use in US Core resources. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| Alternate Names | Provider |
| Invariants | **Defined on this element**  **dom-2**: If the resource is contained in another resource, it SHALL NOT contain nested Resources (: contained.contained.empty()) **dom-3**: If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource (: contained.where((('#'+id in (%resource.descendants().reference | %resource.descendants().as(canonical) | %resource.descendants().as(uri) | %resource.descendants().as(url))) or descendants().where(reference = '#').exists() or descendants().where(as(canonical) = '#').exists() or descendants().where(as(canonical) = '#').exists()).not()).trace('unmatched', id).empty()) **dom-4**: If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated (: contained.meta.versionId.empty() and contained.meta.lastUpdated.empty()) **dom-5**: If a resource is contained in another resource, it SHALL NOT have a security label (: contained.meta.security.empty()) **dom-6**: A resource should have narrative for robust management (: text.`div`.exists()) |
| 2. **Practitioner.id** | |
| Definition | The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Comments | The only time that a resource does not have an id is when it is being submitted to the server using a create operation. |
| 3. **Practitioner.meta** | |
| Definition | The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 4. **Practitioner.meta.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 5. **Practitioner.meta.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Practitioner.meta.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 6. **Practitioner.meta.versionId** | |
| Definition | The version specific identifier, as it appears in the version portion of the URL. This value changes when the resource is created, updated, or deleted. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [id](http://hl7.org/fhir/R4/datatypes.html#id) |
| Comments | The server assigns this value, and ignores what the client specifies, except in the case that the server is imposing version integrity on updates/deletes. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 7. **Practitioner.meta.lastUpdated** | |
| Definition | When the resource last changed - e.g. when the version changed. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [instant](http://hl7.org/fhir/R4/datatypes.html#instant) |
| Comments | This value is always populated except when the resource is first being created. The server / resource manager sets this value; what a client provides is irrelevant. This is equivalent to the HTTP Last-Modified and SHOULD have the same value on a [read](http://hl7.org/fhir/R4/http.html#read) interaction. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 8. **Practitioner.meta.source** | |
| Definition | A uri that identifies the source system of the resource. This provides a minimal amount of [Provenance](http://hl7.org/fhir/R4/provenance.html#) information that can be used to track or differentiate the source of information in the resource. The source may identify another FHIR server, document, message, database, etc. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | In the provenance resource, this corresponds to Provenance.entity.what[x]. The exact use of the source (and the implied Provenance.entity.role) is left to implementer discretion. Only one nominated source is allowed; for additional provenance details, a full Provenance resource should be used.  This element can be used to indicate where the current master source of a resource that has a canonical URL if the resource is no longer hosted at the canonical URL. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 9. **Practitioner.meta.profile** | |
| Definition | A list of profiles (references to [StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html#) resources) that this resource claims to conform to. The URL is a reference to [StructureDefinition.url](http://hl7.org/fhir/R4/structuredefinition-definitions.html#StructureDefinition.url). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [canonical](http://hl7.org/fhir/R4/datatypes.html#canonical)([StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html "http://hl7.org/fhir/StructureDefinition/StructureDefinition")) |
| Comments | It is up to the server and/or other infrastructure of policy to determine whether/how these claims are verified and/or updated over time. The list of profile URLs is a set. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 10. **Practitioner.meta.security** | |
| Definition | Security labels applied to this resource. These tags connect specific resources to the overall security policy and infrastructure. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [All Security Labels](http://hl7.org/fhir/R4/valueset-security-labels.html); other codes may be used where these codes are not suitable Security Labels from the Healthcare Privacy and Security Classification System. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) |
| Comments | The security labels can be updated without changing the stated version of the resource. The list of security labels is a set. Uniqueness is based the system/code, and version and display are ignored. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 11. **Practitioner.meta.tag** | |
| Definition | Tags applied to this resource. Tags are intended to be used to identify and relate resources to process and workflow, and applications are not required to consider the tags when interpreting the meaning of a resource. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | For example codes, see [CommonTags](http://hl7.org/fhir/R4/valueset-common-tags.html) Codes that represent various types of tags, commonly workflow-related; e.g. "Needs review by Dr. Jones". |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) |
| Comments | The tags can be updated without changing the stated version of the resource. The list of tags is a set. Uniqueness is based the system/code, and version and display are ignored. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 12. **Practitioner.implicitRules** | |
| Definition | A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Comments | Asserting this rule set restricts the content to be only understood by a limited set of trading partners. This inherently limits the usefulness of the data in the long term. However, the existing health eco-system is highly fractured, and not yet ready to define, collect, and exchange data in a generally computable sense. Wherever possible, implementers and/or specification writers should avoid using this element. Often, when used, the URL is a reference to an implementation guide that defines these special rules as part of it's narrative along with other profiles, value sets, etc. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 13. **Practitioner.language** | |
| Definition | The base language in which the resource is written. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHOULD be taken from [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html) [Max Binding](http://hl7.org/fhir/R4/extension-elementdefinition-maxvalueset.html "Max Value Set Extension"): [AllLanguages](http://hl7.org/fhir/R4/valueset-all-languages.html) A human language. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| Comments | Language is provided to support indexing and accessibility (typically, services such as text to speech use the language tag). The html language tag in the narrative applies to the narrative. The language tag on the resource may be used to specify the language of other presentations generated from the data in the resource. Not all the content has to be in the base language. The Resource.language should not be assumed to apply to the narrative automatically. If a language is specified, it should it also be specified on the div element in the html (see rules in HTML5 for information about the relationship between xml:lang and the html lang attribute). |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 14. **Practitioner.text** | |
| Definition | A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Narrative](http://hl7.org/fhir/R4/datatypes.html#Narrative) |
| Alternate Names | narrative, html, xhtml, display |
| Comments | Contained resources do not have narrative. Resources that are not contained SHOULD have a narrative. In some cases, a resource may only have text with little or no additional discrete data (as long as all minOccurs=1 elements are satisfied). This may be necessary for data from legacy systems where information is captured as a "text blob" or where text is additionally entered raw or narrated and encoded information is added later. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 15. **Practitioner.contained** | |
| Definition | These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Resource](http://hl7.org/fhir/R4/resource.html) |
| Alternate Names | inline resources, anonymous resources, contained resources |
| Comments | This should never be done when the content can be identified properly, as once identification is lost, it is extremely difficult (and context dependent) to restore it again. Contained resources may have profiles and tags In their meta elements, but SHALL NOT have security labels. |
| 16. **Practitioner.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 17. **Practitioner.modifierExtension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Modifier extensions allow for extensions that *cannot* be safely ignored to be clearly distinguished from the vast majority of extensions which can be safely ignored. This promotes interoperability by eliminating the need for implementers to prohibit the presence of extensions. For further information, see the [definition of modifier extensions](http://hl7.org/fhir/R4/extensibility.html#modifierExtension). |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 18. **Practitioner.identifier** | |
| Definition | An identifier that applies to this person in this role. |
| Note | This is a business identifier, not a resource identifier (see [discussion](http://hl7.org/fhir/R4/resource.html#identifiers)) |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Often, specific identities are assigned for the agent. |
| Comments | NPI must be supported as the identifier system in the US, Tax id is allowed, Local id is allowed in addition to an another identifier supplied by a jurisdictional authority such as a practitioner's *Drug Enforcement Administration (DEA)* number. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Practitioner.identifier. The slices are unordered and Open, and can be differentiated using the following discriminators:  * pattern @ $this |
| 19. **Practitioner.identifier.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 20. **Practitioner.identifier.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Practitioner.identifier.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 21. **Practitioner.identifier.use** | |
| Definition | The purpose of this identifier. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [IdentifierUse](http://hl7.org/fhir/R4/valueset-identifier-use.html) Identifies the purpose for this identifier, if known . |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Allows the appropriate identifier for a particular context of use to be selected from among a set of identifiers. |
| Comments | Applications can assume that an identifier is permanent unless it explicitly says that it is temporary. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 22. **Practitioner.identifier.type** | |
| Definition | A coded type for the identifier that can be used to determine which identifier to use for a specific purpose. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [Identifier Type Codes](http://hl7.org/fhir/R4/valueset-identifier-type.html); other codes may be used where these codes are not suitable A coded type for an identifier that can be used to determine which identifier to use for a specific purpose. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Allows users to make use of identifiers when the identifier system is not known. |
| Comments | This element deals only with general categories of identifiers. It SHOULD not be used for codes that correspond 1..1 with the Identifier.system. Some identifiers may fall into multiple categories due to common usage. Where the system is known, a type is unnecessary because the type is always part of the system definition. However systems often need to handle identifiers where the system is not known. There is not a 1:1 relationship between type and system, since many different systems have the same type. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 23. **Practitioner.identifier.system** | |
| Definition | Establishes the namespace for the value - that is, a URL that describes a set values that are unique. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | There are many sets of identifiers. To perform matching of two identifiers, we need to know what set we're dealing with. The system identifies a particular set of unique identifiers. |
| Comments | Identifier.system is always case sensitive. |
| Example | **General**:http://www.acme.com/identifiers/patient |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 24. **Practitioner.identifier.value** | |
| Definition | The portion of the identifier typically relevant to the user and which is unique within the context of the system. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | If the value is a full URI, then the system SHALL be urn:ietf:rfc:3986. The value's primary purpose is computational mapping. As a result, it may be normalized for comparison purposes (e.g. removing non-significant whitespace, dashes, etc.) A value formatted for human display can be conveyed using the [Rendered Value extension](http://hl7.org/fhir/R4/extension-rendered-value.html). Identifier.value is to be treated as case sensitive unless knowledge of the Identifier.system allows the processer to be confident that non-case-sensitive processing is safe. |
| Example | **General**:123456 |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 25. **Practitioner.identifier.period** | |
| Definition | Time period during which identifier is/was valid for use. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 26. **Practitioner.identifier.assigner** | |
| Definition | Organization that issued/manages the identifier. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([Organization](http://hl7.org/fhir/R4/organization.html "http://hl7.org/fhir/StructureDefinition/Organization")) |
| Comments | The Identifier.assigner may omit the .reference element and only contain a .display element reflecting the name or other textual information about the assigning organization. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 27. **Practitioner.identifier:NPI** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | NPI |
| Definition | An identifier that applies to this person in this role. |
| Note | This is a business identifier, not a resource identifier (see [discussion](http://hl7.org/fhir/R4/resource.html#identifiers)) |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Often, specific identities are assigned for the agent. |
| Pattern Value | <valueIdentifier xmlns="http://hl7.org/fhir">   <system value="http://hl7.org/fhir/sid/us-npi"/> </valueIdentifier> |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 28. **Practitioner.active** | |
| Definition | Whether this practitioner's record is in active use. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [boolean](http://hl7.org/fhir/R4/datatypes.html#boolean) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Need to be able to mark a practitioner record as not to be used because it was created in error. |
| Comments | If the practitioner is not in use by one organization, then it should mark the period on the PractitonerRole with an end date (even if they are active) as they may be active in another role. |
| Meaning if Missing | This resource is generally assumed to be active if no value is provided for the active element |
| Pattern Value | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 29. **Practitioner.name** | |
| Definition | The name(s) associated with the practitioner. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [HumanName](http://hl7.org/fhir/R4/datatypes.html#HumanName) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | The name(s) that a Practitioner is known by. Where there are multiple, the name that the practitioner is usually known as should be used in the display. |
| Comments | The selection of the use property should ensure that there is a single usual name specified, and others use the nickname (alias), old, or other values as appropriate.  In general, select the value to be used in the ResourceReference.display based on this:   1. There is more than 1 name 2. Use = usual 3. Period is current to the date of the usage 4. Use = official 5. Other order as decided by internal business rules. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 30. **Practitioner.name.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 31. **Practitioner.name.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Practitioner.name.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 32. **Practitioner.name.use** | |
| Definition | Identifies the purpose for this name. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [NameUse](http://hl7.org/fhir/R4/valueset-name-use.html) The use of a human name. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Allows the appropriate name for a particular context of use to be selected from among a set of names. |
| Comments | Applications can assume that a name is current unless it explicitly says that it is temporary or old. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 33. **Practitioner.name.text** | |
| Definition | Specifies the entire name as it should be displayed e.g. on an application UI. This may be provided instead of or as well as the specific parts. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | A renderable, unencoded form. |
| Comments | Can provide both a text representation and parts. Applications updating a name SHALL ensure that when both text and parts are present, no content is included in the text that isn't found in a part. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 34. **Practitioner.name.family** | |
| Definition | The part of a name that links to the genealogy. In some cultures (e.g. Eritrea) the family name of a son is the first name of his father. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Alternate Names | surname |
| Comments | Family Name may be decomposed into specific parts using extensions (de, nl, es related cultures). |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 35. **Practitioner.name.given** | |
| Definition | Given name. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Alternate Names | first name, middle name |
| Comments | If only initials are recorded, they may be used in place of the full name parts. Initials may be separated into multiple given names but often aren't due to paractical limitations. This element is not called "first name" since given names do not always come first. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 36. **Practitioner.name.prefix** | |
| Definition | Part of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the start of the name. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 37. **Practitioner.name.suffix** | |
| Definition | Part of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the end of the name. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 38. **Practitioner.name.period** | |
| Definition | Indicates the period of time when this name was valid for the named person. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| Requirements | Allows names to be placed in historical context. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 39. **Practitioner.telecom** | |
| Definition | A contact detail for the practitioner, e.g. a telephone number or an email address. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Need to know how to reach a practitioner independent to any roles the practitioner may have. |
| Comments | Person may have multiple ways to be contacted with different uses or applicable periods. May need to have options for contacting the person urgently and to help with identification. These typically will have home numbers, or mobile numbers that are not role specific. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 40. **Practitioner.telecom.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 41. **Practitioner.telecom.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Practitioner.telecom.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 42. **Practitioner.telecom.extension:contactpoint-availabletime** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | contactpoint-availabletime |
| Definition | An extension representing the days and times a contact point is available |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)([ContactPointAvailableTime](StructureDefinition-contactpoint-availabletime.html "[CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/contactpoint-availabletime]]")) (Complex Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 43. **Practitioner.telecom.extension:via-intermediary** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | via-intermediary |
| Definition | A reference to an alternative point of contact (plannet-PractitionerRole, plannet-Organization, plannet-OrganizationAffiliation, or plannet-Location) for this organization |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)([ViaIntermediary](StructureDefinition-via-intermediary.html "[CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary]]")) (Extension Type: [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetPractitionerRole](StructureDefinition-plannet-PractitionerRole.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole") | [PlannetOrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation") | [PlannetLocation](StructureDefinition-plannet-Location.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location") | [PlannetOrganization](StructureDefinition-plannet-Organization.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization"))) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 44. **Practitioner.telecom.system** | |
| Definition | Telecommunications form for contact point - what communications system is required to make use of the contact. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 This element is affected by the following invariants: cpt-2 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [ContactPointSystem](http://hl7.org/fhir/R4/valueset-contact-point-system.html) Telecommunications form for contact point. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 45. **Practitioner.telecom.value** | |
| Definition | The actual contact point details, in a form that is meaningful to the designated communication system (i.e. phone number or email address). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Requirements | Need to support legacy numbers that are not in a tightly controlled format. |
| Comments | Additional text data such as phone extension numbers, or notes about use of the contact are sometimes included in the value. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 46. **Practitioner.telecom.use** | |
| Definition | Identifies the purpose for the contact point. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [ContactPointUse](http://hl7.org/fhir/R4/valueset-contact-point-use.html) Use of contact point. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Need to track the way a person uses this contact, so a user can choose which is appropriate for their purpose. |
| Comments | Applications can assume that a contact is current unless it explicitly says that it is temporary or old. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 47. **Practitioner.telecom.rank** | |
| Definition | Specifies a preferred order in which to use a set of contacts. ContactPoints with lower rank values are more preferred than those with higher rank values. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [positiveInt](http://hl7.org/fhir/R4/datatypes.html#positiveInt) |
| Comments | Note that rank does not necessarily follow the order in which the contacts are represented in the instance. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 48. **Practitioner.telecom.period** | |
| Definition | Time period when the contact point was/is in use. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 49. **Practitioner.address** | |
| Definition | Address(es) of the practitioner that are not role specific (typically home address). Work addresses are not typically entered in this property as they are usually role dependent. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Address](http://hl7.org/fhir/R4/datatypes.html#Address) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | The home/mailing address of the practitioner is often required for employee administration purposes, and also for some rostering services where the start point (practitioners home) can be used in calculations. |
| Comments | The PractitionerRole does not have an address value on it, as it is expected that the location property be used for this purpose (which has an address). |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 50. **Practitioner.address.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 51. **Practitioner.address.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Practitioner.address.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 52. **Practitioner.address.extension:geolocation** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | geolocation |
| Definition | The absolute geographic location of the Location, expressed using the WGS84 datum (This is the same co-ordinate system used in KML). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)([Geolocation](http://hl7.org/fhir/R4/extension-geolocation.html "[CanonicalType[http://hl7.org/fhir/StructureDefinition/geolocation]]")) (Complex Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | The extension can be further extended to include unique geolocation identifiers, confidence, altitude, etc. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 53. **Practitioner.address.use** | |
| Definition | The purpose of this address. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [AddressUse](http://hl7.org/fhir/R4/valueset-address-use.html) The use of an address. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Allows an appropriate address to be chosen from a list of many. |
| Comments | Applications can assume that an address is current unless it explicitly says that it is temporary or old. |
| Example | **General**:home |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 54. **Practitioner.address.type** | |
| Definition | Distinguishes between physical addresses (those you can visit) and mailing addresses (e.g. PO Boxes and care-of addresses). Most addresses are both. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [AddressType](http://hl7.org/fhir/R4/valueset-address-type.html) The type of an address (physical / postal). |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| Comments | The definition of Address states that "address is intended to describe postal addresses, not physical locations". However, many applications track whether an address has a dual purpose of being a location that can be visited as well as being a valid delivery destination, and Postal addresses are often used as proxies for physical locations (also see the [Location](http://hl7.org/fhir/R4/location.html#) resource). |
| Example | **General**:both |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 55. **Practitioner.address.text** | |
| Definition | Specifies the entire address as it should be displayed e.g. on a postal label. This may be provided instead of or as well as the specific parts. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Requirements | A renderable, unencoded form. |
| Comments | Can provide both a text representation and parts. Applications updating an address SHALL ensure that when both text and parts are present, no content is included in the text that isn't found in a part. |
| Example | **General**:137 Nowhere Street, Erewhon 9132 |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 56. **Practitioner.address.line** | |
| Definition | This component contains the house number, apartment number, street name, street direction, P.O. Box number, delivery hints, and similar address information. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Example | **General**:137 Nowhere Street |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 57. **Practitioner.address.city** | |
| Definition | The name of the city, town, suburb, village or other community or delivery center. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Alternate Names | Municpality |
| Example | **General**:Erewhon |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 58. **Practitioner.address.district** | |
| Definition | The name of the administrative area (county). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Alternate Names | County |
| Comments | District is sometimes known as county, but in some regions 'county' is used in place of city (municipality), so county name should be conveyed in city instead. |
| Example | **General**:Madison |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 59. **Practitioner.address.state** | |
| Definition | Sub-unit of a country with limited sovereignty in a federally organized country. A code may be used if codes are in common use (e.g. US 2 letter state codes). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Alternate Names | Province, Territory |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 60. **Practitioner.address.postalCode** | |
| Definition | A postal code designating a region defined by the postal service. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Alternate Names | Zip |
| Example | **General**:9132 |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 61. **Practitioner.address.country** | |
| Definition | Country - a nation as commonly understood or generally accepted. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Comments | ISO 3166 3 letter codes can be used in place of a human readable country name. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 62. **Practitioner.address.period** | |
| Definition | Time period when address was/is in use. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| Requirements | Allows addresses to be placed in historical context. |
| Example | **General**:<valuePeriod xmlns="http://hl7.org/fhir">   <start value="2010-03-23"/>   <end value="2010-07-01"/> </valuePeriod> |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 63. **Practitioner.gender** | |
| Definition | Administrative Gender - the gender that the person is considered to have for administration and record keeping purposes. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [AdministrativeGender](http://hl7.org/fhir/R4/valueset-administrative-gender.html) The gender of a person used for administrative purposes. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| Requirements | Needed to address the person correctly. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 64. **Practitioner.birthDate** | |
| Definition | The date of birth for the practitioner. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [date](http://hl7.org/fhir/R4/datatypes.html#date) |
| Requirements | Needed for identification. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 65. **Practitioner.photo** | |
| Definition | Image of the person. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Attachment](http://hl7.org/fhir/R4/datatypes.html#Attachment) |
| Requirements | Many EHR systems have the capability to capture an image of patients and personnel. Fits with newer social media usage too. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 66. **Practitioner.qualification** | |
| Definition | The official certifications, training, and licenses that authorize or otherwise pertain to the provision of care by the practitioner. For example, a medical license issued by a medical board authorizing the practitioner to practice medicine within a certian locality. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 67. **Practitioner.qualification.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 68. **Practitioner.qualification.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Practitioner.qualification.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 69. **Practitioner.qualification.extension:practitioner-qualification** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | practitioner-qualification |
| Definition | An extension to add status and whereValid elements to a practitioner’s qualifications. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 This element is affected by the following invariants: ele-1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)([PractitionerQualification](StructureDefinition-practitioner-qualification.html "[CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/practitioner-qualification]]")) (Complex Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 70. **Practitioner.qualification.modifierExtension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Modifier extensions allow for extensions that *cannot* be safely ignored to be clearly distinguished from the vast majority of extensions which can be safely ignored. This promotes interoperability by eliminating the need for implementers to prohibit the presence of extensions. For further information, see the [definition of modifier extensions](http://hl7.org/fhir/R4/extensibility.html#modifierExtension). |
| Alternate Names | extensions, user content, modifiers |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 71. **Practitioner.qualification.identifier** | |
| Definition | An identifier that applies to this person's qualification in this role. |
| Note | This is a business identifier, not a resource identifier (see [discussion](http://hl7.org/fhir/R4/resource.html#identifiers)) |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Often, specific identities are assigned for the qualification. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 72. **Practitioner.qualification.code** | |
| Definition | Coded representation of the qualification. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [Individual Specialties, Degrees, Licenses, and Certificates VS](ValueSet-IndividualSpecialtyAndDegreeLicenseCertificateVS.html); other codes may be used where these codes are not suitable |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 73. **Practitioner.qualification.period** | |
| Definition | Period during which the qualification is valid. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Qualifications are often for a limited period of time, and can be revoked. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 74. **Practitioner.qualification.issuer** | |
| Definition | Organization that regulates and issues the qualification. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([Organization](http://hl7.org/fhir/R4/organization.html "http://hl7.org/fhir/StructureDefinition/Organization")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 75. **Practitioner.communication** | |
| Definition | A language the practitioner can use in patient communication. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHOULD be taken from [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html) [Max Binding](http://hl7.org/fhir/R4/extension-elementdefinition-maxvalueset.html "Max Value Set Extension"): [AllLanguages](http://hl7.org/fhir/R4/valueset-all-languages.html) A human language. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Knowing which language a practitioner speaks can help in facilitating communication with patients. |
| Comments | The structure aa-BB with this exact casing is one the most widely used notations for locale. However not all systems code this but instead have it as free text. Hence CodeableConcept instead of code as the data type. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 76. **Practitioner.communication.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 77. **Practitioner.communication.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Practitioner.communication.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 78. **Practitioner.communication.extension:communication-proficiency** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | communication-proficiency |
| Definition | An extension to express a practitioner’s spoken proficiency with the language indicated in practitioner.communication. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)([CommunicationProficiency](StructureDefinition-communication-proficiency.html "[CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/communication-proficiency]]")) (Extension Type: [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept)) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 79. **Practitioner.communication.coding** | |
| Definition | A reference to a code defined by a terminology system. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) |
| Requirements | Allows for alternative encodings within a code system, and translations to other code systems. |
| Comments | Codes may be defined very casually in enumerations, or code lists, up to very formal definitions such as SNOMED CT - see the HL7 v3 Core Principles for more information. Ordering of codings is undefined and SHALL NOT be used to infer meaning. Generally, at most only one of the coding values will be labeled as UserSelected = true. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 80. **Practitioner.communication.text** | |
| Definition | A human language representation of the concept as seen/selected/uttered by the user who entered the data and/or which represents the intended meaning of the user. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Requirements | The codes from the terminologies do not always capture the correct meaning with all the nuances of the human using them, or sometimes there is no appropriate code at all. In these cases, the text is used to capture the full meaning of the source. |
| Comments | Very often the text is the same as a displayName of one of the codings. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |