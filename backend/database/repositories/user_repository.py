from sqlalchemy import select
from database.schemas.user_schema import UserBaseSchema, UserSchema, UserIdSchema
from database.models.user_model import UserOrm
from database.models.base_model import new_session
from pydantic import EmailStr
from config.authx_ import security, conf
from fastapi import Response

class UsersRepository:
    @classmethod
    async def find_all(cls) -> list[UserIdSchema]:
        async with new_session() as session:
            query = select(UserOrm)
            result = await session.execute(query)
            users_models = result.scalars().all()
            users_schemas = [UserIdSchema.from_orm(users_model) for users_model in users_models]
            return users_schemas

    @classmethod
    async def is_uniq(cls, email: EmailStr) -> bool:
        async with new_session() as session:
            query = select(UserOrm).filter(UserOrm.email == email)
            result = await session.execute(query)
            user_model = result.scalars().first()
            return user_model is None

    @classmethod
    async def add_one(cls, data: UserSchema, response: Response) -> int:
        if await UsersRepository.is_uniq(data.email):
            async with new_session() as session:
                user_dict = data.model_dump()
                user = UserOrm(**user_dict)
                session.add(user)
                await session.flush()
                await session.commit()
                token = security.create_access_token(uid=str(user.id))
                response.set_cookie(conf.JWT_ACCESS_COOKIE_NAME, token)
                return user.id
        return -1

    @classmethod
    async def authx(cls, data: UserBaseSchema) -> bool:
        async with new_session() as session:
            query = select(UserOrm).filter(UserOrm.email == data.email, UserOrm.password == data.password)
            result = await session.execute(query)
            user_model = result.scalars().first()
            return user_model is not None