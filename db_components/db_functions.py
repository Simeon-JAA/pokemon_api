"""File that handles all functions speaking with the database"""

from os import environ

from dotenv import load_dotenv
from psycopg2 import connect
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

    cur = conn.cursor()

    cur.close()

    return


if __name__ == "__main__":

    load_dotenv()

    config = environ

    conn = get_db_connection(config)

    conn.close()
