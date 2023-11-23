from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time
chrome_driver_path = "C:\Program Files\webdriver"
 driver = webdriver.Chrome(executbale_path=chrome_driver_path)
# data =driver.get("https://en.wikipedia.org/wiki/Main_Page")
# number = data.find_element(By.CSS_SELECTOR, "#mp-welcomecount  a")
# print(number.text)
# driver.quit()
# driver.find_element(By.NAME, "Email")
# .send_keys("zgetnet24@gmail.com")
# driver.find_element(By.NAME. "Name")
# .send_keys("zelalem")
# send_keys(keys.ENTER)
data = driver.get("https://orteil.dashnet.org/cookieclicker/")
this = driver.find_element(By.ID, "bigcookie" )
num = driver.find_element(By.ID, "cookies")
new_num = int(num.text)
compare = driver.find_element(By.CLASS_NAME, "price")
new_compare = int(compare.text)
if new_num >

