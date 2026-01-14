# Пример использования строк в повседневной жизни
print("=== Обработка анкеты студента ===")

# Данные студента (как будто введены пользователем)
student_name = "Иван Петров"
university = "МГУ"
course = " Информатика "
year = 2
# Обработка данных для красивого вывода
cleaned_name = student_name.strip().title()
cleaned_course = course.strip()

print("\nИсходные данные студента:")
print(f" Имя:'{student_name}'")
print(f" Университет:'{university}'")
print(f" Курс:'{course}'")
print(f" Год обучения:'{year}'")

print("\nОбработанные данные")
print(f" Имя:{cleaned_name}")
print(f" Университет:{university}")
print(f" Курс:{cleaned_course}")
print(f" Год обучения:{year} ")

# Создание красивого сообщения с помощью f-строк
welcome_message = f" Добро пожаловать, {cleaned_name}!"
info_message = f"Вы учитесь в {university} на {year} курсе, по специальности '{cleaned_course}'"

print(f"\n=== Приветствие ===")
print(welcome_message)
print(info_message)

# Создание email адреса на основе имени
# Преобразуем имя в формат для email
email_name = cleaned_name.lower().replace(" ", ".")
email = f"{email_name}@student.{university.lower()}.ru"
print(f"Ваш студенческий email: {email}")