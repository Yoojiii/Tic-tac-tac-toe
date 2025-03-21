from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine('sqlite+aiosqlite:///users.db')

new_session = async_sessionmaker(engine, expire_on_commit=False)
class Model(DeclarativeBase):
    pass
class UsersOrm(Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]

async def create_user_table():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_user_table():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)

