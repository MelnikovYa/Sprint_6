from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.main_page import MainPage

URL = "https://qa-scooter.praktikum-services.ru/"

def test_click_scooter_logo_returns_to_main(driver):
    page = MainPage(driver)
    page.open(URL)
    page.click_scooter_logo()
    WebDriverWait(driver, 10).until(
        lambda d: d.current_url.startswith(URL)
    )
    assert driver.current_url.startswith(URL)

def test_click_yandex_logo_redirects_to_dzen(driver):
    page = MainPage(driver)
    page.open(URL)

    original_window = driver.current_window_handle
    page.click_yandex_logo()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    new_window = [w for w in driver.window_handles if w != original_window][0]
    driver.switch_to.window(new_window)

    try:
        WebDriverWait(driver, 15).until(
            lambda d: "dzen.ru" in d.current_url.lower()
        )
    except TimeoutException:
        assert False, f"Ожидание редиректа на Dzen не сработало. URL: {driver.current_url}"

    assert "dzen.ru" in driver.current_url.lower()

    driver.close()
    driver.switch_to.window(original_window)
