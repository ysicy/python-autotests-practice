def add(a, b):
    return a + b

def multiply(a, b):
    """Функция для умножения двух чисел"""
    return a * b

def divide(a, b):
    """Функция для деления двух чисел"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b


def test_assertions():
    # Равенство
    assert 2 + 2 == 4
    assert "hello" == "hello"

    # Неравенство
    assert 5 != 3
    assert "cat" != "dog"

    # Больше/меньше
    assert 10 > 5
    assert 3 < 7
    assert 5 >= 5
    assert 4 <= 10

    # Проверка на True/False
    assert True
    assert not False

    # Проверка вхождения
    assert "test" in "testing"
    assert 5 in [1, 2, 3, 4, 5]

    # Проверка типов
    assert isinstance("hello", str)
    assert isinstance(42, int)

    # Проверка на None
    result = None
    assert result is None

    # Проверка длины
    assert len("hello") == 5
    assert len([1, 2, 3]) == 3

def test_add_negative_numbers():
    a =5
    b = 10

    result = add(a, b)

    assert result == 15

def test_add_positive_numbers():
        a = -2
        b = -3

        result = add(a, b)
        assert result == -5

def test_multiply_numbers():
    """Тест умножения чисел"""
    result = multiply(4, 5)
    assert result == 20

def test_divide_numbers():
    """Тест деления чисел"""
    result = divide(10, 2)
    assert result == 5.0

def test_divide_by_zero():
    """Тест деления на ноль - ожидаем исключение"""
    try:
        divide(10, 0)
        assert False, "Должно было возникнуть исключение"
    except ValueError as e:
        assert str(e) == "Деление на ноль невозможно"