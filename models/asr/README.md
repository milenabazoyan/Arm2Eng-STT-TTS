# Arm2Eng-STT-TTS
End-to-End Acoustic and Semantic Modeling For Armenian-to-English Speech and Text Systems

# FastConformer Hybrid ASR for Armenian

This project contains code, configuration, and training artifacts for fine-tuning NVIDIA's FastConformer Hybrid (RNNT + CTC) model for Armenian Automatic Speech Recognition (ASR) using the Mozilla Common Voice dataset.

---
## What This Does

- Fine-tunes [`nvidia/stt_hy_fastconformer_hybrid_large_pc`](https://huggingface.co/nvidia/stt_hy_fastconformer_hybrid_large_pc) for the Armenian language.
- Uses NVIDIA NeMo toolkit for model loading, training, and saving.
- Extracts and reuses tokenizer from the `.nemo` model file.
- Stores large model files and tokenizer artifacts on Hugging Face Hub.

---

## Armenian ASR Fine-Tuned Model on Hugging Face

[**milenabazoyan/fastconformer-hybrid-arm-asr**](https://huggingface.co/milenabazoyan/fastconformer-hybrid-arm-asr)

Includes:
- Fine-tuned model (`.nemo`)
- Tokenizer files (`.model`, `.vocab`, `vocab.txt`)
- Training configuration file (`finetune_fastconformer.yaml`)

---
