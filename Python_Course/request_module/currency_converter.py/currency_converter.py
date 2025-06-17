from tracemalloc import start
import requests

API_KEY = "fca_live_i0YneoamzFb7uTYuEdvSbj5ZMx4eJ5JJXXsRB3zn"
BASE_URL =  f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

currency = ["USD", "CAD","EUR", "CNY"]
print("available currency")


def base_asker():
    available_currnecy = ["USD", "CAD","EUR", "CNY"]
    print(f"Available currnecy:\n{", ".join(available_currnecy)}\n")
    while True:
        base = input("Enter the base currency: ").upper()
        if base in available_currnecy:
            print("available")
            return base
        else:
            print("Invalid base currency...")
    


def currency_converter(base):
    url = f"{BASE_URL}&base_currency={base}&currencies={",".join(currency)}"
    respond = requests.get(url)
    if respond.ok:
        try:
            data = respond.json()
    
            return data["data"]
            
        except:    
            print("Something went wrong...")
            
    else:
        print(f"Did not get respond from server. EROOR: {respond.status_code}")
        return None
        

def data_arranger(data):
    for index, (key, value)in enumerate(data.items(), start= 1):
        print(f"{index}. {key}: {value:.2f}")


if __name__ == "__main__":
    base = base_asker()
    data = currency_converter(base)
    data_arranger(data)

    