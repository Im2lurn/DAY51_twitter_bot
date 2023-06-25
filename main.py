from twitter_details import TWITTER_PASSWORD, TWITTER_USERNAME, TWITTER_EMAIL
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10

CHROME_DRIVER_PATH = 'C:\WEB DEVELOPMENT udemy\chromedriver.exe'
service = Service(CHROME_DRIVER_PATH)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        url = 'https://www.speedtest.net/'
        self.driver.get(url)
        button = self.driver.find_element(By.CLASS_NAME, 'js-start-test.test-mode-multi')
        button.click()

        time.sleep(50)
        self.down = self.driver.find_element(By.CLASS_NAME,
                                             'result-data-large.number.result-data-value.download-speed').text
        self.up = self.driver.find_element(By.CLASS_NAME,
                                           'result-data-large.number.result-data-value.upload-speed').text
        # print(self.down, self.up)
        time.sleep(10)
        self.driver.implicitly_wait(5)
        self.tweet_at_provider()


    def tweet_at_provider(self):
        url1 = 'https://twitter.com/login'
        self.driver.get(url1)
        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()

        input_email = self.driver.find_element(By.NAME, 'text')
        input_email.send_keys(TWITTER_EMAIL)
        input_email.send_keys(Keys.TAB)
        input_email.send_keys(Keys.ENTER)

        self.driver.implicitly_wait(3)
        input_username = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        input_username.send_keys(TWITTER_USERNAME)
        self.driver.implicitly_wait(10)
        input_username.send_keys(Keys.ENTER)

        self.driver.implicitly_wait(3)
        input_password = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        input_password.send_keys(TWITTER_PASSWORD)
        self.driver.implicitly_wait(10)
        input_password.send_keys(Keys.ENTER)

        self.driver.implicitly_wait(3)
        tweet_button = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet_button.click()

        self.driver.implicitly_wait(3)
        tweet_text = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        self.driver.implicitly_wait(3)
        tweet_text.send_keys(f'{self.down}, {self.up}')
        time.sleep(10)
        self.driver.quit()


internet_speed_twitter_bot = InternetSpeedTwitterBot()
internet_speed_twitter_bot.get_internet_speed()
# internet_speed_twitter_bot.tweet_at_provider()
