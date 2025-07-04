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
def location_input_empty_checker(value):
    if value == "":
        print("Input cannot be empty. Please re-enter.. ")
        user_location()
    return value
def input_empty_checker(value, function):
    while value == "":
        print("Input cannot be empty. Please re-enter value: ")
        function
    return value
def input_boolean_checker(value, fucntion):
    while value.lower() not in {"yes","no"}:
        print("Input can only be in boolean(Yes/No) format. Please re-enter value:")
        fucntion
    return value.lower()
def input_day_range_checker(value, function, first_day, last_day):
    try:
        value = int(value)
    except ValueError:
        print(f"Invalid day. {value} cannot be converted int true number. Please re-enter the day:")
        function
        
    while not (1 <= value <= 14):
        print(f"Invalid day. It must be between ({first_day} - {last_day}). Please re-enter the day:")
        function
    return value

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
        print(key)
    user_end_point = custom_input("Please enter the end point: ")
    while user_end_point not in available.keys():  
        print("Invalid end point. Please re-enter end point..")
        user_end_point = custom_input("Please enter the end point: ")
    
    print(f"{user_end_point} accepted as valid endpoint.")
    return user_end_point, available[user_end_point]
def user_location():# <--to get location detail from user   
    location = custom_input("Please enter the location: ")
    location = location_input_empty_checker(location)

    print(f"{location} has been accepted as valid location.")
    return location
def user_params():# <--to get necessery params from user
    

    return

# asking data for prams
def api():
    api = custom_input("Do you want api(get air quality data(Yes/No)): ")
    api = input_empty_checker(api, api())
    api = input_boolean_checker(api, api()) 
    return api
def days():
    first_day = 1
    last_day = 14
    days = custom_input("Enter the day duration (1-14): ")
    days = input_empty_checker(days, days())
    input_day_range_checker(days, days(), first_day, last_day)
def dt():
    pass
# def 

# handeling params according to user end point choice:
def current_weather_params():
    pass
def forecast_params():
    pass
def history_params():
    pass
def alerts_params():
    pass
def future_params():
    pass
def marine_params():
    pass

def data_retriver(): # <-- requesting data form the server
    user_end_point, url_endpoint = user_endpoint()
    location = user_location()
    
    if user_end_point == "current weather":
        current_weather_params()
    elif user_end_point == "forecast":
        forecast_params()
    elif user_end_point == "history":
        history_params()
    elif user_end_point == "alerts":
        alerts_params()
    elif user_end_point == "future":
        future_params()
    else: 
        marine_params()
    

    response = requests.get(url + url_endpoint ,key= API_KEY , q= location, timeout = (3, 10))

    if response.status_code == 200:
        pass
    else:
        print(f"Something went wrong {response.status_code}")


# main section
def main():
    data_retriver()

# entry point
if __name__ == "__main__":
    main()