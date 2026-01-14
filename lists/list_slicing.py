# Срезы списков - получение части списка
print("=== Срезы списков ===")

# Список всех месяцев
months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
print(f"Все месяцы: {months}")

# Базовые срезы
print(f"\nБазовые срезы:")
first_three = months[0:3]  # Элементы с 0 по 2 (3 не включается!)
print(f"Первые три месяца [0:3]: {first_three}")

last_three = months[-3:]  # Последние три элемента
print(f"Последние три месяца [-3:]: {last_three}")

middle_months = months[4:7]  # Элементы с индекса 4 по 6
print(f"Средние месяцы [4:7]: {middle_months}")

# Срезы с шагом
print(f"\nСрезы с шагом:")
every_second = months[::2]  # Каждый второй элемент
print(f"Каждый второй месяц [::2]: {every_second}")

reversed_months = months[::-1]  # Обращение списка
print(f"Обращенный список [::-1]: {reversed_months}")

# Практический пример: разделение месяцев по сезонам
winter_months = months[11:] + months[:2]  # Декабрь, январь, февраль
spring_months = months[2:5]  # Март, апрель, май
summer_months = months[5:8]  # Июнь, июль, август
autumn_months = months[8:11]  # Сентябрь, октябрь, ноябрь

print(f"\nГруппировка по сезонам:")
print(f"Зима: {winter_months}")
print(f"Весна: {spring_months}")
print(f"Лето: {summer_months}")
print(f"Осень: {autumn_months}")