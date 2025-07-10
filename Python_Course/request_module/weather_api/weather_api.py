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
    # line()
    value = input(prompt).strip().lower()
    # line()
    if value in EXIT_KEYWORD:
        print("exiting...")
        exit()
    while value == "":
        print("Input cannot to empty.")
        # line()
        value = input(prompt).strip().lower()
    return value
def input_boolean_checker(value, function): # <--check if the value is boolean or not
    if value in ["yes","no"]:
        print(f"{value.capitalize()} is accepted as boolean value.")
        return value
    else:
        print("Input can only be in boolean(Yes/No) format. Please re-enter value:")
        return function()
def date_asker(): # <--asking date form user in proper format
    while True:
        user_date = custom_input("Enter the date (yyyy-MM-dd) format: ")
        try:
            valid_date = datetime.strptime(user_date, "%Y-%m-%d")
            return valid_date
        except:
            print("Invalid date format or non-date input. Please re-enter.")
def data_display(data): # <--it display key of data received form apis
    line()
    print(f"Available Topics ({len(data)}):")
    line()
    for key in data.keys():
        print("->" + key)
    line()

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
def user_params(**kwargs):# <--to get necessery params from user
    params = dict()
    for key, value in kwargs.items():
        params[str(key)]= str(value)
    return params

# asking data for prams
def aqi(): # <--apis keys function
    user_aqi = custom_input("Do you want aqi(get air quality data(Yes/No)): ")
    user_aqi = input_boolean_checker(user_aqi, aqi)

    return user_aqi
def days(last_day): # <--days keys function
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
def dt(period): # <--date keys function
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
def alerts(): # <--alerts keys function
    user_alerts = custom_input("Enter if you want alerts(Yes/No): ")
    user_alerts = input_boolean_checker(user_alerts, alerts)
    return user_alerts

# handeling params according to user end point choice:
def current_weather_params(): # create prams according to user input for current weather endpoint
    user_aqi = aqi()
    params = user_params(aqi = user_aqi)

    return params
def forecast_params(): # create prams according to user input for forecast endpoint
    user_aqi = aqi()
    user_alerts = alerts()
    user_days = days(14)    
    params = user_params(aqi = user_aqi, alerts = user_alerts, days = user_days)
    return params
def history_params(): # create prams according to user input for history endpoint
    user_date = dt(period="past")
    params = user_params(dt = user_date)

    return params 
def alerts_params(): # create prams according to user input for alerts endpoint
    # params = user_params()
    params = dict()
    return params
def future_params(): # create prams according to user input for future endpoint
    user_date = dt(period = "future")
    params = user_params(dt = user_date)
    return params
def marine_params(): # create prams according to user input for marine endpoint
    user_days = days(7)
    params = user_params(days = user_days)

    return params

def data_retriver(): # <-- requesting data form the server
    user_end_point, url_endpoint = user_endpoint()
    location = user_location()
    user_params = ""

    if user_end_point == "current weather":
        user_params = current_weather_params()
    elif user_end_point == "forecast":
        user_params =  forecast_params()
    elif user_end_point == "history":
        user_params = history_params()
    elif user_end_point == "alerts":
        user_params= alerts_params()
    elif user_end_point == "future":
        user_params = future_params()
    else: 
        user_params = marine_params() 
    
    user_params["key"] = API_KEY
    user_params["q"] = location

    response = requests.get(url + url_endpoint ,params= user_params, timeout = (3, 10))
    
    if response.status_code == 200:
        print("Date received from server")
        return response.json()
    elif response.status_code == 400:
        print(f"Did not found the data of location named {location}. Please try nearby location")
        print(f"Error code: {response.status_code}")
    elif response.status_code == 401:
        print("You dont have access to data from server. Please re-check you access token and permission.")
        print(f"Error code:  {response.status_code}")
    else:
        print(f"Something went wrong. Error code: {response.status_code}")
def data_displayer(data): # <-- to display necessery data to user
    data_display(data) #it display visually about topic in user selected endpoint

# main section
def main():
    data = data_retriver()
    data_displayer(data)

# entry point
if __name__ == "__main__":
    main()