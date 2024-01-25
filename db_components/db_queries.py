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


def get_all_pokemon_abilities(db_conn: connection) -> list[str]:
    """Returns list of all pokemon abilities in the database"""

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute("""SELECT DISTINCT(LOWER(ability_name)) AS ability_name
                FROM pokemon_ability;""")

    except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError) as conn_err:
        raise conn_err("Error: Error with db connection!")

    all_pokemon_abilities = cur.fetchall()
    cur.close()
    all_pokemon_abilities_df = pd.DataFrame(all_pokemon_abilities)

    return all_pokemon_abilities_df["ability_name"].to_list()


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
                STRING_AGG (move_name, ', ') AS all_move_names
                FROM pokemon AS p
                JOIN pokemon_move AS pm
                ON pm.pokemon_id = p.pokemon_id
                GROUP BY p.pokemon_id
                ORDER BY p.pokemon_id;""")

    pokemon_data = cur.fetchall()
    cur.close()
    pokemon_data_df = pd.DataFrame(pokemon_data)

    return pokemon_data_df


def get_pokemon_by_single_move_name(db_conn: connection, pokemon_move: str) -> DataFrame:
    """Return data frame of pokemon that are associated with the move"""

    all_pokemon_moves = get_all_pokemon_moves(db_conn)
    pokemon_move = pokemon_move.lower().strip()

    if pokemon_move not in all_pokemon_moves:
        raise ValueError(
            f"Error: Pokemon move ({pokemon_move.title()}) is not in the database!")

    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT p.pokemon_id, pokemon_name,
                STRING_AGG (move_name, ', ' ORDER BY move_name) AS move_list
                FROM pokemon AS p
                JOIN pokemon_move AS pm
                ON p.pokemon_id = pm.pokemon_id
                GROUP BY p.pokemon_id
                HAVING STRING_AGG (move_name, ', ' ORDER BY move_name) ILIKE %s
                ORDER BY p.pokemon_id;""",
                [f"%{pokemon_move.title()}%"])

    pokemon_by_move = cur.fetchall()
    cur.close()
    pokemon_by_move_df = pd.DataFrame(pokemon_by_move)

    return pokemon_by_move_df


def get_pokemon_by_multiple_move_names(db_conn: connection, pokemon_moves: list[str]) -> DataFrame:
    """Return data frame of pokemon that are associated with the move"""

    all_pokemon_moves = get_all_pokemon_moves(db_conn)

    for p_move in pokemon_moves:

        if not isinstance(p_move, str):
            raise TypeError(f"Error: {p_move} should be a string!")

        if p_move.lower().strip() not in all_pokemon_moves:
            raise ValueError(
                f"Error: {p_move.capitalize()} not in database!")

    pokemon_moves.sort()
    pokemon_moves = list(
        map(lambda p_move: p_move.lower().strip(), pokemon_moves))

    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT p.pokemon_id, pokemon_name,
            STRING_AGG (move_name, ', ' ORDER BY move_name) AS move_list
            FROM pokemon AS p
            JOIN pokemon_move AS pm
            ON p.pokemon_id = pm.pokemon_id
            GROUP BY p.pokemon_id
            HAVING STRING_TO_ARRAY(STRING_AGG (LOWER(move_name), ', '), ', ') @> %s
            ORDER BY p.pokemon_id;""", [pokemon_moves])

    pokemon_by_moves = cur.fetchall()
    cur.close()
    pokemon_by_moves_df = pd.DataFrame(pokemon_by_moves)

    return pokemon_by_moves_df


def get_pokemon_by_single_type(db_conn: connection, pokemon_type: str) -> DataFrame:
    """Returns all pokemon of a specific type"""

    all_pokemon_types = get_all_pokemon_types(db_conn)
    pokemon_type = pokemon_type.lower().strip()

    if pokemon_type not in all_pokemon_types:
        raise ValueError(
            f"Error: Pokemon type ({pokemon_type.capitalize()}) not in database!")

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT p.pokemon_id, pokemon_name,
                STRING_AGG (pokemon_type, ', ' ORDER BY pokemon_type) AS pokemon_types
                FROM pokemon AS p
                JOIN pokemon_types AS pt
                ON p.pokemon_id = pt.pokemon_id
                GROUP BY p.pokemon_id
                HAVING STRING_AGG (pokemon_type, ', ' ORDER BY pokemon_type) ILIKE %s;""",
                [f"%{pokemon_type.title()}%"])

    pokemon_by_type = cur.fetchall()
    pokemon_by_type_df = pd.DataFrame(pokemon_by_type)

    return pokemon_by_type_df


def get_pokemon_by_multiple_types(db_conn: connection, pokemon_types: list[str]) -> DataFrame:
    """Returns all pokemon of multiple specified types"""

    all_pokemon_types = get_all_pokemon_types(db_conn)

    for p_type in pokemon_types:

        if not isinstance(p_type, str):
            raise TypeError(f"Error: {p_type} should be of a string type!")

        if p_type.lower().strip() not in all_pokemon_types:
            raise ValueError(
                f"Error: Pokemon type ({p_type}) not in database!")

    pokemon_types.sort()
    pokemon_types = list(
        map(lambda p_type: p_type.lower().strip(), pokemon_types))

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT p.pokemon_id, pokemon_name,
                STRING_AGG(pokemon_type, ', ' ORDER BY pokemon_type) AS pokemon_types
                FROM pokemon AS p
                JOIN pokemon_types AS pt
                ON p.pokemon_id = pt.pokemon_id
                GROUP BY p.pokemon_id
                HAVING STRING_TO_ARRAY(STRING_AGG (LOWER(pokemon_type), ', '), ', ') @> %s;""",
                [pokemon_types])

    pokemon_by_types = cur.fetchall()

    pokemon_by_types_df = pd.DataFrame(pokemon_by_types)

    return pokemon_by_types_df


def get_pokemon_by_single_ability(db_conn: connection, pokemon_ability: str) -> DataFrame:
    """Returns all pokemon that have listed ability in their roster"""

    all_pokemon_abilities = get_all_pokemon_abilities(db_conn)
    pokemon_ability = pokemon_ability.lower().strip()

    if pokemon_ability not in all_pokemon_abilities:
        raise ValueError(
            f"Error: Pokemon ability ({pokemon_ability.title()}) not in database!")

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT p.pokemon_id, pokemon_name,
                STRING_AGG (ability_name, ', ' ORDER BY ability_name) AS all_abilities
                FROM pokemon AS p
                JOIN pokemon_ability AS pa
                ON p.pokemon_id = pa.pokemon_id
                GROUP BY p.pokemon_id
                HAVING STRING_AGG (ability_name, ', ' ORDER BY ability_name) ILIKE %s;""",
                [f"%{pokemon_ability.title()}"])

    pokemon_by_ability = cur.fetchall()
    cur.close()
    pokemon_by_ability_df = pd.DataFrame(pokemon_by_ability)

    return pokemon_by_ability_df


def get_pokemon_by_multiple_abilities(db_conn: connection, pokemon_ability: str | list[str]) -> DataFrame:
    """Returns all pokemon with listed abilities in their roster"""

    all_pokemon_abilities = get_all_pokemon_abilities(db_conn)

    for p_ability in pokemon_ability:

        if not isinstance(p_ability, str):
            raise TypeError(
                f"Error: {p_ability} should be of a string type!")

        if p_ability.lower().strip() not in all_pokemon_abilities:
            raise ValueError(
                f"Error: Pokemon type {p_ability.title()} not in database!")

    pokemon_ability.sort()
    pokemon_ability = list(
        map(lambda p_ability: p_ability.lower().strip(), pokemon_ability))

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT p.pokemon_id, pokemon_name, 
                STRING_AGG(pa.ability_name, ', ' ORDER BY ability_name) AS all_ability_names
                FROM pokemon AS p
                JOIN pokemon_ability AS pa
                ON p.pokemon_id = pa.pokemon_id
                GROUP BY p.pokemon_id
                HAVING STRING_TO_ARRAY(STRING_AGG(LOWER(pa.ability_name), ', '), ', ') @> %s;""",
                [pokemon_ability])

    pokemon_by_abilities = cur.fetchall()
    cur.close()
    pokemon_by_abilities_df = pd.DataFrame(pokemon_by_abilities)

    return pokemon_by_abilities_df


# TODO find default sql limit value
def get_count_of_moves_known_by_pokemon(db_conn: connection, sql_limit: str = "NULL") -> DataFrame:
    """Returns moves(limit available) with the count of pokemon that know them"""

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT DISTINCT(move_name), COUNT(pokemon_name) AS known_by
                FROM pokemon_move AS pm
                JOIN pokemon AS p ON pm.pokemon_id = p.pokemon_id
                GROUP BY pm.move_name   
                ORDER BY known_by DESC
                LIMIT NULL;""",
                [sql_limit])

    move_count_data = cur.fetchall()
    cur.close()
    move_count_data_df = pd.DataFrame(move_count_data)

    return move_count_data_df


# TODO find default sql limit value
def get_count_of_abilities_known_by_pokemon(db_conn: connection, sql_limit: str = "NULL") -> DataFrame:
    """Returns abilities(limit available) with the count of pokemon that know them"""

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT DISTINCT(ability_name), COUNT(pokemon_name) AS known_by
                FROM pokemon_ability AS pa
                JOIN pokemon AS p ON pa.pokemon_id = p.pokemon_id
                GROUP BY pa.ability_name   
                ORDER BY known_by DESC
                LIMIT NULL;""",
                [sql_limit])

    ability_count_data = cur.fetchall()
    cur.close()
    ability_count_data_df = pd.DataFrame(ability_count_data)

    return ability_count_data_df


# TODO find default sql limit value
def get_count_of_types_of_pokemon(db_conn: connection, sql_limit: str = "NULL") -> DataFrame:
    """Returns amount of pokemon that exist for each type"""

    cur = db_conn.cursor(cursor_factory=RealDictCursor)

    cur.execute("""SELECT DISTINCT(pokemon_type), COUNT(pokemon_name) AS number_of_pokemon
                FROM pokemon_types AS pt
                JOIN pokemon AS p ON pt.pokemon_id = p.pokemon_id
                GROUP BY pt.pokemon_type   
                ORDER BY number_of_pokemon DESC
                LIMIT NULL;""",
                [sql_limit])

    type_count_data = cur.fetchall()
    cur.close()
    type_count_data_df = pd.DataFrame(type_count_data)

    return type_count_data_df


if __name__ == "__main__":

    load_dotenv()

    config = environ

    conn = get_db_connection(config)

    # An example section of code to see this works when run

    # -- This code works
    # all_pokemon_names = get_all_pokemon_names(conn)
    # all_pokemon_types = get_all_pokemon_types(conn)
    # all_pokemon_moves = get_all_pokemon_moves(conn)
    # all_pokemon_abilities = get_all_pokemon_abilities(conn)

    # print(get_all_pokemon(conn))
    # print(get_specific_pokemon(conn, 'Bulbasaur'))
    # print(get_specific_pokemon_count(conn, 'bulbasaur'))
    # print(get_all_pokemon_count(conn))
    # print(get_pokemon_by_single_move_name(conn, "splash"))
    # print(get_pokemon_by_single_type(conn, "ground "))
    # print(get_pokemon_by_multiple_types(conn, ["ground", "poison"]))
    # print(get_pokemon_by_single_ability(conn, "overgrow"))
    # print(get_pokemon_by_multiple_abilities(conn, ["Leaf guard", "Overgrow"]))
    # print(get_pokemon_by_multiple_move_names(
    #     conn, ["Aerial Ace", "ABSORB", "AQUA jet "]))
    # print(get_all_pokemon_move_names(conn))
    # print(get_specific_pokemon_moves(conn, "bulbasaur"))

    # -- This code is testing
    # print(get_count_of_moves_known_by_pokemon(conn))
    # print(get_count_of_abilities_known_by_pokemon(conn))
    # print(get_count_of_types_of_pokemon(conn))

    conn.close()
