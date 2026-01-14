
from playwright.sync_api import Page, expect



class IngredientPage:
    """Page Object для страницы заказов"""

    def __init__(self, page: Page):
        self.page = page

        # Локаторы
        self.ingredients_btn = page.locator("//*[text()='Ингредиенты']")
        self.title_ingredients_= page.locator("//div/h4")
        self.new_order_btn = page.locator("#orders-create-btn")
        self.comment_input = page.locator("//label[text()='Комментарий к заказу']//following::textarea[1]")
        self.ingredients_combobox = page.locator("//div[@role='combobox']")
        self.ingredient_options = page.locator("//ul[@role='listbox']/li")
        self.create_confirm_btn = page.locator("//button[@data-testid='orders-create-confirm-btn']")
        self.created_order_alert = page.locator("//*[text()='Order created!']")
        self.order_cards = page.locator("[data-testid^='order-card-']")

    def check_ingredient_menu_(self):
        self.ingredients_btn.is_enabled()
        self.ingredients_btn.click()
        expect(self.title_ingredients_).to_be_visible()
        expect(self.title_ingredients_).to_have_text("Ингредиенты")


