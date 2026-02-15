import re

from playwright.sync_api import sync_playwright, expect


def test_simple_with_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto("https://www.ya.ru")
            page.wait_for_load_state("domcontentloaded")

            search_box = page.locator("//textarea[@id='text']")
            search_box.fill("Alex Ecko")
            search_box.press("Enter")
            page.wait_for_selector("#search-result", timeout=10000)
            results = page.locator("//li[not(starts-with(@id, 'Futuris_search'))]")
            expect(results).to_have_count(21)
            expect(page).to_have_title(re.compile("Alex Ecko"))
            expect(page.locator("//span[text()='Поиск'][1]")).to_have_text("Поиск")
            expect(page.locator("//span[text()='Алиса']")).to_have_text("Алиса")
        finally:
            browser.close()

