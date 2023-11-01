"""File that handles all functions speaking with the database"""

from os import environ

import pandas as pd
from dotenv import load_dotenv
from psycopg2 import connect
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection


def get_db_connection(config: dict) -> connection:
    """Returns connection to the db"""
    try:
        conn = connect(dbname=config["DBNAME"],
                       host=config["HOST"],
                       user=config["USER"])

    except (ConnectionAbortedError, ConnectionError, ConnectionRefusedError) as con_err:
        con_err("Error: Unable to establish connection to the database!")

    return conn


def get_user_id(conn: connection, user_name: str) -> int:
    """Returns the user_id"""

    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT user_id FROM example.api_user
    WHERE %s = user_name;""", [user_name])

    user_id = cur.fetchall()

    user_id = [x['user_id'] for x in user_id]

    if len(user_id) != 1:
        raise Exception(
            f"Error: Username '{user_name}' not found on system!")

    cur.close()

    return user_id[0]


if __name__ == "__main__":

    load_dotenv()

    config = environ

    conn = get_db_connection(config)

    user_id = get_user_id(conn, "example_user_1")

    print(user_id)

    conn.close()
