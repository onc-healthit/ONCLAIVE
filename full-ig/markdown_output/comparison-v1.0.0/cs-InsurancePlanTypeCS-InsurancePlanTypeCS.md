

InsurancePlanTypeCS vs InsurancePlanTypeCS

## CodeSystem Comparison between http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/InsurancePlanTypeCS vs http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/InsurancePlanTypeCS

### Messages

|  |  |  |
| --- | --- | --- |
| Error | CodeSystem.version | Values for version differ: '1.0.0' vs '1.1.0' |
| Information | CodeSystem.date | Values for date differ: '2020-12-07T21:58:00+00:00' vs '2022-04-04T14:04:34+00:00' |
| Information | CodeSystem.concept.where(code='lowdeductible').definition | Changed value for definition: 'A plan that requires the insured to pay out of pocket a smaller proportion of incurred health care costs.' vs 'A plan that requires the insured to pay out of pocket a smaller proportion of incurred health care costs than a traditional insurance plan.' |

### Metadata

| Name | Value | | Comments |
| --- | --- | --- | --- |
| .caseSensitive |  | true | * Added the item 'true' |
| .compositional |  | |  |
| .content | complete | |  |
| .copyright |  | |  |
| .date | 2020-12-07T21:58:00+00:00 | 2022-04-04T14:04:34+00:00 | * Values Differ |
| .description | Categories of cost-sharing used by plans | |  |
| .experimental |  | |  |
| .hierarchyMeaning |  | |  |
| .jurisdiction |  | |  |
| ..jurisdiction[0] | urn:iso:std:iso:3166#US | |  |
| .name | InsurancePlanTypeCS | |  |
| .publisher | HL7 Financial Management Working Group | |  |
| .purpose |  | |  |
| .status | active | |  |
| .title | Insurance Plan Type | |  |
| .url | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/InsurancePlanTypeCS | |  |
| .version | 1.0.0 | 1.1.0 | * Values Differ |
| .versionNeeded |  | |  |

### Concepts

| Code | Display | | Comments |
| --- | --- | --- | --- |
| .platinum | Platinum-QHP | |  |
| .gold | Gold-QHP | |  |
| .silver | Silver-QHP | |  |
| .bronze | Bronze-QHP | |  |
| .lowdeductible | Low Deductible | | * definition changed from left to right |
| .highdeductible | High Deductible | |  |
| .catastrophic |  | Catastrophic-QHP | * Added this concept |
| .catastrophicplan |  | Catastrophic Plan | * Added this concept |