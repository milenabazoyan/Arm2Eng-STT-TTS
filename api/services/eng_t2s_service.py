from nemo.collections.tts.models import FastPitchModel, HifiGanModel
from TTS.api import TTS
from bark import generate_audio, preload_models
import soundfile as sf
import torch
import torchaudio
from constants.model_name_enum import ModelName
from constants.gender_enum import Gender

MALE_VOICE = "v2/en_speaker_2"
FEMALE_VOICE = "v2/en_speaker_9"

INITIAL_SOUND_FILE_NAME = "initial_sound.wav"
OUTPUT_FILE_NAME = "output.wav"

## Fast Pitch Model
fast_pitch_tts_model = FastPitchModel.from_pretrained(model_name = "tts_en_fastpitch")
vocoder = HifiGanModel.from_pretrained(model_name = "tts_en_hifigan")
# Move to GPU if available
fast_pitch_tts_model = fast_pitch_tts_model.cuda() if torch.cuda.is_available() else fast_pitch_tts_model
vocoder = vocoder.cuda() if torch.cuda.is_available() else vocoder

## YourTTS Model
your_tts_model = TTS(model_name = "tts_models/multilingual/multi-dataset/your_tts", progress_bar = False, gpu = False)

## Bark Model
preload_models()

def text_to_speech(text, model_name, initial_sound = None, gender = None):
    match model_name:
        case ModelName.FAST_PITCH:
            _tts_using_fast_pitch(text)
        case ModelName.YOUR_TTS:
            if (initial_sound is None):
                raise ValueError(f"In case model_name is selected as {ModelName.YOUR_TTS} then initial_sound must be not null")
            _tts_using_your_tts(text, initial_sound)
        case ModelName.BARK:
            if (gender is None):
                raise ValueError(f"In case mode_name is selected as {ModelName.BARK} then gender must be not null")
            _tts_using_bark(text, gender)
        case _:
            raise ValueError(f"Unsupported model: {model_name}")

    return OUTPUT_FILE_NAME

def _tts_using_fast_pitch(text):
    fast_pitch_tts_model.eval()
    vocoder.eval()

    # Generate spectrogram from text
    with torch.no_grad():
        parsed = fast_pitch_tts_model.parse(text)
        spectrogram = fast_pitch_tts_model.generate_spectrogram(tokens = parsed)
        audio = vocoder.convert_spectrogram_to_audio(spec = spectrogram)
        audio = audio.to('cpu').numpy()

    sf.write(OUTPUT_FILE_NAME, audio.T, 22050)

def _tts_using_your_tts(text, initial_sound):
    _save_initial_sound_in_disk(file = initial_sound.file)
    your_tts_model.tts_to_file(
        text = text,
        speaker_wav = INITIAL_SOUND_FILE_NAME,
        file_path = OUTPUT_FILE_NAME,
        language = "en"
    ) # sample rate in this case is 16000 (as much as we receive orginally from initial_sound)

def _tts_using_bark(text, gender):
    voice = MALE_VOICE if gender == Gender.MALE else FEMALE_VOICE
    audio_array = generate_audio(text, history_prompt=voice)
    torchaudio.save(OUTPUT_FILE_NAME, torch.tensor(audio_array).unsqueeze(0), 22050)

def _save_initial_sound_in_disk(file):
    file.seek(0)
    waveform, sample_rate = sf.read(file)
    sf.write(INITIAL_SOUND_FILE_NAME, waveform, sample_rate)
