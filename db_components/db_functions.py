"""File that handles all functions speaking with the database"""

from os import environ

import pandas as pd
from pandas import DataFrame

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
                WHERE user_name = %s;""", [user_name])

    user_id = cur.fetchall()

    user_id = [x['user_id'] for x in user_id]

    if len(user_id) != 1:
        raise Exception(
            f"Error: Username '{user_name}' not found on system!")

    cur.close()

    return user_id[0]


def get_all_user_pokemon(conn: connection, user_id: int) -> DataFrame:
    """Returns all the pokemon associated with that user """

    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT * FROM example.user_pokemon
                WHERE user_id = %s;""", [user_id])

    all_user_pokemon = cur.fetchall()

    all_user_pokemon_df = pd.DataFrame(all_user_pokemon)

    cur.close()

    return all_user_pokemon_df


def get_current_team(conn: connection, user_id: int) -> DataFrame:
    """Returns all the pokemon associated with that user that is in their current team"""

    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT * FROM example.user_pokemon
                WHERE user_id = %s
                AND in_current_team = True;""", [user_id])

    all_user_pokemon = cur.fetchall()

    all_user_pokemon_df = pd.DataFrame(all_user_pokemon)

    cur.close()

    return all_user_pokemon_df


def get_specified_user_pokemon_stats(conn: connection, user_id: int, pokemon_name: str) -> DataFrame:
    """Returns the stats of a specified pokemon under the users_id"""

    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT pokemon_id, pokemon_name, pokemon_type, attack,
                defense, health, pokemon_height, pokemon_weight
                FROM example.pokemon_stats AS eps
                RIGHT JOIN example.user_pokemon AS eup
                ON eps.pokemon_id = eup.user_pokemon_id
                WHERE eup.user_id = %s
                AND eup.pokemon_name = %s;""",
                [user_id, pokemon_name.lower()])

    pokemon_stats = cur.fetchall()

    if len(pokemon_stats) == 0:
        raise ValueError(
            f"Error: {pokemon_name.capitalize()} is not in the user's roster!")

    pokemon_stats_df = pd.DataFrame(pokemon_stats)

    cur.close()

    return pokemon_stats_df


if __name__ == "__main__":

    load_dotenv()

    config = environ

    conn = get_db_connection(config)

    user_id = get_user_id(conn, "example_user_2")

    print(get_all_user_pokemon(conn, user_id))
    print(get_current_team(conn, user_id))
    print(get_specified_user_pokemon_stats(conn, user_id, 'pikachu'))

    conn.close()
