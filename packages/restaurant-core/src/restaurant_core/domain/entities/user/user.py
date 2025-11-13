from restaurant_core.domain.entities.base_table import BaseTable
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(BaseTable):
    __tablename__ = "users"
    
    full_name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)
