from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine("sqlite+aiosqlite:///games.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class GamesOrm(Model):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


async def create_game_table():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_game_table():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)