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


def get_all_pokemon(conn: connection) -> dict:
    """Returns all pokemon from db"""

    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(f"""SELECT * FROM pokemon;""")

    all_pokemon_data = cur.fetchall()

    print(pd.DataFrame(all_pokemon_data))


def get_specific_pokemon(conn: connection, pokemon: str) -> dict:
    """Returns specified pokemon from db and displays
    pokemon, stats and types"""

    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(f"""SELECT p.pokemon_id, pokemon_name AS name, pokemon_type AS type,
                hp, attack, defense, speed, special_attack, special_defense, height, pokemon_weight AS weight 
                FROM pokemon AS p 
                JOIN pokemon_types AS pt
                ON p.pokemon_id = pt.pokemon_id
                JOIN pokemon_stats AS ps 
                ON p.pokemon_id = ps.pokemon_id
                WHERE pokemon_name = %s;""",
                [pokemon.capitalize()])

    pokemon_data = cur.fetchall()

    print(pd.DataFrame(pokemon_data))


def get_pokemon_moves(conn: connection, pokemon: str) -> dict:
    """Returns all moves of a pokemon"""

    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(f"""SELECT p.pokemon_id, pokemon_name AS name,
                pm.move_name, pm.accuracy, pm.power, pm.damage_class
                FROM pokemon AS p
                JOIN pokemon_move AS pm
                ON p.pokemon_id = pm.pokemon_id
                WHERE pokemon_name = %s;""",
                [pokemon.capitalize()])

    pokemon_data = cur.fetchall()

    print(pd.DataFrame(pokemon_data))


# TODO remove limit on SQL statement
def get_pokemon_by_type(conn: connection, pokemon_type: str) -> dict:
    """Returns all pokemon of a specified type"""

    allowed_types = {"grass", "ground"}

    if pokemon_type.lower() not in allowed_types:
        raise ValueError("Error: Pokemon type not recognised!")

    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(f"""SELECT p.pokemon_id, pokemon_name, pokemon_type
                FROM pokemon AS p
                JOIN pokemon_types AS pt
                ON p.pokemon_id = pt.pokemon_id
                WHERE pokemon_type = %s
                LIMIT 10;""",
                [pokemon_type.capitalize()])

    pokemon_data = cur.fetchall()

    print(pd.DataFrame(pokemon_data))


if __name__ == "__main__":

    load_dotenv()

    config = environ

    conn = get_db_connection(config)

    get_all_pokemon(conn)
    get_specific_pokemon(conn, "charmander")
    get_pokemon_by_type(conn, "ground")
    get_pokemon_moves(conn, "bulbasaur")

    conn.close()
