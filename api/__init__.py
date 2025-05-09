from fastapi import FastAPI
from .routers import audio

app = FastAPI()

app.include_router(audio.router)
