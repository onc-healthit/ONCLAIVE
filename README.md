# ASTP/ONC Leveraging Artificial Intelligence Validation and Exploration (ONCLAIVE) for Inferno FHIR Testing

## Overview

This repository includes:

- `pipeline/`: A set of scripts that are run together as part of a pipeline to take in an HL7® FHIR® Implementation Guide, extract requirements, generate a test plan, and develop Inferno Test Kits to test API standards conformance by using generative AI to review IG-related inputs and create the outputs for each phase of the pipeline.
- `full_pipeline.ipynb` / `full_pipeline_demo.ipynb`: Optional Jupyter notebooks to use for running and visualizing each step of the pipeline.
- `us_core_differences`: Directory that contains scripts for detecting requirements differences between difference versions of the US Core Implementation Guide.

## Input/Output Artifacts

When running the pipeline, the user specifies a folder as a location for all of the artifacts associated with the current pipeline run. The pipeline is designed so that each step reads its inputs from and writes its outputs to specific locations in the artifacts folder. The organization of this folder is described in the [demo-artifacts README](demo-artifacts/README.md).

## Running the Pipeline

After performing initial setup, the pipeline can be run using the command line or the Jupyter notebook in `pipeline/full_pipeline_demo.ipynb`.

### Initial Setup

After cloning the repository:

1. Setup APIs of interest:

   - LLMs of interest can be setup in the `llm_utils.py` file in the `pipeline` directory.
   - Individual API keys will need to be generated for each model of interest to fully run each notebook or file using the selected API (see [LLM Setup](#llm-set-up) for instructions). API keys should be saved in a `.env` file in the root directory.

     Example:

     ANTHROPIC_API_KEY=your_anthropic_key_here

     GEMINI_API_KEY=your_gemini_key_here

     OPENAI_API_KEY=your_openai_key_here

2. Install dependencies:

   This repository uses [UV](https://docs.astral.sh/uv/) for Python dependency and project management. You can install UV with the following command, `curl -LsSf https://astral.sh/uv/install.sh | sh` or browse the [Installation Methods](https://docs.astral.sh/uv/getting-started/installation/#installation-methods) page in the documentation. Once installed, run the following command in the root directory of this repository:

   ```shell
   uv sync
   ```

   This will install all necessary packages including API clients as well as data processing libraries that are present in the `uv.lock` and `pyproject.toml` files and creates (or updates) a virtual environment in `.venv` by default.

3. Place the HTML files from the IG you're running the pipeline against in `YOUR_ARTIFACTS_FOLDER/ig/site`.

### Command Line

The following commands run the scripts for each step of the pipeline:

```shell
uv run pipeline/process_ig.py
uv run pipeline/extract_requirements.py
uv run pipeline/generate_test_plan.py
uv run pipeline/generate_tests.py
```

If no other arguments are provided, the scripts will use the [demo-artifacts folder](demo-artifacts) as the location for all input/output. Each script can be run with `-h` to see information on other available arguments.

### Jupyter Notebook

1. Start Jupyter: Start Jupyter to explore and run the notebooks.
   Jupyter notebooks can be run locally using the command line or by opening notebook files in IDEs of choice.

   To open a file using the command line, run `jupyter notebook`
   This will open a web browser showing the Jupyter file explorer. Navigate to the notebook you want to run and click on it.

2. Configure APIs: Configurations for individual APIs can be changed in the llm_utils.py file depending on rate/token limits of user's accounts.

## Pipeline Scripts & Files

### Utilities Files

- `llm_utils.py`: Script to setup LLM configurations, including which APIs can be called by the pipeline scripts, rate limits, and safety filters.
- `prompt_utils.py`: Script to setup imports for/connections between LLM prompts and corresponding scripts/API calls for each step of the process

### Pipeline Steps

The entire pipeline can be run using the Jupyter notebook `full_pipeline.ipynb` in the `pipeline` directory. The pipeline notebook imports the following scripts as modules in sequence to complete all steps in the process.

1. Implementation Guide Prep:

Script: `process_ig.py`
Command Line Command: `uv run pipeline/process_ig.py`
Helper Files:

- `html_narrative_extractor_01.py`: File with helper functions to convert local HTML files (downloaded IG) to markdown format.
- `markdown_cleaner_02.py`: File with helper functions to clean unnecessary content from IG files converted to markdown format.

2. Requirements Extraction:

Script: `extract_requirements.py`
Command Line Command: `uv run pipeline/extract_requirements.py`
Helper Files:

- `reqs_extraction_03.py`: File with helper functions that use an LLM to extract requirements from the input IG.
- `reqs_reviewer_04.py`: File with helper functions to review set of requirements using an LLM and output a refined set.
- `requirement_downselect_05.py`: File with helper functions to review multiple sets of requirements in markdown files and identify the total set of requirements across input lists, while removing duplicates.

3. Test Plan Generation

Script: `generate_test_plan.py`
Command Line Command: `uv run pipeline/generate_test_plan.py`
Helper Files:

- `test_plan_06.py`: File with helper functions to convert a list of requirements to a test plan, using an LLM.

4. Test Kit Generation

Script: `generate_tests.py`
Command Line Command: `uv run pipeline/generate_tests.py`
Helper Files:

- `test_kit_07.py`: File with helper functions to take in a test plan and develop a set of tests to cover the testable IG requirements.

## LLM Set Up

While developing the pipeline, this project primarily experimented with Claude, Gemini, and ChatGPT LLM APIs. To use the pipeline in its current form, individual API keys will need to be generated for each model of interest. Information on how to obtain API keys for Anthropic (Claude), OpenAI (ChatGPT), and Google (Gemini) can be found below.

### Anthropic

The API key is made in [Account Settings](https://console.anthropic.com/account/keys) of an Anthropic account. A credit balance will need to be added to begin using the key.

### OpenAI

Go to Dashboard > [API Keys](https://platform.openai.com/api-keys) in an OpenAI account to create an API key for this project. A credit balance will need to be added to begin using the key.

### Gemini

Create a Gemini [API Key](https://aistudio.google.com/app/apikey?_gl=1*nc11k*_ga*OTIzNzIyMjM0LjE3MzYzNjM5Nzc.*_ga_P1DBVKWT6V*MTczNjM2Mzk3Ni4xLjAuMTczNjM2Mzk3Ni42MC4wLjEyOTEyNzA3OTM.) in Google AI Studio. Billing can also be set up within Studio however many of the services are free of charge until specific rate limits are met. See pricing information [here](https://ai.google.dev/pricing?_gl=1*1ktr08b*_ga*OTIzNzIyMjM0LjE3MzYzNjM5Nzc.*_ga_P1DBVKWT6V*MTczNjM2Mzk3Ni4xLjEuMTczNjM2Mzk3OS41Ny4wLjEyOTEyNzA3OTM.#1_5flash).

## Analyzing differences between US Core versions

The `us_core_differences` folder contains scripts to detect differences in the IG narrative between versions of the US Core IG. The `process_igs.py` script will download two versions of the IG, extract the narrative from html files, and convert it to markdown. The `compare_igs.py` script will identify differences in the narrative between the two versions. The differences will be outputted to `<input_artifacts_dir>/ig/differences.md`.

```sh
> uv run us_core_differences/process_igs.py -n https://hl7.org/fhir/us/core/STU8/full-ig.zip -o https://hl7.org/fhir/us/core/STU7/full-ig.zip ../us-core-comparison

> uv run us_core_differences/compare_igs.py ../us-core-comparison
```

## License

ⓒ2025 The MITRE Corporation.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
