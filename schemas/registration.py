from pydantic import BaseModel
from typing import Optional
from datetime import date
from uuid import UUID

class RegistrationBase(BaseModel):
    event_id: int
    user_id: int

class RegistrationCreate(RegistrationBase):
    pass

class RegistrationUpdate(RegistrationBase):
    event_id: Optional[int] = None
    user_id: Optional[int] = None
    registration_date: Optional[date] = None
    attended: Optional[bool] = None

class Registration(RegistrationBase):
    id: UUID
    registration_date: date
    attended: bool = False

    class Config:
        from_attributes = True