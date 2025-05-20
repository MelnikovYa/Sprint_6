import pytest
from pages.main_page import MainPage
from utils.cookie_handler import CookieHandler
from config import BASE_URL

class TestAccordion:

    @pytest.mark.parametrize("index", range(8))
    def test_accordion_questions(self, driver, index):
        page = MainPage(driver)
        cookie = CookieHandler(driver)

        page.open(BASE_URL)
        cookie.close_cookie_banner()

        page.click_question(index)
        answer = page.get_answer_text(index)
        assert answer != ""
