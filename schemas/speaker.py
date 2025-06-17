from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class SpeakerBase(BaseModel):
    name: str
    topic: str

class SpeakerCreate(SpeakerBase):
    pass

class SpeakerUpdate(BaseModel):
    name: Optional[str] = None
    topic: Optional[str] = None

class Speaker(SpeakerBase):
    id: UUID
