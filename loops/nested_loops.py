# Простые вложенные циклы
print("=== Простые вложенные циклы ===")

# Рисуем прямоугольник из звездочек
print("Прямоугольник 3×3:")
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()  # переход на новую строку

print()

# Счетчик с двумя циклами
print("Парные числа:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()

print()

# Простая таблица умножения 2×2
print("Маленькая таблица умножения:")
for i in range(2, 4):  # 2 и 3
    for j in range(2, 4):  # 2 и 3
        result = i * j
        print(f"{i}×{j}={result}", end="  ")
    print()

print()

# Дни недели и дела
week_tasks = {
    "понедельник": ["учеба", "спорт"],
    "вторник": ["работа", "покупки"],
    "среда": ["встреча", "кино"]
}

print("План на неделю:")
for day, tasks in week_tasks.items():
    print(f"{day}:")
    for task in tasks:
        print(f"  - {task}")

print()

# Подсчет всех дел
total_tasks = 0
for tasks in week_tasks.values():
    for task in tasks:
        total_tasks += 1

print(f"Всего дел запланировано: {total_tasks}")

# Простой поиск
search_task = "спорт"
for day, tasks in week_tasks.items():
    for task in tasks:
        if task == search_task:
            print(f"'{search_task}' запланирован на {day}")