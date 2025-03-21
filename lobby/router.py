from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from .schemas import GameAdd
from .repository import GamesRepository

router = APIRouter(tags=["Lobby"])

@router.get("/lobby/games")
async def games_find_all():
    all_games = await GamesRepository.find_all()
    return all_games

@router.post("/lobby/games/add")
async def game_add(game: Annotated[GameAdd, Depends()]):
    if await GamesRepository.add_one(game) >= 0:
        return {"ok": True}
    raise HTTPException(status_code=401, detail="Create game error")

