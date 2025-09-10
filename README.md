# ASTP/ONC Leveraging Artificial Intelligence Validation and Exploration (ONCLAIVE) for Inferno FHIR Testing 

## Overview
This repository includes a set of scripts that are run together as part of a pipeline to take in a FHIR implementation guide, extract requirements, generate a test plan, and develop Inferno test kits to test API standards conformance. Each phase of the pipeline uses generative AI to review IG-related inputs and create the outputs for the next phase of the pipeline. 


## Pipeline Scripts & Files 

### Utilities Files
- `llm_utils.py`: Script to setup LLM configurations, including which APIs can be called by the pipeline scripts, rate limits, and safety filters.
- `prompt_utils.py`: Script to setup imports for/connections between LLM prompts and corresponding scripts/API calls for each step of the process


### Pipeline Steps

The entire pipeline can be run using the Jupyter notebook `full_pipeline.ipynb` in the `pipeline` directory. The pipeline notebook imports the following scripts as modules in sequence to complete all steps in the process.

1) Implementation Guide Prep: 
- `HTML_narrative_extractor_01.py`: Notebook to convert local HTML files (downloaded IG) to Markdown format. First step of pipeline
- `markdown_cleaner_02.py`: Notebook to clean unnecessary content from IG files converted to Markdown format. Second step of pipeline
- `checkpoints/markdown1`: Outputs from the HTML extraction will save here
- `checkpoints/markdown2`: Outputs from the markdown cleaner will save here

2) Requirements Extraction: 
Scripts to extract requirements using an LLM from the Plan Net IG.
- `reqs_extraction_03.py`: Script that uses an LLM to extract requirements from the Plan Net IG. Third step of pipeline
- `reqs_reviewer_04.py`: Notebook to review set of requirements using an LLM and output a refined set. Fourth step of pipeline
- `requirement_downselect_05.py`: Notebook to review multiple sets of requirements in markdown files and identify the total set of requirements across input lists, while removing duplicates. Fifth step of pipeline
- `checkpoints/requirements_extraction`: Outputs from first requirements extraction step will save here
- `checkpoints/requirements_refinement`: Outputs from first requirements extraction step will save here
- `checkpoints/requirements_downselect`: Outputs from requirements downselect step will save here


3) Test Plan Generation
- `test_plan_06.py`: Notebook to convert a list of requirements to a test plan, using an LLM. Sixth step of pipeline
- `checkpoints/testplan_generation`: Outputs from test plan generation step will save here

4) Test Kit Generation
- `test_kit_07.py`: Notebook to take in a test plan and develop a set of tests to cover the testable IG requirements. Seventh step of pipeline
- `checkpoints/test_kit_generation`: Outputs from test kit generation step will save here

### Prompts
LLM prompts for the various notebooks can be found in the `prompts` folder. Prompts in their current state were optimized for the available LLM models at the time of the pipeline's development. Prompts can be revised to alter instructions or content of the outputs at each step, as well as to work better with different LLM models.

## Working with the Pipeline

The notebook and scripts listed above work with the files saved in the `full-ig` folder.

Other IGs can be used with this pipeline. To do so, download the IG and save the files under the `full-ig` folder. The notebook will pull from the `site` folder under `full-ig`. 

After cloning the repository: 

1. Setup APIs of interest:
    - LLMs of interest can be setup in the `llm_utils.py` file
    - Individual API keys will need to be generated for each model of interest to fully run each notebook using the selected API (see below for instructions). API keys should be saved in a .env file in the root directory. 

        Example: 

        ANTHROPIC_API_KEY=your_anthropic_key_here

        GEMINI_API_KEY=your_gemini_key_here

        OPENAI_API_KEY=your_openai_key_here

2. Install dependencies: This will install all necessary packages including API clients as well as data processing libraries.
    In your working directory, using the command line, run the command `pip install -r requirements.txt`

3. Start Jupyter: Start Jupyter to explore and run the notebooks.
    Jupyter notebooks can be run locally using the command line or by opening notebook files in IDEs of choice. 

    To open a file using the command line, run `jupyter notebook`
    This will open a web browser showing the Jupyter file explorer. Navigate to the notebook you want to run and click on it.

4. If you encounter SSL certificate issues with API requests, modify the `verify_path` variable in the `setup_clients()` function in `llm_utils.py` file.

5. Configure APIs: Configurations for individual APIs can be changed in the llm_utils.py file depending on rate/token limits of user's accounts.


## LLM Set Up

While developing the pipeline, this project primarily experimented with Claude, Gemini, and ChatGPT LLM APIs. To use the notebooks in their current format, individual API keys will need to be generated for each model of interest. Information on how to obtain API keys for Anthropic (Claude), OpenAI (ChatGPT), and Google (Gemini) can be found below. 


### Anthropic

The API key is made in [Account Settings](https://console.anthropic.com/account/keys) of an Anthropic account. A credit balance will need to be added to begin using the key. 

### OpenAI

Go to Dashboard > [API Keys](https://platform.openai.com/api-keys) in an OpenAI account to create an API key for this project. A credit balance will need to be added to begin using the key.

### Gemini

Create a Gemini [API Key](https://aistudio.google.com/app/apikey?_gl=1*nc11k*_ga*OTIzNzIyMjM0LjE3MzYzNjM5Nzc.*_ga_P1DBVKWT6V*MTczNjM2Mzk3Ni4xLjAuMTczNjM2Mzk3Ni42MC4wLjEyOTEyNzA3OTM.) in Google AI Studio. Billing can also be set up within Studio however many of the services are free of charge until specific rate limits are met. See pricing information [here](https://ai.google.dev/pricing?_gl=1*1ktr08b*_ga*OTIzNzIyMjM0LjE3MzYzNjM5Nzc.*_ga_P1DBVKWT6V*MTczNjM2Mzk3Ni4xLjEuMTczNjM2Mzk3OS41Ny4wLjEyOTEyNzA3OTM.#1_5flash). 


## License
ⓒ2025 The MITRE Corporation.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.