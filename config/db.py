# create connection to database postgresql

import psycopg2

def connect():
    conn = psycopg2.connect(
        host="",
        port="",
        database="",
        user="",
        password=""
    )
    return conn