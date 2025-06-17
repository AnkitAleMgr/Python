
import traceback
import requests

API_KEY = "fca_live_i0YneoamzFb7uTYuEdvSbj5ZMx4eJ5JJXXsRB3zn"
BASE_URL =  f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"


available_currency = requests.get(BASE_URL)
data = available_currency.json()
available_currency = list(data["data"].keys())


def base_asker():
    
    print("Available currencies:")
    for i, code in enumerate(available_currency, start=1):
        print(f"{code}", end=", " if i < len(available_currency) else "\n\n")

    while True:
        base = input("Enter the base currency code (e.g., USD, EUR): ").upper()
        if base in available_currency:
            return base
        else:
            print("❌ Invalid currency. Please enter one from the list above.")




def currency_converter(base):

    url = f"{BASE_URL}&base_currency={base}&currencies={",".join(available_currency)}"
    response = requests.get(url)
    if response.ok:
        try:
            data = response.json()
            return data["data"]
        except:    
            print("Something went wrong...")
            traceback.print_exc()
    else:
        print("⚠️ Failed to process the data from the server.")
        return None
        

def data_arranger(data, base):

    if data is not None:
        data2 = {key: value for key, value in data.items() if key != base}
        for index, (key, value) in enumerate(data2.items(), start= 1):
            print(f"{(str(index)+"."):<4}{key}: {value:.2f}")
    else:
        print("⚠️ No data available to arrange.")


def main():
    base = base_asker()
    data = currency_converter(base)
    data_arranger(data, base)
    
if __name__ == "__main__":
    main()