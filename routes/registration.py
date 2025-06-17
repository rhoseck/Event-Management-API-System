from typing import List
from fastapi import APIRouter, HTTPException
from schemas.registration import Registration, RegistrationCreate, RegistrationUpdate
from services.registration import RegistrationService
from uuid import UUID
registration_router = APIRouter()

@registration_router.post("/", response_model=Registration, status_code=201)
async def create_registration(registration_data: RegistrationCreate):
    new_registration = await RegistrationService.register_user(registration_data)
    if new_registration is None:
        raise HTTPException(status_code=400, detail="Registration failed: User or event not found, or already registered.")
    return new_registration

@registration_router.put("/{registration_id}", response_model=Registration, status_code=200)
async def update_registration(registration_id: UUID, registration_data: RegistrationUpdate):
    updated_registration = await RegistrationService.update_registration(registration_id, registration_data)
    if updated_registration is None:
        raise HTTPException(status_code=404, detail="Registration not found")
    return updated_registration

@registration_router.post("/{registration_id}/attendance", response_model=Registration, status_code=200)
async def mark_attendance(registration_id: UUID):
    registration_attendance = await RegistrationService.mark_attendance(registration_id)
    if registration_attendance is None:
        raise HTTPException(status_code=404, detail="Registration not found")
    return registration_attendance

@registration_router.get("/user/{user_id}", response_model=List[Registration], status_code=200)
async def get_user_registrations(user_id: int):
    registrations = await RegistrationService.get_registrations_by_user(user_id)
    if not registrations:
        raise HTTPException(status_code=404, detail="No registrations found for this user")
    return registrations

@registration_router.get("/", response_model=List[Registration], status_code=200)
async def get_all_registrations():
    registrations = await RegistrationService.get_all_registrations()
    return registrations