from playwright.sync_api import Page, expect


class OrdersPage:
    """Page Object для страницы заказов"""

    def __init__(self, page: Page):
        self.page = page

        # Локаторы
        self.title = page.locator("//h4[text()='Мои заказы']")
        self.orders_btn = page.locator("//*[text()='Заказы']")
        self.title_orders_ = page.locator("//*[text()='Текущие заказы']")
        self.new_order_btn = page.locator("#orders-create-btn")

    def check_orders_menu_(self):
        self.orders_btn.is_visible()
        self.orders_btn.click()
        expect(self.title_orders_).to_be_visible()

        return self.title_orders_.text_content()
