from pydantic import BaseModel, EmailStr, Field
class UserBaseSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=4)

class UserSchema(UserBaseSchema):
    nickname: str = Field(max_length=20)

class UserIdSchema(UserSchema):
    id: int
    class Config:
        from_attributes = True
