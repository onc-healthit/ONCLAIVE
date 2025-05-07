

us-core-provider-role vs PractitionerRoleVS

## ValueSet Comparison between http://hl7.org/fhir/us/core/ValueSet/us-core-provider-role vs http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/PractitionerRoleVS

### Messages

|  |  |  |
| --- | --- | --- |
| Error | ValueSet.url | Values for url differ: 'http://hl7.org/fhir/us/core/ValueSet/us-core-provider-role' vs 'http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/PractitionerRoleVS' |
| Error | ValueSet.version | Values for version differ: '3.1.1' vs '1.1.0' |
| Information | ValueSet.name | Values for name differ: 'USCoreProviderRoleNucc' vs 'PractitionerRoleVS' |
| Information | ValueSet.title | Values for title differ: 'US Core Provider Role (NUCC)' vs 'PractitionerRole Code VS' |
| Information | ValueSet.date | Values for date differ: '2019-05-21' vs '2022-04-04T14:04:34+00:00' |
| Information | ValueSet.publisher | Values for publisher differ: 'HL7 US Realm Steering Committee' vs 'HL7 Financial Management Working Group' |

### Metadata

| Name | Value | | Comments |
| --- | --- | --- | --- |
| .compose.inactive |  | |  |
| .compose.lockedDate |  | |  |
| .copyright | This value set includes content from NUCC Health Care Provider Taxonomy Code Set for providers which is copyright © 2016+ American Medical Association. For commercial use, including sales or licensing, a license must be obtained. |  | * Removed the item 'This value set includes content from NUCC Health Care Provider Taxonomy Code Set for providers which is copyright © 2016+ American Medical Association. For commercial use, including sales or licensing, a license must be obtained.' |
| .date | 2019-05-21 | 2022-04-04T14:04:34+00:00 | * Values Differ |
| .description | Provider roles codes which are composed of the NUCC Health Care Provider Taxonomy Code Set classification codes for providers. Only concepts with a classification and no specialization are included. | Codes for the capabilities that an individual, group, or organization is acknowledged to have in a payer network, including general codes from the HL7 PractitionerRole Code System. | * Values Differ |
| .experimental |  | |  |
| .immutable |  | |  |
| .jurisdiction |  | |  |
| ..jurisdiction[0] | urn:iso:std:iso:3166#US | |  |
| .name | USCoreProviderRoleNucc | PractitionerRoleVS | * Values Differ |
| .publisher | HL7 US Realm Steering Committee | HL7 Financial Management Working Group | * Values Differ |
| .purpose |  | |  |
| .status | active | |  |
| .title | US Core Provider Role (NUCC) | PractitionerRole Code VS | * Values Differ |
| .url | http://hl7.org/fhir/us/core/ValueSet/us-core-provider-role | http://hl7.org/fhir/us/davinci-pdex-plan-net/ValueSet/PractitionerRoleVS | * Values Differ |
| .version | 3.1.1 | 1.1.0 | * Values Differ |

### Definition

| Item | Property | | Value | | Comments |
| --- | --- | --- | --- | --- | --- |
| .include | http://nucc.org/provider-taxonomy |  |  |  | * Removed Include |
| .include |  | http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS |  |  | * Added Include |
| .include |  | http://terminology.hl7.org/CodeSystem/practitioner-role |  |  | * Added Include |

### Expansion

| System | Code | Display | | Comments |
| --- | --- | --- | --- | --- |
| .http://nucc.org/provider-taxonomy | 101Y00000X | Counselor |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 102L00000X | Psychoanalyst |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 102X00000X | Poetry Therapist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 103G00000X | Clinical Neuropsychologist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 103K00000X | Behavior Analyst |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 103T00000X | Psychologist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 104100000X | Social Worker |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 106E00000X | Assistant Behavior Analyst |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 106H00000X | Marriage & Family Therapist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 106S00000X | Behavior Technician |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 111N00000X | Chiropractor |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 122300000X | Dentist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 122400000X | Denturist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 124Q00000X | Dental Hygienist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 125J00000X | Dental Therapist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 125K00000X | Advanced Practice Dental Therapist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 125Q00000X | Oral Medicinist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 126800000X | Dental Assistant |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 126900000X | Dental Laboratory Technician |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 132700000X | Dietary Manager |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 133N00000X | Nutritionist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 133V00000X | Dietitian, Registered |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 136A00000X | Dietetic Technician, Registered |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 146D00000X | Personal Emergency Response Attendant |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 146L00000X | Emergency Medical Technician, Paramedic |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 146M00000X | Emergency Medical Technician, Intermediate |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 146N00000X | Emergency Medical Technician, Basic |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 152W00000X | Optometrist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 156F00000X | Technician/Technologist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 163W00000X | Registered Nurse |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 164W00000X | Licensed Practical Nurse |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 164X00000X | Licensed Vocational Nurse |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 167G00000X | Licensed Psychiatric Technician |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 170100000X | Medical Genetics, Ph.D. Medical Genetics |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 170300000X | Genetic Counselor, MS |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 171000000X | Military Health Care Provider |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 171100000X | Acupuncturist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 171M00000X | Case Manager/Care Coordinator |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 171R00000X | Interpreter |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 171W00000X | Contractor |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 172A00000X | Driver |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 172M00000X | Mechanotherapist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 172P00000X | Naprapath |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 172V00000X | Community Health Worker |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 173000000X | Legal Medicine |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 173C00000X | Reflexologist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 173F00000X | Sleep Specialist, PhD |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 174200000X | Meals |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 174400000X | Specialist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 174H00000X | Health Educator |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 174M00000X | Veterinarian |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 174N00000X | Lactation Consultant, Non-RN |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 174V00000X | Clinical Ethicist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 175F00000X | Naturopath |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 175L00000X | Homeopath |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 175M00000X | Midwife, Lay |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 175T00000X | Peer Specialist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 176B00000X | Midwife |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 176P00000X | Funeral Director |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 177F00000X | Lodging |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 183500000X | Pharmacist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 183700000X | Pharmacy Technician |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 193200000X | Multi-Specialty |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 193400000X | Single Specialty |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 202C00000X | Independent Medical Examiner |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 202K00000X | Phlebology |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 204C00000X | Neuromusculoskeletal Medicine, Sports Medicine |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 204D00000X | Neuromusculoskeletal Medicine & OMM |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 204E00000X | Oral & Maxillofacial Surgery |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 204F00000X | Transplant Surgery |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 204R00000X | Electrodiagnostic Medicine |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 207K00000X | Allergy & Immunology |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 207L00000X | Anesthesiology |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 207N00000X | Dermatology |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 207P00000X | Emergency Medicine |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 207Q00000X | Family Medicine |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 207R00000X | Internal Medicine |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 207T00000X | Neurological Surgery |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 207U00000X | Nuclear Medicine |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 207V00000X | Obstetrics & Gynecology |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 207W00000X | Ophthalmology |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 207X00000X | Orthopaedic Surgery |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 207Y00000X | Otolaryngology |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 208000000X | Pediatrics |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 208100000X | Physical Medicine & Rehabilitation |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 208200000X | Plastic Surgery |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 208600000X | Surgery |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 208800000X | Urology |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 208C00000X | Colon & Rectal Surgery |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 208D00000X | General Practice |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 208G00000X | Thoracic Surgery (Cardiothoracic Vascular Surgery) |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 208M00000X | Hospitalist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 208U00000X | Clinical Pharmacology |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 209800000X | Legal Medicine |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 211D00000X | Assistant, Podiatric |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 213E00000X | Podiatrist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 221700000X | Art Therapist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 222Q00000X | Developmental Therapist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 222Z00000X | Orthotist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 224900000X | Mastectomy Fitter |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 224L00000X | Pedorthist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 224P00000X | Prosthetist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 224Y00000X | Clinical Exercise Physiologist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 224Z00000X | Occupational Therapy Assistant |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 225000000X | Orthotic Fitter |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 225100000X | Physical Therapist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 225200000X | Physical Therapy Assistant |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 225400000X | Rehabilitation Practitioner |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 225500000X | Specialist/Technologist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 225600000X | Dance Therapist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 225700000X | Massage Therapist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 225800000X | Recreation Therapist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 225A00000X | Music Therapist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 225B00000X | Pulmonary Function Technologist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 225C00000X | Rehabilitation Counselor |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 225X00000X | Occupational Therapist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 226000000X | Recreational Therapist Assistant |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 226300000X | Kinesiotherapist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 227800000X | Respiratory Therapist, Certified |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 227900000X | Respiratory Therapist, Registered |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 229N00000X | Anaplastologist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 231H00000X | Audiologist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 235500000X | Specialist/Technologist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 235Z00000X | Speech-Language Pathologist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 237600000X | Audiologist-Hearing Aid Fitter |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 237700000X | Hearing Instrument Specialist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 242T00000X | Perfusionist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 243U00000X | Radiology Practitioner Assistant |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 246Q00000X | Specialist/Technologist, Pathology |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 246R00000X | Technician, Pathology |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 246W00000X | Technician, Cardiology |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 246X00000X | Specialist/Technologist Cardiovascular |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 246Y00000X | Specialist/Technologist, Health Information |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 246Z00000X | Specialist/Technologist, Other |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 247000000X | Technician, Health Information |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 247100000X | Radiologic Technologist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 247200000X | Technician, Other |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 251300000X | Local Education Agency (LEA) |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 251B00000X | Case Management |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 251C00000X | Day Training, Developmentally Disabled Services |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 251E00000X | Home Health |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 251F00000X | Home Infusion |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 251G00000X | Hospice Care, Community Based |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 251J00000X | Nursing Care |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 251K00000X | Public Health or Welfare |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 251S00000X | Community/Behavioral Health |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 251T00000X | Program of All-Inclusive Care for the Elderly (PACE) Provider Organization |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 251V00000X | Voluntary or Charitable |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 251X00000X | Supports Brokerage |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 252Y00000X | Early Intervention Provider Agency |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 253J00000X | Foster Care Agency |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 253Z00000X | In Home Supportive Care |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 261Q00000X | Clinic/Center |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 273100000X | Epilepsy Unit |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 273R00000X | Psychiatric Unit |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 273Y00000X | Rehabilitation Unit |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 275N00000X | Medicare Defined Swing Bed Unit |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 276400000X | Rehabilitation, Substance Use Disorder Unit |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 281P00000X | Chronic Disease Hospital |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 282E00000X | Long Term Care Hospital |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 282J00000X | Religious Nonmedical Health Care Institution |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 282N00000X | General Acute Care Hospital |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 283Q00000X | Psychiatric Hospital |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 283X00000X | Rehabilitation Hospital |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 284300000X | Special Hospital |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 286500000X | Military Hospital |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 291900000X | Military Clinical Medical Laboratory |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 291U00000X | Clinical Medical Laboratory |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 292200000X | Dental Laboratory |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 293D00000X | Physiological Laboratory |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 302F00000X | Exclusive Provider Organization |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 302R00000X | Health Maintenance Organization |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 305R00000X | Preferred Provider Organization |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 305S00000X | Point of Service |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 310400000X | Assisted Living Facility |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 310500000X | Intermediate Care Facility, Mental Illness |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 311500000X | Alzheimer Center (Dementia Center) |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 311Z00000X | Custodial Care Facility |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 313M00000X | Nursing Facility/Intermediate Care Facility |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 314000000X | Skilled Nursing Facility |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 315D00000X | Hospice, Inpatient |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 315P00000X | Intermediate Care Facility, Mentally Retarded |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 320600000X | Residential Treatment Facility, Mental Retardation and/or Developmental Disabilities |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 320700000X | Residential Treatment Facility, Physical Disabilities |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 320800000X | Community Based Residential Treatment Facility, Mental Illness |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 320900000X | Community Based Residential Treatment Facility, Mental Retardation and/or Developmental Disabilities |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 322D00000X | Residential Treatment Facility, Emotionally Disturbed Children |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 323P00000X | Psychiatric Residential Treatment Facility |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 324500000X | Substance Abuse Rehabilitation Facility |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 331L00000X | Blood Bank |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 332000000X | Military/U.S. Coast Guard Pharmacy |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 332100000X | Department of Veterans Affairs (VA) Pharmacy |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 332800000X | Indian Health Service/Tribal/Urban Indian Health (I/T/U) Pharmacy |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 332900000X | Non-Pharmacy Dispensing Site |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 332B00000X | Durable Medical Equipment & Medical Supplies |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 332G00000X | Eye Bank |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 332H00000X | Eyewear Supplier |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 332S00000X | Hearing Aid Equipment |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 332U00000X | Home Delivered Meals |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 333300000X | Emergency Response System Companies |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 333600000X | Pharmacy |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 335E00000X | Prosthetic/Orthotic Supplier |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 335G00000X | Medical Foods Supplier |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 335U00000X | Organ Procurement Organization |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 335V00000X | Portable X-ray and/or Other Portable Diagnostic Imaging Supplier |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 341600000X | Ambulance |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 341800000X | Military/U.S. Coast Guard Transport |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 343800000X | Secured Medical Transport (VAN) |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 343900000X | Non-emergency Medical Transport (VAN) |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 344600000X | Taxi |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 344800000X | Air Carrier |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 347B00000X | Bus |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 347C00000X | Private Vehicle |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 347D00000X | Train |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 347E00000X | Transportation Broker |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 363A00000X | Physician Assistant |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 363L00000X | Nurse Practitioner |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 364S00000X | Clinical Nurse Specialist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 367500000X | Nurse Anesthetist, Certified Registered |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 367A00000X | Advanced Practice Midwife |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 367H00000X | Anesthesiologist Assistant |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 372500000X | Chore Provider |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 372600000X | Adult Companion |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 373H00000X | Day Training/Habilitation Specialist |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 374700000X | Technician |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 374J00000X | Doula |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 374K00000X | Religious Nonmedical Practitioner |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 374T00000X | Religious Nonmedical Nursing Personnel |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 374U00000X | Home Health Aide |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 376G00000X | Nursing Home Administrator |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 376J00000X | Homemaker |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 376K00000X | Nurse's Aide |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 385H00000X | Respite Care |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 390200000X | Student in an Organized Health Care Education/Training Program |  | * Removed from expansion |
| .http://nucc.org/provider-taxonomy | 405300000X | Prevention Professional |  | * Removed from expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | ap |  | Admitting Privileges | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | apn |  | Advanced Practice Nursing Providers | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | at |  | Athletic Trainer | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | au |  | Audiologist | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | bh |  | Behavioral Health & Social Service Providers | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | ba |  | Board Certified Behavior Analyst | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | bt |  | Member Of | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | cnw |  | Certified Nurse Midwife | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | crnp |  | Certified Registered Nurse Practitioner | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | ch |  | Chiropractor | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | cs |  | Christian Science Practitioner | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | co |  | Counselor | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | dp |  | Dental Provider | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | de |  | Dentist | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | drr |  | Developmental, Rehabilitative and Restorative Service Providers | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | dn |  | Dietary and Nutritional Service Provider | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | om |  | Doctor of Oriental Medicine | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | em |  | Emergency Medical Service Provider | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | ho |  | Homeopath | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | lpn |  | Licensed Practical Nurse | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | mt |  | Marriage/Family Therapist | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | ma |  | Massage Therapist | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | nh |  | Naprapath | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | na |  | Naturopath | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | nu |  | Nursing Service Related Providers | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | ot |  | Occupational Therapist | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | op |  | Optician | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | oo |  | Optometrist | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | os |  | Other Service Provider | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | rx |  | Pharmacy Service Providers | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | pt |  | Physical Therapist | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | ph |  | Physician | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | pa |  | Physician Assistant | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | po |  | Podiatrist | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | py |  | Psychologist | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | rn |  | Registered Nurse | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | rt |  | Respiratory Therapist | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | sw |  | Social Worker | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | sp |  | Speech Language Pathologist | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | sh |  | Speech, Language and Hearing Service Providers | * Added to expansion |
| .http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS | te |  | Technologists, Technicians and Other Technical Service Providers | * Added to expansion |
| .http://terminology.hl7.org/CodeSystem/practitioner-role | doctor |  | Doctor | * Added to expansion |
| .http://terminology.hl7.org/CodeSystem/practitioner-role | nurse |  | Nurse | * Added to expansion |
| .http://terminology.hl7.org/CodeSystem/practitioner-role | pharmacist |  | Pharmacist | * Added to expansion |
| .http://terminology.hl7.org/CodeSystem/practitioner-role | researcher |  | Researcher | * Added to expansion |
| .http://terminology.hl7.org/CodeSystem/practitioner-role | teacher |  | Teacher/educator | * Added to expansion |
| .http://terminology.hl7.org/CodeSystem/practitioner-role | ict |  | ICT professional | * Added to expansion |