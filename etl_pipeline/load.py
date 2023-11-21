"""Handles all functions loading data into database"""

from os import environ

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


def insert_into_pokemon_table(conn: connection, pokemon_data: dict) -> int:
    """Inserts pokemon into pokemon table
    RETURNS POKEMON ID!!"""

    pokemon_name = pokemon_data["name"]

    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute(f"""INSERT INTO pokemon
                (pokemon_name)
                VALUES
                (%s) RETURNING*;""",
                    [pokemon_name])
    except:
        ConnectionError("Error: Connection to insert data unsuccessful!")

    pokemon_insert_data = cur.fetchall()

    pokemon_id = pokemon_insert_data[0]["pokemon_id"]

    cur.close()

    conn.commit()

    return pokemon_id


def insert_into_pokemon_stats_table(conn: connection, pokemon_data: dict, pokemon_id: int) -> None:
    """Inserts into pokemon_stats table"""

    pokemon_stats = pokemon_data["stats"]

    cur = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cur.execute("""INSERT INTO pokemon_stats
                (pokemon_id, hp, attack, defense, speed, 
                special_attack, special_defense, height, pokemon_weight)
                VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s, %s)RETURNING*;""",
                    [pokemon_id, pokemon_stats["hp"], pokemon_stats["attack"],
                     pokemon_stats["defense"], pokemon_stats["speed"], pokemon_stats["special-attack"],
                     pokemon_stats["special-defense"], pokemon_stats["height"], pokemon_stats["weight"]])
    except:
        ConnectionError(
            "Error: Unsuccessful connection attempt with the database!")

    cur.close()

    conn.commit()


def insert_into_pokemon_types_table(conn: connection, pokemon_data: dict, pokemon_id: int) -> None:
    """Inserts into the pokemon types table"""

    pokemon_types = pokemon_data["stats"]["types"]

    cur = conn.cursor(cursor_factory=RealDictCursor)

    for type in pokemon_types:

        try:
            cur.execute("""INSERT INTO pokemon_types
                        (pokemon_id, pokemon_type)
                        VALUES
                        (%s, %s)
                        RETURNING *;""",
                        [pokemon_id, type.capitalize()])
        except:
            ConnectionError(
                "Error: Unsuccessful connection established to database!")

    cur.close()

    conn.commit()


def load_pokemon_into_db(conn: connection, pokemon_data: dict) -> None:
    """Loads one pokemon into the postgres database"""

    try:
        pokemon_id = insert_into_pokemon_table(conn, pokemon_data)
        insert_into_pokemon_stats_table(conn, pokemon_data, pokemon_id)
        insert_into_pokemon_types_table(conn, pokemon_data, pokemon_id)

    except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError) as conn_err:
        conn_err("Error: Connection unsuccessful with the database!")

    return


if __name__ == "__main__":

    load_dotenv()

    config = environ

    conn = get_db_connection(config)

    conn.close()
