import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.confirmation_page import ConfirmationPage
from utils.cookie_handler import CookieHandler
from config import BASE_URL

class TestOrder:

    @pytest.mark.parametrize("position", ["header", "bottom"])
    def test_order_button_opens_form(self, driver, position):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        cookie = CookieHandler(driver)

        main_page.open(BASE_URL)
        cookie.close_cookie_banner()

        order_page.click_order_button(position)

        assert order_page.is_order_form_displayed()

    @pytest.mark.parametrize("name, surname, address, phone, comment", [
        ("Тест", "Тестов", "Тест, ул. Тестовая, д.9", "89994815162", "Кот домофона"),
        ("Теста", "Тестова", "Тест, Тестовый 9", "88884815162", "Кот домофона")
    ])
    def test_positive_order_flow(self, driver, name, surname, address, phone, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        confirmation_page = ConfirmationPage(driver)
        cookie = CookieHandler(driver)

        main_page.open(BASE_URL)
        cookie.close_cookie_banner()

        order_page.click_order_button()

        order_page.fill_first_form(name, surname, address, phone)
        order_page.fill_second_form(comment)

        assert confirmation_page.is_order_confirmed()
