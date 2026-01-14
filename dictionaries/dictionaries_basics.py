# Основы работы со словарями
print("=== Создание и работа со словарями ===")

# Создание словарей
student_data = {
    "name": "Анна Петрова",
    "specialty": "Информатика",
    "course": 2,
    "scholarship": True
}

# Пустой словарь
empty_dict = {}
# Альтернативный способ создания
another_dict = dict()

print("Данные студента:")
print(student_data)
print(f"Тип данных: {type(student_data)}")

# Доступ к элементам
print(f"\nДоступ к элементам:")
print(f"Имя студента: {student_data['name']}")
print(f"Специальность: {student_data['specialty']}")
print(f"Курс: {student_data['course']}")

# Безопасный доступ с .get()
print(f"\nБезопасный доступ:")
phone = student_data.get("phone", "Не указан")
city = student_data.get("city", "Не указан")
print(f"Телефон: {phone}")
print(f"Город: {city}")

# Проверка наличия ключа
print(f"\nПроверка наличия ключей:")
has_specialty = "specialty" in student_data
has_phone = "phone" in student_data
print(f"Есть специальность: {has_specialty}")
print(f"Есть телефон: {has_phone}")

# Получение всех ключей, значений и пар
print(f"\nСодержимое словаря:")
print(f"Ключи: {list(student_data.keys())}")
print(f"Значения: {list(student_data.values())}")
print(f"Пары ключ-значение: {list(student_data.items())}")