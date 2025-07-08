from curses.ascii import isdigit
import os, requests
import re
from dotenv import load_dotenv
from datetime import datetime, timedelta

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
    while value == "":
        print("Input cannot to empty.")
        line()
        value = input(prompt).strip().lower()
    return value
def input_boolean_checker(value, function):
    if value in ["yes","no"]:
        print(f"{value.capitalize()} is accepted as boolean value.")
        return value
    else:
        print("Input can only be in boolean(Yes/No) format. Please re-enter value:")
        return function()
def date_asker():
    while True:
        user_date = custom_input("Enter the date (yyyy-MM-dd) format: ")
        try:
            valid_date = datetime.strptime(user_date, "%Y-%m-%d")
            return valid_date
        except:
            print("Invalid date format or non-date input. Please re-enter.")

# user dependent fucntion
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
        print(key.capitalize())
    user_end_point = custom_input("Please enter the end point: ")
    while user_end_point not in available.keys():  
        print("Invalid end point. Please re-enter end point..")
        user_end_point = custom_input("Please enter the end point: ")
    print(f"{user_end_point.capitalize()} accepted as valid endpoint.")

    return user_end_point, available[user_end_point]
def user_location():# <--to get location detail from user   
    location = custom_input("Please enter the location: ")

    print(f"{location.capitalize()} has been accepted as valid location.")
    return location
def user_params():# <--to get necessery params from user
    

    return

# asking data for prams
def api():
    user_api = custom_input("Do you want api(get air quality data(Yes/No)): ")
    user_api = input_boolean_checker(user_api, api) 
    return user_api
def days(last_day):
    first_day = 1
    user_days = custom_input(f"Enter the day duration ({first_day}-{last_day}): ")
    while True:
        while not user_days.isdigit():
            print(f"Invalid day. {user_days} cannot be converted into true number. Please re-enter the day:")
            user_days = custom_input(f"Enter the day duration ({first_day}-{last_day}): ")
        if (first_day <= int(user_days) <= last_day):
            break
        else:
            print(f"Day must be between {first_day} - {last_day}")
            user_days = custom_input(f"Enter the day duration ({first_day}-{last_day}): ")   
    return user_days
def dt(period):
    present_date = datetime.now()
    user_date = date_asker()

    if period == "past":
        while user_date.date() >= present_date.date():
            print("Invalid time period. Please enter the date on or after 1st Jan, 2010 in yyyy-MM-dd format.")
            user_date = date_asker()
        print(f"{user_date.date()} has been accepted as valid {period} date")
        return user_date.date()
    if period == "future":
        while not ((present_date.date() + timedelta(days=14)) <= user_date.date() <= (present_date.date() + timedelta(days=300))):
            print("Invalid time period. Please enter the date between 14 days and 300 days from today in the future in yyyy-MM-dd format")
            user_date = date_asker()
        print(f"{user_date.date()} has been accepted as valid {period} date")
        return user_date.date()
    else:
        print("Something went wrong witn tense. Please check the arguments.")
def alerts():
    user_alerts = custom_input("Enter if you want alerts(Yes/No): ")
    user_alerts = input_boolean_checker(user_alerts, alerts)
    return user_alerts

# handeling params according to user end point choice:
def current_weather_params():
    user_api = api()
    return user_api
def forecast_params():
    user_api = api()
    user_alerts = alerts()
    user_days = days(14)    
    return user_api, user_alerts, user_days
def history_params():
    user_date = dt(period="past")
def alerts_params():
    # it has no prams so i will not send empty params/dictionary
    return
def future_params():
    user_date = dt(period = "future")
def marine_params():
    user_day = days(7)

def data_retriver(): # <-- requesting data form the server
    user_end_point, url_endpoint = user_endpoint()
    # location = user_location()
    
    if user_end_point == "current weather":
        user_api = current_weather_params()
    elif user_end_point == "forecast":
        user_api, user_alerts ,user_days =  forecast_params()
    elif user_end_point == "history":
        history_params()
    elif user_end_point == "alerts":
        alerts_params()
    elif user_end_point == "future":
        future_params()
    else: 
        marine_params()
    

    # response = requests.get(url + url_endpoint ,key= API_KEY , q= location, timeout = (3, 10))

    # if response.status_code == 200:
    #     pass
    # else:
    #     print(f"Something went wrong {response.status_code}")

# main section
def main():
    data_retriver()

# entry point
if __name__ == "__main__":
    main()