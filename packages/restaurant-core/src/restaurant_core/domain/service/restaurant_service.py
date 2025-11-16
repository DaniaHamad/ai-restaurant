from typing import List
from restaurant_core.domain.entities.restaurant.restaurant import Restaurant
from restaurant_core.infrastructure.repository.irestaurant_repository import IRestaurantRepository


class RestaurantService:
    def __init__(self, repository: IRestaurantRepository):
        self.repository = repository
    
    def get_restaurants(self) -> List[Restaurant]:
        return self.repository.get_list()
    
    def create_restaurant(self, restaurant_entity: Restaurant):
        self.repository.add(restaurant_entity)