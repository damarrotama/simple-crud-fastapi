# craete json data for actor request

from pydantic import BaseModel

class ActorReq(BaseModel):
    first_name: str
    last_name: str
