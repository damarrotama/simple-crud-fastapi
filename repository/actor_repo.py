# repository for actor
from typing import List
from config.db import connect
from model.actor import Actor

def get_all() -> List[Actor]:
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM actor")
    rows = cur.fetchall()
    actors = []
    for row in rows:
        actor = Actor(actor_id=row[0], first_name=row[1], last_name=row[2])
        actors.append(actor)
    cur.close()
    conn.close()
    return actors

def get_by_id(actor_id: int) -> Actor:
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM actor WHERE actor_id = %s", (actor_id,))
    row = cur.fetchone()

    if row is None:
        return "Actor not found"

    actor = Actor(actor_id=row[0], first_name=row[1], last_name=row[2])
    cur.close()
    conn.close()
    return actor

def create(actor: Actor) -> Actor:
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO actor (first_name, last_name) VALUES (%s, %s) RETURNING actor_id", (actor.first_name, actor.last_name))
    actor_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return get_by_id(actor_id)

def update(actor: Actor) -> Actor:
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE actor SET first_name = %s, last_name = %s WHERE actor_id = %s", (actor.first_name, actor.last_name, actor.actor_id))
    conn.commit()
    cur.close()
    conn.close()
    return get_by_id(actor.actor_id)

def delete(actor_id: int) -> str:
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM actor WHERE actor_id = %s", (actor_id,))
    conn.commit()
    cur.close()
    conn.close()
    return "Actor deleted"