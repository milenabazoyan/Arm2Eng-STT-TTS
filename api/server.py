from fastapi import FastAPI
from routers import audio
from fastapi.middleware.cors import CORSMiddleware

def create_app():
    app = FastAPI(
        title = "ArmSpeech2TextText2EngSpeechPipeline",
        description = "APIs for speech translation",
        version = "1.0.0",
        openapi_url = "/openapi.json",
        docs_url = "/",
        redoc_url = "/redoc"
    )
    app.include_router(audio.router, tags = ['audio'])

    app.add_middleware(
        CORSMiddleware,
        allow_origins = ["*"],
        allow_credentials = True,
        allow_methods = ["*"],
        allow_headers = ["*"],
    )
    return app
