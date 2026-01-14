import json
import allure
import pytest



class ListProcessor:
     def reverse_list(self, lst):
           return lst[::-1]

     def find_max(self, lst):
           return max(lst) if lst else None

     def remove_duplicates(self, lst):
         return list(dict.fromkeys(lst))

@pytest.fixture
def processor():
        return ListProcessor()


@allure.epic("Обработка данных")
@allure.feature("Списки")
@allure.story("Операции со списками")
class TestBasicOperations:


    @allure.title("Тест на проверку обратного порядка букв и чисел")
    @allure.severity(allure.severity_level.NORMAL)
    def test_reverse_list_numbers(self,processor):
        with allure.step("Есть готовый список из чисел и одной буквы"):
            list_numbers = [1, 2, 3, 4, "пять"]

        with allure.step("Преобразуем список в обратном порядке"):
            result = processor.reverse_list(list_numbers)

        with allure.step("Проверяем результат"):
            assert result == ["пять", 4, 3, 2, 1]


    @allure.title("Тест на проверку обратного порядка списков из букв")
    @allure.severity(allure.severity_level.NORMAL)
    def test_reverse_list_strings(self,processor):
        with allure.step("Есть список слов"):
            list_strings = ["Список раз",
                 "Список два"]
        with allure.step("Развернем список в обратную сторону"):
            reversed_list = processor.reverse_list(list_strings)

        with allure.step("Сверим результаты"):
            assert reversed_list == ["Список два", "Список раз"]


    @allure.title("Тест на проверку пустого списка")
    @allure.severity(allure.severity_level.MINOR)
    def test_empty_list(self,processor):
        with allure.step("Есть пустой список"):
            empty_list = []

        with allure.step("Развернем пустой список"):
            reversed_empty_list = processor.reverse_list(empty_list)

        with allure.step("Проверим результат"):
            assert reversed_empty_list == []


    @allure.title("Параметризованный тест на нахождение max в списке")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("numbers, expected",[
        ([1, -2, 33, 14],33),
        ([], None),
    ])
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_max_or_none(self,processor,numbers, expected):

        with allure.step(f"Используем функцию для нахождения max, используя {numbers}"):
            max_number = processor.find_max(numbers)

        allure.attach(
            f"Ожидаемый результат: {expected}\nФактический результат: {max_number}",
            attachment_type=allure.attachment_type.TEXT
        )

        with allure.step("Проверяем, так ли это"):
            assert max_number == expected


    @allure.title("Тест на проверку дубликата")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("number, expected", [
        ([1, 1, "число"], [1, "число"]),
        (["тоже число", 44, 44], ["тоже число", 44]),
    ])
    def test_search_dublicate(self, processor, number, expected):

        with allure.step(f"Используем функцию для нахождения дубликата"):
            unique_number = processor.remove_duplicates(number)

        allure.attach(
            f"Ожидаемый результат:Число: {expected} \nФактический результат: {unique_number}",
            name="Детали",
            attachment_type=allure.attachment_type.TEXT
        )

        with allure.step("Проверяем так ли это"):
            assert unique_number == expected


#Параметризованный тест
@allure.feature("Валидация")
@allure.title("Параметризованный тест на проверку строки")
@allure.story("Проверка является ли строка текстом")
@pytest.mark.parametrize("strings, expected", [
    ("тест", True),
    ('@', True),
    (1, False),
    (-2, False),
    (0, False),
])
def test_its_true_or_false(strings, expected):
    with allure.step(f"Является ли {strings} текстом"):
        result = isinstance(strings, str)

        allure.attach(
            f"Значение: {strings}\nОжидаемый результат: {expected}\nФактический результат: {result}",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step("Проверяем с ожидаемым результатом"):
        assert result == expected

@allure.title("Проверим JSON вложения")
@allure.severity(allure.severity_level.NORMAL)
def test_check_test_data():
    user = {
        "name": "Jordan Weal",
        "age": 33,
        "city": "Moscow",
        "from_country": "US",
        "player": "Dynamo",
        "liga": ["NHL", "KHL"]
    }

    with allure.step(f"Есть у нас пользователь: {user['name']}. Проверим его данные."):
        allure.attach(
            json.dumps(user, indent=2),
            name="Данные хоккеиста",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Проверяем структуру"):
        assert "name" in user
        assert "age" in user
        assert user["city"] == "Moscow"
        assert user["from_country"] == "US"
        assert user["player"] == "Dynamo"
        assert isinstance(user["liga"], list)
        assert "NHL" in user["liga"]
        assert "KHL" in user["liga"]




