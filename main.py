from fastapi import FastAPI, Depends
from typing import Annotated
from fastapi.responses import FileResponse
from models import Login

app = FastAPI()

@app.get("/login", tags=["Sign up"], response_class=FileResponse)
def sign_up_page():
    return FileResponse("login.html")


@app.get("/tic_tac")
def tic_tac():
    return FileResponse("tic_tac_tac_toe.html")

users = []

@app.post("/login", tags=["Sign up"])
async def set_data(login: Annotated[Login, Depends()]):
    users.append(login)
    #тут потом добавить чтобы шло в database
    return {"ok": True}

@app.get("/users")
async def get_users():
    return {"data": users}

