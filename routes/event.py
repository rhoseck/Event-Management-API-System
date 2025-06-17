from fastapi import APIRouter, HTTPException
from typing import List
from schemas.event import Event, EventCreate, EventUpdate, EventResponse
from services.event import EventService

event_router = APIRouter()

@event_router.post("/", response_model=EventResponse, status_code=201)
async def create_event(event_data: EventCreate):
    new_event = await EventService.create_event(event_data)
    if new_event is None:
        raise HTTPException(status_code=400, detail="Event creation failed")
    return EventResponse(message="Event created successfully", event=new_event, speakers=new_event.speakers)

@event_router.get("/{event_id}", response_model=EventResponse, status_code=200)
async def get_event(event_id: int):
    event = await EventService.get_event_by_id(event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return EventResponse(message="Event retrieved successfully", event=event, speakers=event.speakers)

@event_router.get("/", response_model=List[Event], status_code=200)
async def get_all_events():
    return await EventService.get_all_events()

@event_router.put("/{event_id}", response_model=EventResponse, status_code=200)
async def update_event(event_id: int, event_data: EventUpdate):
    updated_event = await EventService.update_event(event_id, event_data)
    if updated_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return EventResponse(message="Event updated successfully", event=updated_event, speakers=updated_event.speakers)

@event_router.delete("/{event_id}", status_code=204)
async def delete_event(event_id: int):
    success = await EventService.delete_event(event_id)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event deleted successfully"}

@event_router.post("/{event_id}/close", response_model=EventResponse, status_code=200)
async def close_event(event_id: int):
    event = await EventService.close_event(event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return EventResponse(message="Event closed successfully", event=event, speakers=event.speakers)



# from fastapi import APIRouter, HTTPException
# from typing import List
# from schemas.event import Event, EventCreate, EventUpdate, EventResponse
# from services.event import EventService

# event_router = APIRouter()

# from fastapi import APIRouter, HTTPException
# from services.event import EventService
# from schemas.event import EventCreate, EventResponse

# event_router = APIRouter()

# @event_router.post("/", response_model=EventResponse, status_code=201)
# async def create_event(event_data: EventCreate):
#     event = await EventService.create_event(event_data)
#     if not event:
#         raise HTTPException(status_code=400, detail="Event creation failed")
#     return EventResponse(message="Event created successfully", event=event)

# @event_router.get("/{event_id}", response_model=EventResponse, status_code=200)
# async def get_event(event_id: int):
#     event = await EventService.get_event_by_id(event_id)
#     if event is None:
#         raise HTTPException(status_code=404, detail="Event not found")
#     enriched_event = await EventService.add_speaker_to_event(Event(**event.__dict__))
#     return EventResponse(message="Event retrieved successfully", event=enriched_event, speakers=enriched_event.speakers)

# @event_router.get("/", response_model=List[Event], status_code=200)
# async def get_all_events():
#     events_list = await EventService.get_all_events()
#     enriched_events = [await EventService.add_speaker_to_event(Event(**event.__dict__)) for event in events_list]
#     return enriched_events

# @event_router.put("/{event_id}", response_model=EventResponse, status_code=200)
# async def update_event(event_id: int, event_data: EventUpdate):
#     updated_event = await EventService.update_event(event_id, event_data)
#     if updated_event is None:
#         raise HTTPException(status_code=404, detail="Event not found")
#     enriched_event = await EventService.add_speaker_to_event(Event(**updated_event.__dict__))
#     return EventResponse(message="Event updated successfully", event=enriched_event, speakers=enriched_event.speakers)

# @event_router.delete("/{event_id}", status_code=204)
# async def delete_event(event_id: int):
#     success = await EventService.delete_event(event_id)
#     if not success:
#         raise HTTPException(status_code=404, detail="Event not found")
#     return {"message": "Event deleted successfully"}

# @event_router.post("/{event_id}/close", response_model=EventResponse, status_code=200)
# async def close_event(event_id: int):
#     event = await EventService.close_event(event_id)
#     if event is None:
#         raise HTTPException(status_code=404, detail="Event not found")
#     enriched_event = await EventService.add_speaker_to_event(Event(**event.__dict__))
#     return EventResponse(message="Event closed successfully", event=enriched_event, speakers=enriched_event.speakers)

# from fastapi import APIRouter, HTTPException
# from schemas.event import Event, EventCreate, EventUpdate
# from services.event import EventService


# event_router = APIRouter()
# @event_router.post("/", response_model=Event, status_code=201)
# async def create_event(event_data: EventCreate):
#     return await EventService.create_event(event_data)

# @event_router.get("/{event_id}", response_model=Event, status_code=200)
# async def get_event(event_id: int):
#     event = await EventService.get_event_by_id(event_id)
#     if event is None:
#         raise HTTPException(status_code=404, detail="Event not found")
#     return event

# @event_router.get("/", response_model=list[Event], status_code=200)
# async def get_all_events():
#     return await EventService.get_all_events()

# @event_router.put("/{event_id}", response_model=Event, status_code=200)
# async def update_event(event_id: int, event_data: EventUpdate):
#     event = await EventService.update_event(event_id, event_data)
#     if event is None:
#         raise HTTPException(status_code=404, detail="Event not found")
#     return event

# @event_router.delete("/{event_id}", status_code=204)
# async def delete_event(event_id: int):
#     success = await EventService.delete_event(event_id)
#     if not success:
#         raise HTTPException(status_code=404, detail="Event not found")
    

# @event_router.post("/{event_id}/close", response_model=Event, status_code=200)
# async def close_event(event_id: int):
#     event = await EventService.close_event(event_id)
#     if event is None:
#         raise HTTPException(status_code=404, detail="Event not found")
#     return event