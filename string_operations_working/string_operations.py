# Демонстрация работы со строками
print("=== Конкатенация строк ===")

# Способ 1: Оператор +
first_name = "Мария"
last_name = "Иванова"
full_name = first_name + " " + last_name
print("Полное имя:", full_name)

# Способ 2: F-строки (рекомендуемый)
age = 32
city = "Moscow"
info = f"Меня зовут {full_name}, мне {age}, и я из {city}"
print("\nОбщая информация: ", info)

# F-строки с вычислениями
current_year = 2025
birth_year = current_year - age
message = f"{first_name} родилась в {birth_year} году"
print("\nСообщение: ", message)

print("\n=== Методы строк ===")
# Исходная строка
user_input = "  ПРИВЕТ, МИР!  "
print("Исходная строка:", f"'{user_input}'")
# Метод .lower() - все буквы строчные
lowercase = user_input.lower()
print("Нижний регистр:", f"'{lowercase}'")

# Метод .upper() - все буквы заглавные
uppercase = user_input.upper()
print("Верхний регистр:", f"'{uppercase}'")

# Метод .strip() - убирает пробелы по краям
cleaned = user_input.strip()
print("Без лишних пробелов:", f"'{cleaned}'")

# Можно комбинировать методы
final_result = user_input.strip().lower()
print("Очищено и в нижнем регистре:", f"'{final_result}'")