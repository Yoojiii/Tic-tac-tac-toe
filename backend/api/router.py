from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Response, Cookie
from database.schemas.user_schema import UserBaseSchema, UserSchema, UserIdSchema
from database.repositories.user_repository import UsersRepository
from config.authx_ import security
from authx import RequestToken

router = APIRouter(tags=["Users"])

@router.post("/users/add")
async def user_add(user: Annotated[UserSchema, Depends()], response: Response):
    if await UsersRepository.add_one(user, response) >= 0:
        return {"ok": True}
    raise HTTPException(status_code=409, detail="Identical email!")
@router.get("/users/find_all")
async def user_find_all() -> list[UserIdSchema]:
    users = await UsersRepository.find_all()
    return users

@router.get("/users/authx")
async def user_authx(user: Annotated[UserBaseSchema, Depends()]):
    if await UsersRepository.authx(user):
        return {"ok": "Successful sign in!"}
    raise HTTPException(status_code=409, detail="User isn't exists!")


@router.get("/protected", dependencies=[Depends(security.get_token_from_request)])
def protected(token: RequestToken = Depends()):
    try:
        security.verify_token(token=token)
        return {"data": "top secret info"}
    except Exception as e:
        raise HTTPException(401,detail={"message":str(e)}) from e