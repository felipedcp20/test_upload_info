import requests

nombre = input("Nombre del Pokémon: ").strip().lower()
url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"

respuesta = requests.get(url, timeout=10)
respuesta.raise_for_status()
pokemon = respuesta.json()

print(f"#{pokemon['id']} {pokemon['name'].capitalize()}")
print("Tipos:", ", ".join(tipo["type"]["name"] for tipo in pokemon["types"]))
print("Habilidades:", ", ".join(h["ability"]["name"] for h in pokemon["abilities"]))
