class Instrument:

    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(f"В наличии музыкальный инструмент: {self.name}")

    def play(self):
        return f"{self.name} издает звук"

    def get_info(self):
        return f"{self.name}, цена: {self.price}"

class Guitar(Instrument):

    def __init__(self, name, price, strings):
        super().__init__(name, price)
        self.strings = strings

    def play(self):
        return f"На {self.name} мы бренчим на гитаре"

    def tune(self):
        return f"У {self.name} настраиваем струны"

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, с количеством струн: {self.strings}"

class Piano(Instrument):

    def __init__(self, name, price, keys):
        super().__init__(name, price)
        self.keys = keys

    def play(self):
        return f"На {self.name} мы играем на пианино"

    def open_lid(self):
        return f"У {self.name} открываем крышку"

    def get_info(self):
        base_info = super().get_info()
        return  f"{base_info}, с количеством клавиш: {self.keys}"


class Drum(Instrument):

    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def play(self):
        return f"На {self.name} мы бьем в барабаны"

    def hit_hard(self):
        return f"На барабанах {self.name} мы сильно ударяем по бочке"

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, с размером: {self.size}"


#Создадим объекты
print(f"\n{'=' * 40}")
print("Описание инструментов:")
print(f"{'=' * 40}")
guitar = Guitar("Yamaha", "25000", strings=6)
piano = Piano("Petrof", "40000",keys=88)
drum = Drum("Roland", "18000",size="маленький")
drum2 = Drum("Ludwig", "22000",size="средний")
drum3 = Drum("Tama", "25000",size="большой")

print(f"\n{'=' * 40}")
print("Общая информация:")
print(f"{'=' * 40}")
instruments = [guitar, piano, drum, drum2, drum3]
for instrument in instruments:
    print(f"{instrument.get_info()}")

print(f"\n{'=' * 40}")
print(f"Как играют инструменты:")
print(f"{'=' * 40}")
for instrument in instruments:
    print(f"{instrument.play()}")

print(f"\n{'=' * 40}")
print("Уникальные методы:")
print(f"{'=' * 40}")
print(guitar.tune())
print(piano.open_lid())
print(drum3.hit_hard())