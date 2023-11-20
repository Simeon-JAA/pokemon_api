"""ETL process"""

from extract import extract_all_pokemon_urls, extract_single_pokemon
from transform import transform_pokemon_data

if __name__ == "__main__":

    pokemon_urls = extract_all_pokemon_urls()

    for url in pokemon_urls:

        pokemon_data = extract_single_pokemon(url)

        pokemon_data_transformed = transform_pokemon_data(pokemon_data)

        break
