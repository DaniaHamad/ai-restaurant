from abc import ABC, abstractmethod
from typing import List
from restaurant_core.domain.entities.restaurant.restaurant import Restaurant


class IRestaurantRepository (ABC):
    @abstractmethod
    def add(self, restaurant : Restaurant) -> None:
        pass

    @abstractmethod
    def get_list(self) -> List [Restaurant]:
        pass