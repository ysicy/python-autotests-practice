# Простой класс студента
print("=== Класс студента ===")


class Student:
    """Класс для представления студента"""

    def __init__(self, name, age, course):
        """Инициализация студента"""
        self.name = name
        self.age = age
        self.course = course
        self.grades = []
        print(f"🎓 Создан студент: {name}")

    def add_grade(self, subject, grade):
        """Добавляет оценку"""
        grade_entry = {
            "subject": subject,
            "grade": grade
        }
        self.grades.append(grade_entry)
        print(f"📝 Добавлена оценка {grade} по предмету {subject}")

    def get_average(self):
        """Вычисляет средний балл"""
        if not self.grades:
            return 0

        total = sum(entry["grade"] for entry in self.grades)
        return round(total / len(self.grades), 2)

    def get_info(self):
        """Возвращает информацию о студенте"""
        return f"{self.name}, {self.age} лет, {self.course} курс (средний балл: {self.get_average()})"

    def print_grades(self):
        """Выводит все оценки"""
        if not self.grades:
            print(f"У {self.name} пока нет оценок")
            return

        print(f"� Оценкии {self.name}:")
        for entry in self.grades:
            print(f"   {entry['subject']}: {entry['grade']}")


# Создание и использование студентов
print("Создание студентов:")

# Создаем студентов
alice = Student("Алиса", 19, 2)
bob = Student("Боб", 20, 3)

print(f"\n{'=' * 30}")
print("ДОБАВЛЕНИЕ ОЦЕНОК")
print(f"{'=' * 30}")

# Добавляем оценки Алисе
alice.add_grade("Математика", 5)
alice.add_grade("Физика", 4)
alice.add_grade("Программирование", 5)

# Добавляем оценки Бобу
bob.add_grade("Математика", 4)
bob.add_grade("История", 3)
bob.add_grade("Английский", 4)

print(f"\n{'=' * 30}")
print("ИНФОРМАЦИЯ О СТУДЕНТАХ")
print(f"{'=' * 30}")

students = [alice, bob]
for student in students:
    print(student.get_info())
    student.print_grades()
    print()