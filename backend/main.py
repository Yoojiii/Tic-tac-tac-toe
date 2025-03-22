from fastapi import FastAPI
from database.models.base_model import create_tables, delete_tables
from contextlib import asynccontextmanager
from api.router import router as user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Base is clean up")
    await create_tables()
    print("Base is ready")
    yield
    print("Off")

app = FastAPI(lifespan=lifespan)
app.include_router(user_router)

