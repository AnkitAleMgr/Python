import requests

# url = "https://newsapi.org/v2/everything?q=tesla&from=2025-05-16&sortBy=publishedAt&apiKey=296188f8ba444a28afdf977afc94f08f"

url = "https://newsapi.org/" 

retrived_value = requests.get(url)


if retrived_value. == 200:
    print("Retrived")
else:
    print(f"Could not be connected. ERROR: {retrived_value}")