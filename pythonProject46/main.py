import requests
from bs4 import BeautifulSoup
day = input("which year do you want tot travel to? Type the date in this format YYY-MM-DD:")
print(day)
URL = "https://www.billboard.com/charts/hot-100/2000-08-12"
response = requests.get(URL)
new_response = response.text
soup = BeautifulSoup(new_response)
print(soup.get_text())
# soup = BeautifulSoup(new_response)
# music = soup.Beautifulsoup(name="h3")
# clientID = 327834284378734


