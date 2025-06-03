import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def get_text(self, locator):
        return self.find(locator).text

    def is_element_displayed(self, locator):
        return self.find(locator).is_displayed()

    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_presence(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    @allure.step("Получение текущего URL окна")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверка, что URL начинается с '{expected_url}'")
    def current_url_starts_with(self, expected_url):
        return self.driver.current_url.startswith(expected_url)

    @allure.step("Проверка, что URL содержит подстроку '{substring}'")
    def current_url_contains(self, substring):
        return substring in self.driver.current_url

    @allure.step("Получение дескриптора текущего окна")
    def get_current_window(self):
        return self.driver.current_window_handle

    @allure.step("Переключение на новое окно, кроме '{original_window}'")
    def switch_to_new_window(self, original_window):
        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break

    @allure.step("Ожидание появления второго окна")
    def wait_for_number_of_windows_to_be(self, count, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(count))

    @allure.step("Ожидание, пока URL будет содержать подстроку '{substring}'")
    def wait_for_url_to_contain(self, substring, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: substring in d.current_url)

    @allure.step("Получаем текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url