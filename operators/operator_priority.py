# Приоритет операторов и использование скобок
print("=== Приоритет операторов ===")

# Арифметические операторы имеют приоритет
result1 = 2 + 3 * 4  # Сначала умножение, потом сложение
print(f"2 + 3 * 4 = {result1}")  # Результат: 14

result2 = (2 + 3) * 4  # Скобки меняют приоритет
print(f"(2 + 3) * 4 = {result2}")  # Результат: 20

# Логические операторы тоже имеют приоритет
# Порядок: not, and, or
a = True
b = False
c = True

result3 = a or b and c  # Сначала and, потом or
print(f"True or False and True = {result3}")  # True

result4 = (a or b) and c  # Скобки меняют порядок
print(f"(True or False) and True = {result4}")  # True

# Практический пример
user_age = 20
is_student = True
has_id = False

# Без скобок (может быть неочевидно)
can_enter1 = user_age >= 18 or is_student and has_id
print(f"Может войти (без скобок): {can_enter1}") #True

# Со скобками (понятнее)
can_enter2 = user_age >= 18 or (is_student and has_id)
print(f"Может войти (со скобками): {can_enter2}") #True

# Еще более понятный вариант
adult = user_age >= 18
student_with_id = is_student and has_id
can_enter3 = adult or student_with_id
print(f"Может войти (с переменными): {can_enter3}")