# Пример 3: Обработка CSV-подобных данных
def save_students(students, filename="students.txt"):
    """Сохраняет список студентов в файл"""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Имя,Возраст,Оценка\n")  # Заголовок
            for student in students:
                line = f"{student['name']},{student['age']},{student['grade']}\n"
                file.write(line)
        print(f"Данные студентов сохранены в {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

def load_students(filename="students.txt"):
    """Загружает список студентов из файла"""
    students = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            # Пропускаем заголовок
            for line in lines[1:]:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    student = {
                        "name": parts[0],
                        "age": int(parts[1]),
                        "grade": parts[2]
                    }
                    students.append(student)
        return students
    except FileNotFoundError:
        print("Файл со студентами не найден!")
        return []
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")
        return []

# Пример использования
students_data = [
    {"name": "Анна", "age": 20, "grade": "A"},
    {"name": "Петр", "age": 19, "grade": "B"},
    {"name": "Мария", "age": 21, "grade": "A"}
]

save_students(students_data)
loaded_students = load_students()

print("Загруженные студенты:")
for student in loaded_students:
    print(f"{student['name']}, {student['age']} лет, оценка: {student['grade']}")