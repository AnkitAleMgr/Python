import os, requests
from dotenv import load_dotenv

load_dotenv() # <-- creating object to read .env file

# getting necessery resources form .env file
BASE_URL = os.getenv("BASE_URL")
BASE_VERSON = os.getenv("BASE_VERSON")
API_KEY = os.getenv("API_KEY")

EXIT_KEYWORD = {"q", "quit", "exit", "e"} # all the exit keyword
url = BASE_URL + BASE_VERSON
length = 170

# visual and utility function
def line():
    print("-"*length)
def custom_input(prompt): # <--custom input
    line()
    value = input(prompt).strip().lower()
    line()
    if value in EXIT_KEYWORD:
        print("exiting...")
        exit()
    return value

def user_endpoint():# <--to get endpoint from available end point
    # available endpoint
    available = {
    "current weather": "/current.json",
    "forecast": "/forecast.json",
    "history": "/history.json",
    "alerts": "/alerts.json",
    "future": "/future.json",
    "marine": "/marine.json"
    }

    line()
    print(f"Available end point ({len(available)}): ")
    line()
    for key, value in available.items():
        print(key)
    user_end_point = custom_input("Please enter the end point: ")
    while user_end_point not in available.keys():  
        print("Invalid end point. Please re-enter end point..")
        user_end_point = custom_input("Please enter the end point: ")
    
    print(f"{user_end_point} accepted as valid endpoint.")
    return available[user_end_point]


def data_retriver(): # <-- requesting data form the server
    endpoint = user_endpoint()


# main section
def main():
    data_retriver()

# entry point
if __name__ == "__main__":
    main()