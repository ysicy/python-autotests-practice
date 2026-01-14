# Циклы со словарями
# Циклы со словарями
print("=== Циклы со словарями ===")

# Простая информация о студенте
student = {
    "name": "Анна",
    "age": 20,
    "group": "ИТ-301"
}

print("Информация о студенте:")
for key, value in student.items():
    print(f"{key}: {value}")

print()

# Оценки по предметам
grades = {
    "математика": 5,
    "физика": 4,
    "химия": 5,
    "история": 3
}

print("Оценки студента:")
for subject, grade in grades.items():
    if grade == 5:
        status = "отлично"
    elif grade == 4:
        status = "хорошо"
    else:
        status = "удовлетворительно"
    print(f"{subject}: {grade} ({status})")

print()

# Подсчет статистики
excellent_count = 0
for grade in grades.values():
    if grade == 5:
        excellent_count += 1

print(f"Количество отличных оценок: {excellent_count}")

# Поиск предметов с оценкой 5
print("Предметы с отличными оценками:")
for subject, grade in grades.items():
    if grade == 5:
        print(f"- {subject}")