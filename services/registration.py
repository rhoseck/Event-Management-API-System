from schemas.registration import RegistrationCreate, Registration, RegistrationUpdate
from database import registrations, events, users
from models import Registration as RegistrationModel
from datetime import datetime
from uuid import UUID, uuid4

class RegistrationService:
    @staticmethod
    async def register_user(registration_data: RegistrationCreate) -> Registration:
        user_id = registration_data.user_id
        event_id = registration_data.event_id

        user = None
        for u in users:
            if u.id == user_id and u.is_active:
                user = u
                break
        if not user:
            return None

        event = None
        for e in events:
            if e.id == event_id and e.is_open:
                event = e
                break
        if not event:
            return None

        for r in registrations:
            if r.user_id == user_id and r.event_id == event_id:
                return None

        new_registration_id = uuid4()
        new_registration = RegistrationModel(
            id=new_registration_id,
            user_id=user_id,
            event_id=event_id,
            registration_date=datetime.now().date(),
            attended=False
        )
        registrations.append(new_registration)
        return Registration(**new_registration.__dict__)

    @staticmethod
    async def update_registration(registration_id: UUID, registration_update: RegistrationUpdate) -> Registration | None:
        for i, registration in enumerate(registrations):
            if registration.id == registration_id:
                if registration_update.event_id is not None:
                    registration.event_id = registration_update.event_id
                if registration_update.user_id is not None:
                    registration.user_id = registration_update.user_id
                if registration_update.registration_date is not None:
                    registration.registration_date = registration_update.registration_date
                if registration_update.attended is not None:
                    registration.attended = registration_update.attended
                registrations[i] = registration
                return Registration(**registration.__dict__)
        return None

    @staticmethod
    async def mark_attendance(registration_id: UUID) -> Registration:
        for registration in registrations:
            if registration.id == registration_id:
                registration.attended = True
                return Registration(**registration.__dict__)
        return None

    @staticmethod
    async def get_registrations_by_user(user_id: int) -> list[Registration]:
        user_registrations = []
        for registration in registrations:
            if registration.user_id == user_id:
                user_registrations.append(Registration(**registration.__dict__))
        return user_registrations

    @staticmethod
    async def get_all_registrations() -> list[Registration]:
        all_registrations = []
        for registration in registrations:
            all_registrations.append(Registration(**registration.__dict__))
        return all_registrations