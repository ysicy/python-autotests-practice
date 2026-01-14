# Сложные условия с логическими операторами
print("=== Сложные условия ===")

# Проверка права на скидку в магазине - покупатель 1
age = 65
is_student = False
is_pensioner = True
purchase_amount = 2000

print(f"Покупатель 1:")
print(f"  Возраст: {age}")
print(f"  Студент: {is_student}")
print(f"  Пенсионер: {is_pensioner}")
print(f"  Сумма покупки: {purchase_amount} руб.")

if is_pensioner and age >= 60:
    print("✓ Скидка 15% (пенсионер)")
elif is_student and age <= 25:
    print("✓ Скидка 10% (студент)")
elif purchase_amount >= 5000 and age >= 18:
    print("✓ Скидка 5% (крупная покупка)")
elif age < 18 and purchase_amount >= 1000:
    print("✓ Скидка 3% (детская скидка)")
else:
    print("✓ Скидка 2% (базовая)")

# Проверка кредита - одобрен
print("=== Проверка кредита ===")
age = 30
income = 60000
has_job = True
credit_history = "отличная"
loan_amount = 500000

print(f"Заявка на кредит:")
print(f"  Возраст: {age} лет")
print(f"  Доход: {income} руб/мес")
print(f"  Есть работа: {has_job}")
print(f"  Кредитная история: {credit_history}")

if age < 18 or age > 65:
    print("❌ Отказ: Возраст не подходит")
elif not has_job:
    print("❌ Отказ: Нет работы")
elif credit_history == "плохая":
    print("❌ Отказ: Плохая история")
elif credit_history == "отличная" and income >= 50000:
    print("✅ Одобрен под 8.5% (отличные условия)")
elif credit_history == "хорошая" and income >= 30000:
    print("✅ Одобрен под 12.0% (хорошие условия)")
elif income >= 20000:
    print("✅ Одобрен под 15.5% (стандартные условия)")
else:
    print("❌ Отказ: Недостаточный доход")