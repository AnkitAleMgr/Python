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


def custon_input(prompt):
    user_input = input(prompt).strip()
    if user_input.lower() in EXIT_KEYWORD:
        exit()
    return user_input

def proper_input_checker(name, email, gender, status):
    # constant varible
    pass

def header_data():
    post_header = dict()
    post_header["Authorization"] = "Bearer " + ACCESS_TOKEN

    return post_header


def body_data():
    while True:
        name = custon_input("Enter you name: ")
        email = custon_input("Enter you email: ")
        gender = custon_input("Enter your gender(male/female): ")
        status = custon_input("Enter you status(active/inactive): ")
        print(name, email, gender, status)


        

def main_operation():
    header = header_data()
    body_data()







def main():
    main_operation()

if __name__ == "__main__":
    main()