from schemas.user import UserCreate, UserUpdate, User
from database import users, registrations
from models import User as UserModel

class UserService:
    @staticmethod
    async def create_user(user_data: UserCreate):
        user_id = len(users) + 1
        user = UserModel(id=user_id, **user_data.model_dump())
        users.append(user)
        return user

    @staticmethod
    async def get_user_by_id(user_id: int):
        for user in users:
            if user.id == user_id:
                return user
        return None

    @staticmethod
    async def get_all_users():
        return users

    @staticmethod
    async def update_user(user_id: int, user_update: UserUpdate):
        for i, user in enumerate(users):
            if user.id == user_id:
                if user_update.name is not None:
                    user.name = user_update.name
                if user_update.email is not None:
                    user.email = user_update.email
                users[i] = user
                return user
        return None

    @staticmethod
    async def delete_user(user_id: int) -> bool:
        for i, user in enumerate(users):
            if user.id == user_id:
                users.pop(i)
                return True
        return False

    @staticmethod
    async def deactivate_user(user_id: int):
        for user in users:
            if user.id == user_id:
                user.is_active = False
                return user
        return None
    
    @staticmethod
    async def get_users_with_attendance() -> list[User]:
        attended_user_ids = []
        for registration in registrations:
            if registration.attended:
                attended_user_ids.append(registration.user_id)

        unique_attended_users = []
        seen_user_ids = set()
        for user in users:
            if user.id in attended_user_ids and user.id not in seen_user_ids:
                unique_attended_users.append(User(**user.__dict__))
                seen_user_ids.add(user.id)
        return unique_attended_users