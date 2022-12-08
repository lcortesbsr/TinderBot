# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def openTinder(self):
        self.driver.get('http://tinder.com')
        sleep(5)

        login = self.driver.find_element('xpath', '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[2]/div[2]/a[1]/div[2]/div[2]')
        login.click()
        sleep(5)

bot = TinderBot()
bot.openTinder()

