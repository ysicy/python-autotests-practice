# БЛОК 1. Python core / алгоритмы (обязательно)
#
# Задачи:
# Найти дубликаты в списке чисел
# Вход: [1,2,3,2,4,1]
# Выход: {1,2}
import json

import pytest


def find_duplicates(lst):
    seen = set()  # Множество для уже увиденных чисел
    duplicates = set()  # Множество для дубликатов

    for number in lst:
        if number in seen:  # Если уже видели это число
            duplicates.add(number)  # Добавляем в дубликаты
        else:
            seen.add(number)  # Иначе добавляем в увиденные

    return duplicates


print(find_duplicates([1, 2, 3, 2, 4, 1]))  # Вывод: {1, 2}

# Подсчитать количество каждого символа в строке
# "hello world" → {'h':1,'e':1,'l':3,...}
def count_symbols(string):
    slovar = {}
    for i in string:
        if i in slovar:
            slovar[i] = slovar[i] + 1
        else:
            slovar[i] = 1
    return slovar
print(count_symbols("hello world"))

# Отфильтровать только уникальные элементы, сохранив порядок
# [1,2,2,3,1] → [1,2,3]
def check_unique(lst):
    unique = []
    for number in lst:
        if number not in unique:
            unique.append(number)
    print(unique)

check_unique([1,2,2,3,1])
# Найти второй по величине элемент в списке
# (с учетом дублей)
def check_second_max(lst):
    if not lst or len(lst) < 2:
        return None
    max_number = max(lst)
    second_max = None
    for number in lst:
        if number < max_number:
            if second_max is None or number > second_max:
                second_max = number

    return second_max
print(check_second_max([1, 2, 4, 6, 1]))
print(check_second_max([6, 6, 5, 4]))
print(check_second_max([5, 5, 5, 5]))
print(check_second_max([1]))
print(check_second_max([]))
print(check_second_max([-5, -5, -10]))


# Проверить, что список отсортирован по возрастанию
def check_sort_list(lst):
    if len(lst) <= 1:
        return True
    for i in range(len(lst) - 1):
        current = lst[i]
        next_ = lst[i + 1]
        if current > next_:
            return False
    else:
        return True

print(check_sort_list([2, 3, 4, 6, 3]))
print(check_sort_list([]))
print(check_sort_list([5]))
print(check_sort_list([1,2,3,4]))
print(check_sort_list([1,2,1,4]))
print(check_sort_list([7, 7, 7, 7]))
print(check_sort_list(["a", "h", "c"]))
print(check_sort_list(["a", "b", "c"]))



# Сгруппировать список слов по первой букве
# ["cat","car","dog"] → {"c":["cat","car"],"d":["dog"]}
def check_first_symbol(lst):
    new_lst = {}
    for i in range(len(lst)):
        first_str = lst[i]
        first_symbol = first_str[0]
        if first_symbol in new_lst:
            new_lst[first_symbol].append(first_str)
        else:
            new_lst[first_symbol] = [first_str]

    return new_lst

print(check_first_symbol(["cat","car","dog"]))

# На что смотрят:
# чистота кода
# использование стандартных структур
# обработка пустых входных данных
#
# БЛОК 2. Работа со строками
# Задачи:
# Проверить, является ли строка палиндромом
# (игнорируя регистр и пробелы)
def is_palindrome(string: str) -> bool:
    s = string.lower()
    only_chrs = [ch for ch in s if ch.isalnum()]
    only_str = ''.join(only_chrs)
    return only_str == only_str[::-1]
print(is_palindrome("У лип Лёша нашёл пилу"))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Madam, I'm Adam"))
print(is_palindrome(""))
assert is_palindrome("a") == True
assert is_palindrome(" ") == True

# Найти первое неповторяющееся значение в строке
# "aabbccd" → "d"
def one_symbol_only(s):
    count = {}
    for char in s:
        if char in count:
            count[char]+=1
        else:
            count[char]=1
    for char in s:
        if count[char] == 1:
            return char

    return None

print(one_symbol_only("aabbccd"))
print(one_symbol_only("aabbcc"))
print(one_symbol_only("abc"))
print(one_symbol_only(""))

# Проверить валидность скобочной последовательности
# "(()())" → True
def is_correct_bracket(text):
    total_=0
    for symbol in text:
        if symbol=='(':
            total_+=1
        elif symbol==')':
            total_-=1
            if total_<0:
                return False
    if total_==0:
        return True
    else:
        return False


print(is_correct_bracket("(()())"))
# Удалить все дубликаты символов из строки
# "banana" → "ban"
def delete_duplicates(s):
    original = ''
    for symbol in s:
        if symbol not in original:
            original+=symbol
    return original
print(delete_duplicates("banana"))

# Найти самое длинное слово в строке
# "Hello my friend" - "friend"
def find_longest_string(s):
    max_length = 0
    longest_word = ""
    for word in s.split():
        clean_word = ''.join(ch for ch in word if ch.isalnum())
        if len(clean_word) > max_length:
            max_length = len(clean_word)
            longest_word = clean_word
    return longest_word

print(find_longest_string("Hello my friend!"))
print(find_longest_string("cat dog fox"))

# На что смотрят:
# методы строк
# аккуратность
# edge cases ("", None)
#
# БЛОК 3. Работа с файлами / данными
#
# Задачи:
# Прочитать текстовый файл и посчитать количество строк
def read_and_count_lines_in_file(file_path):
    with open(file_path, "r",encoding="utf-8") as file:
        lines = file.readlines()
        return f"Количество строк в файле: {len(lines)}"
        # for i, line in enumerate(lines):
        #     print(f"Строка {i+1}: {line}")

count = read_and_count_lines_in_file("live_coding/test.txt")
print(count)
# Прочитать JSON и проверить наличие обязательных ключей
# (id, name, email)
def check_keys_in_json(file_path) -> bool:
    try:
        with open(file_path, "r",encoding="utf-8") as file:
            data = json.load(file)

            required = ["id", "name", "email"]
            for key in required:
                if key not in data:
                    print(f"Missing key {key} in json file")
                    return False

            return True

    except FileNotFoundError:
        print(f"json file not found: {file_path}")
        return False
    except json.JSONDecodeError:
        print("Invalid json file")
        return False
check_keys_in_json("live_coding/user_data.json")


#
# Прочитать CSV и посчитать количество строк, где status = "ERROR"
#
# Записать словарь в JSON-файл
def record_to_json(file_path):
    data = {'title': 'AlexTEst', 'bim': "bam"}
    try:
        with open(file_path, "r",encoding="utf-8") as file:
            current_adata = json.load(file)
        current_adata.update(data)

        with open(file_path, "w",encoding="utf-8") as file:
            json.dump(current_adata, file,  indent=4)
        print("JSON файл обноввлен")
        return True
    except FileNotFoundError as e:
        print(f"not found file, error: {e}")
        return False
    except Exception as e:
        print(e)
        return False


record_to_json("live_coding/user_data.json")




# Найти самое частое значение в колонке CSV
#
# На что смотрят:
# базовый I/O
# обработка ошибок
# аккуратность
#
# БЛОК 4. Pytest / тест-дизайн
#
# Задачи:
#
# Написать pytest-тест для функции add(a, b)
def add(a, b):
    return a + b
class TestAddFunction:

    def test_add(self):
        assert add(2,4) == 6
        assert add(3,7) == 10
        assert add(0.1,0.2) == pytest.approx(0.3)

# Использовать параметризацию для проверки нескольких кейсов
    @pytest.mark.parametrize("a, b, result",[
        (3,5,8),
        (-3,-4,-7),
        (7,7,14),
        (0.2, 0.4, pytest.approx(0.6))
    ])
    def test_add_parametrize(self,a,b,result):
        assert add(a,b) == result

    def test_negative(self):
        assert add(-2,4) == 2
        assert add(-3,7) == 4

    def test_zero(self):
        assert add(0,0) == 0




# Создать фикстуру, возвращающую тестового пользователя
#
# Протестировать функцию, которая может выбросить исключение
#
# Замокать функцию, возвращающую текущее время (time.time)
#
# На что смотрят:
# структуру теста
# фикстуры
# читаемость
#
# БЛОК 5. API тесты (очень важно)
#
# Задачи:
# Написать тест на GET-запрос
# Проверить:
# статус
# тип данных
# обязательные поля
#
# Написать тест на POST-запрос (создание сущности)
#
# Проверить негативный кейс (401 / 400)
#
# Проверить, что данные реально создались (GET после POST)
#
# Использовать фикстуру для авторизации
#
# На что смотрят:
# структура теста
# осмысленные проверки
# отсутствие print вместо assert
#
# БЛОК 6. SQL (часто спрашивают)
#
# Задачи:
# Найти всех пользователей старше 18 лет
# Посчитать количество заказов для каждого пользователя
#
# Найти пользователя с максимальным количеством заказов
# JOIN пользователей и заказов
#
# Найти записи, которых нет в другой таблице
#
# На что смотрят:
# JOIN
# GROUP BY
# логика, а не синтаксические фокусы

# БЛОК 7. UI automation (Selenium / Playwright)
#
# Задачи:
# Написать сценарий логина на сайт
#
# Проверить, что после логина отображается имя пользователя
#
# Кликнуть кнопку и проверить изменение текста
#
# Найти все ссылки на странице и проверить, что их больше N
#
# Реализовать ожидание элемента (не sleep)
#
# На что смотрят:
# локаторы
# ожидания
# стабильность
#
# БЛОК 8. Edge cases / мышление QA
#
# Задачи:
# Функция принимает список — что будет, если:
#
# список пуст
# None
# один элемент
#
# API возвращает 200, но тело пустое — что проверять?
#
# UI элемент есть в DOM, но не видим — как обработать?
#
# Что проверять кроме status_code == 200?