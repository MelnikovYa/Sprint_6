import pytest
from pages.main_page import MainPage

URL = "https://qa-scooter.praktikum-services.ru/"

@pytest.mark.parametrize("index", range(8))
def test_accordion_questions(driver, index):
    page = MainPage(driver)
    page.open(URL)
    page.click_question(index)
    answer = page.get_answer_text(index)
    assert answer != ""
