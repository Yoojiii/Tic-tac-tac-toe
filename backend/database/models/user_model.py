from database.models.base_model import ModelBase
from sqlalchemy.orm import Mapped, mapped_column

class UserOrm(ModelBase):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]