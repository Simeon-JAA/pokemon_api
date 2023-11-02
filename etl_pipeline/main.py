"""ETL process"""

from extract import extract_all_pokemon_urls, extract_single_pokemon
from transform import filter_pokemon_stats

if __name__ == "__main__":

    pokemon_urls = extract_all_pokemon_urls()

    for url in pokemon_urls:

        pokemon_data = extract_single_pokemon(url)

        print(filter_pokemon_stats(pokemon_data))

        break
