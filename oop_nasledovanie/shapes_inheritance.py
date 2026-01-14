# Наследование - геометрические фигуры
print("=== Наследование: Фигуры ===")


class Shape:
    """Базовый класс для всех фигур"""

    def __init__(self, color):
        self.color = color
        print(f"🔷 Создана фигура {color} цвета")

    def get_info(self):
        """Базовая информация о фигуре"""
        return f"Фигура {self.color} цвета"

    def area(self):
        """Базовый метод для площади"""
        return "Площадь не определена"


class Rectangle(Shape):
    """Класс прямоугольника"""

    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
        print(f"📐 Это прямоугольник {width}x{height}")

    def area(self):
        """Переопределяем расчет площади"""
        return self.width * self.height

    def get_info(self):
        """Расширенная информация"""
        base_info = super().get_info()
        return f"{base_info}, прямоугольник {self.width}x{self.height}"


class Circle(Shape):
    """Класс круга"""

    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
        print(f"⭕ Это круг радиусом {radius}")

    def area(self):
        """Переопределяем расчет площади"""
        return 3.14 * self.radius * self.radius

    def get_info(self):
        """Расширенная информация"""
        base_info = super().get_info()
        return f"{base_info}, круг радиусом {self.radius}"


# Создание фигур
print("\nСоздание фигур:")
rectangle = Rectangle("красный", 5, 3)
circle = Circle("синий", 4)

print(f"\n{'=' * 40}")
print("ИНФОРМАЦИЯ О ФИГУРАХ")
print(f"{'=' * 40}")

shapes = [rectangle, circle]
for shape in shapes:
    print(f"📋 {shape.get_info()}")
    print(f"📏 Площадь: {shape.area()}")
    print()