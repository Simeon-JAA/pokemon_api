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


def get_all_pokemon(conn: connection) -> DataFrame:
    """Returns all pokemon from db"""

    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(f"""SELECT * FROM pokemon;""")

    all_pokemon_data = cur.fetchall()

    return pd.DataFrame(all_pokemon_data)


def get_specific_pokemon(conn: connection, pokemon: str) -> DataFrame:
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

    specific_pokemon_data = cur.fetchall()

    return pd.DataFrame(specific_pokemon_data)


def get_specified_pokemon_moves(conn: connection, pokemon: str) -> DataFrame:
    """Returns all moves of a specified pokemon"""

    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(f"""SELECT p.pokemon_id, pokemon_name AS name,
                pm.move_name, pm.accuracy, pm.power, pm.damage_class
                FROM pokemon AS p
                JOIN pokemon_move AS pm
                ON p.pokemon_id = pm.pokemon_id
                WHERE pokemon_name = %s;""",
                [pokemon.capitalize()])

    pokemon_data = cur.fetchall()

    return pd.DataFrame(pokemon_data)


def get_all_pokemon_counts(conn: connection) -> DataFrame:
    """Gets the count of all pokemon moves, abilities & types in the database"""

    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT p.pokemon_name AS name,
                COUNT(DISTINCT pa.pokemon_ability_id) AS ability_count,
                COUNT(DISTINCT pt.pokemon_types_id) AS type_count,
                COUNT(DISTINCT pm.pokemon_move_id) AS move_count 
                FROM pokemon AS p
                INNER JOIN pokemon_ability AS pa ON p.pokemon_id = pa.pokemon_id
                INNER JOIN pokemon_types AS pt ON p.pokemon_id = pt.pokemon_id 
                INNER JOIN pokemon_move AS pm ON p.pokemon_id = pm.pokemon_id
                GROUP BY p.pokemon_name;""")

    pokemon_ability_count_data = cur.fetchall()

    return pd.DataFrame(pokemon_ability_count_data)


# TODO finish sql query
def get_all_pokemon_all_move_names(conn: connection) -> DataFrame:
    """Returns list of all pokemon and all moves associated with that pokemon"""

    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute(f"""SELECT p.pokemon_id AS id, p.pokemon_name AS name,
                GROUP_CONCAT(pm.move_name SEPARATOR ',')
                FROM pokemon AS p
                JOIN pokemon_move AS pm
                ON pm.pokemon_id = p.pokemon_id
                WHERE pokemon_name = 'Squirtle'
                GROUP BY p.pokemon_name;""")

    pokemon_data = cur.fetchall()

    return pd.DataFrame(pokemon_data)


# TODO finish sql query
def get_pokemon_specific_types_count(conn: connection, pokemon_types_in_db: set[str], pokemon_types: list[str]) -> DataFrame:
    """Returns the count of specified_types in the db"""

    pokemon_types = list(map(
        lambda pokemon_type: pokemon_type.capitalize(), pokemon_types))

    for pokemon_type in pokemon_types:

        if pokemon_type not in pokemon_types_in_db:

            raise ValueError(
                f"Error: {pokemon_type.capitalize()} is not in the database!")

    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute(f"""SELECT pokemon_type AS type,
                    COUNT(pokemon_type) AS count
                    FROM pokemon_types
                    WHERE pokemon_type IN (%s)
                    GROUP BY type;""",
                    [", ".join(pokemon_types)])

    except (ConnectionError, ConnectionRefusedError) as conn_err:
        conn_err("Error communicating with the database!")

    pokemon_data = cur.fetchall()

    return pd.DataFrame(pokemon_data)


# TODO remove limit on SQL statement
def get_pokemon_by_type(conn: connection, pokemon_type: str) -> DataFrame:
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

    return pd.DataFrame(pokemon_data)


if __name__ == "__main__":

    load_dotenv()

    config = environ

    conn = get_db_connection(config)

    # An example section of code to see this works when run
    # print(get_all_pokemon(conn))
    # print(get_specific_pokemon(conn, "charmander"))
    # print(get_pokemon_by_type(conn, "ground"))
    # print(get_pokemon_moves(conn, "bulbasaur"))
    # pokemon_types_counts_df = get_pokemon_all_types_count(conn)
    # pokemon_types_in_db = set(pokemon_types_counts_df["type"].to_list())
    # print(get_pokemon_specific_types_count(
    #     conn, pokemon_types_in_db, ["rock", "fire"]))
    # print(get_all_pokemon_all_move_names(conn))
    print(get_all_pokemon_counts(conn))
    print(get_pokemon_all_move_count(conn))

    conn.close()
