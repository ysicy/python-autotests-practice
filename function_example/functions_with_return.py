# Функции с возвращаемыми значениями
print("=== Функции с return ===")

def multiply(a, b):
    """Умножает два числа и возвращает результат"""
    return a * b

def is_adult(age):
    """Проверяет, взрослый ли человек"""
    if age >= 18:

        return True
    else:

        return False

def get_grade(score):
    """Возвращает оценку по баллам"""
    if score >= 90:
        return "Отлично"
    elif score >= 80:
        return "Хорошо"
    elif score >= 60:
        return "Удовлетворительно"
    else:
        return "Плохо"

def calculate_area(width, height):
    """Вычисляет площадь прямоугольника"""
    area = width * height
    return area

# Используем функции и сохраняем результаты
result1 = multiply(4, 5)
print(f"4 × 5 = {result1}")

result2 = multiply(3, 7)
print(f"3 × 7 = {result2}")

# Проверяем возраст
person1_adult = is_adult(25)
person2_adult = is_adult(16)

print(f"Человек 25 лет взрослый: {person1_adult}")
print(f"Человек 16 лет взрослый: {person2_adult}")

# Получаем оценки
grade1 = get_grade(95)
grade2 = get_grade(75)
grade3 = get_grade(45)

print(f"95 баллов = {grade1}")
print(f"75 баллов = {grade2}")
print(f"45 баллов = {grade3}")

# Вычисляем площади
room_area = calculate_area(5, 4)
garden_area = calculate_area(10, 8)

print(f"Площадь комнаты 5×4 = {room_area} м²")
print(f"Площадь сада 10×8 = {garden_area} м²")
