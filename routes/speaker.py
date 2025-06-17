from fastapi import APIRouter
from schemas.speaker import Speaker
from services.speaker import SpeakerService

speaker_router = APIRouter()
@speaker_router.get("/", response_model=list[Speaker], status_code=200)
async def get_all_speakers():
    return await SpeakerService.get_all_speakers()