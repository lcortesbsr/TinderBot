# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


path = '/C'
service = Service(executable_path=path)
web = 'https://tinder.com'
pickup_line = "Hello pretty!"
number_of_swipes = 15



options = Options()
options.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(service=service, options=options)
driver.get(web)
time.sleep(3)

for i in range(number_of_swipes):
    try:
        like_button = driver.find_element(by="xpath", value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[4]/button[1]/span[1]/span[1]/*[name()='svg'][1]")
        driver.execute_script("arguments[0].click();", like_button)
        time.sleep(3)

        say_something_text = driver.find_element(by="xpath", value='//textarea[@placeholder="Say something nice!"]')
        say_something_text.send_keys(pickup_line)
        time.sleep(3)

        send_message_button = driver.find_element(by="xpath", value='//button/span[text()="Send"]')
        send_message_button.click()
        time.sleep(3)

        close_its_match_window = driver.find_element(by="xpath", value='//button[@title="Back to Tinder"]')
        close_its_match_window.click()
    except:
        try:
            popup = driver.find_element(by="xpath",
                                        value='//button/span[text="Maybe Later"]|//button/span[text="Not interested"]|//button/span[text="No Thanks"]')
            popup.click()
        except:
            pass

