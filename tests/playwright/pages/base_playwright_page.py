import allure
from playwright.sync_api import Page


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, page: Page):
        self.page = page

    @allure.step("Ожидание загрузки страницы")
    def wait_page_loaded(self, timeout: int = 30000):
        """Ожидает полной загрузки страницы"""
        self.page.wait_for_load_state("domcontentloaded", timeout=timeout)

    @allure.step("Заполнение поля: {selector}")
    def fill_field(self, selector: str, text: str, timeout: int = 30000):
        """Заполняет поле текстом с предварительной очисткой"""
        element = self.page.locator(selector)
        element.wait_for(state="visible", timeout=timeout)
        element.clear()  # Очищаем поле перед вводом
        element.fill(text)

    @allure.step("Получение всех элементов: {selector}")
    def get_all_elements(self, selector: str) -> list:
        """Получает все элементы по селектору"""
        return self.page.locator(selector).all()