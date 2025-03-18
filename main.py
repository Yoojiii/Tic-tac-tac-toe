from fastapi import FastAPI
from database  import create_table, delete_table
from contextlib import asynccontextmanager
from router import router as user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_table()
    print("Base is clean up")
    await create_table()
    print("Base is ready")
    yield
    print("Off")

app = FastAPI(lifespan=lifespan)
app.include_router(user_router)

