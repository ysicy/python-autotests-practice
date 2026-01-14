import re

from playwright.sync_api import sync_playwright, expect


def test_playwright_simple():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto("http://localhost:5173")
            page.wait_for_load_state("domcontentloaded")

            login_input = page.locator("//input[@id='login-username']")
            login_input.fill("AlexTest")

            password_input = page.locator("//input[@id='login-password']")
            password_input.fill("Alex2301")
            password_input.press("Enter")

            page.wait_for_selector("h4")
            title_ = page.locator("//h4")
            expect(title_).to_be_visible()
            expect(title_).to_have_text("Мои заказы")
            page.locator("//h4").is_visible()
            expect(page).to_have_url(re.compile("http://localhost:5173"))
            expect(title_).to_be_enabled()

        finally:
            browser.close()


def test_check_orders():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto("http://localhost:5173")
            page.wait_for_load_state("domcontentloaded")
            login_input = page.locator("//input[@id='login-username']")
            login_input.fill("AlexTest")

            password_input = page.locator("//input[@id='login-password']")
            password_input.fill("Alex2301")
            password_input.press("Enter")

            orders_btn = page.locator("//*[text()='Заказы']")
            orders_btn.click()

            title_ = page.locator("//h4")
            expect(title_).to_be_visible()
            expect(title_).to_have_text("Текущие заказы")

        finally:
            browser.close()

def test_check_ingredients():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto("http://localhost:5173")
            page.wait_for_load_state("domcontentloaded")
            login_input = page.locator("//input[@id='login-username']")
            login_input.fill("AlexTest")

            password_input = page.locator("//input[@id='login-password']")
            password_input.fill("Alex2301")
            password_input.press("Enter")

            orders_btn = page.locator("//*[text()='Ингредиенты']")
            orders_btn.click()

            title_ = page.locator("//div/h4")
            expect(title_).to_be_visible()
            expect(title_).to_have_text("Ингредиенты")

        finally:
            browser.close()
