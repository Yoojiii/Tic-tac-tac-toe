from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from schemas import UserAdd, User
from repository import UsersRepository
router = APIRouter(tags=["Users"])

@router.post("/users/add")
async def user_add(user: Annotated[UserAdd, Depends()]):
    if await UsersRepository.add_one(user) >= 0:
        return {"ok": True}
    raise HTTPException(status_code=401, detail="Identical email!")
@router.get("/users/find_all")
async def user_find_all() -> list[User]:
    users = await UsersRepository.find_all()
    return users


