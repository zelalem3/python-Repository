import requests

quotes = requests.get(url="https://kanye.rest/")
print(quotes)