
from typing import List
from restaurant_core.domain.entities.restaurant.restaurant import Restaurant
from restaurant_core.infrastructure.repository.irestaurant_repository import IRestaurantRepository
from sqlalchemy.orm import Session


class RestaurantRepository (IRestaurantRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, restaurant : Restaurant) -> None:
        self.session.add(restaurant)
        self.session.commit()
    
    def get_list(self) -> List [Restaurant]:
        return self.session.query(Restaurant).all()