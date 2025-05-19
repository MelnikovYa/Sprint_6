import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.confirmation_page import ConfirmationPage

URL = "https://qa-scooter.praktikum-services.ru/"


@pytest.mark.parametrize("button_xpath", [
    "//button[contains(@class, 'Button_Button__ra12g')][1]",
    "//div[contains(@class, 'Home_FinishButton')]/button"
])
def test_order_button_opens_form(driver, button_xpath):
    driver.get(URL)
    main_page = MainPage(driver)
    main_page.close_cookie_banner()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, button_xpath))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, button_xpath))
    ).click()

    assert driver.find_element(By.XPATH, "//input[@placeholder='* Имя']").is_displayed()

@pytest.mark.parametrize("name, surname, address, phone, comment", [
    ("Тест", "Тестов", "Тест, ул. Тестовая, д.9", "89994815162", "Кот домофона"),
    ("Теста", "Тестова", "Тест, Тестовый 9", "88884815162", "Кот домофона")
])
def test_positive_order_flow(driver, name, surname, address, phone, comment):
    main_page = MainPage(driver)
    order_page = OrderPage(driver)
    confirmation_page = ConfirmationPage(driver)

    main_page.open(URL)
    main_page.close_cookie_banner()

    driver.find_element(By.XPATH, "//button[@class='Button_Button__ra12g']").click()
    order_page.fill_first_form(name, surname, address, phone)
    order_page.fill_second_form(comment)

    assert confirmation_page.is_order_confirmed()