# BioASQ Biomedical Question Answering

This repository contains code for biomedical question answering on BioASQ datasets, using PubMed retrieval and large language models.

## Requirements and installation

Use Python 3.11 and run all commands from the repository root. Internet access is required to install dependencies and access the model and PubMed APIs.

```bash
python -m venv .venv
```

Activate the environment on Linux or macOS:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies, including the `en_core_sci_md` sentence segmentation model:

```bash
python -m pip install -r requirements.txt
```

## API configuration

Copy `.env.example` to `.env` and fill in `OPENAI_API_KEY`, `GEMINI_API_KEY`, `GEMINI_MODEL`, and `ENTREZ_EMAIL`. `ENTREZ_API_KEY` is optional. The current code requires `GEMINI_API_KEY` to be set even when using OpenAI because the Gemini module is imported at startup.

## Data preparation

Place the BioASQ JSON input file in `dataset/`. Dataset files are not tracked in this repository and must be supplied separately. The input must contain a top-level `questions` list; each question must include `id`, `body`, and `type`.

For Phase B, use data containing PubMed `documents` and/or `snippets`, depending on the selected document type. Evaluation additionally requires reference `ideal_answer` values and `exact_answer` values for yes/no questions. The example below assumes `dataset/12B1_golden.json` is available.

## Running the code

Run Phase B with OpenAI and PubMed abstracts:

```bash
python src/main.py --data_path dataset/12B1_golden.json --phase B --model openai --model_name gpt-4o-mini --document_type abstract --output output/predictions.json
```

To enable question classification, decomposition, and subsequent queries, append `--next_query True`. To retrieve documents directly from the question instead of using the supplied Phase B documents, replace `--phase B` with `--phase A+`.

For input without reference answers, append `--submit True` to skip evaluation. To use the supplied snippets in Phase B, replace `--document_type abstract` with `--document_type snippet`.

## Output

Predictions are saved to `output/predictions.json`. Detailed question records, prompts, and retrieval information are saved to `all_info.json` in the repository root. Existing files at these paths are overwritten on subsequent runs.

Unless `--submit True` is specified, the program prints ROUGE-2 and ROUGE-SU4 recall and F1 scores, together with yes/no accuracy.
