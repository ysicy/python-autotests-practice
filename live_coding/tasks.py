# БЛОК 1. Python core / алгоритмы (обязательно)
#
# Задачи:
# Найти дубликаты в списке чисел
# Вход: [1,2,3,2,4,1]
# Выход: {1,2}
from shlex import split


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
#
# Найти первое неповторяющееся значение в строке
# "aabbccd" → "d"
#
# Проверить валидность скобочной последовательности
# "(()())" → True
#
# Удалить все дубликаты символов из строки
# "banana" → "ban"
#
# Найти самое длинное слово в строке
#
# На что смотрят:
# методы строк
# аккуратность
# edge cases ("", None)
#
# БЛОК 3. Работа с файлами / данными
#
# Задачи:
# Прочитать текстовый файл и посчитать количество строк
#
# Прочитать JSON и проверить наличие обязательных ключей
# (id, name, email)
#
# Прочитать CSV и посчитать количество строк, где status = "ERROR"
#
# Записать словарь в JSON-файл
#
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
#
# Использовать параметризацию для проверки нескольких кейсов
#
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