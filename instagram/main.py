from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


email = "zgetnet24@gmail.com"
password = "zelalem1249"

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

username = driver.find_element(By.CLASS_NAME, "x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1xmf6yo x1e56ztr x540dpk x1m39q7l x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1")
# password = driver.find_element(By.CLASS_NAME, "")

username.click()
# password.send_keys(password)
# login.click()

driver.close()
