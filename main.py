from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import username,password 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import random


class InstagramBot():

    def __init__(self, username, password):

        self.username = username
        self.password = password
        s = Service(r"path for chrome drivers")
        self.browser = webdriver.Chrome(service=s)

    def close_browser(self):

        self.browser.close()
        self.browser.quit()

    def login(self):
    
        browser = self.browser
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element(By.NAME,'username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(random.randrange(2,5))

        password_input = browser.find_element(By.NAME,'password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

    def xpath_exists(self, url):
    
        browser = self.browser
        try:
            browser.find_element(By.XPATH,url)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist


        

            




bot = InstagramBot(username,password)
bot.login()

bot.close_browser()
