# Демонстрация операторов сравнения
print("=== Операторы сравнения ===")

# Данные студентов для сравнения
student1_name = "Анна"
student1_grade = 85
student2_name = "Иван"
student2_grade = 92
passing_grade = 60

# Проверки равенства
print("Проверки равенства:")
same_names = student1_name == student2_name
print(f"Имена одинаковые: {same_names}")

same_grades = student1_grade == student2_grade
print(f"Оценки одинаковые: {same_grades}")

# Проверки неравенства
print("\nПроверки неравенства:")
different_grades = student1_grade != student2_grade
print(f"Оценки разные: {different_grades}")

# Числовые сравнения
print("\nЧисловые сравнения:")
student1_passed = student1_grade >= passing_grade
student2_passed = student2_grade >= passing_grade
student2_better = student2_grade > student1_grade

print(f"Анна прошла курс: {student1_passed}")
print(f"Иван прошел курс: {student2_passed}")
print(f"Иван учится лучше Анны: {student2_better}")

# Сравнение строк (важно помнить про регистр!)
print("\nСравнение строк:")
language1 = "Python"
language2 = "python"
language3 = "Python"

print(f"'{language1}' == '{language2}': {language1 == language2}")  # False - регистр важен!
print(f"'{language1}' == '{language3}': {language1 == language3}")  # True
print(f"'{language1}'.lower() == '{language2}': {language1.lower() == language2}")  # True

# Практический пример - проверка возраста
print("\nПроверка возраста:")
user_age = 17
min_age = 18
can_vote = user_age >= min_age
years_to_wait = min_age - user_age if user_age < min_age else 0

print(f"Возраст пользователя: {user_age}")
print(f"Может голосовать: {can_vote}")
if not can_vote:
    print(f"Нужно подождать еще {years_to_wait} лет")