# ONCLAIVE Gitlab Repo 

## Useful Scripts & Files 
### General: 
- `local_HTML_narrative_extractor.ipynb`: Notebook to convert local HTML files to Markdown format. First step of current pipeline
- `markdown_cleaner.ipynb`: Notebook to clean unnecessary content from IG files converted to Markdown format. Second step of current pipeline

### reqs_extraction: 
Scripts to extract requirements using an LLM from the Plan Net IG
- `reqs_extraction.ipynb`: Most recent experimental notebook to extract requirements from the Plan Net IG using an LLM, including a request in the prompt to align requirements with INCOSE standards. Third step of current pipeline
- `reqs_reviewer.ipynb`: Notebook to review set of requirements using an LLM and output a refined set. Fourth step of current pipeline
- `reqs_extraction/initial_reqs_outputs`: Outputs from reqs_extraction notebook will save here
- `reqs_extraction/revised_reqs_outputs`: Outputs from reqs_revision notebook will save here

### test_kit_dev: 
- `reqs_to_testplan_grouped.ipynb`: Notebook to convert a list of requirements to a test plan, using an LLM. Fifth step of current pipeline
- `plan_to_tests.ipynb`: Notebook to take in a test plan and develop a set of tests to cover the testable IG requirements. Sixth step of current pipeline
- `test_kit_dev/test_plan_output`: Outputs from reqs_to_testplan_grouped notebook will save here
- `test_kit_dev/test_output`: Outputs from plan_to_tests notebook will save here

### prompts
LLM prompts for the various notebooks can be found in the `prompts` folder.

## Working with Above Scripts

The notebooks listed above work with the files saved in the `full-ig` folder, which have been downloaded from the below link:

- [Da Vinci PDex Plan Net IG Download](https://build.fhir.org/ig/HL7/davinci-pdex-plan-net/downloads.html)

After cloning the repository: 

1. Setup API keys: Individual API keys will need to be generated for each model in order to fully run each notebook (see below for instructions). API keys should be saved in a .env file in the root directory with the following format: 

ANTHROPIC_API_KEY=your_anthropic_key_here

GEMINI_API_KEY=your_gemini_key_here

OPENAI_API_KEY=your_openai_key_here

2. Install dependencies: This will install all necessary packages including API clients for Claude, Gemini, and GPT, as well as data processing libraries.
In your working directory, using the command line, run the command `pip install -r requirements.txt`

3. Start Jupyter: Start Jupyter to explore and run the notebooks.
In the command line, run `jupyter notebook`
This will open a web browser showing the Jupyter file explorer. Navigate to the notebook you want to run and click on it.

4. If you encounter SSL certificate issues with API requests, modify the `verify_path` variable in the `setup_clients()` function in llm_utils.py file.

5. Configure APIs: Configurations for the individual APIs can be changed in the llm_utils.py file depending on rate/token limits of user's accounts.

5. The current workflow of notebooks in the pipeline is the following: 
- `local_HTML_narrative_extractor.ipynb`
- `markdown_cleaner.ipynb`
- `reqs_extraction.ipynb`
- `reqs_reviewer.ipynb`
- `reqs_to_testplan_grouped.ipynb`
- `plan_to_tests.ipynb`

6. There are example output files to review or use as inputs for other notebooks in the output folders. After running the notebooks, you will generate a new set of outputs you can use in the pipeline as well.

Currently, the RAG and clustering notebooks are not integrated into the notebook pipeline.

## LLM Set Up

For this project, subscriptions to Claude Pro, ChatGPT Plus, and Gemini Pro and/or credits for the associated APIs will need to be purchased. Individual API keys will need to be generated as well for each model in order to fully run each notebook. 

### Anthropic

The API key is made in [Account Settings](https://console.anthropic.com/account/keys) of your Anthropic account. Be sure to add credit balance to begin using the key. 

### OpenAI

Go to Dashboard > [API Keys](https://platform.openai.com/api-keys) in your OpenAI account to create an API key for this project. 

### Gemini

Create your Gemini [API Key](https://aistudio.google.com/app/apikey?_gl=1*nc11k*_ga*OTIzNzIyMjM0LjE3MzYzNjM5Nzc.*_ga_P1DBVKWT6V*MTczNjM2Mzk3Ni4xLjAuMTczNjM2Mzk3Ni42MC4wLjEyOTEyNzA3OTM.) in Google AI Studio. Billing can also be set up within Studio however many of the services are free of charge until specific rate limits are met. See pricing information [here](https://ai.google.dev/pricing?_gl=1*1ktr08b*_ga*OTIzNzIyMjM0LjE3MzYzNjM5Nzc.*_ga_P1DBVKWT6V*MTczNjM2Mzk3Ni4xLjEuMTczNjM2Mzk3OS41Ny4wLjEyOTEyNzA3OTM.#1_5flash). 

