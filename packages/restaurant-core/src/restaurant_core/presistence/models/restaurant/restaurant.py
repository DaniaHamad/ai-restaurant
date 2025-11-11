from restaurant_core.presistence.models.base_table import BaseTable
from sqlalchemy import Column, String


class Restaurant(BaseTable):
    __tablename__ = "restaurants"

    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    cuisine = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    


