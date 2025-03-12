# Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plan-Net OrganizationAffiliation**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-plannet-OrganizationAffiliation.html)
* [Detailed Descriptions](#)
* [Mappings](StructureDefinition-plannet-OrganizationAffiliation-mappings.html)
* [Examples](StructureDefinition-plannet-OrganizationAffiliation-examples.html)

## Resource Profile: PlannetOrganizationAffiliation - Detailed Descriptions

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Definitions for the plannet-OrganizationAffiliation resource profile.

|  |  |
| --- | --- |
| 1. **OrganizationAffiliation** | |
| Definition | Defines an affiliation/assotiation/relationship between 2 distinct oganizations, that is not a part-of relationship/sub-division relationship. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| Invariants | **Defined on this element**  **dom-2**: If the resource is contained in another resource, it SHALL NOT contain nested Resources (: contained.contained.empty()) **dom-3**: If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource (: contained.where((('#'+id in (%resource.descendants().reference | %resource.descendants().as(canonical) | %resource.descendants().as(uri) | %resource.descendants().as(url))) or descendants().where(reference = '#').exists() or descendants().where(as(canonical) = '#').exists() or descendants().where(as(canonical) = '#').exists()).not()).trace('unmatched', id).empty()) **dom-4**: If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated (: contained.meta.versionId.empty() and contained.meta.lastUpdated.empty()) **dom-5**: If a resource is contained in another resource, it SHALL NOT have a security label (: contained.meta.security.empty()) **dom-6**: A resource should have narrative for robust management (: text.`div`.exists()) **organization-or-participatingOrganization**: PlannetOrganizationAffiliation.organization or PlannetOrganizationAffiliation.participatingOrganization (: organization.exists() or participatingOrganization.exists()) |
| 2. **OrganizationAffiliation.id** | |
| Definition | The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Comments | The only time that a resource does not have an id is when it is being submitted to the server using a create operation. |
| 3. **OrganizationAffiliation.meta** | |
| Definition | The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 4. **OrganizationAffiliation.meta.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 5. **OrganizationAffiliation.meta.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on OrganizationAffiliation.meta.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 6. **OrganizationAffiliation.meta.versionId** | |
| Definition | The version specific identifier, as it appears in the version portion of the URL. This value changes when the resource is created, updated, or deleted. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [id](http://hl7.org/fhir/R4/datatypes.html#id) |
| Comments | The server assigns this value, and ignores what the client specifies, except in the case that the server is imposing version integrity on updates/deletes. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 7. **OrganizationAffiliation.meta.lastUpdated** | |
| Definition | When the resource last changed - e.g. when the version changed. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [instant](http://hl7.org/fhir/R4/datatypes.html#instant) |
| Comments | This value is always populated except when the resource is first being created. The server / resource manager sets this value; what a client provides is irrelevant. This is equivalent to the HTTP Last-Modified and SHOULD have the same value on a [read](http://hl7.org/fhir/R4/http.html#read) interaction. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 8. **OrganizationAffiliation.meta.source** | |
| Definition | A uri that identifies the source system of the resource. This provides a minimal amount of [Provenance](http://hl7.org/fhir/R4/provenance.html#) information that can be used to track or differentiate the source of information in the resource. The source may identify another FHIR server, document, message, database, etc. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | In the provenance resource, this corresponds to Provenance.entity.what[x]. The exact use of the source (and the implied Provenance.entity.role) is left to implementer discretion. Only one nominated source is allowed; for additional provenance details, a full Provenance resource should be used.  This element can be used to indicate where the current master source of a resource that has a canonical URL if the resource is no longer hosted at the canonical URL. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 9. **OrganizationAffiliation.meta.profile** | |
| Definition | A list of profiles (references to [StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html#) resources) that this resource claims to conform to. The URL is a reference to [StructureDefinition.url](http://hl7.org/fhir/R4/structuredefinition-definitions.html#StructureDefinition.url). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [canonical](http://hl7.org/fhir/R4/datatypes.html#canonical)([StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html "http://hl7.org/fhir/StructureDefinition/StructureDefinition")) |
| Comments | It is up to the server and/or other infrastructure of policy to determine whether/how these claims are verified and/or updated over time. The list of profile URLs is a set. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 10. **OrganizationAffiliation.meta.security** | |
| Definition | Security labels applied to this resource. These tags connect specific resources to the overall security policy and infrastructure. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [All Security Labels](http://hl7.org/fhir/R4/valueset-security-labels.html); other codes may be used where these codes are not suitable Security Labels from the Healthcare Privacy and Security Classification System. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) |
| Comments | The security labels can be updated without changing the stated version of the resource. The list of security labels is a set. Uniqueness is based the system/code, and version and display are ignored. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 11. **OrganizationAffiliation.meta.tag** | |
| Definition | Tags applied to this resource. Tags are intended to be used to identify and relate resources to process and workflow, and applications are not required to consider the tags when interpreting the meaning of a resource. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | For example codes, see [CommonTags](http://hl7.org/fhir/R4/valueset-common-tags.html) Codes that represent various types of tags, commonly workflow-related; e.g. "Needs review by Dr. Jones". |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) |
| Comments | The tags can be updated without changing the stated version of the resource. The list of tags is a set. Uniqueness is based the system/code, and version and display are ignored. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 12. **OrganizationAffiliation.implicitRules** | |
| Definition | A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Comments | Asserting this rule set restricts the content to be only understood by a limited set of trading partners. This inherently limits the usefulness of the data in the long term. However, the existing health eco-system is highly fractured, and not yet ready to define, collect, and exchange data in a generally computable sense. Wherever possible, implementers and/or specification writers should avoid using this element. Often, when used, the URL is a reference to an implementation guide that defines these special rules as part of it's narrative along with other profiles, value sets, etc. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 13. **OrganizationAffiliation.language** | |
| Definition | The base language in which the resource is written. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHOULD be taken from [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html) [Max Binding](http://hl7.org/fhir/R4/extension-elementdefinition-maxvalueset.html "Max Value Set Extension"): [AllLanguages](http://hl7.org/fhir/R4/valueset-all-languages.html) A human language. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| Comments | Language is provided to support indexing and accessibility (typically, services such as text to speech use the language tag). The html language tag in the narrative applies to the narrative. The language tag on the resource may be used to specify the language of other presentations generated from the data in the resource. Not all the content has to be in the base language. The Resource.language should not be assumed to apply to the narrative automatically. If a language is specified, it should it also be specified on the div element in the html (see rules in HTML5 for information about the relationship between xml:lang and the html lang attribute). |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 14. **OrganizationAffiliation.text** | |
| Definition | A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Narrative](http://hl7.org/fhir/R4/datatypes.html#Narrative) |
| Alternate Names | narrative, html, xhtml, display |
| Comments | Contained resources do not have narrative. Resources that are not contained SHOULD have a narrative. In some cases, a resource may only have text with little or no additional discrete data (as long as all minOccurs=1 elements are satisfied). This may be necessary for data from legacy systems where information is captured as a "text blob" or where text is additionally entered raw or narrated and encoded information is added later. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 15. **OrganizationAffiliation.contained** | |
| Definition | These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Resource](http://hl7.org/fhir/R4/resource.html) |
| Alternate Names | inline resources, anonymous resources, contained resources |
| Comments | This should never be done when the content can be identified properly, as once identification is lost, it is extremely difficult (and context dependent) to restore it again. Contained resources may have profiles and tags In their meta elements, but SHALL NOT have security labels. |
| 16. **OrganizationAffiliation.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on OrganizationAffiliation.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 17. **OrganizationAffiliation.extension:qualification** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | qualification |
| Definition | An extension to add qualifications for an organization (e.g. accreditation) or practitionerRole (e.g. registered to prescribe controlled substances). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* This element is affected by the following invariants: ele-1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)([Qualification](StructureDefinition-qualification.html "[CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/qualification]]")) (Complex Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 18. **OrganizationAffiliation.modifierExtension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Modifier extensions allow for extensions that *cannot* be safely ignored to be clearly distinguished from the vast majority of extensions which can be safely ignored. This promotes interoperability by eliminating the need for implementers to prohibit the presence of extensions. For further information, see the [definition of modifier extensions](http://hl7.org/fhir/R4/extensibility.html#modifierExtension). |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 19. **OrganizationAffiliation.identifier** | |
| Definition | Business identifiers that are specific to this role. |
| Note | This is a business identifier, not a resource identifier (see [discussion](http://hl7.org/fhir/R4/resource.html#identifiers)) |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) |
| Requirements | Often, specific identities are assigned for the agent. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 20. **OrganizationAffiliation.identifier.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 21. **OrganizationAffiliation.identifier.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on OrganizationAffiliation.identifier.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 22. **OrganizationAffiliation.identifier.use** | |
| Definition | The purpose of this identifier. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [IdentifierUse](http://hl7.org/fhir/R4/valueset-identifier-use.html) Identifies the purpose for this identifier, if known . |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Allows the appropriate identifier for a particular context of use to be selected from among a set of identifiers. |
| Comments | Applications can assume that an identifier is permanent unless it explicitly says that it is temporary. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 23. **OrganizationAffiliation.identifier.type** | |
| Definition | A coded type for the identifier that can be used to determine which identifier to use for a specific purpose. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [Identifier Type Codes](http://hl7.org/fhir/R4/valueset-identifier-type.html); other codes may be used where these codes are not suitable A coded type for an identifier that can be used to determine which identifier to use for a specific purpose. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Allows users to make use of identifiers when the identifier system is not known. |
| Comments | This element deals only with general categories of identifiers. It SHOULD not be used for codes that correspond 1..1 with the Identifier.system. Some identifiers may fall into multiple categories due to common usage. Where the system is known, a type is unnecessary because the type is always part of the system definition. However systems often need to handle identifiers where the system is not known. There is not a 1:1 relationship between type and system, since many different systems have the same type. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 24. **OrganizationAffiliation.identifier.system** | |
| Definition | Establishes the namespace for the value - that is, a URL that describes a set values that are unique. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Requirements | There are many sets of identifiers. To perform matching of two identifiers, we need to know what set we're dealing with. The system identifies a particular set of unique identifiers. |
| Comments | Identifier.system is always case sensitive. |
| Example | **General**:http://www.acme.com/identifiers/patient |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 25. **OrganizationAffiliation.identifier.value** | |
| Definition | The portion of the identifier typically relevant to the user and which is unique within the context of the system. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | If the value is a full URI, then the system SHALL be urn:ietf:rfc:3986. The value's primary purpose is computational mapping. As a result, it may be normalized for comparison purposes (e.g. removing non-significant whitespace, dashes, etc.) A value formatted for human display can be conveyed using the [Rendered Value extension](http://hl7.org/fhir/R4/extension-rendered-value.html). Identifier.value is to be treated as case sensitive unless knowledge of the Identifier.system allows the processer to be confident that non-case-sensitive processing is safe. |
| Example | **General**:123456 |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 26. **OrganizationAffiliation.identifier.period** | |
| Definition | Time period during which identifier is/was valid for use. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 27. **OrganizationAffiliation.identifier.assigner** | |
| Definition | Organization that issued/manages the identifier. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([Organization](http://hl7.org/fhir/R4/organization.html "http://hl7.org/fhir/StructureDefinition/Organization")) |
| Comments | The Identifier.assigner may omit the .reference element and only contain a .display element reflecting the name or other textual information about the assigning organization. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 28. **OrganizationAffiliation.active** | |
| Definition | Whether this organization affiliation record is in active use. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [boolean](http://hl7.org/fhir/R4/datatypes.html#boolean) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Need to be able to mark an organization affiliation record as not to be used because it was created in error, or otherwise no longer in active use. |
| Comments | If this value is false, you may refer to the period to see when the role was in active use. If there is no period specified, no inference can be made about when it was active. |
| Meaning if Missing | This resource is generally assumed to be active if no value is provided for the active element |
| Pattern Value | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 29. **OrganizationAffiliation.period** | |
| Definition | The period during which the participatingOrganization is affiliated with the primary organization. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | An affiliation may be created ahead of time and only be active for a defined period of time. Once the affiliation is complete, the fact that it existed may still be required. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 30. **OrganizationAffiliation.organization** | |
| Definition | Organization where the role is available (primary organization/has members). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetOrganization](StructureDefinition-plannet-Organization.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 31. **OrganizationAffiliation.participatingOrganization** | |
| Definition | The Participating Organization provides/performs the role(s) defined by the code to the Primary Organization (e.g. providing services or is a member of). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetOrganization](StructureDefinition-plannet-Organization.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 32. **OrganizationAffiliation.network** | |
| Definition | Health insurance provider network in which the participatingOrganization provides the role's services (if defined) at the indicated locations (if defined). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetNetwork](StructureDefinition-plannet-Network.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Network")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 33. **OrganizationAffiliation.code** | |
| Definition | Definition of the role the participatingOrganization plays in the association. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [OrganizationAffiliation Roles](ValueSet-OrganizationAffiliationRoleVS.html); other codes may be used where these codes are not suitable |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 34. **OrganizationAffiliation.specialty** | |
| Definition | Specific specialty of the participatingOrganization in the context of the role. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [Specialties VS](ValueSet-SpecialtiesVS.html) |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 35. **OrganizationAffiliation.location** | |
| Definition | The location(s) at which the role occurs. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetLocation](StructureDefinition-plannet-Location.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 36. **OrganizationAffiliation.healthcareService** | |
| Definition | Healthcare services provided through the role. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetHealthcareService](StructureDefinition-plannet-HealthcareService.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-HealthcareService")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 37. **OrganizationAffiliation.telecom** | |
| Definition | Contact details at the participatingOrganization relevant to this Affiliation. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Sometimes a participating organization provides dedicated contacts to handle enquiries specifically for the role provided to the affiliated organization. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 38. **OrganizationAffiliation.telecom.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 39. **OrganizationAffiliation.telecom.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on OrganizationAffiliation.telecom.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 40. **OrganizationAffiliation.telecom.system** | |
| Definition | Telecommunications form for contact point - what communications system is required to make use of the contact. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 This element is affected by the following invariants: cpt-2 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [ContactPointSystem](http://hl7.org/fhir/R4/valueset-contact-point-system.html) Telecommunications form for contact point. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 41. **OrganizationAffiliation.telecom.value** | |
| Definition | The actual contact point details, in a form that is meaningful to the designated communication system (i.e. phone number or email address). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Need to support legacy numbers that are not in a tightly controlled format. |
| Comments | Additional text data such as phone extension numbers, or notes about use of the contact are sometimes included in the value. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 42. **OrganizationAffiliation.telecom.use** | |
| Definition | Identifies the purpose for the contact point. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [ContactPointUse](http://hl7.org/fhir/R4/valueset-contact-point-use.html) Use of contact point. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Need to track the way a person uses this contact, so a user can choose which is appropriate for their purpose. |
| Comments | Applications can assume that a contact is current unless it explicitly says that it is temporary or old. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 43. **OrganizationAffiliation.telecom.rank** | |
| Definition | Specifies a preferred order in which to use a set of contacts. ContactPoints with lower rank values are more preferred than those with higher rank values. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [positiveInt](http://hl7.org/fhir/R4/datatypes.html#positiveInt) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | Note that rank does not necessarily follow the order in which the contacts are represented in the instance. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 44. **OrganizationAffiliation.telecom.period** | |
| Definition | Time period when the contact point was/is in use. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 45. **OrganizationAffiliation.endpoint** | |
| Definition | Technical endpoints providing access to services operated for this role. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetEndpoint](StructureDefinition-plannet-Endpoint.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Endpoint")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |