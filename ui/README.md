# Frontend for AM → EN Speech Translation Pipeline

This module provides the frontend interface for demonstrating the Armenian-to-English speech translation pipeline in a user-friendly, minimal, and visually aesthetic manner.

## Features

- Record Armenian speech directly in the browser.
- Maximum recording duration of **30 seconds** (auto-stops if limit is reached).
- Option to manually stop recording earlier.
- Real-time waveform visualizer while recording.
- Live countdown timer.
- Choose between different voice synthesis models:
  - **Fast Pitch**
  - **Your TTS**
  - **Bark** (includes gender selection: *male* or *female*)
- Subtle, inline **loading indicator** while waiting for the translation response.
- The translated English output is returned as a playable `.wav` file.

## How It Works

1. Click **"Start Recording"**.
2. Speak in Armenian — your voice is visualized live, and a 30-second countdown begins.
3. Recording stops automatically at 30 seconds or when you click **"Stop Recording"**.
4. An HTTP POST request is sent to the backend at:
http://localhost:8080/translations/audio?model=<MODEL>[&gender=<GENDER>]
- The request contains the recorded audio (`multipart/form-data`).
- If the selected model is `bark`, an additional `gender` query parameter is sent with value `male` or `female`.
5. The backend processes the input using:
- Armenian ASR
- Machine translation
- English TTS (based on selected model/gender)
6. A translated `.wav` file is returned and made available in the UI player for playback.

## Running Locally

1. Ensure the backend API is running at: `http://localhost:8080/translations/audio`.
2. Open `index.html` in a modern browser (e.g., Chrome, Firefox, Edge) that supports:
- `MediaStream` (microphone recording)
- Web Audio API
3. Use the interface to test the pipeline.
- Grant microphone access when prompted.
- Choose a model and, optionally, gender (if using Bark).
- The returned audio will be playable in the embedded player.
