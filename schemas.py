from pydantic import BaseModel, EmailStr, Field

class UserAdd(BaseModel):
    nickname: str = Field(max_length=20)
    password: str = Field(min_length=4)
    email: EmailStr
class User(UserAdd):
    id: int
    class Config:
        #orm_mode = True
        from_attributes = True

