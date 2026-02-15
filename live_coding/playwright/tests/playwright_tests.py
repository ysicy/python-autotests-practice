import re

import pytest
from playwright.sync_api import sync_playwright, expect, Page

from live_coding.playwright.page.login_page import LoginPage


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




def test_with_fixtures(page):
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

def test_qa_thread(page):
    page.goto("https://lms.threadqa.ru/auth/login")
    page.wait_for_load_state("domcontentloaded")

    name_input = page.locator("//input[@type='email']")
    name_input.fill("alexeyecko@gmail.com")

    pass_input = page.locator("//input[@name='password']")
    pass_input.fill("Alexeykaecko093+")

    voyti_btn = page.locator("//button[@type='submit']")
    voyti_btn.click()

    page.wait_for_load_state("domcontentloaded")
    span_name = page.locator("//h1//span")
    expect(span_name).to_have_text("Alex!")
    menu_profile = page.locator("//button[@data-state='closed'][3]")
    menu_profile.click()
    exit_btn = page.locator("(//div[@data-orientation='vertical'])[3]")
    exit_btn.click()
    welcome_text = page.locator("//h1")
    expect(welcome_text).to_have_text("Добро пожаловать!")

def tests_with_page_object(page):
    login_page = LoginPage(page)
    login_page.page.goto("https://lms.threadqa.ru/auth/login")
    login_page.login("alexeyecko@gmail.com", "Alexeykaecko093+")
    login_page.wait_page_loaded()
    expect(login_page.get_logged_username_text()).to_have_text("Alex!")
    login_page.log_out()
    expect(login_page.get_welcome_text()).to_have_text("Добро пожаловать!")
