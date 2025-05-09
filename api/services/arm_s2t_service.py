from nemo.collections.asr.models import EncDecHybridRNNTCTCBPEModel
import torchaudio
import tempfile

speech_to_text_model = EncDecHybridRNNTCTCBPEModel.from_pretrained(
    model_name = "milenabazoyan/fastconformer-hybrid-arm-asr"
)

async def speech_to_text(file):
    with tempfile.NamedTemporaryFile(delete = True, suffix = ".wav") as tmp:
        tmp.write(await file.read())
        tmp.flush()
        waveform, sample_rate = torchaudio.load(tmp.name)
        text = speech_to_text_model.transcribe([waveform.squeeze().numpy()])[0].text
    return text
