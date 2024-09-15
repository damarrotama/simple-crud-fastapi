# usecase for actor
from typing import List
from model.actor import Actor
from repository.actor_repo import get_all as get_all_actors
from repository.actor_repo import get_by_id as get_actor_by_id
from repository.actor_repo import create as create_actor
from repository.actor_repo import update as update_actor
from repository.actor_repo import delete as delete_actor

def get_all() -> List[Actor]:
    return get_all_actors()

def get_by_id(actor_id: int) -> Actor:
    return get_actor_by_id(actor_id)

def create(actor: Actor) -> Actor:
    return  create_actor(actor)

def update(actor: Actor) -> Actor:
    return update_actor(actor)

def delete(actor_id: int) -> str:
    return delete_actor(actor_id)

