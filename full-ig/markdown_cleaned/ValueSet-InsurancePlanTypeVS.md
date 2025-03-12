# ValueSet: Insurance Plan TypeVS

* [**Table of Contents**](toc.html)
* [**Artifacts Summary**](artifacts.html)
* **Insurance Plan TypeVS**

Publication Build: This will be filled in by the publication tooling

* [Narrative Content](#)

## ValueSet: Insurance Plan TypeVS

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| *Official URL*: http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/InsurancePlanTypeVS | | | | *Version*: 1.1.0 |
| Active as of 2022-04-04 | | | | *Computable Name*: InsurancePlanTypeVS |

Categories of cost-sharing used by plans.

**References**

* [Plan-Net InsurancePlan](StructureDefinition-plannet-InsurancePlan.html)

### Logical Definition (CLD)

* Include all codes defined in [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/InsurancePlanTypeCS`](CodeSystem-InsurancePlanTypeCS.html)

### Expansion

This value set contains 8 concepts

Expansion based on [Insurance Plan Type v1.1.0 (CodeSystem)](CodeSystem-InsurancePlanTypeCS.html)

All codes in this table are from the system [`http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/InsurancePlanTypeCS`](CodeSystem-InsurancePlanTypeCS.html)

|  |  |  |
| --- | --- | --- |
| **Code** | **Display** | **Definition** |
| [platinum](CodeSystem-InsurancePlanTypeCS.html#InsurancePlanTypeCS-platinum) | Platinum-QHP | Plan with highest monthly premium and lowest costs when you need care A Qualified Health Plan with the highest monthly premiums and smallest out-of-pocket costs for the member in comparison to other metal-category plans |
| [gold](CodeSystem-InsurancePlanTypeCS.html#InsurancePlanTypeCS-gold) | Gold-QHP | Plan with high monthly premium and low costs when you need care A Qualified Health Plan with the higher monthly premiums and smaller out-of-pocket costs for the member in comparison to other metal-category plans |
| [silver](CodeSystem-InsurancePlanTypeCS.html#InsurancePlanTypeCS-silver) | Silver-QHP | Plan with moderate monthly premium and moderate costs when you need care A Qualified Health Plan with the lower monthly premiums and larger out-of-pocket costs for the member in comparison to other metal-category plans |
| [bronze](CodeSystem-InsurancePlanTypeCS.html#InsurancePlanTypeCS-bronze) | Bronze-QHP | Plan with lowest monthly premium and highest costs when you need care A Qualified Health Plan with the lowest monthly premiums and largest out-of-pocket costs for the member in comparison to other metal-category plans |
| [catastrophic](CodeSystem-InsurancePlanTypeCS.html#InsurancePlanTypeCS-catastrophic) | Catastrophic-QHP | A plan with low monthly premiums and very high deductibles and are available only to those under 30 or with certain special exemptions. |
| [lowdeductible](CodeSystem-InsurancePlanTypeCS.html#InsurancePlanTypeCS-lowdeductible) | Low Deductible | A plan that requires the insured to pay out of pocket a smaller proportion of incurred health care costs than a traditional insurance plan. |
| [highdeductible](CodeSystem-InsurancePlanTypeCS.html#InsurancePlanTypeCS-highdeductible) | High Deductible | A plan that requires the insured to pay out of pocket a larger proportion of incurred health care costs than a traditional insurance plan. |
| [catastrophicplan](CodeSystem-InsurancePlanTypeCS.html#InsurancePlanTypeCS-catastrophicplan) | Catastrophic Plan | A plan that requires the insured to pay out of pocket a much larger proportion of incurred health care costs than a traditional insurance plan. |

---

Explanation of the columns that may appear on this page:

|  |  |
| --- | --- |
| Level | A few code lists that FHIR defines are hierarchical - each code is assigned a level. In this scheme, some codes are under other codes, and imply that the code they are under also applies |
| System | The source of the definition of the code (when the value set draws in codes defined elsewhere) |
| Code | The code (used as the code in the resource instance) |
| Display | The display (used in the *display* element of a [Coding](http://hl7.org/fhir/R4/datatypes.html#Coding)). If there is no display, implementers should not simply display the code, but map the concept into their application |
| Definition | An explanation of the meaning of the concept |
| Comments | Additional notes about how to use the code |