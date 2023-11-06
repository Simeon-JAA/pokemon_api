"""Handles all functions loading data into database"""

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


def insert_stats_into_table(conn: connection, pokemon_data: dict) -> None:
    """Inserts pokemon stat data into the database"""

    stats = pokemon_data["stats"]

    try:
        cur = conn.cursor()

        cur.execute("""INSERT INTO
                    health, attack, defense, special_attack, 
                    special_defense, speed, height, weight
                    VALUES 
                    (%s, %s, %s, %s, %s, %s, %s, %s);""",
                    [stats["health"], stats["attack"], stats["defense"],
                     stats["special-attack"], stats["special-defense"], stats["speed"],
                     stats["height"], stats["weight"]])

        conn.commit()

    except (ConnectionError, ConnectionAbortedError) as conn_err:
        conn_err("Error: Unable to successfully input data into database!")

    cur.close()

    return


if __name__ == "__main__":

    load_dotenv()

    config = environ

    conn = get_db_connection(config)

    conn.close()
