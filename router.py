from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from schemas import UserAdd, User, UserAuthx
from repository import UsersRepository
router = APIRouter(tags=["Users"])

@router.post("/users/add")
async def user_add(user: Annotated[UserAdd, Depends()]):
    if await UsersRepository.add_one(user) >= 0:
        return {"ok": True}
    raise HTTPException(status_code=409, detail="Identical email!")
@router.get("/users/find_all")
async def user_find_all() -> list[User]:
    users = await UsersRepository.find_all()
    return users

@router.get("/users/authx")
async def user_authx(user: Annotated[UserAuthx, Depends()]):
    if await UsersRepository.authx(user):
        return {"ok": "Successful sign in!"}
    raise HTTPException(status_code=409, detail="User isn't exists!")