"""ETL process"""

from os import environ

from dotenv import load_dotenv

from extract import extract_all_pokemon_urls, extract_single_pokemon
from transform import transform_pokemon_data
from load import get_db_connection, load_pokemon_into_db

if __name__ == "__main__":

    load_dotenv()

    config = environ

    conn = get_db_connection(config)

    pokemon_urls = extract_all_pokemon_urls()

    for url in pokemon_urls:

        pokemon_data = extract_single_pokemon(url)

        pokemon_data_transformed = transform_pokemon_data(pokemon_data)

        load_pokemon_into_db(conn, pokemon_data)

    conn.close()
