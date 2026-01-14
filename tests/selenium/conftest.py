import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def browser_config():
    """Конфигурация браузера"""
    return {
        "headless": False,  # Показывать браузер или нет
        "window_size": (1920, 1080),
        "timeout": 10
    }

@pytest.fixture
def base_ui_url():
    return "http://localhost:5173"

@pytest.fixture
def chrome_driver(browser_config, request):
    """Фикстура для Chrome драйвера"""

    # Настройки Chrome
    chrome_options = Options()

    if browser_config["headless"]:
        chrome_options.add_argument("--headless")

    chrome_options.add_argument(
        f"--window-size={browser_config['window_size'][0]},{browser_config['window_size'][1]}")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Создаем драйвер
    driver = webdriver.Chrome(options=chrome_options)

    # Устанавливаем неявное ожидание
    driver.implicitly_wait(browser_config["timeout"])

    # Сохраняем ссылку на драйвер в объекте теста
    # Это позволит pytest хукам получить доступ к драйверу
    # для создания скриншотов при падении тестов
    request.node.driver = driver

    yield driver

    # Закрываем браузер после теста
    driver.quit()