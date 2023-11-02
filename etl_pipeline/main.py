"""ETL process"""

from extract import extract_all_pokemon_urls, extract_single_pokemon

if __name__ == "__main__":

    pokemon_urls = extract_all_pokemon_urls()

    for url in pokemon_urls:

        pokemon_data = extract_single_pokemon(url)

        print(url)

        break
