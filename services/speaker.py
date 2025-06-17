from schemas.speaker import SpeakerCreate, SpeakerUpdate
from database import speakers
from models import Speaker

class SpeakerService:
    @staticmethod
    async def get_all_speakers() -> list[Speaker]:
        return speakers