
from restaurant_core.domain.entities.restaurant.restaurant import Restaurant
from restaurant_core.domain.service.restaurant_service import RestaurantService
from .create_restaurant_command import CreateRestaurantCommand
from automapper import mapper

class CreateRestaurantCommandHandler:
    def __init__(self, restaurant_service: RestaurantService):
        self.restaurant_service = restaurant_service
    
    def handle(self, command: CreateRestaurantCommand):
        restaurant_entity: Restaurant = mapper.to(Restaurant).map(command)
        self.restaurant_service.create_restaurant(restaurant_entity)
        return restaurant_entity