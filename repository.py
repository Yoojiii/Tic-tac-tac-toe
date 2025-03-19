from sqlalchemy import select
from schemas import User, UserAdd, UserAuthx
from database import new_session, UsersOrm
from pydantic import EmailStr

class UsersRepository:
    @classmethod
    async def find_all(cls) -> list[User]:
        async with new_session() as session:
            query = select(UsersOrm)
            result = await session.execute(query)
            users_models = result.scalars().all()
            users_schemas = [User.from_orm(users_model) for users_model in users_models]
            return users_schemas

    @classmethod
    async def is_uniq(cls, email: EmailStr) -> bool:
        async with new_session() as session:
            query = select(UsersOrm).filter(UsersOrm.email == email)
            result = await session.execute(query)
            user_model = result.scalars().first()
            return user_model is None

    @classmethod
    async def add_one(cls, data: UserAdd) -> int:
        if await UsersRepository.is_uniq(data.email):
            async with new_session() as session:
                user_dict = data.model_dump()
                user = UsersOrm(**user_dict)
                session.add(user)
                await session.flush()
                await session.commit()
                return user.id
        return -1

    @classmethod
    async def authx(cls, data: UserAuthx) -> bool:
        async with new_session() as session:
            query = select(UsersOrm).filter(UsersOrm.email == data.email, UsersOrm.password == data.password)
            result = await session.execute(query)
            user_model = result.scalars().first()
            return user_model is not None