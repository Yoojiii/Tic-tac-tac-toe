from fastapi import FastAPI
from registration.database import create_user_table, delete_user_table
from lobby.database import create_game_table, delete_game_table
from contextlib import asynccontextmanager
from registration.router import router as user_router
from lobby.router import router as lobby_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_user_table()
    print("User database is clean up")
    await create_user_table()
    print("User database is ready")

    await delete_game_table()
    print("Games database is clean up")
    await create_game_table()
    print("Games database is ready")
    yield
    print("Off")

app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
app.include_router(lobby_router)

