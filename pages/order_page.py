from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.CLASS_NAME, "select-search__input")
    METRO_OPTION = (By.CLASS_NAME, "Order_Text__2broi")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_PICK = (By.CLASS_NAME, "react-datepicker__day--001")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENT_OPTION = (By.XPATH, "//div[text()='двое суток']")
    COLOR_CHECKBOX = (By.ID, "black")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]//button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")

    def fill_first_form(self, name, surname, address, phone):
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
        self.driver.find_element(*self.METRO_INPUT).click()
        self.driver.find_elements(*self.METRO_OPTION)[0].click()
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def fill_second_form(self, comment):
        self.driver.find_element(*self.DATE_INPUT).click()
        self.driver.find_element(*self.DATE_PICK).click()
        self.driver.find_element(*self.RENT_DROPDOWN).click()
        self.driver.find_element(*self.RENT_OPTION).click()
        self.driver.find_element(*self.COLOR_CHECKBOX).click()
        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)

        order_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.ORDER_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_btn)
        order_btn.click()

        confirm_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.CONFIRM_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", confirm_btn)
        confirm_btn.click()
