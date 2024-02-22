from selenium import webdriver
import pyautogui
import time
from PIL import Image

jump = Image.open("works.png")

# pyautogui.screenshot("screenshot2.png")

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get("https://elgoog.im/dinosaur-game/")
time.sleep(2)
pyautogui.press('space')

im = Image.open("screenshot2.png")
Game = True
while Game:
    try:
        if pyautogui.locateOnScreen(jump):
            pyautogui.press('space')
            print("Image found1")
        else:
            print("Image not found1")
    except pyautogui.ImageNotFoundException:
        print("Image not found1")

    try:
        if pyautogui.locateOnScreen(im):
            pyautogui.press('space')
            print("Image found")
        else:
            print("Image not found")
    except pyautogui.ImageNotFoundException:
        print("Image not found")
driver.quit()
