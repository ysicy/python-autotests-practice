class Coffe:
    def __init__(self, name, price):
        self.name = name #Атрибут
        self.price = price #Атрибут

    def get_info(self):
        return f"{self.name} - {self.price} руб."

    def add_price(self, new_price):
        self.price+= new_price

latte = Coffe("Латте", 170)
info = latte.get_info()
print(info)

cappuccino = Coffe("Капучино", 200)
print(cappuccino.get_info())
cappuccino.add_price(50)
print(cappuccino.get_info())