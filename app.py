from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close();

    def login(self):
        driver = self.driver
        driver.get('https://instagram.com/')
        time.sleep(3)

        username_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(self.username)

        password_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(3)
        for i in range(1, 2):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)
        
        links = driver.find_elements_by_tag_name('a')
        links_href = [elem.get_attribute('href') for elem in links]

        for href in links_href:
            driver.get(href)
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
            time.sleep(3)



testAccount = InstagramBot('youremail', 'yourpassword')
testAccount.login()
testAccount.like_photo('hashtag')