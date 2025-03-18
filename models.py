from pydantic import BaseModel, EmailStr, Field

class Login(BaseModel):
    nickname: str = Field(max_length=10)
    email: str
    password: str = Field(min_length=4)

