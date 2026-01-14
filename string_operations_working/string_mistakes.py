# Типичные ошибки при работе со строками
print("=== Изучаем типичные ошибки ===")

name = "Анна"
age = 25

# Ошибка 1: Попытка сложить строку и число
# wrong = "Мне " + age + " лет"  # Это вызовет ошибку!

# Правильные способы:
correct1 = "Мне " + str(age) + " лет"  # Превращаем число в строку
correct2 = f"Мне {age} лет"            # Используем f-строку
print("Способ 1:", correct1)
print("Способ 2:", correct2)

# Ошибка 2: Забыли про регистр при сравнении
user_input = "ДА"
expected = "да"

# Неправильное сравнение
wrong_comparison = user_input == expected
print(f"Неправильное сравнение: {wrong_comparison}")

# Правильное сравнение
correct_comparison = user_input.lower() == expected.lower()
print(f"Правильное сравнение: {correct_comparison}")

# Ошибка 3: Не учли пробелы
user_data = "  admin  "
expected_user = "admin"

wrong_check = user_data == expected_user
correct_check = user_data.strip() == expected_user

print(f"Проверка с пробелами: {wrong_check}")
print(f"Проверка без пробелов: {correct_check}")