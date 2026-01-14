# Наследование - работники
print("=== Наследование: Работники ===")


class Employee:
    """Базовый класс для всех работников"""

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = "Общий"
        print(f"👤 Принят на работу: {name}")

    def work(self):
        """Базовый метод работы"""
        return f"{self.name} работает"

    def get_salary_info(self):
        """Информация о зарплате"""
        return f"Зарплата {self.name}: {self.salary} руб."

    def get_info(self):
        """Базовая информация о работнике"""
        return f"{self.name}, {self.age} лет, отдел: {self.department}"


class Developer(Employee):
    """Класс разработчика"""

    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language
        self.department = "IT"
        print(f"💻 Разработчик на {programming_language}")

    def work(self):
        """Переопределяем работу разработчика"""
        return f"{self.name} пишет код на {self.programming_language}"

    def debug(self):
        """Уникальный метод разработчика"""
        return f"{self.name} ищет и исправляет баги"

    def get_info(self):
        """Расширенная информация"""
        base_info = super().get_info()
        return f"{base_info}, язык: {self.programming_language}"


class Designer(Employee):
    """Класс дизайнера"""

    def __init__(self, name, age, salary, design_tool):
        super().__init__(name, age, salary)
        self.design_tool = design_tool
        self.department = "Дизайн"
        print(f"🎨 Дизайнер, работает в {design_tool}")

    def work(self):
        """Переопределяем работу дизайнера"""
        return f"{self.name} создает дизайн в {self.design_tool}"

    def create_mockup(self):
        """Уникальный метод дизайнера"""
        return f"{self.name} создает макет интерфейса"

    def get_info(self):
        """Расширенная информация"""
        base_info = super().get_info()
        return f"{base_info}, инструмент: {self.design_tool}"


class Manager(Employee):
    """Класс менеджера"""

    def __init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.team_size = team_size
        self.department = "Управление"
        print(f"👔 Менеджер команды из {team_size} человек")

    def work(self):
        """Переопределяем работу менеджера"""
        return f"{self.name} управляет командой из {self.team_size} человек"

    def hold_meeting(self):
        """Уникальный метод менеджера"""
        return f"{self.name} проводит совещание с командой"

    def get_info(self):
        """Расширенная информация"""
        base_info = super().get_info()
        return f"{base_info}, размер команды: {self.team_size}"


# Создание работников
print("\nПрием на работу:")
dev = Developer("Алексей", 28, 80000, "Python")
designer = Designer("Мария", 25, 60000, "Figma")
manager = Manager("Иван", 35, 100000, 8)

print(f"\n{'=' * 50}")
print("ИНФОРМАЦИЯ О СОТРУДНИКАХ")
print(f"{'=' * 50}")

employees = [dev, designer, manager]
for employee in employees:
    print(f"📋 {employee.get_info()}")
    print(f"💰 {employee.get_salary_info()}")
    print()

print(f"{'=' * 50}")
print("РАБОЧИЙ ДЕНЬ")
print(f"{'=' * 50}")

for employee in employees:
    print(f"⚡ {employee.work()}")

print(f"\n{'=' * 50}")
print("СПЕЦИАЛЬНЫЕ ЗАДАЧИ")
print(f"{'=' * 50}")

print(f"🐛 {dev.debug()}")
print(f"🖼️ {designer.create_mockup()}")
print(f"📊 {manager.hold_meeting()}")

print(f"\n{'=' * 50}")
print("СТАТИСТИКА ПО ОТДЕЛАМ")
print(f"{'=' * 50}")

departments = {}
total_salary = 0

for employee in employees:
    dept = employee.department
    if dept not in departments:
        departments[dept] = []
    departments[dept].append(employee.name)
    total_salary += employee.salary

print("👥 Сотрудники по отделам:")
for dept, names in departments.items():
    print(f"   {dept}: {', '.join(names)}")

print(f"\n💼 Общий фонд зарплат: {total_salary} руб.")
print(f"📊 Средняя зарплата: {total_salary // len(employees)} руб.")