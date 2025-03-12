# Resource Profile: PlannetInsurancePlan - Detailed Descriptions

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plan-Net InsurancePlan**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-plannet-InsurancePlan.html)
* [Detailed Descriptions](#)
* [Mappings](StructureDefinition-plannet-InsurancePlan-mappings.html)
* [Examples](StructureDefinition-plannet-InsurancePlan-examples.html)

## Resource Profile: PlannetInsurancePlan - Detailed Descriptions

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Definitions for the plannet-InsurancePlan resource profile.

|  |  |
| --- | --- |
| 1. **InsurancePlan** | |
| Definition | Details of a Health Insurance product/plan provided by an organization. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| Invariants | **Defined on this element**  **dom-2**: If the resource is contained in another resource, it SHALL NOT contain nested Resources (: contained.contained.empty()) **dom-3**: If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource (: contained.where((('#'+id in (%resource.descendants().reference | %resource.descendants().as(canonical) | %resource.descendants().as(uri) | %resource.descendants().as(url))) or descendants().where(reference = '#').exists() or descendants().where(as(canonical) = '#').exists() or descendants().where(as(canonical) = '#').exists()).not()).trace('unmatched', id).empty()) **dom-4**: If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated (: contained.meta.versionId.empty() and contained.meta.lastUpdated.empty()) **dom-5**: If a resource is contained in another resource, it SHALL NOT have a security label (: contained.meta.security.empty()) **dom-6**: A resource should have narrative for robust management (: text.`div`.exists()) **ipn-1**: The organization SHALL at least have a name or an idendtifier, and possibly more than one (: (identifier.count() + name.count()) > 0) **network-or-plan-Network**: If an insuranceplan does not define a network, then each plan must define one (: network.exists() or plan.network.exists.allTrue()) **plan-type-is-distinct**: Each InsurancePlan.plan should have a distinct plan.type. (: plan.type.coding.code.isDistinct()) |
| 2. **InsurancePlan.id** | |
| Definition | The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Comments | The only time that a resource does not have an id is when it is being submitted to the server using a create operation. |
| 3. **InsurancePlan.meta** | |
| Definition | The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 4. **InsurancePlan.meta.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 5. **InsurancePlan.meta.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on InsurancePlan.meta.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 6. **InsurancePlan.meta.versionId** | |
| Definition | The version specific identifier, as it appears in the version portion of the URL. This value changes when the resource is created, updated, or deleted. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [id](http://hl7.org/fhir/R4/datatypes.html#id) |
| Comments | The server assigns this value, and ignores what the client specifies, except in the case that the server is imposing version integrity on updates/deletes. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 7. **InsurancePlan.meta.lastUpdated** | |
| Definition | When the resource last changed - e.g. when the version changed. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [instant](http://hl7.org/fhir/R4/datatypes.html#instant) |
| Comments | This value is always populated except when the resource is first being created. The server / resource manager sets this value; what a client provides is irrelevant. This is equivalent to the HTTP Last-Modified and SHOULD have the same value on a [read](http://hl7.org/fhir/R4/http.html#read) interaction. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 8. **InsurancePlan.meta.source** | |
| Definition | A uri that identifies the source system of the resource. This provides a minimal amount of [Provenance](http://hl7.org/fhir/R4/provenance.html#) information that can be used to track or differentiate the source of information in the resource. The source may identify another FHIR server, document, message, database, etc. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | In the provenance resource, this corresponds to Provenance.entity.what[x]. The exact use of the source (and the implied Provenance.entity.role) is left to implementer discretion. Only one nominated source is allowed; for additional provenance details, a full Provenance resource should be used.  This element can be used to indicate where the current master source of a resource that has a canonical URL if the resource is no longer hosted at the canonical URL. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 9. **InsurancePlan.meta.profile** | |
| Definition | A list of profiles (references to [StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html#) resources) that this resource claims to conform to. The URL is a reference to [StructureDefinition.url](http://hl7.org/fhir/R4/structuredefinition-definitions.html#StructureDefinition.url). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [canonical](http://hl7.org/fhir/R4/datatypes.html#canonical)([StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html "http://hl7.org/fhir/StructureDefinition/StructureDefinition")) |
| Comments | It is up to the server and/or other infrastructure of policy to determine whether/how these claims are verified and/or updated over time. The list of profile URLs is a set. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 10. **InsurancePlan.meta.security** | |
| Definition | Security labels applied to this resource. These tags connect specific resources to the overall security policy and infrastructure. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [All Security Labels](http://hl7.org/fhir/R4/valueset-security-labels.html); other codes may be used where these codes are not suitable Security Labels from the Healthcare Privacy and Security Classification System. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) |
| Comments | The security labels can be updated without changing the stated version of the resource. The list of security labels is a set. Uniqueness is based the system/code, and version and display are ignored. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 11. **InsurancePlan.meta.tag** | |
| Definition | Tags applied to this resource. Tags are intended to be used to identify and relate resources to process and workflow, and applications are not required to consider the tags when interpreting the meaning of a resource. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | For example codes, see [CommonTags](http://hl7.org/fhir/R4/valueset-common-tags.html) Codes that represent various types of tags, commonly workflow-related; e.g. "Needs review by Dr. Jones". |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) |
| Comments | The tags can be updated without changing the stated version of the resource. The list of tags is a set. Uniqueness is based the system/code, and version and display are ignored. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 12. **InsurancePlan.implicitRules** | |
| Definition | A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Comments | Asserting this rule set restricts the content to be only understood by a limited set of trading partners. This inherently limits the usefulness of the data in the long term. However, the existing health eco-system is highly fractured, and not yet ready to define, collect, and exchange data in a generally computable sense. Wherever possible, implementers and/or specification writers should avoid using this element. Often, when used, the URL is a reference to an implementation guide that defines these special rules as part of it's narrative along with other profiles, value sets, etc. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 13. **InsurancePlan.language** | |
| Definition | The base language in which the resource is written. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHOULD be taken from [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html) [Max Binding](http://hl7.org/fhir/R4/extension-elementdefinition-maxvalueset.html "Max Value Set Extension"): [AllLanguages](http://hl7.org/fhir/R4/valueset-all-languages.html) A human language. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| Comments | Language is provided to support indexing and accessibility (typically, services such as text to speech use the language tag). The html language tag in the narrative applies to the narrative. The language tag on the resource may be used to specify the language of other presentations generated from the data in the resource. Not all the content has to be in the base language. The Resource.language should not be assumed to apply to the narrative automatically. If a language is specified, it should it also be specified on the div element in the html (see rules in HTML5 for information about the relationship between xml:lang and the html lang attribute). |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 14. **InsurancePlan.text** | |
| Definition | A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Narrative](http://hl7.org/fhir/R4/datatypes.html#Narrative) |
| Alternate Names | narrative, html, xhtml, display |
| Comments | Contained resources do not have narrative. Resources that are not contained SHOULD have a narrative. In some cases, a resource may only have text with little or no additional discrete data (as long as all minOccurs=1 elements are satisfied). This may be necessary for data from legacy systems where information is captured as a "text blob" or where text is additionally entered raw or narrated and encoded information is added later. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 15. **InsurancePlan.contained** | |
| Definition | These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Resource](http://hl7.org/fhir/R4/resource.html) |
| Alternate Names | inline resources, anonymous resources, contained resources |
| Comments | This should never be done when the content can be identified properly, as once identification is lost, it is extremely difficult (and context dependent) to restore it again. Contained resources may have profiles and tags In their meta elements, but SHALL NOT have security labels. |
| 16. **InsurancePlan.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the resource. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 17. **InsurancePlan.modifierExtension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Modifier extensions allow for extensions that *cannot* be safely ignored to be clearly distinguished from the vast majority of extensions which can be safely ignored. This promotes interoperability by eliminating the need for implementers to prohibit the presence of extensions. For further information, see the [definition of modifier extensions](http://hl7.org/fhir/R4/extensibility.html#modifierExtension). |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 18. **InsurancePlan.identifier** | |
| Definition | Business identifiers assigned to this health insurance product which remain constant as the resource is updated and propagates from server to server. |
| Note | This is a business identifier, not a resource identifier (see [discussion](http://hl7.org/fhir/R4/resource.html#identifiers)) |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* This element is affected by the following invariants: ipn-1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 19. **InsurancePlan.identifier.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 20. **InsurancePlan.identifier.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on InsurancePlan.identifier.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 21. **InsurancePlan.identifier.use** | |
| Definition | The purpose of this identifier. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [IdentifierUse](http://hl7.org/fhir/R4/valueset-identifier-use.html) Identifies the purpose for this identifier, if known . |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Allows the appropriate identifier for a particular context of use to be selected from among a set of identifiers. |
| Comments | Applications can assume that an identifier is permanent unless it explicitly says that it is temporary. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 22. **InsurancePlan.identifier.type** | |
| Definition | A coded type for the identifier that can be used to determine which identifier to use for a specific purpose. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [Identifier Type Codes](http://hl7.org/fhir/R4/valueset-identifier-type.html); other codes may be used where these codes are not suitable A coded type for an identifier that can be used to determine which identifier to use for a specific purpose. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Allows users to make use of identifiers when the identifier system is not known. |
| Comments | This element deals only with general categories of identifiers. It SHOULD not be used for codes that correspond 1..1 with the Identifier.system. Some identifiers may fall into multiple categories due to common usage. Where the system is known, a type is unnecessary because the type is always part of the system definition. However systems often need to handle identifiers where the system is not known. There is not a 1:1 relationship between type and system, since many different systems have the same type. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 23. **InsurancePlan.identifier.system** | |
| Definition | Establishes the namespace for the value - that is, a URL that describes a set values that are unique. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Requirements | There are many sets of identifiers. To perform matching of two identifiers, we need to know what set we're dealing with. The system identifies a particular set of unique identifiers. |
| Comments | Identifier.system is always case sensitive. |
| Example | **General**:http://www.acme.com/identifiers/patient |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 24. **InsurancePlan.identifier.value** | |
| Definition | The portion of the identifier typically relevant to the user and which is unique within the context of the system. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | If the value is a full URI, then the system SHALL be urn:ietf:rfc:3986. The value's primary purpose is computational mapping. As a result, it may be normalized for comparison purposes (e.g. removing non-significant whitespace, dashes, etc.) A value formatted for human display can be conveyed using the [Rendered Value extension](http://hl7.org/fhir/R4/extension-rendered-value.html). Identifier.value is to be treated as case sensitive unless knowledge of the Identifier.system allows the processer to be confident that non-case-sensitive processing is safe. |
| Example | **General**:123456 |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 25. **InsurancePlan.identifier.period** | |
| Definition | Time period during which identifier is/was valid for use. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 26. **InsurancePlan.identifier.assigner** | |
| Definition | Organization that issued/manages the identifier. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([Organization](http://hl7.org/fhir/R4/organization.html "http://hl7.org/fhir/StructureDefinition/Organization")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | The Identifier.assigner may omit the .reference element and only contain a .display element reflecting the name or other textual information about the assigning organization. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 27. **InsurancePlan.status** | |
| Definition | The current state of the health insurance product. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [PublicationStatus](http://hl7.org/fhir/R4/valueset-publication-status.html) The lifecycle status of an artifact. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Need a flag to indicate a record is no longer to be used and should generally be hidden for the user in the UI. |
| Meaning if Missing | Default interpretation is active. |
| Fixed Value | active |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 28. **InsurancePlan.type** | |
| Definition | The kind of health insurance product. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [Insurance Product Type VS](ValueSet-InsuranceProductTypeVS.html); other codes may be used where these codes are not suitable |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 29. **InsurancePlan.name** | |
| Definition | Official name of the health insurance product as designated by the owner. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 This element is affected by the following invariants: ipn-1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | If the name of the product/plan changes, consider putting the old name in the alias column so that it can still be located through searches. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 30. **InsurancePlan.alias** | |
| Definition | A list of alternate names that the product is known as, or was known as in the past. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Over time products/plans go through many changes and can be known by different names.  For searching knowing previous names that the product/plan was known by can be very useful. |
| Comments | There are no dates associated with the alias/historic names, as this is not intended to track when names were used, but to assist in searching so that older names can still result in identifying the product/plan. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 31. **InsurancePlan.period** | |
| Definition | The period of time that the health insurance product is available. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 32. **InsurancePlan.ownedBy** | |
| Definition | The entity that is providing the health insurance product and underwriting the risk. This is typically an insurance carriers, other third-party payers, or health plan sponsors comonly referred to as 'payers'. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetOrganization](StructureDefinition-plannet-Organization.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Alternate Names | Payer |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 33. **InsurancePlan.administeredBy** | |
| Definition | An organization which administer other services such as underwriting, customer service and/or claims processing on behalf of the health insurance product owner. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetOrganization](StructureDefinition-plannet-Organization.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 34. **InsurancePlan.coverageArea** | |
| Definition | The geographic region in which a health insurance product's benefits apply. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetLocation](StructureDefinition-plannet-Location.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 35. **InsurancePlan.contact** | |
| Definition | The contact for the health insurance product for a certain purpose. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Need to keep track of assigned contact points within bigger organization. |
| Comments | Where multiple contacts for the same purpose are provided there is a standard extension that can be used to determine which one is the preferred contact to use. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 36. **InsurancePlan.contact.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 37. **InsurancePlan.contact.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 38. **InsurancePlan.contact.modifierExtension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Modifier extensions allow for extensions that *cannot* be safely ignored to be clearly distinguished from the vast majority of extensions which can be safely ignored. This promotes interoperability by eliminating the need for implementers to prohibit the presence of extensions. For further information, see the [definition of modifier extensions](http://hl7.org/fhir/R4/extensibility.html#modifierExtension). |
| Alternate Names | extensions, user content, modifiers |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 39. **InsurancePlan.contact.purpose** | |
| Definition | Indicates a purpose for which the contact can be reached. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [ContactEntityType](http://hl7.org/fhir/R4/valueset-contactentity-type.html); other codes may be used where these codes are not suitable The purpose for which you would contact a contact party. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| Requirements | Need to distinguish between multiple contact persons. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 40. **InsurancePlan.contact.name** | |
| Definition | A name associated with the contact. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [HumanName](http://hl7.org/fhir/R4/datatypes.html#HumanName) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Need to be able to track the person by name. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 41. **InsurancePlan.contact.name.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 42. **InsurancePlan.contact.name.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on InsurancePlan.contact.name.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 43. **InsurancePlan.contact.name.use** | |
| Definition | Identifies the purpose for this name. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [NameUse](http://hl7.org/fhir/R4/valueset-name-use.html) The use of a human name. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Allows the appropriate name for a particular context of use to be selected from among a set of names. |
| Comments | Applications can assume that a name is current unless it explicitly says that it is temporary or old. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 44. **InsurancePlan.contact.name.text** | |
| Definition | Specifies the entire name as it should be displayed e.g. on an application UI. This may be provided instead of or as well as the specific parts. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | A renderable, unencoded form. |
| Comments | Can provide both a text representation and parts. Applications updating a name SHALL ensure that when both text and parts are present, no content is included in the text that isn't found in a part. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 45. **InsurancePlan.contact.name.family** | |
| Definition | The part of a name that links to the genealogy. In some cultures (e.g. Eritrea) the family name of a son is the first name of his father. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Alternate Names | surname |
| Comments | Family Name may be decomposed into specific parts using extensions (de, nl, es related cultures). |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 46. **InsurancePlan.contact.name.given** | |
| Definition | Given name. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Alternate Names | first name, middle name |
| Comments | If only initials are recorded, they may be used in place of the full name parts. Initials may be separated into multiple given names but often aren't due to paractical limitations. This element is not called "first name" since given names do not always come first. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 47. **InsurancePlan.contact.name.prefix** | |
| Definition | Part of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the start of the name. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 48. **InsurancePlan.contact.name.suffix** | |
| Definition | Part of the name that is acquired as a title due to academic, legal, employment or nobility status, etc. and that appears at the end of the name. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 49. **InsurancePlan.contact.name.period** | |
| Definition | Indicates the period of time when this name was valid for the named person. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| Requirements | Allows names to be placed in historical context. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 50. **InsurancePlan.contact.telecom** | |
| Definition | A contact detail (e.g. a telephone number or an email address) by which the party may be contacted. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | People have (primary) ways to contact them in some way such as phone, email. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 51. **InsurancePlan.contact.telecom.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 52. **InsurancePlan.contact.telecom.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on InsurancePlan.contact.telecom.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 53. **InsurancePlan.contact.telecom.system** | |
| Definition | Telecommunications form for contact point - what communications system is required to make use of the contact. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 This element is affected by the following invariants: cpt-2 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [ContactPointSystem](http://hl7.org/fhir/R4/valueset-contact-point-system.html) Telecommunications form for contact point. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 54. **InsurancePlan.contact.telecom.value** | |
| Definition | The actual contact point details, in a form that is meaningful to the designated communication system (i.e. phone number or email address). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Need to support legacy numbers that are not in a tightly controlled format. |
| Comments | Additional text data such as phone extension numbers, or notes about use of the contact are sometimes included in the value. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 55. **InsurancePlan.contact.telecom.use** | |
| Definition | Identifies the purpose for the contact point. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [ContactPointUse](http://hl7.org/fhir/R4/valueset-contact-point-use.html) Use of contact point. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Need to track the way a person uses this contact, so a user can choose which is appropriate for their purpose. |
| Comments | Applications can assume that a contact is current unless it explicitly says that it is temporary or old. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 56. **InsurancePlan.contact.telecom.rank** | |
| Definition | Specifies a preferred order in which to use a set of contacts. ContactPoints with lower rank values are more preferred than those with higher rank values. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [positiveInt](http://hl7.org/fhir/R4/datatypes.html#positiveInt) |
| Comments | Note that rank does not necessarily follow the order in which the contacts are represented in the instance. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 57. **InsurancePlan.contact.telecom.period** | |
| Definition | Time period when the contact point was/is in use. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 58. **InsurancePlan.contact.address** | |
| Definition | Visiting or postal addresses for the contact. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Address](http://hl7.org/fhir/R4/datatypes.html#Address) |
| Requirements | May need to keep track of a contact party's address for contacting, billing or reporting requirements. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 59. **InsurancePlan.endpoint** | |
| Definition | The technical endpoints providing access to services operated for the health insurance product. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetEndpoint](StructureDefinition-plannet-Endpoint.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Endpoint")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Organizations have multiple systems that provide various services and need to be able to define the technical connection details for how to connect to them, and for what purpose. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 60. **InsurancePlan.network** | |
| Definition | Reference to the network included in the health insurance product. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetNetwork](StructureDefinition-plannet-Network.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Network")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | Networks are represented as a hierarchy of organization resources. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 61. **InsurancePlan.coverage** | |
| Definition | Details about the coverage offered by the insurance product. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 62. **InsurancePlan.coverage.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 63. **InsurancePlan.coverage.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 64. **InsurancePlan.coverage.modifierExtension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Modifier extensions allow for extensions that *cannot* be safely ignored to be clearly distinguished from the vast majority of extensions which can be safely ignored. This promotes interoperability by eliminating the need for implementers to prohibit the presence of extensions. For further information, see the [definition of modifier extensions](http://hl7.org/fhir/R4/extensibility.html#modifierExtension). |
| Alternate Names | extensions, user content, modifiers |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 65. **InsurancePlan.coverage.type** | |
| Definition | Type of coverage (Medical; Dental; Mental Health; Substance Abuse; Vision; Drug; Short Term; Long Term Care; Hospice; Home Health). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 66. **InsurancePlan.coverage.network** | |
| Definition | Reference to the network that providing the type of coverage. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([Organization](http://hl7.org/fhir/R4/organization.html "http://hl7.org/fhir/StructureDefinition/Organization")) |
| Comments | Networks are represented as a hierarchy of organization resources. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 67. **InsurancePlan.coverage.benefit** | |
| Definition | Specific benefits under this type of coverage. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 68. **InsurancePlan.coverage.benefit.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 69. **InsurancePlan.coverage.benefit.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 70. **InsurancePlan.coverage.benefit.modifierExtension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Modifier extensions allow for extensions that *cannot* be safely ignored to be clearly distinguished from the vast majority of extensions which can be safely ignored. This promotes interoperability by eliminating the need for implementers to prohibit the presence of extensions. For further information, see the [definition of modifier extensions](http://hl7.org/fhir/R4/extensibility.html#modifierExtension). |
| Alternate Names | extensions, user content, modifiers |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 71. **InsurancePlan.coverage.benefit.type** | |
| Definition | Type of benefit (primary care; speciality care; inpatient; outpatient). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 72. **InsurancePlan.coverage.benefit.requirement** | |
| Definition | The referral requirements to have access/coverage for this benefit. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 73. **InsurancePlan.coverage.benefit.limit** | |
| Definition | The specific limits on the benefit. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 74. **InsurancePlan.coverage.benefit.limit.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 75. **InsurancePlan.coverage.benefit.limit.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 76. **InsurancePlan.coverage.benefit.limit.modifierExtension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Modifier extensions allow for extensions that *cannot* be safely ignored to be clearly distinguished from the vast majority of extensions which can be safely ignored. This promotes interoperability by eliminating the need for implementers to prohibit the presence of extensions. For further information, see the [definition of modifier extensions](http://hl7.org/fhir/R4/extensibility.html#modifierExtension). |
| Alternate Names | extensions, user content, modifiers |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 77. **InsurancePlan.coverage.benefit.limit.value** | |
| Definition | The maximum amount of a service item a plan will pay for a covered benefit. For examples. wellness visits, or eyeglasses. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Quantity](http://hl7.org/fhir/R4/datatypes.html#Quantity) |
| Comments | May also be called “eligible expense,” “payment allowance,” or “negotiated rate.”. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 78. **InsurancePlan.coverage.benefit.limit.code** | |
| Definition | The specific limit on the benefit. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| Comments | Use `CodeableConcept.text` element if the data is free (uncoded) text. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 79. **InsurancePlan.plan** | |
| Definition | Details about an insurance plan. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 80. **InsurancePlan.plan.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 81. **InsurancePlan.plan.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 82. **InsurancePlan.plan.modifierExtension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Modifier extensions allow for extensions that *cannot* be safely ignored to be clearly distinguished from the vast majority of extensions which can be safely ignored. This promotes interoperability by eliminating the need for implementers to prohibit the presence of extensions. For further information, see the [definition of modifier extensions](http://hl7.org/fhir/R4/extensibility.html#modifierExtension). |
| Alternate Names | extensions, user content, modifiers |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 83. **InsurancePlan.plan.identifier** | |
| Definition | Business identifiers assigned to this health insurance plan which remain constant as the resource is updated and propagates from server to server. |
| Note | This is a business identifier, not a resource identifier (see [discussion](http://hl7.org/fhir/R4/resource.html#identifiers)) |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 84. **InsurancePlan.plan.type** | |
| Definition | Type of plan. For example, "Platinum" or "High Deductable". |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [Insurance Plan TypeVS](ValueSet-InsurancePlanTypeVS.html); other codes may be used where these codes are not suitable |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 85. **InsurancePlan.plan.coverageArea** | |
| Definition | The geographic region in which a health insurance plan's benefits apply. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetLocation](StructureDefinition-plannet-Location.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 86. **InsurancePlan.plan.network** | |
| Definition | Reference to the network that providing the type of coverage. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetNetwork](StructureDefinition-plannet-Network.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Network")) |
| Comments | Networks are represented as a hierarchy of organization resources. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 87. **InsurancePlan.plan.generalCost** | |
| Definition | Overall costs associated with the plan. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 88. **InsurancePlan.plan.generalCost.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 89. **InsurancePlan.plan.generalCost.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 90. **InsurancePlan.plan.generalCost.modifierExtension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Modifier extensions allow for extensions that *cannot* be safely ignored to be clearly distinguished from the vast majority of extensions which can be safely ignored. This promotes interoperability by eliminating the need for implementers to prohibit the presence of extensions. For further information, see the [definition of modifier extensions](http://hl7.org/fhir/R4/extensibility.html#modifierExtension). |
| Alternate Names | extensions, user content, modifiers |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 91. **InsurancePlan.plan.generalCost.type** | |
| Definition | Type of cost. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 92. **InsurancePlan.plan.generalCost.groupSize** | |
| Definition | Number of participants enrolled in the plan. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [positiveInt](http://hl7.org/fhir/R4/datatypes.html#positiveInt) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 93. **InsurancePlan.plan.generalCost.cost** | |
| Definition | Value of the cost. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Money](http://hl7.org/fhir/R4/datatypes.html#Money) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 94. **InsurancePlan.plan.generalCost.comment** | |
| Definition | Additional information about the general costs associated with this plan. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 95. **InsurancePlan.plan.specificCost** | |
| Definition | Costs associated with the coverage provided by the product. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 96. **InsurancePlan.plan.specificCost.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 97. **InsurancePlan.plan.specificCost.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 98. **InsurancePlan.plan.specificCost.modifierExtension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Modifier extensions allow for extensions that *cannot* be safely ignored to be clearly distinguished from the vast majority of extensions which can be safely ignored. This promotes interoperability by eliminating the need for implementers to prohibit the presence of extensions. For further information, see the [definition of modifier extensions](http://hl7.org/fhir/R4/extensibility.html#modifierExtension). |
| Alternate Names | extensions, user content, modifiers |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 99. **InsurancePlan.plan.specificCost.category** | |
| Definition | General category of benefit (Medical; Dental; Vision; Drug; Mental Health; Substance Abuse; Hospice, Home Health). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 100. **InsurancePlan.plan.specificCost.benefit** | |
| Definition | List of the specific benefits under this category of benefit. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 101. **InsurancePlan.plan.specificCost.benefit.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 102. **InsurancePlan.plan.specificCost.benefit.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 103. **InsurancePlan.plan.specificCost.benefit.modifierExtension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Modifier extensions allow for extensions that *cannot* be safely ignored to be clearly distinguished from the vast majority of extensions which can be safely ignored. This promotes interoperability by eliminating the need for implementers to prohibit the presence of extensions. For further information, see the [definition of modifier extensions](http://hl7.org/fhir/R4/extensibility.html#modifierExtension). |
| Alternate Names | extensions, user content, modifiers |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 104. **InsurancePlan.plan.specificCost.benefit.type** | |
| Definition | Type of specific benefit (preventative; primary care office visit; speciality office visit; hospitalization; emergency room; urgent care). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 105. **InsurancePlan.plan.specificCost.benefit.cost** | |
| Definition | List of the costs associated with a specific benefit. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 106. **InsurancePlan.plan.specificCost.benefit.cost.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 107. **InsurancePlan.plan.specificCost.benefit.cost.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 108. **InsurancePlan.plan.specificCost.benefit.cost.modifierExtension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Modifier extensions allow for extensions that *cannot* be safely ignored to be clearly distinguished from the vast majority of extensions which can be safely ignored. This promotes interoperability by eliminating the need for implementers to prohibit the presence of extensions. For further information, see the [definition of modifier extensions](http://hl7.org/fhir/R4/extensibility.html#modifierExtension). |
| Alternate Names | extensions, user content, modifiers |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 109. **InsurancePlan.plan.specificCost.benefit.cost.type** | |
| Definition | Type of cost (copay; individual cap; family cap; coinsurance; deductible). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 110. **InsurancePlan.plan.specificCost.benefit.cost.applicability** | |
| Definition | Whether the cost applies to in-network or out-of-network providers (in-network; out-of-network; other). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [BenefitCostApplicability](http://hl7.org/fhir/R4/valueset-insuranceplan-applicability.html) Whether the cost applies to in-network or out-of-network providers. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 111. **InsurancePlan.plan.specificCost.benefit.cost.qualifiers** | |
| Definition | Additional information about the cost, such as information about funding sources (e.g. HSA, HRA, FSA, RRA). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 112. **InsurancePlan.plan.specificCost.benefit.cost.value** | |
| Definition | The actual cost value. (some of the costs may be represented as percentages rather than currency, e.g. 10% coinsurance). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Quantity](http://hl7.org/fhir/R4/datatypes.html#Quantity) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |