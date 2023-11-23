from selenium import webdriver
from time import sleep
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = "djk"
username = "zgetnet242gmail.com"
password = "zelalem1249"
SIMILAR_ACCOUNT = "lionel messi"


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome()

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(username)
        password.send_keys(password)
        sleep(5)

        password.send_keys(keys.ENTER)

    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        sleep(2)
        followers = self.driver.find_element(By.XPATH,
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        sleep(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):

        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(5)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]'")
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login(username, password)
bot.find_followers()
bot.follow()
