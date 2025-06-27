import requests

url = "http://httpbin.org/get"

response = requests.get(url)

print(response)