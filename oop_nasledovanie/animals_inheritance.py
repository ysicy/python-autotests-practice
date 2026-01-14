# Наследование - животные
print("=== Наследование: Животные ===")


class Animal:
    """Базовый класс для всех животных"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"🐾 Создано животное: {name}")

    def speak(self):
        """Базовый метод для звука"""
        return f"{self.name} издает звук"

    def eat(self):
        """Метод для еды"""
        return f"{self.name} ест"

    def sleep(self):
        """Метод для сна"""
        return f"{self.name} спит"

    def get_info(self):
        """Информация о животном"""
        return f"{self.name}, возраст: {self.age}"


class Dog(Animal):
    """Класс собаки, наследует от Animal"""

    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Вызываем конструктор родителя
        self.breed = breed
        print(f"🐕 Это собака породы {breed}")

    def speak(self):
        """Переопределяем метод speak"""
        return f"{self.name} говорит: Гав-гав!"

    def fetch(self):
        """Новый метод только для собак"""
        return f"{self.name} приносит палку"

    def get_info(self):
        """Расширяем метод родителя"""
        base_info = super().get_info()
        return f"{base_info}, порода: {self.breed}"


class Cat(Animal):
    """Класс кошки, наследует от Animal"""

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        print(f"🐱 Это кошка {color} цвета")

    def speak(self):
        """Переопределяем метод speak"""
        return f"{self.name} говорит: Мяу-мяу!"

    def purr(self):
        """Новый метод только для кошек"""
        return f"{self.name} мурлычет: мур-мур-мур"

    def get_info(self):
        """Расширяем метод родителя"""
        base_info = super().get_info()
        return f"{base_info}, цвет: {self.color}"


# Создание объектов
print("\nСоздание животных:")
dog = Dog("Бобик", 3, "Лабрадор")
cat = Cat("Мурка", 2, "рыжий")

print(f"\n{'=' * 40}")
print("ИНФОРМАЦИЯ О ЖИВОТНЫХ")
print(f"{'=' * 40}")

animals = [dog, cat]
for animal in animals:
    print(f"📋 {animal.get_info()}")

print(f"\n{'=' * 40}")
print("ЗВУКИ ЖИВОТНЫХ")
print(f"{'=' * 40}")

for animal in animals:
    print(f"🔊 {animal.speak()}")

print(f"\n{'=' * 40}")
print("ОБЩИЕ ДЕЙСТВИЯ")
print(f"{'=' * 40}")

for animal in animals:
    print(f"🍽️ {animal.eat()}")
    print(f"😴 {animal.sleep()}")

print(f"\n{'=' * 40}")
print("УНИКАЛЬНЫЕ СПОСОБНОСТИ")
print(f"{'=' * 40}")

print(f"🎾 {dog.fetch()}")
print(f"😸 {cat.purr()}")