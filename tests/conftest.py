import pytest
import requests
from playwright.sync_api import expect


@pytest.fixture(scope="session")
def my_admin_login():
    test_data = {
        "username": "AlexTest",
        "password": "Alex2301"
    }

    response = requests.post("http://localhost:8080/api/auth/login", json=test_data)
    token = response.json()['token']
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture()
def create_user(my_admin_login):
    test_data = {
        "username": "AlexQ",
        "email": "alex@ru",
        "password": "Andrew123"
    }
    response = requests.post("http://localhost:8080/api/auth/register", json=test_data)
    user =  response.json()

    yield user

    requests.delete(
        f"http://localhost:8080/api/users/{user['id']}",
        headers=my_admin_login
    )

def admin_auth_playwright(page):
    """Функция авторизации администратора"""
    page.goto("http://localhost:5173/")

    # Заполняем форму авторизации
    page.fill("#login-username", "admin")
    page.fill("#login-password", "admin")
    page.click("#login-submit")

    # Ждем появления заголовка и проверяем его
    header = page.locator("h4")
    expect(header).to_have_text("Мои заказы")
