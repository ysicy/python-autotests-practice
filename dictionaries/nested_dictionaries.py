# Вложенные словари - словари внутри словарей
print("=== Вложенные словари ===")

# Комплексная структура данных о университете
university = {
    "name": "Московский государственный университет",
    "location": {
        "city": "Москва",
        "country": "Россия",
        "address": "Ленинские горы, 1"
    },
    "faculties": {
        "computer_science": {
            "name": "Факультет вычислительной математики и кибернетики",
            "students": 1200,
            "dean": "Иванов И.И."
        },
        "physics": {
            "name": "Физический факультет",
            "students": 800,
            "dean": "Петров П.П."
        },
        "mathematics": {
            "name": "Механико-математический факультет",
            "students": 600,
            "dean": "Сидоров С.С."
        }
    },
    "statistics": {
        "total_students": 2600,
        "total_faculties": 3,
        "founded_year": 1755
    }
}

print("Информация об университете:")
print(f"Название: {university['name']}")
print(f"Город: {university['location']['city']}")
print(f"Страна: {university['location']['country']}")
print(f"Адрес: {university['location']['address']}")

# Доступ к информации о конкретных факультетах
print(f"\nИнформация о факультетах:")

# Факультет ВМК
cs_faculty = university['faculties']['computer_science']
print(f"ВМК: {cs_faculty['name']}")
print(f"  Студентов: {cs_faculty['students']}")
print(f"  Декан: {cs_faculty['dean']}")

# Физический факультет
physics_faculty = university['faculties']['physics']
print(f"Физфак: {physics_faculty['name']}")
print(f"  Студентов: {physics_faculty['students']}")
print(f"  Декан: {physics_faculty['dean']}")

# Мехмат
math_faculty = university['faculties']['mathematics']
print(f"Мехмат: {math_faculty['name']}")
print(f"  Студентов: {math_faculty['students']}")
print(f"  Декан: {math_faculty['dean']}")

# Общая статистика
print(f"\nОбщая статистика:")
print(f"Всего студентов: {university['statistics']['total_students']}")
print(f"Всего факультетов: {university['statistics']['total_faculties']}")
print(f"Год основания: {university['statistics']['founded_year']}")

# Добавление нового факультета
print(f"\nДобавление нового факультета:")
new_faculty = {
    "name": "Факультет журналистики",
    "students": 400,
    "dean": "Журналов Ж.Ж."
}

# Добавляем новый факультет
university['faculties']['journalism'] = new_faculty
university['statistics']['total_faculties'] = 4
university['statistics']['total_students'] = 3050

print("После добавления факультета журналистики:")
print(f"  Название: {university['faculties']['journalism']['name']}")
print(f"  Студентов: {university['faculties']['journalism']['students']}")
print(f"  Декан: {university['faculties']['journalism']['dean']}")

print(f"\nОбновленная статистика:")
print(f"Всего факультетов: {university['statistics']['total_faculties']}")
print(f"Всего студентов: {university['statistics']['total_students']}")

# Проверяем доступ к глубоко вложенным данным
print(f"\nПримеры доступа к вложенным данным:")
print(f"Адрес университета: {university['location']['address']}")
print(f"Количество студентов на физфаке: {university['faculties']['physics']['students']}")
print(f"Декан мехмата: {university['faculties']['mathematics']['dean']}")

# Создаем еще один вложенный словарь - профиль студента
student_profile = {
    "personal_info": {
        "name": "Иван Петров",
        "age": 20,
        "email": "ivan.petrov@mail.ru"
    },
    "academic_info": {
        "faculty": "computer_science",
        "year": 3,
        "group": "301"
    },
    "grades": {
        "mathematics": 5,
        "physics": 4,
        "programming": 5
    }
}

print(f"\n=== Профиль студента ===")
print(f"Имя: {student_profile['personal_info']['name']}")
print(f"Возраст: {student_profile['personal_info']['age']}")
print(f"Email: {student_profile['personal_info']['email']}")

print(f"Факультет: {student_profile['academic_info']['faculty']}")
print(f"Курс: {student_profile['academic_info']['year']}")
print(f"Группа: {student_profile['academic_info']['group']}")

print(f"Оценки:")
print(f"  Математика: {student_profile['grades']['mathematics']}")
print(f"  Физика: {student_profile['grades']['physics']}")
print(f"  Программирование: {student_profile['grades']['programming']}")

# Вычисляем среднюю оценку
total_grades = student_profile['grades']['mathematics'] + student_profile['grades']['physics'] + student_profile['grades']['programming']
average_grade = total_grades / 3
print(f"Средняя оценка: {average_grade:.1f}")