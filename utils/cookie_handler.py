from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class CookieHandler:
    def __init__(self, driver):
        self.driver = driver

    def close_cookie_banner(self):
        self.driver.find_element(By.ID, "rcc-confirm-button").click()
