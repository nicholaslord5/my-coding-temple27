# Fetch Data from a Space API Write a Python script that makes a GET request to a space API (e.g., [The Solar System OpenData](https://api.le-systeme-solaire.net/en/)) to fetch data about planets.
# Parse the JSON response and extract information about each planet, such as its name, mass, and orbit period.

import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    
    for planet in planets:
        if planet.get('isPlanet'):
            name = planet.get('englishName', 'Unknown')
            mass = planet.get('mass', {}).get('massValue', 'N/A')
            orbit_period = planet.get('sideralOrbit', 'N/A')
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()
