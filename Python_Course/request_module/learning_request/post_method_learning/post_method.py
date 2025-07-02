import requests, os, traceback
from dotenv import load_dotenv
from enum import Enum


load_dotenv() # <-- creating object name load_dotenv() to acess .env file data

# Access token imported from .env file
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
# url/ Link
BASE_URL = os.getenv("BASE_URL")

# Varibale
EXIT_KEYWORD = ("q","quit","e","exit") # <-- all the word that reqresent user quiting intenson
length = 170 # <-- to change the length of outline

# Enue to collect expected value/input
class Gender(Enum):
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
    # constant varible
    pass



def body_data():
    name, email, gender, status = input_asker()
    name, email, gender, status = input_empty_checker(name, email, gender, status)

    



        

def main_operation():
    header = header_data()
    body_data()







def main():
    main_operation()

if __name__ == "__main__":
    main()