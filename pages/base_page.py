from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def is_element_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def close_cookie_banner(self):
        try:
            cookie_button = self.driver.find_element(By.ID, "rcc-confirm-button")
            cookie_button.click()
        except NoSuchElementException:
            pass
