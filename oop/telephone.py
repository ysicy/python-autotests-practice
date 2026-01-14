print("=== Телефоны ===")

class Telephone:
    def __init__(self, brand, model, battery = 100, is_on = False):
        self.brand = brand
        self.model = model
        self.battery = battery
        self.is_on = is_on
        print(f"В наличии телефон: {self.brand}, модель: {self.model}")

    def turn_on(self):
        if self.is_on:
            print(f"{self.brand} {self.model} включен.")
        elif self.battery <= 0:
            print(f"{self.brand} {self.model} нельзя включить, т.к заряд батареи 0%")
        else:
            self.is_on = True
            print(f"{self.brand} {self.model} уже включен.")

    def turn_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} выключен.")
        else:
            print(f"{self.brand} {self.model} уже выключен.")

    def make_call(self, duration):
        if not self.is_on:
            print(f"{self.brand} {self.model} выключен. Включите телефон, чтобы совершать звонки")
            return

        battery_usage = duration * 2

        if self.battery >= battery_usage:
            self.battery -= battery_usage
            print(f"Кому-то звонит. Звонок продолжительностью {duration} минут(ы) совершен. Заряда батарейки осталось: {self.battery}%")
        else:
            print("Маловато заряда батарейки для совершения звонка")

    def charge(self, amount):
        old_battery = self.battery
        self.battery = min(old_battery + amount, 100)
        print(f"{self.brand} {self.model} заряжен с {old_battery}% до {self.battery}%")

    def get_status(self):
        if self.is_on:
            status = f"{self.brand} {self.model} включен"
        else:
            status = f"{self.brand} {self.model} выключен"

        if self.battery > 50:
            smail = "😎"
        elif self.battery > 20:
            smail = "🥴"
        elif self.battery <= 0:
            smail = "💣"
        else:
            smail = "💀"
        print(f"{status}. Заряд батареи: {self.battery}% {smail}")

print("\nТелефон 1")
iphone = Telephone("Ипхон", "16 Pro Max")
iphone.get_status()
iphone.turn_on()
iphone.make_call(5)
iphone.get_status()
iphone.make_call(40) #балаболка какая-то
iphone.get_status()
iphone.make_call(10)
iphone.charge(20)
iphone.make_call(3)
iphone.get_status()
iphone.turn_off()
iphone.turn_off()

print("\nТелефон 2")
xiaomi = Telephone("Сяоми", "Li6", battery=0)
xiaomi.get_status()
xiaomi.turn_on()



print("\nТелефон 3")
shantsung = Telephone("Самсунг", "Galaxy 20 Ultra Maximus 4AWD")
shantsung.get_status()
shantsung.turn_on()
shantsung.turn_on()
shantsung.make_call(10)
shantsung.make_call(20)
shantsung.get_status()
shantsung.charge(20)
shantsung.get_status()
shantsung.turn_off()
shantsung.get_status()
