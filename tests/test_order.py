# tests/test_order.py
import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.confirmation_page import ConfirmationPage
from utils.cookie_handler import CookieHandler
from config import BASE_URL

class TestOrder:

    @pytest.mark.parametrize("button_locator", [
        OrderPage.ORDER_BUTTON_HEADER,
        OrderPage.ORDER_BUTTON_BOTTOM,
    ])
    def test_order_button_opens_form(self, driver, button_locator):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        cookie = CookieHandler(driver)

        main_page.open(BASE_URL)
        cookie.close_cookie_banner()

        element = order_page.wait_for_presence(button_locator)
        order_page.scroll_to(element)
        order_page.wait_for_clickable(button_locator).click()

        assert order_page.is_element_displayed(OrderPage.NAME_INPUT)

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

        order_page.wait_for_clickable(OrderPage.ORDER_BUTTON_HEADER).click()

        order_page.fill_first_form(name, surname, address, phone)
        order_page.fill_second_form(comment)

        assert confirmation_page.is_order_confirmed()
