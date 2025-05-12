#!/bin/bash
pip install 'nemo_toolkit[asr]'
pip install uvicorn
python run.py
pip install fastapi
pip install torchaudio
pip install seaborn
pip install TTS
pip install git+https://github.com/suno-ai/bark.git
pip uninstall torch -Y
pip uninstall torchvision -Y
pip uninstall torchaudio -Y
pip install --force-reinstall torch==2.5.1 --index-url https://download.pytorch.org/whl/cpu
pip install torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cpu
pip install typing-extensions==4.12.2
pip install python-multipart