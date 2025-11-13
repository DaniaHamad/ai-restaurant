from restaurant_core.domain.entities.base_table import BaseTable
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Restaurant(BaseTable):
    __tablename__ = "restaurants"

    name: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)
    cuisine: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)



