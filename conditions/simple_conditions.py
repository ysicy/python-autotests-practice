# Простые условные конструкции
print("=== Простые условия ===")

# Проверка возраста для получения водительских прав
student_age = 17
print(f"Возраст студента: {student_age}")

if student_age >= 18:
    print("✓ Можно получить водительские права")
    print("✓ Доступ к курсам вождения разрешен")

print("Проверка завершена")

# Проверка наличия имени
student_name = "Анна"
print(f"\nИмя студента: '{student_name}'")

if student_name:  # Непустая строка = True
    print(f"✓ Студент: {student_name}")
else:
    print("✗ Имя студента не указано")

# Проверка с пустой строкой
empty_name = ""
print(f"\nПустое имя: '{empty_name}'")

if empty_name:
    print(f"✓ Студент: {empty_name}")
else:
    print("✗ Имя студента пустое")