# Основы циклов for
print("=== Простые циклы со списками ===")

# Список покупок
shopping_list = ["хлеб", "молоко", "яйца", "сыр", "яблоки"]

print("Список покупок:")
for item in shopping_list:
    print(f"  Купить: {item}")

print("\nПокупки завершены!")

# Список оценок студентов
grades = [5, 4, 5, 3, 4]
subjects = ["Математика", "Физика", "Химия", "История", "Литература"]

print(f"\n=== Анализ оценок ===")
for i in range(len(subjects)):
    subject = subjects[i]
    grade = grades[i]
    if grade == 5:
        status = "✅ ОТЛИЧНО"
    elif grade == 4:
        status = "👍 ХОРОШО"
    else:
        status = "⚠️ УДОВЛЕТВОРИТЕЛЬНО"
    print(f"{subject}: {grade} ({status})")

# Более элегантный способ с zip()
print(f"\n=== Анализ оценок (элегантный способ) ===")
for subject, grade in zip(subjects, grades):
    status = "✅ ОТЛИЧНО" if grade == 5 else "👍 ХОРОШО" if grade == 4 else "⚠️ УДОВЛЕТВОРИТЕЛЬНО"
    print(f"{subject}: {grade} ({status})")

# Подсчет статистики
excellent_count = 0
good_count = 0
satisfactory_count = 0

for grade in grades:
    if grade == 5:
        excellent_count += 1
    elif grade == 4:
        good_count += 1
    else:
        satisfactory_count += 1

total_subjects = len(grades)
average_grade = sum(grades) / total_subjects

print(f"\n=== Статистика успеваемости ===")
print(f"Всего предметов: {total_subjects}")
print(f"Отличных оценок: {excellent_count}")
print(f"Хороших оценок: {good_count}")
print(f"Удовлетворительных оценок: {satisfactory_count}")
print(f"Средняя оценка: {average_grade:.1f}")