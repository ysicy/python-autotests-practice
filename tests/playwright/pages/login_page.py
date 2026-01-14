import time

import allure
from playwright.sync_api import Page

from tests.playwright.pages.base_playwright_page import BasePage

class LoginPage(BasePage):
    """Страница авторизации"""

    def __init__(self, page: Page):
        super().__init__(page)

        self.username_field = "//input[@id='login-username']"
        self.password_field = "//input[@id='login-password']"
        self.login_button = "#login-submit"
        self.register_link = "a[href='/register']"
        self.error_message = "div.MuiAlert-message"

    @allure.step("Ввод имени пользователя: {username}")
    def enter_username(self, username: str):
        """Вводит имя пользователя"""
        self.fill_field(self.username_field, username)

    @allure.step("Ввод пароля")
    def enter_password(self, password: str):
        """Вводит пароль"""
        self.fill_field(self.password_field, password)

    @allure.step("Клик по кнопке входа")
    def click_login_button(self):
        """Кликает по кнопке входа"""
        self.click_element(self.login_button)

    @allure.step("Авторизация пользователя: {username}")
    def login(self, username: str, password: str):
        """Выполняет полную авторизацию"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(1)

    @allure.step("Получение сообщения об ошибке")
    def get_error_message(self) -> str:
        """Получает текст сообщения об ошибке"""
        if self.is_element_visible(self.error_message):
            return self.get_element_text(self.error_message)
        return ""

    @allure.step("Проверка наличия ошибки авторизации")
    def has_login_error(self) -> bool:
        """Проверяет наличие ошибки авторизации"""
        return self.is_element_visible(self.error_message)

    @allure.step("Очистка полей формы")
    def clear_form(self):
        """Очищает поля формы авторизации"""
        self.page.locator(self.username_field).clear()
        self.page.locator(self.password_field).clear()