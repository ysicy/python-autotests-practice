import pytest
from playwright.sync_api import sync_playwright, Browser, ViewportSize, BrowserContext


@pytest.fixture(scope="session")
def browser():
    """Создает браузер для всей сессии тестов"""
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,  # Видимый режим для отладки
            args=[
                "--no-sandbox",           # Для CI/CD
                "--disable-dev-shm-usage" # Для Docker
            ]
        )
        yield browser
        browser.close()

@pytest.fixture
def context(browser: Browser):
    """Создает новый контекст для каждого теста"""
    context = browser.new_context(
        viewport=ViewportSize(width=1920, height=1080),  # Размер окна
        accept_downloads=True  # Разрешает загрузки файлов
    )
    context.set_default_timeout(30000)  # 30 секунд по умолчанию
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context: BrowserContext):
    """Создает новую страницу для каждого теста."""
    page = context.new_page()
    yield page
    page.close()