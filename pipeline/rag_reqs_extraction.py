import random
import os
from glob import glob
import re
import chromadb
from chromadb.utils import embedding_functions
import pandas as pd
from copy import deepcopy
import json

PROMPT_1_PATH = "../prompts/contains_requirement.txt"

PROMPT_2_PATH = "../prompts/requirement_extraction_rag.txt"

Q_TEXT = "Does the provided IG text contain at least one specific, testable requirement for a behavior or capability that can be verified through software testing or attestation? Give your answer as a boolean (TRUE or FALSE) with no additional explanation or justification"

SYSTEM_PROMPTS = {
    "claude": """You are a seasoned Healthcare Integration Test Engineer with expertise in INCOSE Systems Engineering standards, 
    analyzing a FHIR Implementation Guide to extract precise testable requirements in INCOSE format.""",
    "gemini": """You are a Healthcare Integration Test Engineer with expertise in INCOSE Systems Engineering standards, analyzing FHIR 
    Implementation Guide content to identify and format testable requirements following INCOSE specifications.""",
    "gpt": """As a Healthcare Integration Test Engineer with INCOSE Systems Engineering expertise, analyze this FHIR 
    Implementation Guide content to extract specific testable requirements in INCOSE-compliant format."""
}


with open(PROMPT_1_PATH, 'r') as f:
    PROMPT_1 = f.read()

with open(PROMPT_2_PATH, 'r') as f:
    PROMPT_2 = f.read()

def md_sections(markdown):
    '''separates markdown string into sections'''
    sections = []
    section_matches = list(re.finditer("(#+ )", markdown))
    for i in range(len(section_matches)):
        if i == (len(section_matches)-1):
            sections.append(markdown[section_matches[i].span()[0]:])
        else:
            sections.append(markdown[section_matches[i].span()[0]:section_matches[i+1].span()[0]])
    return sections

def first_pass(clients, api_type, source_dir):
    '''gets llm judgements of whether passages 
    from markdown files in a directory have requirements'''
    # os.makedirs(destination_dir, exist_ok=True)
    fp_questions = []
    responses = {'prompt': PROMPT_1, 'responses': []}
    for fname in glob(source_dir+"/*.md"):
        with open(fname) as f:
            data = f.read()
            sections = md_sections(data)
            for i, section in enumerate(sections):
                response_entry = {
                    'filename': fname,
                    'total_sections': len(sections),
                    'section_id': i,
                    'text': section
                }
                task_base = deepcopy(PROMPT_1)
                task_base += "<TASK> <TEXT> " \
                    + section + "</TEXT>" \
                    + f"<QUESTION> {Q_TEXT} </QUESTION>"\
                    + "<ANSWER>"
                fp_questions.append(task_base)
                responses['responses'].append(response_entry)
    fp_responses = clients.make_llm_request(api_type, fp_questions, sys_prompt=SYSTEM_PROMPTS[api_type], raise_on_error=True, reformat=True)
    for i, r in enumerate(responses['responses']):
        r['llm_response'] = fp_responses[i]
    return responses
    

def postprocess_fp(first_pass):
    processed = {"processed": [], "unable_to_process":[]}
    for section in first_pass['responses']:
        if section['llm_response'].lower() == 'true':
            section['contains_requirement'] = True
            processed['processed'].append(deepcopy(section))
        elif section['llm_response'].lower() == 'false':
            section['contains_requirement'] = False
            processed['processed'].append(deepcopy(section))
        else:
            section['contains_requirement'] = None
            processed['unable_to_process'].append(deepcopy(section))
    return processed

def instantiate_vectordb(sourcedir="/Users/ceadams/Documents/onclaive/onclaive/pipeline/hl7.fhir.uv.subscriptions_1.1.0_requirements_with_reference_text.csv"):
    chroma_client = chromadb.Client()
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-mpnet-base-v2"
        )
    if 'subscription_reqs' not in chroma_client.list_collections():
        reqdf = pd.read_csv("/Users/ceadams/Documents/onclaive/onclaive/pipeline/hl7.fhir.uv.subscriptions_1.1.0_requirements_with_reference_text.csv", index_col=0)
        obj = {}
        for t in reqdf.reference_text.unique():
            sub_df = reqdf[reqdf.reference_text == t]
            sub_reqs = []
            for i, row in sub_df.iterrows():
                if row["Conformance*"].upper() != 'DEPRECATED':
                    sub_req = {
                        "Requirement*": row["Requirement*"],
                        "Conformance*": row["Conformance*"],
                        "Actor*": row["Actor*"],
                        "Verifiable?": row["Verifiable?"],
                        "Planning To Test?": row["Planning To Test?"],
                        "Grouping": row["Grouping"],
                        "Test Plan": row["Test Plan"],
                        "Simulation Approach": row["Simulation Approach"]
                    }
                    sub_reqs.append(sub_req)
            obj[t] = {'requirements': json.dumps(sub_reqs)}
        collection = chroma_client.create_collection(name="subscription_reqs", embedding_function=sentence_transformer_ef)
        texts, reqs = zip(*obj.items())
        collection.add(
            documents=list(texts),
            metadatas=list(reqs),
            ids=[str(x) for x in range(len(texts))]
        )
    else:
        collection = chroma_client.get_collection('subscription_reqs', embedding_function=sentence_transformer_ef)

    return collection

def fill_prompt(q_texts, coll, n_examples=4):
    prompts = []
    qts = [q['text'] for q in q_texts]
    resp = coll.query(query_texts=qts)
    for i, q_text in enumerate(qts):
        template = deepcopy(PROMPT_2)
        template += "<EXAMPLES> "
        for j in range(n_examples):
            template += "<TASK> <TEXT>" + resp['documents'][i][j] + " </TEXT>"
            template += " <RESPONSE> "+ resp['metadatas'][i][j]['requirements'] + " </RESPONSE> </TASK>"

        template += "</EXAMPLES> <TASK> <TEXT>" + q_text + " </TEXT> <RESPONSE>"
        prompts.append(template)
    return prompts

def full_pass(clients, api_type, input_directory, output_directory):
    fp_responses = first_pass(clients, api_type, input_directory)
    postprocessed_fp = postprocess_fp(fp_responses)
    sections_with_requirement = list(filter(lambda x: x['contains_requirement'], postprocessed_fp['processed']))
    collection = instantiate_vectordb()
    final_prompts = fill_prompt(sections_with_requirement, collection)
    generated_requirements = clients.make_llm_request(api_type, final_prompts, sys_prompt=SYSTEM_PROMPTS[api_type], raise_on_error=False, reformat=True)
    all_requirements = []
    for i, qr in enumerate(generated_requirements):
        if "</RESPONSE>" in qr:
            tag_end = qr.index("</RESPONSE>")
        else:
            tag_end = len(qr)
        qrs = qr[:tag_end].replace("<RESPONSE>","")
        try:
            jqrs = json.loads(qrs)
            sections_with_requirement[i]['successfully_processed_requirements'] = jqrs
            all_requirements.extend(jqrs)
        except:
            sections_with_requirement[i]['unsuccessfully_processed_requirements'] = qrs
    os.makedirs(output_directory, exist_ok=True)
    with open(output_directory+"/raw_output.json", "w+") as raw:
        json.dump(postprocessed_fp, raw)
    with open(output_directory+"/requirements.json", "w+") as reqs:
        json.dump(all_requirements, reqs)