from pydantic import BaseModel, EmailStr, Field
class UserAuthx(BaseModel):
    email: EmailStr
    password: str = Field(min_length=4)

class UserAdd(UserAuthx):
    nickname: str = Field(max_length=20)

class User(UserAdd):
    id: int
    class Config:
        from_attributes = True

