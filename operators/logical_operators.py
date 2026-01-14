# Демонстрация логических операторов
print("=== Логические операторы ===")

# Данные пользователя для проверки доступа
user_age = 25
is_registered = True
has_premium = False
is_admin = False

# Оператор AND - все условия должны быть True
print("Оператор AND:")
can_access_content = user_age >= 18 and is_registered
print(f"Может получить доступ к контенту: {can_access_content}")

can_access_premium = is_registered and has_premium
print(f"Может получить доступ к премиум контенту: {can_access_premium}")

# Оператор OR - хотя бы одно условие должно быть True
print("\nОператор OR:")
gets_discount = user_age < 18 or user_age > 65
print(f"Получает скидку (младше 18 или старше 65): {gets_discount}")

has_special_access = has_premium or is_admin
print(f"Имеет специальный доступ: {has_special_access}")

# Оператор NOT - инвертирует результат
print("\nОператор NOT:")
is_adult = not (user_age < 18)
print(f"Является взрослым: {is_adult}")

is_regular_user = not (has_premium or is_admin)
print(f"Обычный пользователь: {is_regular_user}")

# Сложные условия
print("\nСложные условия:")
can_post_comment = is_registered and (user_age >= 13) and not is_admin
print(f"Может оставлять комментарии: {can_post_comment}")

needs_verification = (not is_registered) or (user_age < 18 and not has_premium)
print(f"Нужна дополнительная верификация: {needs_verification}")