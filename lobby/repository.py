from .database import new_session, GamesOrm
from sqlalchemy import select
from .schemas import Game, GameAdd


class GamesRepository:
    @classmethod
    async def find_all(cls) -> list[Game]:
        async with new_session() as session:
            query = select(GamesOrm)
            result = await session.execute(query)
            games_models = result.scalars().all()
            games_schemas = [Game.from_orm(games_model) for games_model in games_models]
            return games_schemas

    @classmethod
    async def add_one(cls, data: GameAdd) -> int:
        async with new_session() as session:
            games_dict = data.model_dump()
            game = GamesOrm(**games_dict)
            session.add(game)
            await session.flush()
            await session.commit()
            return game.id
