import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ConfirmationPage(BasePage):
    MODAL_HEADER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    @allure.step("Проверяем, что заказ подтверждён")
    def is_order_confirmed(self):
        return "Заказ оформлен" in self.get_text(self.MODAL_HEADER)
