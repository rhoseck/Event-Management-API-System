from __future__ import annotations
from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from schemas.speaker import Speaker

class EventBase(BaseModel):
    title: str
    location: str
    date: date
    event_time: str = "00:00"


class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    title: Optional[str] = None
    location: Optional[str] = None
    date: Optional[str] = "YYYY-MM-DD"
    event_time: Optional[str] = "00:00"

class Event(EventBase):
    id: int
    is_open: bool = True
    speakers: List[Speaker] = []


class EventResponse(BaseModel):
    message: str
    event: Event