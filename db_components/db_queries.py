"""File that handles all functions speaking with the database"""

from os import environ

import pandas as pd
from pandas import DataFrame
from dotenv import load_dotenv
from psycopg2 import connect
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection


def get_db_connection(env_config: dict) -> connection:
    """Returns connection to the db"""
    try:
        db_conn = connect(dbname=env_config["DBNAME"],
                          host=env_config["HOST"],
                          user=env_config["USER"])

    except (ConnectionAbortedError, ConnectionError, ConnectionRefusedError) as con_err:
        con_err("Error: Unable to establish connection to the database!")

    return db_conn


def get_all_pokemon_names(db_conn: connection) -> list[str]:
    """Returns all pokemon_names from the db in a set"""

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute("""SELECT LOWER(pokemon_name) AS name
                FROM pokemon;""")
    except:
        raise Exception("Error: Error with connection/database query!")

    all_pokemon_names = cur.fetchall()
    cur.close()
    all_pokemon_names_df = pd.DataFrame(all_pokemon_names)

    return all_pokemon_names_df["name"].to_list()


def get_all_pokemon_types(db_conn: connection) -> list[str]:
    """Returns list of all pokemon types in the database"""

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute("""SELECT DISTINCT(LOWER(pokemon_type)) AS types
                FROM pokemon_types;""")

    except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError) as conn_err:
        raise conn_err("Error: Error with db connection!")

    all_pokemon_types = cur.fetchall()
    cur.close()
    all_pokemon_types_df = pd.DataFrame(all_pokemon_types)

    return all_pokemon_types_df["types"].to_list()


def get_all_pokemon_moves(db_conn: connection) -> list[str]:
    """Returns list of all pokemon moves in the database"""

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute("""SELECT DISTINCT(LOWER(move_name)) AS name
                FROM pokemon_move;""")

    except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError) as conn_err:
        raise conn_err("Error: Error with db connection!")

    all_pokemon_moves = cur.fetchall()
    cur.close()
    all_pokemon_moves_df = pd.DataFrame(all_pokemon_moves)

    return all_pokemon_moves_df["name"].to_list()


def get_all_pokemon(db_conn: connection) -> DataFrame:
    """Returns all pokemon from db"""

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT p.pokemon_id, p.pokemon_name,
                STRING_AGG (pt.pokemon_type, ', ') AS types,
                hp, attack, defense, speed, special_attack, special_defense, height, pokemon_weight AS weight
                FROM pokemon AS p
                JOIN pokemon_types AS pt 
                ON p.pokemon_id = pt.pokemon_id
                JOIN pokemon_stats AS ps
                ON p.pokemon_id = ps.pokemon_id
                GROUP BY p.pokemon_id,
                ps.hp, ps.attack, ps.defense, ps.speed, ps.special_attack, 
                ps.special_defense, ps.height, ps.pokemon_weight
                ORDER BY p.pokemon_name;""")

    all_pokemon_data = cur.fetchall()
    cur.close()
    all_pokemon_data_df = pd.DataFrame(all_pokemon_data)

    return pd.DataFrame(all_pokemon_data_df)


def get_specific_pokemon(db_conn: connection, pokemon_name: str) -> DataFrame:
    """Returns specified pokemon from db and displays
    pokemon, stats and types"""

    all_pokemon_names = get_all_pokemon_names(db_conn)

    if pokemon_name.capitalize() not in all_pokemon_names:
        raise ValueError("Error: Pokemon not in database!")

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT p.pokemon_id, pokemon_name AS name, 
                STRING_AGG(pokemon_type,  ', ') AS types,
                hp, attack, defense, speed, special_attack, special_defense, height, pokemon_weight AS weight
                FROM pokemon AS p
                JOIN pokemon_types AS pt
                ON p.pokemon_id = pt.pokemon_id
                JOIN pokemon_stats AS ps
                ON p.pokemon_id = ps.pokemon_id
                WHERE pokemon_name = %s
                GROUP BY p.pokemon_id,
                ps.hp, ps.attack, ps.defense, ps.speed, ps.special_attack, 
                ps.special_defense, ps.height, ps.pokemon_weight;""",
                [pokemon_name.capitalize()])

    specific_pokemon_data = cur.fetchall()
    cur.close()
    specific_pokemon_data_df = pd.DataFrame(specific_pokemon_data)

    return pd.DataFrame(specific_pokemon_data_df)


def get_specific_pokemon_moves(db_conn: connection, pokemon_name: str) -> DataFrame:
    """Returns all moves of a specific pokemon"""

    all_pokemon_names = get_all_pokemon_names(db_conn)

    if pokemon_name.lower() not in all_pokemon_names:
        raise ValueError("Error: Pokemon not in database!")

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT p.pokemon_id, pokemon_name AS name,
                pm.move_name, pm.accuracy, pm.power, pm.damage_class
                FROM pokemon AS p
                JOIN pokemon_move AS pm
                ON p.pokemon_id = pm.pokemon_id
                WHERE pokemon_name = %s;""",
                [pokemon_name.capitalize()])

    pokemon_data = cur.fetchall()

    return pd.DataFrame(pokemon_data)


def get_specific_pokemon_count(db_conn: connection, pokemon_name: str) -> DataFrame:
    """Return DF of the specified pokemon, including count of moves, abilities & types"""

    all_pokemon_names = get_all_pokemon_names(db_conn)

    if pokemon_name.lower() not in all_pokemon_names:
        raise ValueError("Error: Pokemon not in database!")

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute("""SELECT p.pokemon_name AS name,
            COUNT(DISTINCT pa.pokemon_ability_id) AS ability_count,
            COUNT(DISTINCT pt.pokemon_types_id) AS type_count,
            COUNT(DISTINCT pm.pokemon_move_id) AS move_count 
            FROM pokemon AS p
            INNER JOIN pokemon_ability AS pa ON p.pokemon_id = pa.pokemon_id
            INNER JOIN pokemon_types AS pt ON p.pokemon_id = pt.pokemon_id 
            INNER JOIN pokemon_move AS pm ON p.pokemon_id = pm.pokemon_id
            WHERE p.pokemon_name = %s
            GROUP BY p.pokemon_name;""",
                    [pokemon_name.capitalize()])

    except Exception as exc:
        raise exc("Error: Error with connection/database query!")

    pokemon_data = cur.fetchall()

    return pd.DataFrame(pokemon_data)


def get_all_pokemon_count(db_conn: connection) -> DataFrame:
    """Gets the count of all pokemon moves, abilities & types in the database"""

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute("""SELECT p.pokemon_name AS name,
            COUNT(DISTINCT pa.pokemon_ability_id) AS ability_count,
            COUNT(DISTINCT pt.pokemon_types_id) AS type_count,
            COUNT(DISTINCT pm.pokemon_move_id) AS move_count 
            FROM pokemon AS p
            INNER JOIN pokemon_ability AS pa ON p.pokemon_id = pa.pokemon_id
            INNER JOIN pokemon_types AS pt ON p.pokemon_id = pt.pokemon_id 
            INNER JOIN pokemon_move AS pm ON p.pokemon_id = pm.pokemon_id
            GROUP BY p.pokemon_name;""")

    except:
        raise Exception("Error: Error with connection/database query!")

    pokemon_ability_count_data = cur.fetchall()
    cur.close()
    pokemon_ability_count_data_df = pd.DataFrame(pokemon_ability_count_data)

    return pokemon_ability_count_data_df


def get_all_pokemon_move_names(db_conn: connection) -> DataFrame:
    """Returns list of all pokemon and name of all moves the pokemon has"""

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT p.pokemon_id, pokemon_name AS name, 
                STRING_AGG (move_name, ',') AS all_move_names
                FROM pokemon AS p
                JOIN pokemon_move AS pm
                ON pm.pokemon_id = p.pokemon_id
                GROUP BY p.pokemon_id
                ORDER BY p.pokemon_id;""")

    pokemon_data = cur.fetchall()
    cur.close()
    pokemon_data_df = pd.DataFrame(pokemon_data)

    return pokemon_data_df


def get_pokemon_by_move_name(db_conn: connection, pokemon_move: str) -> DataFrame:
    """Return data frame of pokemon that are associated with the move"""

    all_pokemon_moves = get_all_pokemon_moves(db_conn)

    if pokemon_move.lower() not in all_pokemon_moves:
        raise ValueError("Error: Pokemon move is not in the database!")

    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT p.pokemon_id, pokemon_name,
                STRING_AGG (move_name, ', ') AS move_list
                FROM pokemon AS p
                JOIN pokemon_move AS pm
                ON p.pokemon_id = pm.pokemon_id
                GROUP BY p.pokemon_id
                HAVING STRING_AGG (move_name, ', ') ILIKE %s
                ORDER BY p.pokemon_id;""",
                [f"%{pokemon_move.lower()}%"])

    pokemon_by_move = cur.fetchall()
    cur.close()
    pokemon_by_move_df = pd.DataFrame(pokemon_by_move)

    return pokemon_by_move_df


# TODO finish sql query
def get_pokemon_specific_types_count(db_conn: connection, pokemon_types_input: list[str]) -> DataFrame:
    """Returns the count of specified_types in the db"""

    all_pokemon_types = get_all_pokemon_types(db_conn)

    for p_type in pokemon_types_input:

        if p_type.lower() not in all_pokemon_types:

            raise ValueError(
                f"Error: {p_type.capitalize()} is not in the database!")

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute("""SELECT pokemon_type AS type,
                    COUNT(pokemon_type) AS count
                    FROM pokemon_types
                    WHERE pokemon_type IN (%s)
                    GROUP BY type;""",
                    [", ".join(pokemon_types_input)])

    except (ConnectionError, ConnectionRefusedError) as conn_err:
        conn_err("Error communicating with the database!")

    pokemon_data = cur.fetchall()

    return pd.DataFrame(pokemon_data)


def get_pokemon_by_type(db_conn: connection, pokemon_type: str) -> DataFrame:
    """Returns all pokemon of a specific type"""

    all_pokemon_types = get_all_pokemon_types(db_conn)

    if pokemon_type.lower() not in all_pokemon_types:
        raise ValueError("Error: Pokemon type not in database!!")

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT p.pokemon_id, pokemon_name,
                STRING_AGG (pokemon_type, ', ') AS pokemon_types
                FROM pokemon AS p
                JOIN pokemon_types AS pt
                ON p.pokemon_id = pt.pokemon_id
                GROUP BY p.pokemon_id
                HAVING STRING_AGG (pokemon_type, ', ') ILIKE %s;""",
                [f"%{pokemon_type.capitalize()}%"])

    pokemon_by_type = cur.fetchall()
    pokemon_by_type_df = pd.DataFrame(pokemon_by_type)

    return pokemon_by_type_df


# TODO version_group_control count
def specific_version_control_count(db_conn: connection, move_name: str) -> DataFrame:
    """Return version control for move specified"""

    all_move_names = get_all_pokemon_moves(conn)

    if move_name.lower() not in all_move_names:
        raise (ValueError("Error: Not found in db!"))

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT COUNT(*) 
                FROM pokemon_move AS pm
                LEFT JOIN pokemon_move_flavor_text AS pmft
                ON pm.pokemon_move_id = pmft.pokemon_move_id;""")

    data = cur.fetchall()

    cur.close()

    data_df = pd.DataFrame(data)
    # print(data["version_group"])
    return data_df


if __name__ == "__main__":

    load_dotenv()

    config = environ

    conn = get_db_connection(config)

    # An example section of code to see this worksp when run

    # -- This code works
    # all_pokemon_names = get_all_pokemon_names(conn)
    # all_pokemon_types = get_all_pokemon_types(conn)
    # all_pokemon_moves = get_all_pokemon_moves(conn)

    # print(get_all_pokemon(conn))
    # print(get_specific_pokemon(conn, 'Bulbasaur'))
    # print(get_specific_pokemon_count(conn, 'bulbasaur'))
    # print(get_all_pokemon_count(conn))
    # print(get_all_pokemon_move_names(conn))
    # print(get_pokemon_by_move_name(conn, "Double Slap"))

    # -- This code is testing
    print(get_pokemon_by_type(conn, "ghost"))
    # print(get_specific_pokemon_moves(conn, "bulbasaur"))
    # print(version_control_count(conn))

    # -- This code doesn't work
    # print(get_pokemon_by_type(conn, "ground"))
    # print(get_pokemon_moves(conn, "bulbasaur"))
    # pokemon_types_counts_df = get_pokemon_all_types_count(conn)
    # pokemon_types_in_db = set(pokemon_types_counts_df["type"].to_list())
    # print(get_pokemon_specific_types_count(
    #     conn, pokemon_types_in_db, ["rock", "fire"]))
    # print(get_all_pokemon_all_move_names(conn))
    # print(get_all_pokemon_counts(conn))
    # print(get_pokemon_all_move_count(conn))

    conn.close()
