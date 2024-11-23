# Modify pikachu_api.py to fetch and display 3 pokemon. Create function to calculate and return avg weight of those Pokemon. Print the names, abilities, and average weight of the three Pokémon

import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    return {
        "name": data['name'],
        "abilities": [ability['ability']['name'] for ability in data['abilities']],
        "weight": data['weight']
    }

def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "squirtle", "charmander"]
pokemon_data_list = [fetch_pokemon_data(name) for name in pokemon_names]

for pokemon in pokemon_data_list:
    print(f"Name: {pokemon['name']}")
    print(f"Abilities: {', '.join(pokemon['abilities'])}")
    print()

average_weight = calculate_average_weight(pokemon_data_list)
print(f"Average Weight: {average_weight} units")
