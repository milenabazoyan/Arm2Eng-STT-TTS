# Armenian Automatic Speech Recognition (ASR)

This module provides a fine-tuned ASR model for Armenian based on NVIDIA's FastConformer-Hybrid architecture. The pipeline includes data preprocessing, manifest generation, model fine-tuning, and inference evaluation.

## Directory Structure

- `configs/`: YAML config file for model fine-tuning.
- `data/`: Contains both raw `.tsv` files from Common Voice and processed `.csv` files used for training and evaluation.
- `manifests/`: JSONL manifest files for training, validation, and testing (both relative and absolute paths).
- `notebooks/`:
  - `preprocess.ipynb`: Processes raw Common Voice TSV data into filtered, cleaned CSVs.
  - `create_manifest.ipynb`: Converts CSVs into NeMo-compatible JSONL manifest files.
  - `fine_tune_fastconformer.ipynb`: Trains the FastConformer model using NeMo.
  - `inference_demo/test_transcription.ipynb`: Runs ASR inference on demo samples.

## Instructions

### 1. Data Preprocessing

To access the `.wav` audio data used for training, visit the following Google Drive folder:  
[Armenian ASR Audio Dataset](https://drive.google.com/drive/u/0/folders/1HWpB0iMj1EcJldwR3Q5gHbjUiL-wDRiq)

Run `preprocess.ipynb` to:
- Normalize and clean text.
- Filter audio files by duration (0.5s–15s).
- Create `final_train.csv`, `train.csv`, and `validation.csv`.

### 2. Manifest Generation

Run `create_manifest.ipynb` to generate JSONL manifests required for training and evaluation.

### 3. Model Training

Use `fine_tune_fastconformer.ipynb` to fine-tune the model. This notebook loads data, configures the model with `finetune_fastconformer.yaml`, and launches training.

### 4. Inference

Test the model by running `test_transcription.ipynb` with sample `.wav` inputs.

## How to Use

1. Open notebooks diretory.
2. Open the corresponding `.ipynb` notebook (if you are going to run it locally please remove the embadded pip installs from ipynb when opening notebook and by using venv pip install requirements.txt).

