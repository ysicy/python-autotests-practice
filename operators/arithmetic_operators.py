# Демонстрация арифметических операторов
print("=== Арифметические операторы ===")

monthly_salary = 50000
rent = 15000
food = 12000
transport = 5000

#Основные операторы
# Основные операции
print("Семейный бюджет:")
print(f"Зарплата: {monthly_salary} руб.")
print(f"Аренда: {rent} руб.")
print(f"Еда: {food} руб.")
print(f"Транспорт: {transport} руб.")

#Вычислим общие расходы
total_express = rent + food + transport
print(f"\nОбщие расходы: {rent} + {food} + {transport} = {total_express} руб.")

#Остаток
remaining_money = monthly_salary - total_express
print(f"Остается: {monthly_salary} - {total_express} = {remaining_money} руб.")

#Вычислим проценты
expenses_percentage = (total_express / monthly_salary) * 100
savings_percentage = (remaining_money / monthly_salary) * 100

print(f"\nСтатистика")
print(f"Тратим: {expenses_percentage:.1f}% от зарплаты")
print(f"Экономим: {savings_percentage:.1f}% от зарплаты ")

# Работа с остатком от деления и степенями
print(f"\nДополнительные операции:")
print(f"Остаток от деления 100 на 7: {100 % 7}")
print(f"Целочисленное деление 100 на 7: {100 // 7}")
print(f"2 в степени 8: {2 ** 8}")

