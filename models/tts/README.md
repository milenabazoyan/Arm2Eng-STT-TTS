# English Text-to-Speech (TTS)

This module synthesizes English speech from translated Armenian text using three models:
1. **FastPitch + HiFi-GAN** (Fast and intelligible)
2. **YourTTS** (Voice cloning and multilingual)
3. **Bark** (Highly expressive and supports speaker style transfer)

## Directory Structure

- `Fastpitch/`: FastPitch + HiFi-GAN notebook and mel-spectrogram visualization.
- `YourTTS/`: YourTTS notebook, waveform visualization, and demo output.
- `bark/`: Bark notebook with sample male and female outputs.
- `latency_evaluation/`: Generation time plots for each model.

## Model Overviews

| Model       | Strengths                              | Use Case                             |
|-------------|----------------------------------------|--------------------------------------|
| FastPitch   | Real-time synthesis, efficient         | Live systems requiring low latency   |
| YourTTS     | Speaker similarity, multilingual       | Personalized or voice-cloning needs |
| Bark        | High expressiveness, background sound  | Creative or media applications       |

## How to Use

1. Choose the desired model directory.
2. Open the corresponding `.ipynb` notebook (if you are going to run it locally please remove the embadded pip installs from ipynb when opening notebook and by using venv pip install requirements.txt).

