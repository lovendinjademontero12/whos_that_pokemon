import random
import requests

#added list for the pokemon choice idea
pokemon_list = ["pikachu", "charmander", "bulbasaur", "squirtle", "snorlax"]
name = random.choice(pokemon_list)

#data fetch from the API
try:
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + name)
except requests.exceptions.RequestException:
    print("Trouble in fetching data.")
    exit()

#match casing for the error handling and the game logic
match response.status_code:
    case 200:
        data = response.json()
        real_name = data["name"]
        height = data["height"]
        weight = data["weight"]

        #prints the height and weight but not the name, also included the choices in the print
        print("Who's that Pokemon?")
        print("You only have 3 attempts!")
        print("Height:", height)
        print("Weight:", weight)
        print("Choices:", ", ".join(pokemon_list))

        #attempts counter and result status
        attempts = 0
        won = False

        #loop and attempts system
        while attempts < 3:
            guess = input("Your guess: ").lower().strip()

            #validity checker
            if guess not in pokemon_list:
                print("That Pokemon is not in the list. Try again!")
                continue

            attempts = attempts + 1

            #guess result check
            if guess == real_name:
                won = True
                break
            else:
                print("Wrong! Try again.")

        #final result check and print       
        if won:
            print("Correct! You win!")
        else:
            print("You lost! It was", real_name, "!")

    case _:
        print("Something went wrong:", response.status_code)