from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "login-username")
    PASSWORD = (By.ID, "login-password")
    SUBMIT   = (By.XPATH, "//button[text()='Войти']")
    REGISTER = (By.CSS_SELECTOR, "a[href='/register']")
    ERROR    = (By.XPATH, "//div[contains(@class,'MuiAlert-message')]")

    def open(self, base_url: str ):
        super().open(f"{base_url}/login")
        return self

    def login_as(self, username: str, password: str):
        self.fill(*self.USERNAME, text=username)
        self.fill(*self.PASSWORD, text=password)
        self.click(*self.SUBMIT)


    def login_with_error(self, username: str, password: str) -> str:
        self.login_as(username, password)
        return self.text(*self.ERROR)

    def go_to_register(self):
        self.click(*self.REGISTER)


    def wait_loaded(self):
        self.is_visible(*self.USERNAME)
        return self