"""ETL process"""

import time
from os import environ

from dotenv import load_dotenv

from etl_pipeline.etl.extract import extract_all_pokemon_urls, extract_single_pokemon
from transform import transform_pokemon_data
from load import get_db_connection, load_pokemon_into_db

if __name__ == "__main__":

    load_dotenv()

    config = environ

    conn = get_db_connection(config)

    pokemon_urls = extract_all_pokemon_urls()

    start_time = time.time()

    for url in pokemon_urls:

        pokemon_data = extract_single_pokemon(url)

        pokemon_data_transformed = transform_pokemon_data(pokemon_data)

        load_pokemon_into_db(conn, pokemon_data)

        load_time = time.time()

        pokemon_name = pokemon_data_transformed["name"]

        print(f"{pokemon_name} added to database! {load_time - start_time}s ...")

    conn.close()
