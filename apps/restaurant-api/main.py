from fastapi import FastAPI
from restaurant_core.datetime_lib import get_utc_timestamp
from restaurant_core.domain.service.restaurant_service import RestaurantService
from restaurant_core.infrastructure.presistence.session import Session
from restaurant_core.infrastructure.repository.restaurant_repository import RestaurantRepository
from .queries.restaurant_queries.get_resturants_query_handler import GetRestaurantsQueryHandler
from .queries.restaurant_queries.get_restaurants_query import GetRestaurantsQuery
from .commands.restaurant_commands.create_restaurant_command import CreateRestaurantCommand
from .commands.restaurant_commands.create_restaurant_command_handler import CreateRestaurantCommandHandler
from automapper import mapper
from .dtos.restaurant_dto import RestaurantDTO

app = FastAPI()


@app.get("/")
async def root():
    return {"timestamp": get_utc_timestamp()}

@app.get("/restaurants/")
def get_restaurants():
    db_session = Session()
    repo = RestaurantRepository(db_session)

    service = RestaurantService(repo)
    handler = GetRestaurantsQueryHandler(service)

    query = GetRestaurantsQuery()

    return handler.handle(query)

@app.post("/restaurants/")
def create_restaurant(command: CreateRestaurantCommand):
    db_session = Session()
    repo = RestaurantRepository(db_session)

    service = RestaurantService(repo)
    handler = CreateRestaurantCommandHandler(service)
    
    restaurant = handler.handle(command)
    return mapper.to(RestaurantDTO).map(restaurant)

