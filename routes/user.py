from fastapi import APIRouter, HTTPException
from schemas.user import User, UserCreate, UserUpdate
from services.user import UserService
from typing import List

user_router = APIRouter()

@user_router.post("/", response_model=User, status_code=201)
async def create_user(user_data: UserCreate):
    return await UserService.create_user(user_data)

@user_router.get("/{user_id}", response_model=User, status_code=200)
async def get_user(user_id: int):
    user = await UserService.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.get("/", response_model=list[User], status_code=200)
async def get_all_users():
    return await UserService.get_all_users()

@user_router.put("/{user_id}", response_model=User, status_code=200)
async def update_user(user_id: int, user_data: UserUpdate):
    user = await UserService.update_user(user_id, user_data)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@user_router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int):
    success = await UserService.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Successfully deleted"}

@user_router.post("/{user_id}/deactivate", status_code=200)
async def deactivate_user(user_id: int):
    user = await UserService.deactivate_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "successfully deactivated"}

@user_router.get("/attendance/events", response_model=List[User], status_code=200)
async def get_users_with_attendance():
    users_with_attendance = await UserService.get_users_with_attendance()
    if not users_with_attendance:
        raise HTTPException(status_code=404, detail="No users with attendance found")
    return users_with_attendance

