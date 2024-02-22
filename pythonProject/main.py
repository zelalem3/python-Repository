from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/?next=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fedit%2F%3F__coig_login%3D1")
time.sleep(20)
# login_button = driver.find_element_by_id('header-login-button')
username = driver.find_element(By.CLASS_NAME, "_aa4b _add6 _ac4d")
# username = driver.find_element_by_name("username")
# password = driver.find_element_by_name("password")

username.send_keys("zelalem1249")
# password.send_keys("Scooponset1")


   # "e13wiwn61 css-10uhe97-Button-StyledLoginButton ehk74z00"

time.sleep(20)
driver.quit()
