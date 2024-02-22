import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.nba.com/stats")
result = requests.get("https://www.nba.com/stats")
response = BeautifulSoup(response.text, "html.parser")
response = response.get_text()

print(response)
