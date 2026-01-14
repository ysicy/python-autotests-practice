# Циклы с функцией range()
print("=== Циклы с range() ===")

# Простой счетчик от 1 до 5
print("Счет от 1 до 5:")
for i in range(1, 6):
    print(f"Число: {i}")

print()

# Обратный счет
print("Обратный счет от 5 до 1:")
for i in range(5, 0, -1):
    print(f"Осталось: {i}")
print("Готово!")

print()

# Таблица умножения на 3
print("Таблица умножения на 3:")
for i in range(1, 6):
    result = 3 * i
    print(f"3 × {i} = {result}")

print()

# Создание списка учеников
students = []
for i in range(1, 6):
    student_name = f"Студент_{i}"
    students.append(student_name)

print("Список студентов:")
for student in students:
    print(f"- {student}")

print()

# Подсчет суммы чисел от 1 до 10
total = 0
for number in range(1, 11):
    total += number

print(f"Сумма чисел от 1 до 10: {total}")

# Работа с индексами списка
colors = ["красный", "синий", "зеленый", "желтый"]
print("\nЦвета с номерами:")
for i in range(len(colors)):
    print(f"{i + 1}. {colors[i]}")

# Четные числа от 2 до 10
print("\nЧетные числа от 2 до 10:")
for i in range(2, 11, 2):
    print(f"Четное число: {i}")