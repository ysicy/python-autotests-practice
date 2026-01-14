from tests.conftest import admin_auth_playwright
from tests.playwright.pages.ingredient_page import IngredientPage
from tests.playwright.pages.order_page import OrdersPage


def test_w_pw(page):
    admin_auth_playwright(page)
    order_page = OrdersPage(page)
    order_page.check_orders_menu_()
    assert order_page.check_orders_menu_() == "Текущие заказы"

def test_w_pw2(page):
    admin_auth_playwright(page)
    ingredient_page = IngredientPage(page)
    ingredient_page.check_ingredient_menu_()

