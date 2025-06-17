
import traceback
import requests

API_KEY = "fca_live_i0YneoamzFb7uTYuEdvSbj5ZMx4eJ5JJXXsRB3zn"
BASE_URL =  f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"


available_currency = requests.get(BASE_URL)
data = available_currency.json()
available_currency = list(data["data"].keys())


def base_asker():
    
    print(f"Available currencies:\n{', '.join(available_currency)}\n")
    while True:
        base = input("Enter the base currency: ").upper()
        if base in available_currency:
            return base
        else:
            print("Invalid base currency...")



def currency_converter(base):

    url = f"{BASE_URL}&base_currency={base}&currencies={",".join(available_currency)}"
    respond = requests.get(url)
    if respond.ok:
        try:
            data = respond.json()
            return data["data"]
        except:    
            print("Something went wrong...")
            traceback.print_exc()
    else:
        print(f"Did not get respond from server. EROOR: {respond.status_code}")
        return None
        

def data_arranger(data, base):
    
    del data[base]
    for index, (key, value)in enumerate(data.items(), start= 1):
        
        print(f"{(str(index)+"."):<4}{key}: {value:.2f}")



def main():
    base = base_asker()
    data = currency_converter(base)
    data_arranger(data, base)

if __name__ == "__main__":
    main()