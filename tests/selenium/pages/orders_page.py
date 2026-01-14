from tests.selenium.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrdersPage(BasePage):
    TITLE = (By.XPATH, "//h4[text()='Мои заказы']")
    MY_ORDERS_BTN = (By.XPATH, "//*[text()='Заказы']")
    MY_ORDERS_TITLE = (By.XPATH, "//*[text()='Текущие заказы']")



    def wait_loaded(self) -> "OrdersPage":
        self.is_visible(*self.TITLE)
        return self

    def orders_title(self):
        self.click(*self.MY_ORDERS_BTN)

    def wait_title(self):
        self.is_visible(*self.MY_ORDERS_TITLE)

    def get_my_orders_title_text(self):
        return self.text(*self.MY_ORDERS_TITLE)

    def get_orders_title_text(self):
        return self.text(*self.TITLE)