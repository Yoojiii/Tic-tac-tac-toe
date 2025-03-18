from typing import Annotated
from fastapi import APIRouter, Depends
from schemas import UserAdd, User
from repository import UsersRepository
router = APIRouter(tags=["Users"])

@router.post("/users/add")
async def user_add(user: Annotated[UserAdd, Depends()]):
    await UsersRepository.add_one(user)
    return {"ok": True}

@router.get("/users/find_all")
async def user_find_all() -> list[User]:
    users = await UsersRepository.find_all()
    return users

