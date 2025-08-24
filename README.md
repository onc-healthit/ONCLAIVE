# ONCLAIVE Gitlab Repo 

## Overview
This repository includes a set of scripts that are run together as part of a pipeline to take in a FHIR implementation guide, extract requirements, generate a test plan, and develop Inferno test kits to test API standards conformance. Each phase of the pipeline uses generative AI to review IG-related inputs and create the outputs for the next phase of the pipeline. 


## Pipeline Scripts & Files 

### Utilities Files
- `llm_utils.py`: Script to setup LLM configurations, including which APIs can be called by the pipeline scripts, rate limits, and safety filters.
- `prompt_utils.py`: Script to setup imports for/connections between LLM prompts and corresponding scripts/API calls for each step of the process


### Pipeline Steps

The entire pipeline can be run using the Jupyter notebook `full_pipeline.ipynb`. The pipeline notebook imports the following scripts as modules in sequence to complete all steps in the process.

1) Implementation Guide Prep: 
- `local_HTML_narrative_extractor.py`: Notebook to convert local HTML files (downloaded IG) to Markdown format. First step of pipeline
- `markdown_cleaner.py`: Notebook to clean unnecessary content from IG files converted to Markdown format. Second step of pipeline

2) Requirements Extraction: 
Scripts to extract requirements using an LLM from the Plan Net IG.
- `reqs_extraction.py`: Script that uses an LLM to extract requirements from the Plan Net IG. Third step of pipeline
- `reqs_reviewer.py`: Notebook to review set of requirements using an LLM and output a refined set. Fourth step of pipeline
- `requirement_downselect.py`: Notebook to review multiple sets of requirements in markdown files and identify the total set of requirements across input lists, while removing duplicates. Fifth step of pipeline
- `checkpoints/requirements_extraction`: Outputs from first requirements extraction step will save here
- `checkpoints/requirements_refinement`: Outputs from first requirements extraction step will save here
- `checkpoints/requirements_downselect`: Outputs from requirements downselect step will save here


3) Test Plan Generation
- `req_to_testplan.py`: Notebook to convert a list of requirements to a test plan, using an LLM. Sixth step of pipeline
- `checkpoints/testplan_generation`: Outputs from test plan generation step will save here

4) Test Kit Generation
- `plan_to_tests.py`: Notebook to take in a test plan and develop a set of tests to cover the testable IG requirements. Seventh step of pipeline
- `checkpoints/test_kit_generation`: Outputs from test kit generation step will save here

### Prompts
LLM prompts for the various notebooks can be found in the `prompts` folder.

## Working with the Pipeline

The notebook and scripts listed above work with the files saved in the `full-ig` folder, which have been downloaded from the below link:

- [Da Vinci PDex Plan Net IG Download](https://build.fhir.org/ig/HL7/davinci-pdex-plan-net/downloads.html)

After cloning the repository: 

1. Setup API keys: Individual API keys will need to be generated for each model in order to fully run each notebook (see below for instructions). API keys should be saved in a .env file in the root directory. 

Example: 

ANTHROPIC_API_KEY=your_anthropic_key_here

GEMINI_API_KEY=your_gemini_key_here

OPENAI_API_KEY=your_openai_key_here

2. Install dependencies: This will install all necessary packages including API clients as well as data processing libraries.
In your working directory, using the command line, run the command `pip install -r requirements.txt`

3. Start Jupyter: Start Jupyter to explore and run the notebooks.
In the command line, run `jupyter notebook`
This will open a web browser showing the Jupyter file explorer. Navigate to the notebook you want to run and click on it.

4. If you encounter SSL certificate issues with API requests, modify the `verify_path` variable in the `setup_clients()` function in llm_utils.py file.

5. Configure APIs: Configurations for individual APIs can be changed in the llm_utils.py file depending on rate/token limits of user's accounts.


## LLM Set Up

This project primarily experimented with Claude, Gemini, and ChatGPT LLM APIs. To use the notebooks in their current format, individual API keys will need to be generated for each model of interest. Information on how to obtain API keys for Anthropic (Claude), OpenAI (ChatGPT), and Google (Gemini) can be found below. 


### Anthropic

The API key is made in [Account Settings](https://console.anthropic.com/account/keys) of an Anthropic account. Be sure to add credit balance to begin using the key. 

### OpenAI

Go to Dashboard > [API Keys](https://platform.openai.com/api-keys) in an OpenAI account to create an API key for this project. 

### Gemini

Create a Gemini [API Key](https://aistudio.google.com/app/apikey?_gl=1*nc11k*_ga*OTIzNzIyMjM0LjE3MzYzNjM5Nzc.*_ga_P1DBVKWT6V*MTczNjM2Mzk3Ni4xLjAuMTczNjM2Mzk3Ni42MC4wLjEyOTEyNzA3OTM.) in Google AI Studio. Billing can also be set up within Studio however many of the services are free of charge until specific rate limits are met. See pricing information [here](https://ai.google.dev/pricing?_gl=1*1ktr08b*_ga*OTIzNzIyMjM0LjE3MzYzNjM5Nzc.*_ga_P1DBVKWT6V*MTczNjM2Mzk3Ni4xLjEuMTczNjM2Mzk3OS41Ny4wLjEyOTEyNzA3OTM.#1_5flash). 

