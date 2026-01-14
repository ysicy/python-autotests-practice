import allure
import json
import pytest

#Запуск тестов:
# Запуск всех тестов с сохранением результатов для Allure
#pytest --alluredir=allure-results

# Запуск с подробным выводом
#pytest --alluredir=allure-results -v

#Генерация и просмотр отчета:
# Генерация отчета и автоматическое открытие в браузере
#allure serve allure-results

# Или генерация в папку (для ручного открытия)
#allure generate allure-results --output allure-report --clean


@allure.feature("Калькулятор")
@allure.story("Базовые операции")
def test_addiction():
    result = 2 + 3
    assert result == 5

@allure.feature("Калькулятор")
@allure.story("Базовые операции")

def test_multiplication():
    result = 10 * 3
    assert result == 30

@allure.feature("Строковые операции")
@allure.story("Деление")
def test_division():
    result = 10 / 3
    rounded_result = round(result, 1)
    assert rounded_result == 3.3

@allure.feature("Строковые операции")
@allure.title("Проверка сложения положительных чисел")
def test_positive_addiction():
    assert 2 + 2 == 4

@allure.feature("Строковые операции")
@allure.title("Проверка вычитания положительных чисел")
def test_negative_addiction():
    assert 2 - 2 == 0

@allure.feature("Строковые операции")
@allure.description("Тест написан на проверку корректности функции деления."
                    "Плюсом учусь писать красивые аннотации для руководителей, чтобы меньше вопросов задавали"
                    "Тоже мне , питоны ссаные")
def test_addiction():
    assert 10 / 2 == 5


#Простые шаги:
def test_user_registration():
    with allure.step("Открываем форму регистрации"):
        # Здесь был бы код открытия формы
        form_opened = True
        assert form_opened

    with allure.step("Заполняем обязательные поля"):
        username = "testuser"
        email = "test@example.com"
        password = "password123"
        assert len(username) > 0
        assert "@" in email
        assert len(password) >= 8

    with allure.step("Нажимаем кнопку 'Зарегистрироваться'"):
        # Здесь был бы код нажатия кнопки
        registration_success = True
        assert registration_success

    with allure.step("Проверяем успешную регистрацию"):
        success_message = "Регистрация прошла успешно"
        assert "успешно" in success_message


#Шаги с параметрами:
def calculate_discount(price, discount_percent):
    return price * (1 - discount_percent / 100)

@allure.feature("Скидки")
@allure.story("Расчет скидки")
def test_discount_calculation():
    original_price = 1000
    discount = 20

    with allure.step(f"Применяем скидку {discount}% к цене {original_price} руб"):
        result = calculate_discount(original_price, discount)

    with allure.step(f"Проверяем, что итоговая цена равна {original_price * 0.8} руб"):
        expected_price = 800
        assert result == expected_price


#Вложенные шаги:
def test_shopping_cart():
    with allure.step("Подготовка корзины покупок"):
        cart = []

        with allure.step("Создаем пустую корзину"):
            assert len(cart) == 0

        with allure.step("Добавляем первый товар"):
            cart.append({"name": "Книга", "price": 500})
            assert len(cart) == 1

        with allure.step("Добавляем второй товар"):
            cart.append({"name": "Ручка", "price": 50})
            assert len(cart) == 2

    with allure.step("Расчет итоговой суммы"):
        total = sum(item["price"] for item in cart)

        with allure.step("Проверяем корректность суммы"):
            assert total == 550


#Добавление вложений
def test_text_processing():
    text = "Hello, World!"

    with allure.step("Обрабатываем текст"):
        processed_text = text.upper()

        # Добавляем исходный текст как вложение
        allure.attach(
            text,
            name="Исходный текст",
            attachment_type=allure.attachment_type.TEXT
        )

        # Добавляем обработанный текст
        allure.attach(
            processed_text,
            name="Обработанный текст",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Проверяем результат"):
        assert processed_text == "HELLO, WORLD!"


#JSON вложения:
def test_data_processing():
    user_data = {
        "name": "Иван Петров",
        "age": 30,
        "city": "Москва",
        "skills": ["Python", "Testing", "Automation"]
    }

    with allure.step("Обрабатываем данные пользователя"):
        # Добавляем данные как JSON вложение
        allure.attach(
            json.dumps(user_data, ensure_ascii=False, indent=2),
            name="Данные пользователя",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверяем структуру данных"):
        assert "name" in user_data
        assert "age" in user_data
        assert isinstance(user_data["skills"], list)


#Полный пример с группировкой
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль")
        return a / b


@pytest.fixture
def calculator():
    return Calculator()


@allure.epic("Математические операции")
@allure.feature("Калькулятор")
@allure.story("Базовые операции")
class TestBasicOperations:

    @allure.title("Тест сложения двух чисел")
    @allure.description("Проверяем корректность сложения положительных чисел")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_addition(self, calculator):
        with allure.step("Подготавливаем числа для сложения"):
            a, b = 5, 3
            allure.attach(f"a = {a}, b = {b}", name="Входные данные",
                          attachment_type=allure.attachment_type.TEXT)

        with allure.step("Выполняем сложение"):
            result = calculator.add(a, b)

        with allure.step("Проверяем результат"):
            expected = 8
            allure.attach(f"Ожидаемый результат: {expected}, Фактический: {result}",
                          name="Сравнение результатов",
                          attachment_type=allure.attachment_type.TEXT)
            assert result == expected

    @allure.title("Тест вычитания чисел")
    @allure.severity(allure.severity_level.CRITICAL )
    def test_subtraction(self, calculator):
        with allure.step("Подготавливаем числа для вычитания"):
            a, b = 10, 4

        with allure.step("Выполняем вычитание"):
            result = calculator.subtract(a, b)

        with allure.step("Проверяем результат"):
            assert result == 6


@allure.epic("Математические операции")
@allure.feature("Калькулятор")
@allure.story("Продвинутые операции")
class TestAdvancedOperations:

    @allure.title("Тест деления чисел")
    @allure.severity(allure.severity_level.NORMAL )
    def test_division(self, calculator):
        with allure.step("Выполняем деление"):
            result = calculator.divide(10, 2)

        with allure.step("Проверяем результат"):
            assert result == 5.0

    @allure.title("Тест деления на ноль")
    @allure.severity(allure.severity_level.NORMAL)
    def test_division_by_zero(self, calculator):
        with allure.step("Пытаемся разделить на ноль"):
            with pytest.raises(ValueError, match="Деление на ноль"):
                calculator.divide(10, 0)


# Параметризованный тест с Allure
@allure.feature("Валидация")
@allure.story("Проверка четности")
@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, False),
    (0, True),
    (-2, True),
    (-3, False),
])
def test_is_even(number, expected):
    allure.dynamic.title(f"Проверка четности числа {number}")

    with allure.step(f"Проверяем четность числа {number}"):
        result = number % 2 == 0

        allure.attach(
            f"Число: {number}\nОжидаемый результат: {expected}\nФактический результат: {result}",
            name="Детали проверки",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Сравниваем с ожидаемым результатом"):
        assert result == expected