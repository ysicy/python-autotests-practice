import requests
import pytest
from requests.exceptions import RequestException, Timeout, ConnectionError

# Запрос к API, который возвращает JSON
response = requests.get('https://jsonplaceholder.typicode.com/users/1')

# Проверяем успешность запроса
if response.status_code == 200:
    # Автоматически парсим JSON
    user_data = response.json()

    print(f"Имя пользователя: {user_data['name']}")
    print(f"Email: {user_data['email']}")
    print(f"Город: {user_data['address']['city']}")
else:
    print(f"Ошибка: {response.status_code}")

# Параметры запроса
params = {
    'userId': 1,
    'completed': "false"
}

print(f"\nОтправляем GET запрос с параметрами")
response = requests.get('https://jsonplaceholder.typicode.com/todos', params=params)

print(f"URL запроса: {response.url}")
# Результат: https://jsonplaceholder.typicode.com/todos?userId=1&completed=false

todos = response.json()
print(f"Найдено задач: {len(todos)}")

# Данные для отправки
new_post = {
    'title': 'Мой новый пост',
    'body': 'Содержимое поста',
    'userId': 1
}

print(f"\nОтправляем POST запрос ")
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)

if response.status_code == 201:  # 201 = Created
    created_post = response.json()
    print(f"Пост создан с ID: {created_post['id']}")
    print(f"Заголовок: {created_post['title']}")
else:
    print(f"Ошибка создания: {response.status_code}")


print(f"\nДобавляем заголовки")
headers = {
    'User-Agent': 'My Test App 1.0',
    'Accept': 'application/json',
    'Authorization': 'Bearer my-token-123'
}

response = requests.get('https://httpbin.org/headers', headers=headers)

# Смотрим заголовки ответа
print("Заголовки ответа:")
for key, value in response.headers.items():
    print(f"{key}: {value}")

# Получаем конкретный заголовок
content_type = response.headers.get('Content-Type')
print(f"Тип содержимого: {content_type}")


def safe_api_request(url):
    try:
        # Устанавливаем таймаут в 5 секунд
        response = requests.get(url, timeout=5)

        # Проверяем статус код
        response.raise_for_status()  # Вызовет исключение для 4xx и 5xx

        return response.json()

    except Timeout:
        print("Превышено время ожидания")
        return None
    except ConnectionError:
        print("Ошибка подключения")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP ошибка: {e}")
        return None
    except RequestException as e:
        print(f"Общая ошибка запроса: {e}")
        return None


print(f"\nТестируем функцию:")
data = safe_api_request('https://jsonplaceholder.typicode.com/users/1')
if data:
    print(f"Получены данные: {data['name']}")


print(f"\nРазличные HTTP методы:")
base_url = 'https://jsonplaceholder.typicode.com/posts/1'

# GET - получить данные
response = requests.get(base_url)
print(f"GET статус: {response.status_code}")

# PUT - обновить полностью
updated_data = {
    'id': 1,
    'title': 'Обновленный заголовок',
    'body': 'Обновленное содержимое',
    'userId': 1
}
response = requests.put(base_url, json=updated_data)
print(f"PUT статус: {response.status_code}")

# PATCH - частичное обновление
partial_data = {
    'title': 'Частично обновленный заголовок'
}
response = requests.patch(base_url, json=partial_data)
print(f"PATCH статус: {response.status_code}")

# DELETE - удалить
response = requests.delete(base_url)
print(f"DELETE статус: {response.status_code}")

print(f"\nТест создания и получения пользователя:")
def test_user_lifecycle():
    """Полный жизненный цикл пользователя"""
    base_url = 'https://jsonplaceholder.typicode.com'

    # 1. Создаем пользователя
    new_user = {
        'name': 'Тестовый Пользователь',
        'username': 'testuser',
        'email': 'test@example.com'
    }

    create_response = requests.post(f'{base_url}/users', json=new_user)
    assert create_response.status_code == 201

    created_user = create_response.json()
    user_id = created_user['id']

    # 2. Получаем созданного пользователя
    get_response = requests.get(f'{base_url}/users/{user_id}')
    assert get_response.status_code == 200

    retrieved_user = get_response.json()
    assert retrieved_user['name'] == new_user['name']
    assert retrieved_user['email'] == new_user['email']

    # 3. Обновляем пользователя
    updated_data = {'name': 'Обновленное Имя'}
    update_response = requests.patch(f'{base_url}/users/{user_id}', json=updated_data)
    assert update_response.status_code == 200

    # 4. Удаляем пользователя
    delete_response = requests.delete(f'{base_url}/users/{user_id}')
    assert delete_response.status_code == 200

print(f"\nТест валидации данных:")
def test_user_validation():
    """Тест валидации при создании пользователя"""
    base_url = 'https://jsonplaceholder.typicode.com'

    # Тест с пустыми данными
    empty_user = {}
    response = requests.post(f'{base_url}/users', json=empty_user)

    # В реальном API это должно вернуть 400 Bad Request
    # JSONPlaceholder всегда возвращает 201, но в реальности:
    # assert response.status_code == 400

    # Тест с невалидным email
    invalid_user = {
        'name': 'Test User',
        'email': 'invalid-email'  # Невалидный email
    }
    response = requests.post(f'{base_url}/users', json=invalid_user)
    # В реальном API: assert response.status_code == 400


print(f"\nПолезные методы объекта Response:")
response = requests.get('https://jsonplaceholder.typicode.com/users/1')

# Основные свойства
print(f"Статус код: {response.status_code}")
print(f"URL запроса: {response.url}")
print(f"Заголовки: {response.headers}")
print(f"Время выполнения: {response.elapsed}")

# Содержимое ответа
print(f"Текст: {response.text}")           # Строка
print(f"JSON: {response.json()}")          # Словарь (если JSON)
print(f"Байты: {response.content}")        # Байты

# Проверки
print(f"Успешный запрос: {response.ok}")   # True для 200-299
print(f"Есть ошибка: {response.status_code >= 400}")

# Вызвать исключение при ошибке
response.raise_for_status()  # Ничего не делает если статус OK