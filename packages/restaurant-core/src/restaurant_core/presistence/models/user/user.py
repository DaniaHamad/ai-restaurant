from restaurant_core.presistence.models.base_table import BaseTable
from sqlalchemy import Column, String


class User(BaseTable):
    __tablename__ = "users"
    
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
