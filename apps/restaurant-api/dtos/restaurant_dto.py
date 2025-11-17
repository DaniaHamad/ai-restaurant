from uuid import UUID
from pydantic import BaseModel

class RestaurantDTO(BaseModel):
    id: UUID
    name: str
    location: str
    cuisine: str
