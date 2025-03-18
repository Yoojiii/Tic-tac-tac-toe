from sqlalchemy import select
from schemas import User, UserAdd
from database import new_session, UsersOrm

class UsersRepository:
    @classmethod
    async def add_one(cls, data: UserAdd) -> int:
        async with new_session() as session:
            user_dict = data.model_dump()
            user = UsersOrm(**user_dict)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id
    @classmethod
    async def find_all(cls) -> list[User]:
        async with new_session() as session:
            query = select(UsersOrm)
            result = await session.execute(query)
            users_models = result.scalars().all()
            users_schemas = [User.from_orm(users_model) for users_model in users_models]
            return users_schemas
