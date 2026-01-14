import random

import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

fake = Faker()


def test_simple_login():
    driver = webdriver.Chrome()

    try:
        driver.get("http://localhost:5173/")

        login = driver.find_element(By.XPATH, "//input[@id='login-username']")
        login.send_keys("AlexTest")
        password = driver.find_element(By.XPATH, "//input[@id='login-password']")
        password.send_keys("Alex2301")

        submit_btn = driver.find_element(By.XPATH, "//button[text()='Войти']")
        submit_btn.click()

        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "h4"))
        )

        header = driver.find_element(By.CSS_SELECTOR, "h4")
        assert header.text == "Мои заказы"

    finally:
        driver.quit()


@pytest.fixture(scope="session")
def browser_config():
    """Конфигурация браузера"""
    return {
        "headless": False,  # Показывать браузер или нет
        "window_size": (1400, 1600),
        "timeout": 10
    }


@pytest.fixture
def chrome_driver(browser_config):
    """Фикстура для Chrome драйвера"""

    # Настройки Chrome
    chrome_options = Options()

    if browser_config["headless"]:
        chrome_options.add_argument("--headless")

    chrome_options.add_argument(f"--window-size={browser_config['window_size'][0]},{browser_config['window_size'][1]}")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Создаем драйвер
    driver = webdriver.Chrome(options=chrome_options)

    # Устанавливаем неявное ожидание
    driver.implicitly_wait(browser_config["timeout"])

    yield driver

    # Закрываем браузер после теста
    driver.quit()


def test_login_with_fixture(chrome_driver):
    chrome_driver.get("http://localhost:5173/")

    login = chrome_driver.find_element(By.XPATH, "//input[@id='login-username']")
    login.send_keys("AlexTest")

    password = chrome_driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("Alex2301")

    submit_btn = chrome_driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_btn.click()

    WebDriverWait(chrome_driver, 10).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "h4"))
    )

    header = chrome_driver.find_element(By.CSS_SELECTOR, "h4")
    assert header.text == "Мои заказы"


def test_check_orders(chrome_driver):
    chrome_driver.get("http://localhost:5173/")

    login = chrome_driver.find_element(By.XPATH, "//input[@id='login-username']")
    login.send_keys("AlexTest")

    password = chrome_driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("Alex2301")

    submit_btn = chrome_driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_btn.click()

    chrome_driver.find_element(By.XPATH, "//*[text()='Заказы']").click()

    WebDriverWait(chrome_driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//div/h4"))
    )

    header = chrome_driver.find_element(By.XPATH, "//div/h4")
    assert header.text == "Текущие заказы"


def test_check_ingredients(chrome_driver):
    chrome_driver.get("http://localhost:5173/")
    login = chrome_driver.find_element(By.XPATH, "//input[@id='login-username']")
    login.send_keys("AlexTest")

    password = chrome_driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("Alex2301")

    submit_btn = chrome_driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_btn.click()

    chrome_driver.find_element(By.XPATH, "//*[text()='Ингредиенты']").click()

    WebDriverWait(chrome_driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//div/h4"))
    )

    header = chrome_driver.find_element(By.XPATH, "//div/h4")
    assert header.text == "Ингредиенты"


def test_check_users(chrome_driver):
    chrome_driver.get("http://localhost:5173/")
    login = chrome_driver.find_element(By.XPATH, "//input[@id='login-username']")
    login.send_keys("AlexTest")

    password = chrome_driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("Alex2301")

    submit_btn = chrome_driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_btn.click()

    chrome_driver.find_element(By.XPATH, "//*[text()='Пользователи']").click()

    WebDriverWait(chrome_driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//div/h4"))
    )

    header = chrome_driver.find_element(By.XPATH, "//div/h4")
    assert header.text == "Пользователи"


def test_check_graphql(chrome_driver):
    chrome_driver.get("http://localhost:5173/")
    login = chrome_driver.find_element(By.XPATH, "//input[@id='login-username']")
    login.send_keys("AlexTest")

    password = chrome_driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("Alex2301")

    submit_btn = chrome_driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_btn.click()

    chrome_driver.find_element(By.XPATH, "//*[text()='GraphQL']").click()

    WebDriverWait(chrome_driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//div/h6"))
    )

    header = chrome_driver.find_element(By.XPATH, "//div/h6")
    assert header.text == "GraphQL Schema"


def test_check_grpc(chrome_driver):
    chrome_driver.get("http://localhost:5173/")
    login = chrome_driver.find_element(By.XPATH, "//input[@id='login-username']")
    login.send_keys("AlexTest")

    password = chrome_driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("Alex2301")

    submit_btn = chrome_driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_btn.click()

    chrome_driver.find_element(By.XPATH, "//*[text()='gRPC Proxy']").click()

    WebDriverWait(chrome_driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//div/h4"))
    )

    header = chrome_driver.find_element(By.XPATH, "//div/h4")
    assert header.text == "gRPC Proxy Demo"


def test_check_soap(chrome_driver):
    chrome_driver.get("http://localhost:5173/")
    login = chrome_driver.find_element(By.XPATH, "//input[@id='login-username']")
    login.send_keys("AlexTest")

    password = chrome_driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("Alex2301")

    submit_btn = chrome_driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_btn.click()

    chrome_driver.find_element(By.XPATH, "//*[text()='SOAP Proxy']").click()

    WebDriverWait(chrome_driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//div/h4"))
    )

    header = chrome_driver.find_element(By.XPATH, "//div/h4")
    assert header.text == "SOAP Proxy Demo"


def test_check_kafka(chrome_driver):
    chrome_driver.get("http://localhost:5173/")
    login = chrome_driver.find_element(By.XPATH, "//input[@id='login-username']")
    login.send_keys("AlexTest")

    password = chrome_driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("Alex2301")

    submit_btn = chrome_driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_btn.click()

    chrome_driver.find_element(By.XPATH, "//*[text()='Kafka']").click()

    WebDriverWait(chrome_driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//div/h4"))
    )

    header = chrome_driver.find_element(By.XPATH, "//div/h4")
    assert header.text == "Kafka события заказов"


def test_check_notify(chrome_driver):
    chrome_driver.get("http://localhost:5173/")
    login = chrome_driver.find_element(By.XPATH, "//input[@id='login-username']")
    login.send_keys("AlexTest")

    password = chrome_driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("Alex2301")

    submit_btn = chrome_driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_btn.click()

    chrome_driver.find_element(By.XPATH, "//*[text()='Уведомления']").click()

    WebDriverWait(chrome_driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//div/h4"))
    )

    header = chrome_driver.find_element(By.XPATH, "//div/h4")
    assert header.text == "Уведомления"


def test_check_logout(chrome_driver):
    chrome_driver.get("http://localhost:5173/")
    login = chrome_driver.find_element(By.XPATH, "//input[@id='login-username']")
    login.send_keys("AlexTest")

    password = chrome_driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("Alex2301")

    submit_btn = chrome_driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_btn.click()

    chrome_driver.find_element(By.XPATH, "//*[text()='Выход']").click()

    WebDriverWait(chrome_driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//div/h1"))
    )

    header = chrome_driver.find_element(By.XPATH, "//div/h1")
    assert header.text == "Вход в аккаунт"


def admin_auth(chrome_driver):
    chrome_driver.get("http://localhost:5173/")

    login = chrome_driver.find_element(By.XPATH, "//input[@id='login-username']")
    login.send_keys("AlexTest")

    password = chrome_driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("Alex2301")

    submit_btn = chrome_driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_btn.click()

    WebDriverWait(chrome_driver, 10).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "h4"))
    )

    header = chrome_driver.find_element(By.CSS_SELECTOR, "h4")
    assert header.text == "Мои заказы"


def test_create_order(chrome_driver):
    waiter = WebDriverWait(chrome_driver, 10)

    admin_auth(chrome_driver)

    chrome_driver.find_element(By.ID, "orders-create-btn").click()
    chrome_driver.find_element(By.XPATH, "//div[@role='combobox']").click()

    waiter.until(expected_conditions.visibility_of_all_elements_located((By.XPATH, "//ul[@role='listbox']/li")))

    ingredients = chrome_driver.find_elements(By.XPATH, "//ul[@role='listbox']/li")
    random.choice(ingredients).click()

    chrome_actions = ActionChains(chrome_driver)
    chrome_actions.send_keys(Keys.ESCAPE).perform()

    comment_input = chrome_driver.find_element(By.XPATH,
                                               "//label[text()='Комментарий к заказу']//following::textarea[1]")
    comment_input.send_keys("Alex2301")

    chrome_driver.find_element(By.XPATH, "//button[@data-testid='orders-create-confirm-btn']").click()

    waiter.until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[text()='Order created!']"))
    )


def test_create_ingredient(chrome_driver):
    waiter = WebDriverWait(chrome_driver, 10)

    admin_auth(chrome_driver)

    chrome_driver.find_element(By.XPATH, "//*[text()='Ингредиенты']").click()

    WebDriverWait(chrome_driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//div/h4"))
    )
    chrome_driver.find_element(By.XPATH, "//button[text()='+ Добавить ингредиент']").click()

    name = fake.first_name()
    chislo = fake.random_int(1, 10)
    name_ingredient = chrome_driver.find_element(By.XPATH, "//div/input[@type='text']")
    name_ingredient.send_keys(name)

    comment_input = chrome_driver.find_element(By.XPATH, "//input[@type='number']")
    comment_input.send_keys(chislo)

    chrome_driver.find_element(By.XPATH, "//button[text()='Добавить']").click()

    waiter.until(
        expected_conditions.presence_of_element_located((By.XPATH, "//*[text()='Ингредиент добавлен!']"))
    )
