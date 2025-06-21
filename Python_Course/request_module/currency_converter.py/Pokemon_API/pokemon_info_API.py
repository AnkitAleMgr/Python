# from urllib import response
import requests
import os
import difflib
from dotenv import load_dotenv

# for acessing .env for data and url
load_dotenv() # <-- creating object
BASE_URL = os.getenv("base_url") #<-- use to get url from .env file using os

# variable
EXIT_KEYWORD = {"q","quit","exit","e"} # <-- set of key word used to quit

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
    Available_end_point = {point for point in requests.get(BASE_URL).json()}

    # infinite loop to ask valid end point form the user
    while True:
        # asking input form the user
        end_point = user_input("\nEnter the Topic you want to see(Pokemon, berry, ability, move): ")
        suggestion = difflib.get_close_matches(end_point, list(Available_end_point), n=1, cutoff=0.6)
        
        # checking if it is empty or not
        if end_point == "" or any(char.isdigit() for char in end_point):
            print("Invalid input")
        else:
            if end_point.lower() in Available_end_point:
                print(f"\nEnd point {end_point} accepted. Proceding....")
                print(BASE_URL + "/"+ end_point.lower()+ "\n")
                return end_point.lower()
            else:
                suggestion_text = ", ".join(s.title() for s in suggestion)
                print(f"Did not find end point named {end_point}, do you mean {suggestion_text}.") if suggestion else print(f"Did not find end point named {end_point}, no suggestions.")


# for filter unecessery data by asking user name or ID
def name_id_asker(end_point):

    url = BASE_URL+"/"+end_point.lower() 
    response = requests.get(url)
    data = response.json()
    total_count = data["count"]
    print(f"total_count = {total_count}")
    new_url = BASE_URL+"/"+end_point.lower()+ f"?offset=0&limit={total_count}"

    available_name_id = requests.get(new_url)
    data = available_name_id.json()
    result = data["results"]
    name_list= [pokemon["name"] for pokemon in result]    
    name_list= {name.replace("-"," ") for name in name_list}
    
    # infinite loop to ask valid name form the user
    while True:
        # asking name or id from the user 
        name_id = user_input(f"\nEnter the name of {end_point}: ")
        suggestion = difflib.get_close_matches(name_id, list(name_list), n=1, cutoff=0.6)

        if name_id == "":
            print("Invalid input")
        else:
            if name_id.lower() in name_list:
                print(f"\nName {name_id} accepted as end point of {end_point}")
                print(BASE_URL+"/"+end_point+"/"+name_or_id)
                return name_id.lower()
            print(f"Cannot find {end_point} named {name_id}, Do you mean {"".join(suggestion)}?") \
                if suggestion else print(f"Cannot find {end_point} named {name_id}, No suggestion.")
            
# function that retrive data form server
def detail_retriver(end_point, name):
    # basic retriving data form server
    url = BASE_URL+"/"+end_point+"/"+name
    response = requests.get(url)
    data = response.json()
    topics = [topic for topic in data]
    # print(f"\n{topic}\n{url}")
    # topics = ['abilities', 'base_experience', 'cries', 'forms', 'game_indices', 'height', 'held_items', 'id', 'is_default', 'location_area_encounters', 'moves', 'name', 'order', 'past_abilities', 'past_types', 'species', 'sprites', 'stats', 'types', 'weight']
    new_topic = [topic.replace("_"," ") for topic in topics]
    
    # varibales
    user_topic_choice = ""

    while True:
        print("\n"+"-"*214)
        print("Available Topic:")
        
        print(", ".join(new_topic))

        user_topic_choice = user_input("\nEnter the topic number you want: ").lower()
        if user_topic_choice == "":
            print("Invalid input.")
        elif user_topic_choice in new_topic:
            print(f"Topic {user_topic_choice} has be accepted.")
            break 
        else:
            suggestion = difflib.get_close_matches(user_topic_choice, topics, n=1, cutoff=0.6)
            print(f"There is no topic name {user_topic_choice}, Do you mean {"".join(suggestion).capitalize()}.") if suggestion else print(f"There is no topic name {user_topic_choice}, No suggestion.")
        
    value = data[user_topic_choice]
    if isinstance(value, list):
        for containt in value:
            print(containt)
    if isinstance(value, dict):
        for i, j in value.items():
            print(f"{i}: {j}")
    else:
        print(value)



def main():
    # end_point = endpoint_asker()
    # name = name_id_asker(end_point)
    detail_retriver(end_point="pokemon", name="pikachu")
    


if __name__ == "__main__":
    main()