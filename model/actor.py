# create model actor
from pydantic import BaseModel

class Actor(BaseModel):
    actor_id: int = None
    first_name: str
    last_name: str