# Пример использования переменных в повседневной жизни
print("=== Информация о покупке ===")

product_name = "Ноутбук"
price = 47.500
quantity = 2
has_discount = True

#Вычисляем общую стоимость
total_cost = price * quantity
print("Товар:", product_name)
print("Цена:", price)
print("Количество:", quantity)
print("Есть скидка:", has_discount)
print("Тип переменной has_discount:", type(has_discount))

# Информация о студенте
print("\n=== Информация об успеваемости ===")
student_name = "Алексей"
math_grade = 4
physics_grade = 4
chemistry_grade = 3

# Вычисляем средний балл
average_grade = (math_grade + physics_grade + chemistry_grade) / 3
print("Студент:", student_name)
print("Математика:", math_grade)
print("Физика:", physics_grade)
print("Химия:", chemistry_grade)
print("Средний балл:", round(average_grade, 2))