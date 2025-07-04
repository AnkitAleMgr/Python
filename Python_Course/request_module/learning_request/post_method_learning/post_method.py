import requests, os, traceback
from dotenv import load_dotenv
from enum import Enum

# objects
load_dotenv() # <-- creating object name load_dotenv() to acess .env file data

# Access token imported from .env file
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
BASE_URL = os.getenv("BASE_URL") # url/ Link

# Varibale
EXIT_KEYWORD = ("q","quit","e","exit") # <-- all the word that reqresent user quiting intenson
length = 170 # <-- to change the length of outline

# Enum to collect expected value/input
class Genders(Enum):
    MALE = "male"
    FEMALE = "female"
class Status(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

# method and decuratives
def header_data():
    post_header = dict()
    post_header["Authorization"] = "Bearer " + ACCESS_TOKEN

    return post_header
def custon_input(prompt):
    user_input = input(prompt).strip()
    if user_input.lower() in EXIT_KEYWORD:
        exit()
    return user_input
def up_vertical_line():
    print("-"*length+"\n")
def down_vertical_line():
    print("\n"+"-"*length)

# input validation checker section
def input_asker():
    up_vertical_line()
    name = custon_input("Enter you name: ")
    email = custon_input("Enter you email: ")
    gender = custon_input("Enter your gender(male/female): ")
    status = custon_input("Enter you status(active/inactive): ")
    down_vertical_line()

    return name, email, gender, status   
def input_empty_checker(name, email, gender, status):
    while name == "" or email == "" or gender == "" or status == "":
        print("Input cannot be empty. Please input proper input.")
        name, email, gender, status = input_asker()
    return name, email, gender, status
def proper_input_checker(name, email, gender, status):
    valid_genders = {g.value for g in Genders}
    valid_statuses = {s.value for s in Status}
    # constant varible
    while gender not in valid_genders or status not in valid_statuses or name.isdigit() or email.isdigit():
        print("Value you provide is not matching expected. Re-enter with proper input.")
        body_data()
    return name, email, gender, status

# main body
def body_data():
    name, email, gender, status = input_asker()
    name, email, gender, status = input_empty_checker(name, email, gender, status)
    name, email, gender, status = proper_input_checker(name, email, gender, status)
    
    post_body = dict()
    post_body["name"] = name
    post_body["email"] = email
    post_body["gender"] = gender
    post_body["status"] = status

    return post_body

def post(header, body):
    post_variable = requests.post(BASE_URL, headers = header, json= body, timeout = (3, 10))

    # trying to convert into json format
    try:
       response_data  = post_variable.json()
    except ValueError:
        print("❌ Invalid JSON response.")
        return None
    
    # error code handeling
    if post_variable.status_code == 201:
        up_vertical_line()
        print(f"Individual name {body["name"]} has be added in database with id {response_data["id"]}: ")
        print(response_data)
        down_vertical_line()
    elif post_variable.status_code == 403:
        up_vertical_line()
        print("Access denide. Please check your given permission.")
        down_vertical_line()
    elif post_variable.json()[0]["message"] == "has already been taken":
        print(f"Individual name {body["name"]} has already been created. Please try puting new data.")
    else:
        print(f"Something went wrong. Error code {post_variable.status_code}")
    return response_data

def main_operation():
    header = header_data()
    body = body_data()
    post(header, body)

def main():
    main_operation()

if __name__ == "__main__":
    main()