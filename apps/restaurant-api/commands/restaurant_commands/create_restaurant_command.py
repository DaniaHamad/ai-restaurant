from pydantic import BaseModel

class CreateRestaurantCommand(BaseModel):
    name : str 
    location: str
    phone_number: str
    cuisine: str