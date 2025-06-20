from curses.ascii import isalnum
from http.client import responses
import requests, os
from dotenv import load_dotenv

# for acessing .env for data and url
load_dotenv() # <-- creating object
BASE_URL = os.getenv("base_url") #<-- use to get url from .env file using os

# variable
EXIT_KEYWORD = {"q","quit","exit","e"} # <-- set of key word used to quit

available_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon?offset=0&limit=10")
available_pokemon_data = available_pokemon.json()
available_pokemon = [pokemon["name"] for pokemon in available_pokemon_data["results"]]


# user dependent variable
end_point = ""
name_or_id = ""

# custom input for checking empty, invalid input, quit and forcing user to put input
def user_input(prompt):
    # infinite loop
    while True:
        # asking user input
        name = input(prompt).strip()
        # checking if user is trying to quit
        if name.lower() in EXIT_KEYWORD:
            print("Exiting......")
            exit() # <-- it end the program
        # returning the valid user input
        return name.title()
    
# for filter unecessery data by asking user endpoint 
def endpoint_asker():

    # limiting the available option
    Available_end_point = {"Pokemon","Berry","Ability"}

    # infinite loop to ask valid end point form the user
    while True:
        # asking input form the user
        end_point = user_input("\nEnter the Topic you want to see(Pokemon, berry, ability): ")
        # checking if it is empty or not
        if end_point == "" or any(char.isdigit() for char in end_point) or end_point not in Available_end_point:
            print("Invalid input")
        else:
            print(f"End point {end_point} accepted. Proceding..")
            return end_point

# for filter unecessery data by asking user name or ID
def name_id_asker(end_point):

    # infinite loop to ask valid name form the user
    while True:
        
        # asking name or id from the user 
        name_id = user_input(f"\nEnter the name or id of {end_point}: ")
        if name_id == "":
            print("Invalid input")
        else:
            print(f"Name(ID) {name_id} has been accepted of {end_point}\n")
            return name_id


# function that retrive data form server
def retriver(id, type):
    # variable
    url = "{}/{}/{}".format(BASE_URL, type, id)
    print(url)

    responses = requests.get(url)
    
    # checking if responce is ok or not
    if responses.ok:
        data = responses.json()
        return data["abilities"]
    else:
        print(f"Did not got the data. Error {responses.status_code}")


def main():
    end_point = endpoint_asker()
    name_or_id = name_id_asker(end_point)
    data = retriver(name_or_id, end_point)
    print(data)

    # endpoint_and_name_id_asker()

    # for index, pokemon in enumerate(available_pokemon_data["results"], start=1): 
    #     print(f"{index:^5}", pokemon["name"])
    
    # print(available_pokemon)



if __name__ == "__main__":
    main()