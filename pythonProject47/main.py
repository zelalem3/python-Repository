from selenium import webdriver
chrome_driver_path = "C:\Program Files"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.python.org/")
# data = driver.find_element_ny_class("widget-title")
# print(data.text)
# driver.find_element(By.CLASS, 'widget-title')
driver.get("https://en.wikipedia.org/wiki/Main_Page")
data
