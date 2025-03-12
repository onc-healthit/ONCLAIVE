# Resource Profile: PlannetLocation - Detailed Descriptions

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plan-Net Location**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-plannet-Location.html)
* [Detailed Descriptions](#)
* [Mappings](StructureDefinition-plannet-Location-mappings.html)
* [Examples](StructureDefinition-plannet-Location-examples.html)

## Resource Profile: PlannetLocation - Detailed Descriptions

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Definitions for the plannet-Location resource profile.

|  |  |
| --- | --- |
| 1. **Location** | |
| Definition | Details and position information for a physical place where services are provided and resources and participants may be stored, found, contained, or accommodated. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| Invariants | **Defined on this element**  **dom-2**: If the resource is contained in another resource, it SHALL NOT contain nested Resources (: contained.contained.empty()) **dom-3**: If the resource is contained in another resource, it SHALL be referred to from elsewhere in the resource or SHALL refer to the containing resource (: contained.where((('#'+id in (%resource.descendants().reference | %resource.descendants().as(canonical) | %resource.descendants().as(uri) | %resource.descendants().as(url))) or descendants().where(reference = '#').exists() or descendants().where(as(canonical) = '#').exists() or descendants().where(as(canonical) = '#').exists()).not()).trace('unmatched', id).empty()) **dom-4**: If a resource is contained in another resource, it SHALL NOT have a meta.versionId or a meta.lastUpdated (: contained.meta.versionId.empty() and contained.meta.lastUpdated.empty()) **dom-5**: If a resource is contained in another resource, it SHALL NOT have a security label (: contained.meta.security.empty()) **dom-6**: A resource should have narrative for robust management (: text.`div`.exists()) |
| 2. **Location.id** | |
| Definition | The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Comments | The only time that a resource does not have an id is when it is being submitted to the server using a create operation. |
| 3. **Location.meta** | |
| Definition | The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Meta](http://hl7.org/fhir/R4/datatypes.html#Meta) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 4. **Location.meta.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 5. **Location.meta.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Location.meta.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 6. **Location.meta.versionId** | |
| Definition | The version specific identifier, as it appears in the version portion of the URL. This value changes when the resource is created, updated, or deleted. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [id](http://hl7.org/fhir/R4/datatypes.html#id) |
| Comments | The server assigns this value, and ignores what the client specifies, except in the case that the server is imposing version integrity on updates/deletes. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 7. **Location.meta.lastUpdated** | |
| Definition | When the resource last changed - e.g. when the version changed. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [instant](http://hl7.org/fhir/R4/datatypes.html#instant) |
| Comments | This value is always populated except when the resource is first being created. The server / resource manager sets this value; what a client provides is irrelevant. This is equivalent to the HTTP Last-Modified and SHOULD have the same value on a [read](http://hl7.org/fhir/R4/http.html#read) interaction. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 8. **Location.meta.source** | |
| Definition | A uri that identifies the source system of the resource. This provides a minimal amount of [Provenance](http://hl7.org/fhir/R4/provenance.html#) information that can be used to track or differentiate the source of information in the resource. The source may identify another FHIR server, document, message, database, etc. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Comments | In the provenance resource, this corresponds to Provenance.entity.what[x]. The exact use of the source (and the implied Provenance.entity.role) is left to implementer discretion. Only one nominated source is allowed; for additional provenance details, a full Provenance resource should be used.  This element can be used to indicate where the current master source of a resource that has a canonical URL if the resource is no longer hosted at the canonical URL. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 9. **Location.meta.profile** | |
| Definition | A list of profiles (references to [StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html#) resources) that this resource claims to conform to. The URL is a reference to [StructureDefinition.url](http://hl7.org/fhir/R4/structuredefinition-definitions.html#StructureDefinition.url). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [canonical](http://hl7.org/fhir/R4/datatypes.html#canonical)([StructureDefinition](http://hl7.org/fhir/R4/structuredefinition.html "http://hl7.org/fhir/StructureDefinition/StructureDefinition")) |
| Comments | It is up to the server and/or other infrastructure of policy to determine whether/how these claims are verified and/or updated over time. The list of profile URLs is a set. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 10. **Location.meta.security** | |
| Definition | Security labels applied to this resource. These tags connect specific resources to the overall security policy and infrastructure. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [All Security Labels](http://hl7.org/fhir/R4/valueset-security-labels.html); other codes may be used where these codes are not suitable Security Labels from the Healthcare Privacy and Security Classification System. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) |
| Comments | The security labels can be updated without changing the stated version of the resource. The list of security labels is a set. Uniqueness is based the system/code, and version and display are ignored. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 11. **Location.meta.tag** | |
| Definition | Tags applied to this resource. Tags are intended to be used to identify and relate resources to process and workflow, and applications are not required to consider the tags when interpreting the meaning of a resource. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | For example codes, see [CommonTags](http://hl7.org/fhir/R4/valueset-common-tags.html) Codes that represent various types of tags, commonly workflow-related; e.g. "Needs review by Dr. Jones". |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) |
| Comments | The tags can be updated without changing the stated version of the resource. The list of tags is a set. Uniqueness is based the system/code, and version and display are ignored. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 12. **Location.implicitRules** | |
| Definition | A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Comments | Asserting this rule set restricts the content to be only understood by a limited set of trading partners. This inherently limits the usefulness of the data in the long term. However, the existing health eco-system is highly fractured, and not yet ready to define, collect, and exchange data in a generally computable sense. Wherever possible, implementers and/or specification writers should avoid using this element. Often, when used, the URL is a reference to an implementation guide that defines these special rules as part of it's narrative along with other profiles, value sets, etc. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 13. **Location.language** | |
| Definition | The base language in which the resource is written. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHOULD be taken from [CommonLanguages](http://hl7.org/fhir/R4/valueset-languages.html) [Max Binding](http://hl7.org/fhir/R4/extension-elementdefinition-maxvalueset.html "Max Value Set Extension"): [AllLanguages](http://hl7.org/fhir/R4/valueset-all-languages.html) A human language. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| Comments | Language is provided to support indexing and accessibility (typically, services such as text to speech use the language tag). The html language tag in the narrative applies to the narrative. The language tag on the resource may be used to specify the language of other presentations generated from the data in the resource. Not all the content has to be in the base language. The Resource.language should not be assumed to apply to the narrative automatically. If a language is specified, it should it also be specified on the div element in the html (see rules in HTML5 for information about the relationship between xml:lang and the html lang attribute). |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 14. **Location.text** | |
| Definition | A human-readable narrative that contains a summary of the resource and can be used to represent the content of the resource to a human. The narrative need not encode all the structured data, but is required to contain sufficient detail to make it "clinically safe" for a human to just read the narrative. Resource definitions may define what content should be represented in the narrative to ensure clinical safety. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Narrative](http://hl7.org/fhir/R4/datatypes.html#Narrative) |
| Alternate Names | narrative, html, xhtml, display |
| Comments | Contained resources do not have narrative. Resources that are not contained SHOULD have a narrative. In some cases, a resource may only have text with little or no additional discrete data (as long as all minOccurs=1 elements are satisfied). This may be necessary for data from legacy systems where information is captured as a "text blob" or where text is additionally entered raw or narrated and encoded information is added later. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 15. **Location.contained** | |
| Definition | These resources do not have an independent existence apart from the resource that contains them - they cannot be identified independently, and nor can they have their own independent transaction scope. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Resource](http://hl7.org/fhir/R4/resource.html) |
| Alternate Names | inline resources, anonymous resources, contained resources |
| Comments | This should never be done when the content can be identified properly, as once identification is lost, it is extremely difficult (and context dependent) to restore it again. Contained resources may have profiles and tags In their meta elements, but SHALL NOT have security labels. |
| 16. **Location.extension** | |
| Definition | An Extension |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Location.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 17. **Location.extension:newpatients** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | newpatients |
| Definition | New Patients indicates whether new patients are being accepted in general, or from a specific network.  This extension is included in the PractitionerRole, HealthcareService, and Location profiles.  This provides needed flexibility for specifying whether a provider accepts new patients by location and network. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* This element is affected by the following invariants: ele-1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)([NewPatients](StructureDefinition-newpatients.html "[CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients]]")) (Complex Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) **new-patients-characteristics**: If no new patients are accepted, no characteristics are allowed (: extension('acceptingPatients').valueCodeableConcept.coding.exists(code = 'no') implies extension('characteristics').empty()) |
| 18. **Location.extension:accessibility** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | accessibility |
| Definition | An extension to describe accessibility options offered by a practitioner or at a location. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* This element is affected by the following invariants: ele-1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)([Accessibility](StructureDefinition-accessibility.html "[CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/accessibility]]")) (Extension Type: [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept)) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 19. **Location.extension:region** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | region |
| Definition | A boundary shape that represents the outside edge of the location (in GeoJSON format) This shape may have holes, and disconnected shapes. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 This element is affected by the following invariants: ele-1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)([boundary-geojson](http://hl7.org/fhir/R4/extension-location-boundary-geojson.html "[CanonicalType[http://hl7.org/fhir/StructureDefinition/location-boundary-geojson]]")) (Extension Type: [Attachment](http://hl7.org/fhir/R4/datatypes.html#Attachment)) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | The format of the content is GeoJSON in both the JSON and XML formats. It will be stored in the resource using the .data property, and externally referenced via the URL property. The mimetype to be used will be 'application/geo+json'. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 20. **Location.modifierExtension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the resource and that modifies the understanding of the element that contains it and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer is allowed to define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Modifier extensions allow for extensions that *cannot* be safely ignored to be clearly distinguished from the vast majority of extensions which can be safely ignored. This promotes interoperability by eliminating the need for implementers to prohibit the presence of extensions. For further information, see the [definition of modifier extensions](http://hl7.org/fhir/R4/extensibility.html#modifierExtension). |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 21. **Location.identifier** | |
| Definition | Unique code or number identifying the location to its users. |
| Note | This is a business identifier, not a resource identifier (see [discussion](http://hl7.org/fhir/R4/resource.html#identifiers)) |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Identifier](http://hl7.org/fhir/R4/datatypes.html#Identifier) |
| Requirements | Organization label locations in registries, need to keep track of those. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 22. **Location.identifier.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 23. **Location.identifier.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Location.identifier.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 24. **Location.identifier.use** | |
| Definition | The purpose of this identifier. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [IdentifierUse](http://hl7.org/fhir/R4/valueset-identifier-use.html) Identifies the purpose for this identifier, if known . |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Allows the appropriate identifier for a particular context of use to be selected from among a set of identifiers. |
| Comments | Applications can assume that an identifier is permanent unless it explicitly says that it is temporary. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 25. **Location.identifier.type** | |
| Definition | A coded type for the identifier that can be used to determine which identifier to use for a specific purpose. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [Identifier Type Codes](http://hl7.org/fhir/R4/valueset-identifier-type.html); other codes may be used where these codes are not suitable A coded type for an identifier that can be used to determine which identifier to use for a specific purpose. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Allows users to make use of identifiers when the identifier system is not known. |
| Comments | This element deals only with general categories of identifiers. It SHOULD not be used for codes that correspond 1..1 with the Identifier.system. Some identifiers may fall into multiple categories due to common usage. Where the system is known, a type is unnecessary because the type is always part of the system definition. However systems often need to handle identifiers where the system is not known. There is not a 1:1 relationship between type and system, since many different systems have the same type. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 26. **Location.identifier.system** | |
| Definition | Establishes the namespace for the value - that is, a URL that describes a set values that are unique. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [uri](http://hl7.org/fhir/R4/datatypes.html#uri) |
| Requirements | There are many sets of identifiers. To perform matching of two identifiers, we need to know what set we're dealing with. The system identifies a particular set of unique identifiers. |
| Comments | Identifier.system is always case sensitive. |
| Example | **General**:http://www.acme.com/identifiers/patient |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 27. **Location.identifier.value** | |
| Definition | The portion of the identifier typically relevant to the user and which is unique within the context of the system. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | If the value is a full URI, then the system SHALL be urn:ietf:rfc:3986. The value's primary purpose is computational mapping. As a result, it may be normalized for comparison purposes (e.g. removing non-significant whitespace, dashes, etc.) A value formatted for human display can be conveyed using the [Rendered Value extension](http://hl7.org/fhir/R4/extension-rendered-value.html). Identifier.value is to be treated as case sensitive unless knowledge of the Identifier.system allows the processer to be confident that non-case-sensitive processing is safe. |
| Example | **General**:123456 |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 28. **Location.identifier.period** | |
| Definition | Time period during which identifier is/was valid for use. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 29. **Location.identifier.assigner** | |
| Definition | Organization that issued/manages the identifier. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([Organization](http://hl7.org/fhir/R4/organization.html "http://hl7.org/fhir/StructureDefinition/Organization")) |
| Comments | The Identifier.assigner may omit the .reference element and only contain a .display element reflecting the name or other textual information about the assigning organization. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 30. **Location.status** | |
| Definition | The status property covers the general availability of the resource, not the current value which may be covered by the operationStatus, or by a schedule/slots if they are configured for the location. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [LocationStatus](http://hl7.org/fhir/R4/valueset-location-status.html) Indicates whether the location is still in use. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Fixed Value | active |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 31. **Location.operationalStatus** | |
| Definition | The operational status covers operation values most relevant to beds (but can also apply to rooms/units/chairs/etc. such as an isolation unit/dialysis chair). This typically covers concepts such as contamination, housekeeping, and other activities like maintenance. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHOULD be taken from [hl7VS-bedStatus](http://terminology.hl7.org/3.1.0/ValueSet-v2-0116.html) The operational status if the location (where typically a bed/room). |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 32. **Location.name** | |
| Definition | Name of the location as used by humans. Does not need to be unique. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | If the name of a location changes, consider putting the old name in the alias column so that it can still be located through searches. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 33. **Location.alias** | |
| Definition | A list of alternate names that the location is known as, or was known as, in the past. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Over time locations and organizations go through many changes and can be known by different names.  For searching knowing previous names that the location was known by can be very useful. |
| Comments | There are no dates associated with the alias/historic names, as this is not intended to track when names were used, but to assist in searching so that older names can still result in identifying the location. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 34. **Location.description** | |
| Definition | Description of the Location, which helps in finding or referencing the place. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Humans need additional information to verify a correct location has been identified. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 35. **Location.mode** | |
| Definition | Indicates whether a resource instance represents a specific location or a class of locations. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..0 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [LocationMode](http://hl7.org/fhir/R4/valueset-location-mode.html) Indicates whether a resource instance represents a specific location or a class of locations. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| Requirements | When using a Location resource for scheduling or orders, we need to be able to refer to a class of Locations instead of a specific Location. |
| Comments | This is labeled as a modifier because whether or not the location is a class of locations changes how it can be used and understood. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 36. **Location.type** | |
| Definition | Indicates the type of function performed at the location. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [ServiceDeliveryLocationRoleType](http://terminology.hl7.org/3.1.0/ValueSet-v3-ServiceDeliveryLocationRoleType.html); other codes may be used where these codes are not suitable Indicates the type of function performed at the location. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 37. **Location.telecom** | |
| Definition | The contact details of communication devices available at the location. This can include phone numbers, fax numbers, mobile numbers, email addresses and web sites. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [ContactPoint](http://hl7.org/fhir/R4/datatypes.html#ContactPoint) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 38. **Location.telecom.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 39. **Location.telecom.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Location.telecom.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 40. **Location.telecom.extension:contactpoint-availabletime** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | contactpoint-availabletime |
| Definition | An extension representing the days and times a contact point is available |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)([ContactPointAvailableTime](StructureDefinition-contactpoint-availabletime.html "[CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/contactpoint-availabletime]]")) (Complex Extension) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 41. **Location.telecom.extension:via-intermediary** | |
| [SliceName](http://hl7.org/fhir/R4/profiling.html#slicing) | via-intermediary |
| Definition | A reference to an alternative point of contact (plannet-PractitionerRole, plannet-Organization, plannet-OrganizationAffiliation, or plannet-Location) for this organization |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension)([ViaIntermediary](StructureDefinition-via-intermediary.html "[CanonicalType[http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/via-intermediary]]")) (Extension Type: [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetPractitionerRole](StructureDefinition-plannet-PractitionerRole.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole") | [PlannetOrganizationAffiliation](StructureDefinition-plannet-OrganizationAffiliation.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-OrganizationAffiliation") | [PlannetLocation](StructureDefinition-plannet-Location.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location") | [PlannetOrganization](StructureDefinition-plannet-Organization.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization"))) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 42. **Location.telecom.system** | |
| Definition | Telecommunications form for contact point - what communications system is required to make use of the contact. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 This element is affected by the following invariants: cpt-2 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [ContactPointSystem](http://hl7.org/fhir/R4/valueset-contact-point-system.html) Telecommunications form for contact point. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 43. **Location.telecom.value** | |
| Definition | The actual contact point details, in a form that is meaningful to the designated communication system (i.e. phone number or email address). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Need to support legacy numbers that are not in a tightly controlled format. |
| Comments | Additional text data such as phone extension numbers, or notes about use of the contact are sometimes included in the value. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 44. **Location.telecom.use** | |
| Definition | Identifies the purpose for the contact point. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [ContactPointUse](http://hl7.org/fhir/R4/valueset-contact-point-use.html) Use of contact point. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Need to track the way a person uses this contact, so a user can choose which is appropriate for their purpose. |
| Comments | Applications can assume that a contact is current unless it explicitly says that it is temporary or old. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 45. **Location.telecom.rank** | |
| Definition | Specifies a preferred order in which to use a set of contacts. ContactPoints with lower rank values are more preferred than those with higher rank values. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [positiveInt](http://hl7.org/fhir/R4/datatypes.html#positiveInt) |
| Comments | Note that rank does not necessarily follow the order in which the contacts are represented in the instance. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 46. **Location.telecom.period** | |
| Definition | Time period when the contact point was/is in use. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 47. **Location.address** | |
| Definition | Physical location. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Address](http://hl7.org/fhir/R4/datatypes.html#Address) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | If locations can be visited, we need to keep track of their address. |
| Comments | Additional addresses should be recorded using another instance of the Location resource, or via the Organization. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 48. **Location.address.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 49. **Location.address.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| [Slicing](http://hl7.org/fhir/R4/profiling.html#slicing) | This element introduces a set of slices on Location.address.extension. The slices are unordered and Open, and can be differentiated using the following discriminators:  * value @ url |
| 50. **Location.address.use** | |
| Definition | The purpose of this address. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [AddressUse](http://hl7.org/fhir/R4/valueset-address-use.html) The use of an address. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Allows an appropriate address to be chosen from a list of many. |
| Comments | Applications can assume that an address is current unless it explicitly says that it is temporary or old. |
| Example | **General**:home |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 51. **Location.address.type** | |
| Definition | Distinguishes between physical addresses (those you can visit) and mailing addresses (e.g. PO Boxes and care-of addresses). Most addresses are both. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [AddressType](http://hl7.org/fhir/R4/valueset-address-type.html) The type of an address (physical / postal). |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| Comments | The definition of Address states that "address is intended to describe postal addresses, not physical locations". However, many applications track whether an address has a dual purpose of being a location that can be visited as well as being a valid delivery destination, and Postal addresses are often used as proxies for physical locations (also see the [Location](http://hl7.org/fhir/R4/location.html#) resource). |
| Example | **General**:both |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 52. **Location.address.text** | |
| Definition | Specifies the entire address as it should be displayed e.g. on a postal label. This may be provided instead of or as well as the specific parts. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Requirements | A renderable, unencoded form. |
| Comments | Can provide both a text representation and parts. Applications updating an address SHALL ensure that when both text and parts are present, no content is included in the text that isn't found in a part. |
| Example | **General**:137 Nowhere Street, Erewhon 9132 |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 53. **Location.address.line** | |
| Definition | This component contains the house number, apartment number, street name, street direction, P.O. Box number, delivery hints, and similar address information. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Example | **General**:137 Nowhere Street |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 54. **Location.address.city** | |
| Definition | The name of the city, town, suburb, village or other community or delivery center. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Alternate Names | Municpality |
| Example | **General**:Erewhon |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 55. **Location.address.district** | |
| Definition | The name of the administrative area (county). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Alternate Names | County |
| Comments | District is sometimes known as county, but in some regions 'county' is used in place of city (municipality), so county name should be conveyed in city instead. |
| Example | **General**:Madison |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 56. **Location.address.state** | |
| Definition | Sub-unit of a country with limited sovereignty in a federally organized country. A code may be used if codes are in common use (e.g. US 2 letter state codes). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [USPS Two Letter Alphabetic Codes](http://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-usps-state.html); other codes may be used where these codes are not suitable Two letter USPS alphabetic codes. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Alternate Names | Province, Territory |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 57. **Location.address.postalCode** | |
| Definition | A postal code designating a region defined by the postal service. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Alternate Names | Zip |
| Example | **General**:9132 |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 58. **Location.address.country** | |
| Definition | Country - a nation as commonly understood or generally accepted. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| Comments | ISO 3166 3 letter codes can be used in place of a human readable country name. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 59. **Location.address.period** | |
| Definition | Time period when address was/is in use. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Period](http://hl7.org/fhir/R4/datatypes.html#Period) |
| Requirements | Allows addresses to be placed in historical context. |
| Example | **General**:<valuePeriod xmlns="http://hl7.org/fhir">   <start value="2010-03-23"/>   <end value="2010-07-01"/> </valuePeriod> |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 60. **Location.physicalType** | |
| Definition | Physical form of the location, e.g. building, room, vehicle, road. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | For example codes, see [LocationType](http://hl7.org/fhir/R4/valueset-location-physical-type.html) Physical form of the location. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [CodeableConcept](http://hl7.org/fhir/R4/datatypes.html#CodeableConcept) |
| Requirements | For purposes of showing relevant locations in queries, we need to categorize locations. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 61. **Location.position** | |
| Definition | The absolute geographic location of the Location, expressed using the WGS84 datum (This is the same co-ordinate system used in KML). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | For mobile applications and automated route-finding knowing the exact location of the Location is required. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 62. **Location.position.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 63. **Location.position.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 64. **Location.position.modifierExtension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Modifier extensions allow for extensions that *cannot* be safely ignored to be clearly distinguished from the vast majority of extensions which can be safely ignored. This promotes interoperability by eliminating the need for implementers to prohibit the presence of extensions. For further information, see the [definition of modifier extensions](http://hl7.org/fhir/R4/extensibility.html#modifierExtension). |
| Alternate Names | extensions, user content, modifiers |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 65. **Location.position.longitude** | |
| Definition | Longitude. The value domain and the interpretation are the same as for the text of the longitude element in KML (see notes below). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [decimal](http://hl7.org/fhir/R4/datatypes.html#decimal) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 66. **Location.position.latitude** | |
| Definition | Latitude. The value domain and the interpretation are the same as for the text of the latitude element in KML (see notes below). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 1..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [decimal](http://hl7.org/fhir/R4/datatypes.html#decimal) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 67. **Location.position.altitude** | |
| Definition | Altitude. The value domain and the interpretation are the same as for the text of the altitude element in KML (see notes below). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [decimal](http://hl7.org/fhir/R4/datatypes.html#decimal) |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 68. **Location.managingOrganization** | |
| Definition | The organization responsible for the provisioning and upkeep of the location. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetOrganization](StructureDefinition-plannet-Organization.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Need to know who manages the location. |
| Comments | This can also be used as the part of the organization hierarchy where this location provides services. These services can be defined through the HealthcareService resource. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 69. **Location.partOf** | |
| Definition | Another Location of which this Location is physically a part of. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetLocation](StructureDefinition-plannet-Location.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | For purposes of location, display and identification, knowing which locations are located within other locations is important. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 70. **Location.hoursOfOperation** | |
| Definition | What days/times during a week is this location usually open. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [BackboneElement](http://hl7.org/fhir/R4/datatypes.html#BackboneElement) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Comments | This type of information is commonly found published in directories and on websites informing customers when the facility is available.  Specific services within the location may have their own hours which could be shorter (or longer) than the locations hours. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 71. **Location.hoursOfOperation.id** | |
| Definition | Unique id for the element within a resource (for internal references). This may be any string value that does not contain spaces. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| 72. **Location.hoursOfOperation.extension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| Alternate Names | extensions, user content |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 73. **Location.hoursOfOperation.modifierExtension** | |
| Definition | May be used to represent additional information that is not part of the basic definition of the element and that modifies the understanding of the element in which it is contained and/or the understanding of the containing element's descendants. Usually modifier elements provide negation or qualification. To make the use of extensions safe and manageable, there is a strict set of governance applied to the definition and use of extensions. Though any implementer can define an extension, there is a set of requirements that SHALL be met as part of the definition of the extension. Applications processing a resource are required to check for modifier extensions.  Modifier extensions SHALL NOT change the meaning of any elements on Resource or DomainResource (including cannot change the meaning of modifierExtension itself). |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Extension](http://hl7.org/fhir/R4/extensibility.html#Extension) |
| [Is Modifier](http://hl7.org/fhir/R4/conformance-rules.html#ismodifier) | true |
| Requirements | Modifier extensions allow for extensions that *cannot* be safely ignored to be clearly distinguished from the vast majority of extensions which can be safely ignored. This promotes interoperability by eliminating the need for implementers to prohibit the presence of extensions. For further information, see the [definition of modifier extensions](http://hl7.org/fhir/R4/extensibility.html#modifierExtension). |
| Alternate Names | extensions, user content, modifiers |
| Comments | There can be no stigma associated with the use of extensions by any application, project, or standard - regardless of the institution or jurisdiction that uses or defines the extensions. The use of extensions is what allows the FHIR specification to retain a core level of simplicity for everyone. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) **ext-1**: Must have either extensions or value[x], not both (: extension.exists() != value.exists()) |
| 74. **Location.hoursOfOperation.daysOfWeek** | |
| Definition | Indicates which days of the week are available between the start and end Times. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Binding](http://hl7.org/fhir/R4/terminologies.html) | The codes SHALL be taken from [DaysOfWeek](http://hl7.org/fhir/R4/valueset-days-of-week.html) The days of the week. |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [code](http://hl7.org/fhir/R4/datatypes.html#code) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 75. **Location.hoursOfOperation.allDay** | |
| Definition | The Location is open all day. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [boolean](http://hl7.org/fhir/R4/datatypes.html#boolean) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 76. **Location.hoursOfOperation.openingTime** | |
| Definition | Time that the Location opens. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [time](http://hl7.org/fhir/R4/datatypes.html#time) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 77. **Location.hoursOfOperation.closingTime** | |
| Definition | Time that the Location closes. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [time](http://hl7.org/fhir/R4/datatypes.html#time) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 78. **Location.availabilityExceptions** | |
| Definition | A description of when the locations opening ours are different to normal, e.g. public holiday availability. Succinctly describing all possible exceptions to normal site availability as detailed in the opening hours Times. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..1 |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [string](http://hl7.org/fhir/R4/datatypes.html#string) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |
| 79. **Location.endpoint** | |
| Definition | Technical endpoints providing access to services operated for the location. |
| [Control](http://hl7.org/fhir/R4/conformance-rules.html#conformance) | 0..\* |
| [Type](http://hl7.org/fhir/R4/datatypes.html) | [Reference](http://hl7.org/fhir/R4/references.html#Reference)([PlannetEndpoint](StructureDefinition-plannet-Endpoint.html "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Endpoint")) |
| [Must Support](http://hl7.org/fhir/R4/conformance-rules.html#mustSupport) | true |
| Requirements | Organizations may have different systems at different locations that provide various services and need to be able to define the technical connection details for how to connect to them, and for what purpose. |
| Invariants | **Defined on this element**  **ele-1**: All FHIR elements must have a @value or children (: hasValue() or (children().count() > id.count())) |