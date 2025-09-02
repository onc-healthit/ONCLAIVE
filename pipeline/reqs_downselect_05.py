"""
Requirement Downselect Module

This module provides functionality to identify and remove duplicate requirements from 
FHIR Implementation Guide requirement lists using semantic similarity analysis.

Features:
- Load requirements from markdown and RAG JSON files
- Generate semantic embeddings using sentence transformers
- Calculate similarity scores between all requirement pairs
- Group similar requirements and remove duplicates
- Output consolidated requirements in markdown or JSON format

Usage:
    from requirement_downselect import full_pass, get_md_files_from_directory
    
    # Get markdown files from directory
    md_files = get_md_files_from_directory('path/to/requirements')
    
    # Process and consolidate requirements
    full_pass(md_files=md_files, output_dir='output', threshold=0.98)
"""

import json
from sentence_transformers import SentenceTransformer, util
import pandas as pd
from itertools import product
import re
from uuid import uuid4
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple, Any
from glob import glob


def load_mdfile(mdfile: str) -> List[Dict[str, Any]]:
    """
    Load requirements from a markdown file with structured format.
    
    Expected format:
    # REQ-XX
    **Summary**: text
    **Text**: text
    **Context**: text
    etc.
    
    Args:
        mdfile: Path to markdown file containing requirements
        
    Returns:
        List of requirement dictionaries with parsed fields
        
    Note:
        Looks for either 'description' or 'text' field as the main requirement content.
        Extracts IG section numbers from 'source' field if available.
    """
    all_reqs = []
    
    try:
        with open(mdfile, 'r', encoding='utf-8') as f:
            mdreqs = f.read()
    except Exception as e:
        print(f"Error reading file {mdfile}: {e}")
        return all_reqs
    
    sections = list(re.finditer(r"# REQ-\d+", mdreqs))
    
    # Check if any sections were found
    if not sections:
        print(f"Warning: No requirement sections found in {mdfile}")
        print("Expected format: # REQ-XX where XX is a number")
        return all_reqs
    
    # Split content between requirement sections
    md_splits = []
    for i in range(len(sections) - 1):
        md_splits.append(mdreqs[sections[i].span()[1]:sections[i+1].span()[0]])
    
    # Add the last section
    if sections:
        md_splits.append(mdreqs[sections[-1].span()[1]:])

    # Parse each requirement section
    for split in md_splits:
        req_dict = {}
        headings = list(re.finditer(r"\*\*\w+\*\*\:", split))
        
        # Check if any headings were found
        if not headings:
            print(f"Warning: No headings found in requirement section")
            continue
            
        # Extract content for each heading
        for i in range(len(headings) - 1):
            heading = headings[i]
            field_name = heading.group()[2:-3].lower()  # Remove ** and :
            field_content = split[heading.span()[1]:headings[i+1].span()[0]].strip()
            req_dict[field_name] = field_content
        
        # Process the last heading
        if headings:
            heading = headings[-1]
            field_name = heading.group()[2:-3].lower()
            field_content = split[heading.span()[1]:].strip()
            req_dict[field_name] = field_content
        
        # Create requirement object
        main_text = ""
        if 'description' in req_dict:
            main_text = req_dict['description']
        elif 'text' in req_dict:
            main_text = req_dict['text']
        else:
            print(f"Warning: No 'description' or 'text' field found in requirement")
            continue
            
        req = {
            "text": main_text,
            "raw": split,
            "source": mdfile,
            "parsed": req_dict,
            "id": str(uuid4())
        }
        
        # Extract IG section number if available
        if 'source' in req_dict:
            secnum = re.findall(r'((?:\d+\.)+\d+)', req_dict['source'])
            if secnum:
                req['ig_section'] = secnum[0]
                
        all_reqs.append(req)

    return all_reqs


def rag_parse(rag_json: Dict[str, Any]) -> Dict[str, Any]:
    """
    Unify RAG-generated requirement headings with standard methodology format.
    
    Args:
        rag_json: Raw RAG requirement dictionary
        
    Returns:
        Parsed requirement dictionary with normalized field names
    """
    parsed_rag = {}
    for key, val in rag_json.items():
        if key == "Requirement*":
            parsed_rag['description'] = val
        else:
            parsed_rag[key.replace("*", "").lower()] = val
    return parsed_rag


def load_ragfile(ragfile: str) -> List[Dict[str, Any]]:
    """
    Load requirements from a RAG-generated JSON file.
    
    Expected format: JSON with responses.processed array containing requirement objects.
    
    Args:
        ragfile: Path to RAG JSON file
        
    Returns:
        List of requirement dictionaries extracted from RAG format
    """
    ragreq_list = []
    
    try:
        with open(ragfile, 'r', encoding='utf-8') as f:
            ragreqs = json.load(f)
    except Exception as e:
        print(f"Error reading RAG file {ragfile}: {e}")
        return ragreq_list
    
    try:
        for ragreq in ragreqs['responses']['processed']:
            if ragreq.get('contains_requirement', False):
                extracted_reqs = ragreq.get('extracted_requirement', [])
                for x in extracted_reqs:
                    if 'Requirement*' in x:
                        req_obj = {
                            'text': x['Requirement*'],
                            'raw': x,
                            'source': ragfile,
                            "parsed": rag_parse(x),
                            "id": str(uuid4())
                        }
                        ragreq_list.append(req_obj)
    except KeyError as e:
        print(f"Error parsing RAG file structure in {ragfile}: missing key {e}")
    except Exception as e:
        print(f"Error processing RAG file {ragfile}: {e}")

    return ragreq_list


def generate_embeddings(reqlist: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Generate semantic embeddings for all requirements using sentence transformers.
    
    Args:
        reqlist: List of requirement dictionaries
        
    Returns:
        Same list with 'embedding' field added to each requirement
        
    Note:
        Uses 'all-mpnet-base-v2' model for generating embeddings.
        Shows progress every 50 requirements processed.
    """
    print("Loading sentence transformer model...")
    model = SentenceTransformer("all-mpnet-base-v2")

    print(f"Generating embeddings for {len(reqlist)} requirements...")
    for i, areq in enumerate(reqlist):
        if (i + 1) % 50 == 0:
            print(f"  {i + 1} of {len(reqlist)}", end='\r')
        areq['embedding'] = model.encode(areq['text'])
    
    print(f"  Completed embeddings for {len(reqlist)} requirements")
    return reqlist


def calculate_scores(embed_list: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Calculate cosine similarity scores between all pairs of requirements.
    
    Args:
        embed_list: List of requirements with embeddings
        
    Returns:
        DataFrame with columns: Requirement1, Requirement2, Similarity Score
        
    Note:
        Uses cosine similarity between embeddings. Shows progress every 1000 pairs.
        Excludes self-comparisons (same requirement ID).
    """
    print("Calculating similarity scores...")
    scored_prod_list = [['Requirement1', "Requirement2", "Similarity Score"]]
    prod_list = list(product(embed_list, embed_list))
    
    for i, (req1, req2) in enumerate(prod_list):
        counter = i + 1
        if counter % 1000 == 0:
            print(f"  Pair {counter} of {len(prod_list)}", end='\r')
            
        # Skip self-comparisons
        if req1['id'] != req2['id']:
            emb1 = req1['embedding']
            emb2 = req2['embedding']
            score = float(util.pytorch_cos_sim(emb1, emb2)[0][0])
            scored_prod_list.append([req1['id'], req2['id'], score])
    
    print(f"  Completed {len(prod_list)} similarity calculations")
    df = pd.DataFrame(scored_prod_list[1:], columns=scored_prod_list[0])
    return df


def find_dupe_groups(scoreframe: pd.DataFrame, threshold: float) -> Tuple[List[str], List[str]]:
    """
    Identify groups of duplicate requirements based on similarity threshold.
    
    Args:
        scoreframe: DataFrame with similarity scores between requirements
        threshold: Similarity threshold for considering requirements as duplicates
        
    Returns:
        Tuple of (duplicate_ids_to_remove, ids_to_keep)
        
    Algorithm:
        1. Filter pairs above threshold
        2. Group connected requirements (transitive closure)
        3. Keep first ID from each group, mark others for removal
    """
    print(f"Finding duplicate groups with threshold >= {threshold}")
    dupdf = scoreframe[scoreframe['Similarity Score'] >= threshold]
    print(f"  Found {len(dupdf)} requirement pairs above threshold")
    
    # Build groups of connected requirements
    groups = {}
    unique_reqs = set(list(dupdf['Requirement1'].unique()) + list(dupdf['Requirement2'].unique()))
    
    for req_id in unique_reqs:
        # Find all requirements similar to this one
        subdf = dupdf[(dupdf['Requirement1'] == req_id) | (dupdf['Requirement2'] == req_id)]
        connected_ids = set(subdf['Requirement1'].tolist() + subdf['Requirement2'].tolist())
        
        # Update group membership (transitive closure)
        for connected_id in connected_ids:
            if connected_id not in groups:
                groups[connected_id] = connected_ids
            else:
                # Merge with existing group
                new_group = groups[connected_id].union(connected_ids)
                # Update all members to point to the merged group
                for member in new_group:
                    groups[member] = new_group

    # Find unique groups (remove duplicates)
    unique_groups = set()
    for val in groups.values():
        unique_groups.add(frozenset(val))

    # Select one representative from each group
    to_keep = []
    dup_ids = []
    for group in unique_groups:
        group_list = list(group)
        to_keep.append(group_list[0])  # Keep first ID
        dup_ids.extend(group_list[1:])  # Remove the rest

    print(f"  Identified {len(unique_groups)} duplicate groups")
    print(f"  Will remove {len(dup_ids)} duplicate requirements")
    return dup_ids, to_keep


def convert_to_markdown(reqlist: List[Dict[str, Any]], output_dir: str) -> str:
    """
    Convert requirements list to a structured markdown file.
    
    Args:
        reqlist: List of requirement dictionaries
        output_dir: Directory to save the markdown file
        
    Returns:
        Path to the created markdown file
        
    Note:
        Creates requirements numbered sequentially as REQ-01, REQ-02, etc.
        Extracts standard fields from the 'parsed' dictionary.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_filename = os.path.join(output_dir, 'consolidated_reqs.md')
    
    print(f"Writing {len(reqlist)} requirements to {output_filename}")
    
    with open(output_filename, 'w', encoding='utf-8') as md_file:
        md_file.write("# Consolidated FHIR Requirements\n\n")
        md_file.write("This document contains deduplicated requirements from FHIR Implementation Guide processing.\n\n")
        
        for i, req in enumerate(reqlist, 1):
            # Extract fields from parsed data with fallbacks
            parsed_data = req.get('parsed', {})
            summary = parsed_data.get('summary', 'N/A').strip()
            text = parsed_data.get('text', parsed_data.get('description', 'N/A')).strip()
            context = parsed_data.get('context', 'N/A').strip()
            verification = parsed_data.get('verification', 'N/A').strip()
            actor = parsed_data.get('actor', 'N/A').strip()
            conformance = parsed_data.get('conformance', 'N/A').strip()
            conditional = parsed_data.get('conditional', 'N/A').strip()
            source = parsed_data.get('source', 'N/A').strip()

            md_file.write(f"""---

# REQ-{i:03d}

**Summary**: {summary}

**Text**: {text}

**Context**: {context}

**Verification**: {verification}

**Actor**: {actor}

**Conformance**: {conformance}

**Conditional**: {conditional}

**Source**: {source}

""")
    
    return output_filename


def full_pass(md_files: List[str] = None, rag_files: List[str] = None, 
              output_dir: str = "checkpoints/requirements_downselect", 
              threshold: float = 0.98, output_format: str = 'markdown') -> Dict[str, Any]:
    """
    Complete pipeline for requirement deduplication and consolidation.
    
    Args:
        md_files: List of markdown files to process (optional)
        rag_files: List of RAG JSON files to process (optional)  
        output_dir: Directory to save output files
        threshold: Similarity threshold for duplicate detection (0.0-1.0)
        output_format: Output format ('markdown' or 'json')
        
    Returns:
        Dictionary containing processing results and statistics
        
    Pipeline:
        1. Load requirements from all input files
        2. Generate semantic embeddings
        3. Calculate similarity scores between all pairs
        4. Group duplicates above threshold
        5. Remove duplicates and save consolidated results
        
    Raises:
        ValueError: If no input files provided or invalid parameters
    """
    # Validate inputs
    if md_files is None:
        md_files = []
    if rag_files is None:
        rag_files = []
        
    if not md_files and not rag_files:
        raise ValueError("At least one markdown or RAG file must be provided")
    
    if not 0.0 <= threshold <= 1.0:
        raise ValueError("Threshold must be between 0.0 and 1.0")
    
    if output_format not in ['markdown', 'json']:
        raise ValueError("Output format must be 'markdown' or 'json'")
    
    print("=" * 60)
    print("REQUIREMENT DEDUPLICATION PIPELINE")
    print("=" * 60)
    print(f"Markdown files: {len(md_files)}")
    print(f"RAG files: {len(rag_files)}")
    print(f"Similarity threshold: {threshold}")
    print(f"Output format: {output_format}")
    print()
    
    # Load all requirements
    all_reqs = []
    
    print("Loading requirements from files...")
    for md_file in md_files:
        print(f"  Processing: {md_file}")
        reqs = load_mdfile(md_file)
        all_reqs.extend(reqs)
        print(f"    Loaded {len(reqs)} requirements")
        
    for rag_file in rag_files:
        print(f"  Processing: {rag_file}")
        reqs = load_ragfile(rag_file)
        all_reqs.extend(reqs)
        print(f"    Loaded {len(reqs)} requirements")
    
    print(f"\nTotal requirements loaded: {len(all_reqs)}")
    
    if not all_reqs:
        raise ValueError("No requirements were successfully loaded from input files")

    # Generate embeddings
    all_reqs = generate_embeddings(all_reqs)

    # Calculate similarity scores
    score_df = calculate_scores(all_reqs)

    # Find and remove duplicates
    dup_ids, to_keep = find_dupe_groups(score_df, threshold)
    filtered_reqs = [req for req in all_reqs if req['id'] not in dup_ids]

    print(f"\nDeduplication Results:")
    print(f"  Original requirements: {len(all_reqs)}")
    print(f"  Duplicates removed: {len(dup_ids)}")
    print(f"  Final requirements: {len(filtered_reqs)}")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Save results
    output_files = []
    if output_format == 'json':
        # Save embeddings separately
        embeds_only = {}
        for req in filtered_reqs:
            if 'embedding' in req:
                embeds_only[req['id']] = [float(x) for x in req.pop('embedding')]

        embed_file = os.path.join(output_dir, 'ids_to_embeddings.json')
        with open(embed_file, 'w', encoding='utf-8') as f:
            json.dump(embeds_only, f, indent=2)
        output_files.append(embed_file)
        
        # Save consolidated requirements
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        #req_file = os.path.join(output_dir, f'consolidated_reqs_{timestamp}.json')
        req_file = os.path.join(output_dir,'consolidated_reqs.json')
        with open(req_file, 'w', encoding='utf-8') as f:
            json.dump(filtered_reqs, f, indent=2)
        output_files.append(req_file)
        
        print(f"\nOutput saved in JSON format:")
        for file in output_files:
            print(f"  {file}")
        
    elif output_format == 'markdown':
        output_file = convert_to_markdown(filtered_reqs, output_dir)
        output_files.append(output_file)
        print(f"\nOutput saved in Markdown format:")
        print(f"  {output_file}")

    return {
        "input_files": {
            "markdown": md_files},
        "original_count": len(all_reqs),
        "duplicates_removed": len(dup_ids),
        "final_count": len(filtered_reqs),
        "threshold": threshold,
        "output_format": output_format,
        "output_files": output_files,
        "output_dir": output_dir
    }


def get_md_files_from_directory(directory_path: str, pattern: str = "*.md") -> List[str]:
    """
    Get markdown files from a directory with optional pattern filtering.
    
    Args:
        directory_path: Path to directory containing markdown files
        pattern: Glob pattern to match files (default: "*.md")
        
    Returns:
        List of full file paths to matching markdown files, sorted alphabetically
        
    Raises:
        FileNotFoundError: If directory doesn't exist
        
    Example:
        >>> md_files = get_md_files_from_directory('requirements/', '*_v2.md')
        >>> print(f"Found {len(md_files)} files")
    """
    directory = Path(directory_path)
    if not directory.exists():
        raise FileNotFoundError(f"Directory does not exist: {directory_path}")
    
    md_files = list(directory.glob(pattern))
    file_paths = sorted([str(f) for f in md_files])
    
    print(f"Found {len(file_paths)} files matching '{pattern}' in {directory_path}")
    return file_paths