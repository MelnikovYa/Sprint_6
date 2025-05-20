import pytest
from pages.main_page import MainPage
from utils.cookie_handler import CookieHandler
from config import BASE_URL

class TestLogos:

    def test_click_scooter_logo_returns_to_main(self, driver):
        page = MainPage(driver)
        cookie = CookieHandler(driver)

        page.open(BASE_URL)
        cookie.close_cookie_banner()
        page.click_scooter_logo()

        assert page.current_url_starts_with(BASE_URL)

    def test_click_yandex_logo_redirects_to_dzen(self, driver):
        page = MainPage(driver)
        cookie = CookieHandler(driver)

        page.open(BASE_URL)
        cookie.close_cookie_banner()

        original_window = page.get_current_window()
        page.click_yandex_logo()
        page.wait_for_number_of_windows_to_be(2)
        page.switch_to_new_window(original_window)
        page.wait_for_url_to_contain("dzen.ru")

        assert page.current_url_contains("dzen.ru")