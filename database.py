from models import User, Event, Speaker, Registration
from uuid import uuid4

users: list[User] = []
events: list[Event] = []
registrations: list[Registration] = []
speakers: list[Speaker] = [
    Speaker(id=uuid4(), name="Dr. Smith", topic="Acute Pulmonary Edema"),
    Speaker(id=uuid4(), name="Prof. Jones", topic="Acute Kidney Injury"),
    Speaker(id=uuid4(), name="Ms. Lee", topic="Web Development")
]
