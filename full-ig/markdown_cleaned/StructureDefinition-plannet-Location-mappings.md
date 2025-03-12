# Resource Profile: PlannetLocation - Mappings

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Plan-Net Location**

Publication Build: This will be filled in by the publication tooling

* [Content](StructureDefinition-plannet-Location.html)
* [Detailed Descriptions](StructureDefinition-plannet-Location-definitions.html)
* [Mappings](#)
* [Examples](StructureDefinition-plannet-Location-examples.html)

## Resource Profile: PlannetLocation - Mappings

|  |  |
| --- | --- |
| Active as of 2022-04-04 | |

Mappings for the plannet-Location resource profile.

### Mappings for ServD (<http://www.omg.org/spec/ServD/1.0/>)

|  |  |  |
| --- | --- | --- |
| **PlannetLocation** | | |
| Location | Organization |
| identifier |  |
| system | ./IdentifierType |
| value | ./Value |
| period | ./StartDate and ./EndDate |
| assigner | ./IdentifierIssuingAuthority |
| name | ./PrimaryAddress and ./OtherAddresses |
| telecom |  |
| system | ./ContactPointType |
| value | ./Value |
| use | ./ContactPointPurpose |
| period | ./StartDate and ./EndDate |
| address | n/a |
| use | ./AddressPurpose |
| line | ./StreetAddress (newline delimitted) |
| city | ./Jurisdiction |
| state | ./Region, ./Sites |
| postalCode | ./PostalIdentificationCode |
| country | ./Country |
| period | ./StartDate and ./EndDate |

### Mappings for RIM Mapping ([http://hl7.org/v3](http://hl7.org/comparison-v3.html))

|  |  |  |
| --- | --- | --- |
| **PlannetLocation** | | |
| Location | Entity. Role, or Act, .Role[classCode=SDLC] |
| meta |  |
| id | n/a |
| extension | n/a |
| text | Act.text? |
| contained | N/A |
| modifierExtension | N/A |
| identifier | .id |
| id | n/a |
| extension | n/a |
| use | Role.code or implied by context |
| type | Role.code or implied by context |
| system | II.root or Role.id.root |
| value | II.extension or II.root if system indicates OID or GUID (Or Role.id.extension or root) |
| period | Role.effectiveTime or implied by context |
| assigner | II.assigningAuthorityName but note that this is an improper use by the definition of the field. Also Role.scoper |
| status | .statusCode |
| operationalStatus | n/a |
| name | .name |
| alias | .name |
| description | .playingEntity[classCode=PLC determinerCode=INSTANCE].desc |
| type | .code |
| telecom | .telecom |
| id | n/a |
| extension | n/a |
| system | ./scheme |
| value | ./url |
| use | unique(./use) |
| rank | n/a |
| period | ./usablePeriod[type="IVL<TS>"] |
| address | .addr |
| id | n/a |
| extension | n/a |
| use | unique(./use) |
| type | unique(./use) |
| text | ./formatted |
| line | AD.part[parttype = AL] |
| city | AD.part[parttype = CTY] |
| district | AD.part[parttype = CNT | CPA] |
| state | AD.part[parttype = STA] |
| postalCode | AD.part[parttype = ZIP] |
| country | AD.part[parttype = CNT] |
| period | ./usablePeriod[type="IVL<TS>"] |
| physicalType | .playingEntity [classCode=PLC].code |
| position | .playingEntity [classCode=PLC determinerCode=INSTANCE].positionText |
| id | n/a |
| extension | n/a |
| modifierExtension | N/A |
| longitude | (RIM Opted not to map the sub-elements of GPS location, is now an OBS) |
| latitude | (RIM Opted not to map the sub-elements of GPS location, is now an OBS) |
| altitude | (RIM Opted not to map the sub-elements of GPS location, is now an OBS) |
| managingOrganization | .scopingEntity[classCode=ORG determinerKind=INSTANCE] |
| partOf | .inboundLink[typeCode=PART].source[classCode=SDLC] |
| hoursOfOperation | .effectiveTime |
| id | n/a |
| extension | n/a |
| modifierExtension | N/A |
| daysOfWeek | .effectiveTime |
| allDay | .effectiveTime |
| openingTime | .effectiveTime |
| closingTime | .effectiveTime |
| availabilityExceptions | n/a |
| endpoint | n/a |

### Mappings for FiveWs Pattern Mapping (http://hl7.org/fhir/fivews)

|  |  |  |
| --- | --- | --- |
| **PlannetLocation** | | |
| Location |  |
| identifier | FiveWs.identifier |
| status | FiveWs.status |
| operationalStatus | FiveWs.status |
| type | FiveWs.class |
| physicalType | FiveWs.class |