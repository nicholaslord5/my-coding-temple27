import requests

# Task 2 Fetch data
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    return {
        "name": data['name'],
        "abilities": [ability['ability']['name'] for ability in data['abilities']],
        "weight": data['weight']
    }

# Pikachu's data
pokemon_data = fetch_pokemon_data("pikachu")
print(f"Name: {pokemon_data['name']}")
print(f"Abilities: {', '.join(pokemon_data['abilities'])}")
