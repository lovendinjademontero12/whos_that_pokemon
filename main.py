import random
import requests

pokemon_id = random.randint(1, 1000)

#fetch the data from the API
try:
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(pokemon_id))
except requests.exceptions.RequestException:
    print("Network error.")
    exit()

#match casing for the error handling and alongside the game structure
match response.status_code:
    case 200:
        data = response.json()
        real_name = data["name"]
        height = data["height"]
        weight = data["weight"]

        print("Who's that Pokemon?")
        print("Height:", height)
        print("Weight:", weight)

        guess = input("Your guess: ")

    case _:
        print("Something went wrong:", response.status_code)