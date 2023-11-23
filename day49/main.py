from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

email = "zgetnet24@gmail.com"
phone_num = "251968610963"
password = "zelalem1249"
path = "C:\Program Files\chromedriver_win32"
driver = webdriver.Chrome(path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
sign_in = driver.find_element_link_text ("sign in")
sign_in.click()

time.sleep(5)

email_field = driver.find_element_by_id("username")
email_field.send_keys(email)
password_field = driver.find_element_by_id("password")
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)


