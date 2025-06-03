import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage
from config import BASE_URL

class MainPage(BasePage):
    QUESTIONS = [
        (By.ID, f"accordion__heading-{i}") for i in range(8)
    ]
    ANSWERS = [
        (By.ID, f"accordion__panel-{i}") for i in range(8)
    ]

    SAMOKAT_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")


    @allure.step("Кликаем по вопросу #{index}")
    def click_question(self, index):
        element = self.find(self.QUESTIONS[index])
        self.scroll_to(element)
        self.wait_for_clickable(self.QUESTIONS[index])
        element.click()

    @allure.step("Получаем текст ответа #{index}")
    def get_answer_text(self, index):
        return self.get_text(self.ANSWERS[index])

    @allure.step("Кликаем по логотипу Самокат")
    def click_scooter_logo(self):
        self.click(self.SAMOKAT_LOGO)

    @allure.step("Кликаем по логотипу Яндекс")
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)

    @allure.step("Проверка, что выполнен переход на главную страницу")
    def is_on_main_page(self):
        return self.get_current_url().startswith(BASE_URL)

    @allure.step("Проверка, что выполнен переход на Дзен")
    def is_on_dzen_page(self):
        return self.current_url_contains("dzen.ru")

    @allure.step("Проверка, что текст ответа отображается")
    def is_answer_displayed(self, index):
        return self.get_answer_text(index).strip() != ""