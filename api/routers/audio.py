from fastapi import APIRouter, File, UploadFile, Query, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from services import arm_s2t_service, eng_t2s_service, translation_service
from constants.model_name_enum import ModelName
from constants.gender_enum import Gender

router = APIRouter()

@router.post("/translations/audio")
async def transcribe_audio(
    arm_speech: UploadFile = File(..., description = "Armenian speech file in wav format to translate"),
    model: ModelName = Query(..., description = "Choose the model to run for TTS"),
    gender: Gender = Query(None, description = "Choose the gender for returned speech in case Bark model is chosen")
):
    if arm_speech.content_type not in ["audio/wav", "audio/x-wav"]:
        raise HTTPException(status_code = 400, detail = "Invalid audio format")

    arm_text = await arm_s2t_service.speech_to_text(file = arm_speech)
    eng_text = translation_service.translate(text = arm_text)
    eng_speech = eng_t2s_service.text_to_speech(
        text = eng_text,
        model_name = model,
        initial_sound = arm_speech,
        gender = gender
    )

    return FileResponse(
        path = eng_speech,
        media_type = "audio/wav",
        filename = eng_speech
    )
