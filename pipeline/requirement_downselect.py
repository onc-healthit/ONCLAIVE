import json
from sentence_transformers import SentenceTransformer, util
import pandas as pd
from glob import glob
from itertools import product
import re
from uuid import uuid4
import os

def load_mdfile(mdfile):
    all_reqs = []
    with open(mdfile) as f:
        mdreqs = f.read()
    sections = list(re.finditer("#+ REQ-[0-9]+", mdreqs))
    md_splits = []
    for i in range(len(sections)-1):

        md_splits.append(mdreqs[sections[i].span()[1]:sections[i+1].span()[0]])
    md_splits.append(mdreqs[sections[-1].span()[1]:])

    for split in md_splits:
        req_dict = {}
        headings = list(re.finditer("\*\*\w+\*\*\:", split))
        for i in range(len(headings)-1):
            heading = headings[i]
            req_dict[heading.group()[2:-3].lower()] = split[heading.span()[1]:headings[i+1].span()[0]]
        heading = headings[-1]
        req_dict[heading.group()[2:-3].lower()] = split[heading.span()[1]:]
        if 'description' in req_dict:
            all_reqs.append({"text": req_dict['description'], "raw": split, "source": mdfile, 'parsed': req_dict, "id": str(uuid4())})

    return all_reqs

def rag_parse(rag_json):
    '''
    Unifies Rag-generated requirement headings with those generated from the other methodology
    '''
    parsed_rag = {}
    for key, val in rag_json.items():
        if key == "Requirement*":
            parsed_rag['description'] = val
        else:
            parsed_rag[key.replace("*", "").lower()] = val
    return parsed_rag

def load_ragfile(ragfile):
    ragreq_list = []
    with open(ragfile) as f:
        ragreqs = json.load(f)
    for ragreq in ragreqs['responses']['processed']:
        if ragreq['contains_requirement']:
            ragreq_list.extend([
                {
                    'text': x['Requirement*'],
                    'raw': x,
                    'source': ragfile,
                    "parsed": rag_parse(x),
                    "id": str(uuid4())
                } for x in ragreq['extracted_requirement']
            ])

    return ragreq_list

def generate_embeddings(reqlist):
    model = SentenceTransformer("all-mpnet-base-v2")

    for i, areq in enumerate(reqlist):
        if (i+1) % 50 == 0:
            print(f"{i+1} of {len(reqlist)}", end='\r')
        areq['embedding'] = model.encode(areq['text'])

    return reqlist

def calculate_scores(embed_list):
    scored_prod_list = [['Requirement1', "Requirement2", "Similarity Score"]]
    prod_list = list(product(embed_list, embed_list))
    for i, prod in enumerate(prod_list):
        counter = i+1
        if counter % 1000 == 0:
            print(f"Pair {counter} of {len(prod_list)}", end='\r')
        if prod[0]['id'] != prod[1]['id']:
            emb0 = prod[0]['embedding']
            emb1 = prod[1]['embedding']
            score = float(util.pytorch_cos_sim(emb0, emb1)[0][0])
            scored_prod_list.append([prod[0]['id'], prod[1]['id'], score])
    print(f"Pair {counter} of {len(prod_list)}", end='\r')
    df = pd.DataFrame(scored_prod_list[1:], columns=scored_prod_list[0])

    return df

def find_dupe_groups(scoreframe, threshhold):
    dupdf = scoreframe[scoreframe['Similarity Score'] >= threshhold]
    groups = {}
    for r1 in set(list(dupdf['Requirement1'].unique()) + list(dupdf['Requirement2'].unique())):
        subdf = dupdf[(dupdf['Requirement1'] == r1)|(dupdf['Requirement2'] == r1)]
        grouped_ids = set(subdf['Requirement1'].to_list() + subdf['Requirement2'].to_list())
        for gid in grouped_ids:
            if gid not in groups:
                groups[gid] = grouped_ids
            else:
                new_group = groups[gid].union(grouped_ids)
                groups[gid] = new_group 

    unique_groups = set()
    for val in groups.values():
        unique_groups.add(frozenset(val))

    to_keep = []
    dup_ids = []
    for ugroup in unique_groups:
        glist = list(ugroup)
        to_keep.append(glist[0])
        dup_ids.extend(glist[1:])

    return dup_ids, to_keep


def full_pass(md_files=[], rag_files=[], output_dir="checkpoints/requirements_downselect", threshhold=0.98):
    all_reqs = []
    for md_file in md_files:
        all_reqs.extend(load_mdfile(md_file))
    for rag_file in rag_files:
        all_reqs.extend(load_ragfile(rag_file))

    generate_embeddings(all_reqs)

    score_df = calculate_scores(all_reqs)

    dup_ids, to_keep = find_dupe_groups(score_df, threshhold)

    filtered_allreqs = list(filter(lambda x: x['id'] not in dup_ids, all_reqs))

    embeds_only = {}
    for areq in filtered_allreqs:
        embeds_only[areq['id']] = [float(x) for x in areq.pop('embedding')]

    os.makedirs(output_dir, exist_ok=True)

    with open(output_dir+'/ids_to_embeddings.json', 'w+') as f:
        json.dump(embeds_only, f, indent=2)

    with open(output_dir+'/filtered_requirements.json', 'w+') as f:
        json.dump(filtered_allreqs, f, indent=2)