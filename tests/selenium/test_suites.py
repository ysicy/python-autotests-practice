from tests.selenium.pages.ingredient_page import IngredientsPage
from tests.selenium.pages.login_page import LoginPage
from tests.selenium.pages.orders_page import OrdersPage


def test_login(chrome_driver,base_ui_url):
    login_page = LoginPage(chrome_driver)
    login_page.open(base_ui_url)
    login_page.login_as("AlexTest","Alex2301")

    orders_page = OrdersPage(chrome_driver)
    orders_page.wait_loaded()
    assert orders_page.get_orders_title_text() == "Мои заказы"

def test_check_my_orders(chrome_driver,base_ui_url):
    login_page = LoginPage(chrome_driver)
    login_page.open(base_ui_url)
    login_page.login_as("AlexTest","Alex2301")

    orders_page = OrdersPage(chrome_driver)
    orders_page.orders_title()
    orders_page.wait_title()
    assert orders_page.get_my_orders_title_text() == "Текущие заказы"

def test_check_ingredients(chrome_driver,base_ui_url):
    login_page = LoginPage(chrome_driver)
    login_page.open(base_ui_url)
    login_page.login_as("AlexTest","Alex2301")

    ingredient = IngredientsPage(chrome_driver)
    ingredient.ingredients()
    ingredient.wait_ingredients_title()
    assert ingredient.get_title_text() == "Ингредиенты"
