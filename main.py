from fastapi import FastAPI
from usecase.actor_uc import get_all, get_by_id, create, update, delete
from model.request.actor_req import ActorReq
from model.actor import Actor
from fastapi import Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# get all actors
@app.get("/actors")
def get_all_actors():
    return get_all()

# get actor by id
@app.get("/actors/{actor_id}")
def get_actor_by_id(actor_id: int):
    return get_by_id(actor_id)

# create actor
@app.post("/actors")
async def create_actor(request: Request):
    req = ActorReq(**await request.json())
    actor = Actor(first_name=req.first_name, last_name=req.last_name)
    return create(actor)

@app.put("/actors/{actor_id}")
async def update_actor(actor_id: int, request: Request):
    req = ActorReq(**await request.json())
    actor = Actor(actor_id=actor_id, first_name=req.first_name, last_name=req.last_name)
    return update(actor)

@app.delete("/actors/{actor_id}")
def delete_actor(actor_id: int):
    return delete(actor_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)