# Первый класс - кофе в кофейне
print("=== Класс кофе ===")

class Coffee:
    """Класс для представления кофе"""

    def __init__(self, name, price, size="средний"):
        """Конструктор - вызывается при создании объекта"""
        self.name = name
        self.price = price
        self.size = size
        self.is_hot = True
        print(f"☕ Создан кофе: {name}")

    def get_info(self):
        """Метод для получения информации о кофе"""
        temp = "горячий" if self.is_hot else "холодный"
        return f"{self.name} ({self.size}, {temp}) - {self.price} руб."

    def make_cold(self):
        """Делает кофе холодным"""
        self.is_hot = False
        print(f"{self.name} теперь холодный")

    def change_size(self, new_size):
        """Изменяет размер кофе"""
        old_size = self.size
        self.size = new_size
        print(f"Размер {self.name} изменен с {old_size} на {new_size}")


# Создание объектов кофе
print("Создание напитков:")
latte = Coffee("Латте", 150)
cappuccino = Coffee("Капучино", 120, "большой")
americano = Coffee("Американо", 100, "маленький")

print("\nИнформация о кофе:")
coffees = [latte, cappuccino, americano]
for coffee in coffees:
    print(coffee.get_info())

print("\nИзменения:")
latte.make_cold()
cappuccino.change_size("средний")

print("\nОбновленная информация:")
for coffee in coffees:
    print(coffee.get_info())