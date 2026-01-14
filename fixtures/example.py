# def test_user_creation():
#     #Подготовка данных
#     database = connect_to_database()
#     user_data = {"name": "John", "email": "john@example.com"}
#
#     #Тест
#     user = create_user(user_data)
#     assert user.name == "John"
#
#     #Очистка
#     database.delete_user(user.id)
#     database.close()
#
#
# def test_user_update():
#     #ПОдготавливаем данные
#     database = connect_to_database()
#     user_data = {"name": "John", "email": "john@example.com"}
#     user = create_user(user_data)
#
#     #Тест
#     updated_user = update_user(user.id, {"name": "Don John"})
#     assert updated_user.name == "Don John"
#
#     #Снова очищаем - обязательно
#     database.delete_user(user.id)
#     database.close()

# @pytest.fixture
# def database():
#     """Фикстура для подключения к базе данных"""
#     db = connect_to_database()
#     yield db  # Возвращаем ресурс
#     db.close()  # Автоматическая очистка
#
# @pytest.fixture
# def sample_user(database):
#     """Фикстура для создания тестового пользователя"""
#     user_data = {"name": "John", "email": "john@example.com"}
#     user = create_user(user_data)
#     yield user  # Возвращаем пользователя
#     database.delete_user(user.id)  # Автоматическая очистка
#
# def test_user_creation(sample_user):
#     """Тест использует фикстуру - код стал чище!"""
#     assert sample_user.name == "John"
#     assert sample_user.email == "john@example.com"
#
# def test_user_update(sample_user, database):
#     """Еще один тест с теми же фикстурами"""
#     updated_user = update_user(sample_user.id, {"name": "Jane"})
#     assert updated_user.name == "Jane"
#     assert database.get_by_id(updated_user.id).name == "Jane"

import os
import tempfile
import pytest

@pytest.fixture
def sample_data():
    return {
        "users": ["Леша", "Саня", "Димон"],
        "numbers": [1, 2, 3, 4, 5],
        "config": {"debug": True, "timeout": 20}
    }

def test_users_count(sample_data):
    assert len(sample_data["users"]) == 3

def test_sum_numbers(sample_data):
    assert sum(sample_data["numbers"]) == 15

def test_check_config(sample_data):
    assert sample_data["config"]["timeout"] == 20

def test_check_debug(sample_data):
    assert sample_data["config"]["debug"] == True

@pytest.fixture
def temp_file():
    file = tempfile.NamedTemporaryFile(mode="w", delete=False)
    file.write("Test data")
    file.close()

    yield file.name

    os.unlink(file.name)

def test_file_read(temp_file):
    with open(temp_file, "r") as f:
        content = f.read()
        assert content == "Test data"

def test_file_exists(temp_file):
    assert os.path.exists(temp_file)

@pytest.fixture
def return_ints():
    return [1, 2, 3, 4, 5]

def test_return_ints(return_ints):
    assert return_ints == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (4, 5, 20),
    (3, 3, 9),
])

def test_multiply(a, b, expected):
    result = (a * b)
    assert result == expected