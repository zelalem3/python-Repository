# import browser
#
# import selenium
# from selenium import webdriver
#
driver_path = "chromedriver_win32"
# driver = webdriver.Chrome()
# driver.get(c)
# driver.quit()
from selenium import webdriver
# from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome(driver_path)
# get google.co.in
# driver.get("https://google.co.in")
# value = driver.find_element("id", "input")
# value = driver.find_element(By.ID, 'input')
# value.send_keys("http://www.python.org")
driver.get("secure-retreat-92358.herokuapp.com")
name = driver.find_element("name", "fName")
name.send_keys("zelalem")
lname = driver.find_element("name", "lName")
name.send_keys("getnet")
email = driver.find_element("name", "email")
email.send_keys("zgetnet24@gmail.com")
click = driver.find_element("class", "btn-block")
click.click()