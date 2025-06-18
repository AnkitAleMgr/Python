import traceback
import requests

API_KEY = "fca_live_i0YneoamzFb7uTYuEdvSbj5ZMx4eJ5JJXXsRB3zn"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
QUIT_KEYWORD = ["Q", "QUIT", "EXIT"]

# Fetch and extract available currencies
available_currency = requests.get(BASE_URL).json()["data"]
available_currency = list(available_currency.keys())


def input_asker(prompt):
    response = input(prompt).strip()
    if response.upper() in QUIT_KEYWORD:
        print("👋 Exiting the program.")
        exit()
    return response


def get_currency_input():
    print("\nAvailable currencies:")
    for i, code in enumerate(available_currency, start=1):
        print(f"{code}", end=", " if i < len(available_currency) else "\n")

    while True:
        try:
            base = input_asker("\nEnter the base currency code (e.g., USD, EUR) or exit: ").upper()
            if base in available_currency:
                while True:
                    try:
                        amount_input = input_asker("Enter the amount to convert: ")
                        amount = float(amount_input)
                        if amount >= 1:
                            return base, amount
                        else:
                            print("❌ Invalid amount. Please enter a value greater than or equal to 1.")
                    except ValueError:
                        print("❌ Please enter a valid number.")
            else:
                print("❌ Invalid currency. Please enter again.")
        except Exception:
            print("An unexpected error occurred.")
            traceback.print_exc()


def currency_converter(base):
    url = f"{BASE_URL}&base_currency={base}&currencies={','.join(available_currency)}"
    response = requests.get(url)
    if response.ok:
        try:
            return response.json()["data"]
        except Exception:
            print("Something went wrong while parsing data.")
            traceback.print_exc()
    else:
        print("⚠️ Failed to retrieve data from the server.")
    return None


def data_arranger(data, base, amount):
    if data:
        data2 = {key: value for key, value in data.items() if key != base}
        print("\n" + "=" * 38)
        print("|{:^6}|{:^10}|{:^18}|".format("No.", "Currency", "Converted Amount"))
        print("-" * 38)
        for index, (key, value) in enumerate(data2.items(), start=1):
            print("|{:^6}|{:^10}|   {:<15.2f}|".format(index, key, value * amount))
        print("=" * 38)
    else:
        print("⚠️ No data available to arrange.")



def main():
    while True:
        base, amount = get_currency_input()
        data = currency_converter(base)
        data_arranger(data, base, amount)


if __name__ == "__main__":
    main()
