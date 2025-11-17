
from restaurant_core.domain.service.restaurant_service import RestaurantService
from .get_restaurants_query import GetRestaurantsQuery

class GetRestaurantsQueryHandler:
    def __init__(self, restaurant_service: RestaurantService):
        self.restaurant_service = restaurant_service

    def handle(self, query: GetRestaurantsQuery):
        return self.restaurant_service.get_restaurants()

