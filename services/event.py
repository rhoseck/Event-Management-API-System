import random
from schemas.event import EventCreate, EventUpdate, Event
from schemas.speaker import Speaker as SpeakerSchema
from database import events, speakers
from models import Event as EventModel, Speaker as SpeakerModel

class EventService:
    @staticmethod
    async def create_event(event_data: EventCreate) -> Event:
        event_id = len(events) + 1
        assigned_speakers: list[SpeakerModel] = []
        if speakers:
            chosen_speaker = random.choice(speakers)
            assigned_speakers = [chosen_speaker]

        event = EventModel(id=event_id, **event_data.model_dump(), speakers=assigned_speakers)
        events.append(event)
        return await EventService.add_speaker_to_event(event)

    @staticmethod
    async def add_speaker_to_event(event: EventModel) -> Event:
        return Event(
            id=event.id,
            title=event.title,
            location=event.location,
            date=event.date,
            event_time=event.event_time,
            is_open=event.is_open,
            speakers=[
                SpeakerSchema(id=s.id, name=s.name, topic=s.topic) for s in event.speakers
            ]
        )

    @staticmethod
    async def close_event(event_id: int) -> Event | None:
        for event in events:
            if event.id == event_id:
                event.is_open = False
                return await EventService.add_speaker_to_event(event)
        return None

    @staticmethod
    async def get_event_by_id(event_id: int) -> Event | None:
        for event in events:
            if event.id == event_id:
                return await EventService.add_speaker_to_event(event)
        return None

    @staticmethod
    async def get_all_events() -> list[Event]:
        return [await EventService.add_speaker_to_event(event) for event in events]

    @staticmethod
    async def update_event(event_id: int, event_update: EventUpdate) -> Event | None:
        for i, event in enumerate(events):
            if event.id == event_id:
                updated_data = event_update.model_dump(exclude_unset=True)
                for key, value in updated_data.items():
                    setattr(event, key, value)
                events[i] = event
                return await EventService.add_speaker_to_event(event)
        return None

    @staticmethod
    async def delete_event(event_id: int) -> bool:
        for i, event in enumerate(events):
            if event.id == event_id:
                events.pop(i)
                return True
        return False
