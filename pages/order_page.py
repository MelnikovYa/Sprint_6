import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage

class OrderPage(BasePage):
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

    ORDER_BUTTON_HEADER = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g')][1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button")

    @allure.step("Заполняем первую форму заказа")
    def fill_first_form(self, name, surname, address, phone):
        self.find(self.NAME_INPUT).send_keys(name)
        self.find(self.SURNAME_INPUT).send_keys(surname)
        self.find(self.ADDRESS_INPUT).send_keys(address)
        self.find(self.METRO_INPUT).click()
        self.find_all(self.METRO_OPTION)[0].click()
        self.find(self.PHONE_INPUT).send_keys(phone)
        self.click(self.NEXT_BUTTON)

    @allure.step("Заполняем вторую форму заказа и подтверждаем")
    def fill_second_form(self, comment):
        self.click(self.DATE_INPUT)
        self.click(self.DATE_PICK)
        self.click(self.RENT_DROPDOWN)
        self.click(self.RENT_OPTION)
        self.click(self.COLOR_CHECKBOX)
        self.find(self.COMMENT_INPUT).send_keys(comment)

        order_btn = self.wait_for_clickable(self.ORDER_BUTTON, timeout=20)
        self.scroll_to(order_btn)
        order_btn.click()

        confirm_btn = self.wait_for_clickable(self.CONFIRM_BUTTON, timeout=20)
        self.scroll_to(confirm_btn)
        confirm_btn.click()
