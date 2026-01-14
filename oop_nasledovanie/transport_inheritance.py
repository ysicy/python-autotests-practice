# Наследование - транспорт
print("=== Наследование: Транспорт ===")


class Vehicle:
    """Базовый класс для всех транспортных средств"""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
        print(f"🚗 Создано транспортное средство: {brand} {model}")

    def start(self):
        """Запуск транспорта"""
        if self.is_running:
            return f"{self.brand} {self.model} уже запущен"

        self.is_running = True
        return f"{self.brand} {self.model} запущен"

    def stop(self):
        """Остановка транспорта"""
        if not self.is_running:
            return f"{self.brand} {self.model} уже остановлен"

        self.is_running = False
        return f"{self.brand} {self.model} остановлен"

    def get_info(self):
        """Базовая информация"""
        status = "работает" if self.is_running else "остановлен"
        return f"{self.brand} {self.model} ({self.year}) - {status}"


class Car(Vehicle):
    """Класс автомобиля"""

    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.doors = 4
        print(f"🚙 Это автомобиль на {fuel_type}")

    def honk(self):
        """Сигналить"""
        return f"{self.brand} {self.model}: Би-би!"

    def get_info(self):
        """Расширенная информация для автомобиля"""
        base_info = super().get_info()
        return f"{base_info}, топливо: {self.fuel_type}, дверей: {self.doors}"


class Motorcycle(Vehicle):
    """Класс мотоцикла"""

    def __init__(self, brand, model, year, engine_volume):
        super().__init__(brand, model, year)
        self.engine_volume = engine_volume
        self.wheels = 2
        print(f"🏍️ Это мотоцикл с двигателем {engine_volume}л")

    def rev_engine(self):
        """Газовать"""
        return f"{self.brand} {self.model}: Врум-врум!"

    def get_info(self):
        """Расширенная информация для мотоцикла"""
        base_info = super().get_info()
        return f"{base_info}, объем двигателя: {self.engine_volume}л, колес: {self.wheels}"


class Bicycle(Vehicle):
    """Класс велосипеда"""

    def __init__(self, brand, model, year, gear_count):
        super().__init__(brand, model, year)
        self.gear_count = gear_count
        self.has_engine = False
        print(f"🚴 Это велосипед с {gear_count} скоростями")

    def start(self):
        """Переопределяем запуск для велосипеда"""
        self.is_running = True
        return f"Начинаем крутить педали на {self.brand} {self.model}"

    def ring_bell(self):
        """Звонить в звонок"""
        return f"{self.brand} {self.model}: Динь-динь!"

    def get_info(self):
        """Расширенная информация для велосипеда"""
        base_info = super().get_info()
        return f"{base_info}, скоростей: {self.gear_count}, двигатель: нет"


# Создание транспорта
print("\nСоздание транспорта:")
car = Car("Toyota", "Camry", 2020, "бензин")
motorcycle = Motorcycle("Yamaha", "R1", 2021, 1.0)
bicycle = Bicycle("Trek", "Mountain", 2022, 21)

print(f"\n{'=' * 50}")
print("ИНФОРМАЦИЯ О ТРАНСПОРТЕ")
print(f"{'=' * 50}")

vehicles = [car, motorcycle, bicycle]
for vehicle in vehicles:
    print(f"📋 {vehicle.get_info()}")

print(f"\n{'=' * 50}")
print("ЗАПУСК ТРАНСПОРТА")
print(f"{'=' * 50}")

for vehicle in vehicles:
    print(f"🔑 {vehicle.start()}")

print(f"\n{'=' * 50}")
print("УНИКАЛЬНЫЕ ЗВУКИ")
print(f"{'=' * 50}")

print(f"📯 {car.honk()}")
print(f"🏍️ {motorcycle.rev_engine()}")
print(f"🔔 {bicycle.ring_bell()}")

print(f"\n{'=' * 50}")
print("ОСТАНОВКА ТРАНСПОРТА")
print(f"{'=' * 50}")

for vehicle in vehicles:
    print(f"🛑 {vehicle.stop()}")