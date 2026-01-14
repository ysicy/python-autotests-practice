from tests.selenium.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class IngredientsPage(BasePage):
    TITLE = (By.XPATH, "//h4[text()='Мои заказы']")
    INGREDIENS_BTN = (By.XPATH, "//*[text()='Ингредиенты']")
    INGREDIEN_TITLE = (By.XPATH, "//h4[text()='Ингредиенты']")



    def wait_loaded(self) -> "OrdersPage":
        self.is_visible(*self.TITLE)
        return self

    def ingredients(self):
        self.click(*self.INGREDIENS_BTN)

    def wait_ingredients_title(self):
        self.is_visible(*self.INGREDIEN_TITLE)
        return

    def get_title_text(self):
        return self.text(*self.INGREDIEN_TITLE)