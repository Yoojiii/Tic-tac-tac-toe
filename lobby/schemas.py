from pydantic import BaseModel, Field

class GameAdd(BaseModel):
    name: str = Field(max_length=20)

class Game(GameAdd):
    id: int

    class Config:
        from_attributes = True
