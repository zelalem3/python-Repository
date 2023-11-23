import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PASSWORD = "ZELALEM1249"
USERNAME = "DFJHDFGJH"

# response = requests.get("https://www.tiktok.com/explore")
# print(response.text)

driver = webdriver.Chrome()
driver.get("https://www.tiktok.com/foryou")
driver.maximize_window()


login_button = driver.find_element(By.ID, "header-login-button" )

# driver.find_element_by_id("top-login-button").send_keys(Keys.ENTER)
# # phone_number = driver.find_element(By.)
# # phone_number.send_keys("0968610963")
# # password = driver.find_element(By.)
# # password.send_keys("zelalem1249")
# follow_button = driver.find_element(By.CLASS_NAME, "tiktok-2bezmsi-Button ehk74z00")
# time.sleep(10)

# follow_button.send_keys("click")
# driver.find_element(By.CSS_SELECTOR, )



# driver.quit()
