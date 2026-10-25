import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
print(response.status_code)