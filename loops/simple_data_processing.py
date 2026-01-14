# Простая обработка списка товаров
print("=== Обработка данных о товарах ===")

# Список товаров в магазине
products = [
    {"name": "хлеб", "price": 50, "quantity": 20},
    {"name": "молоко", "price": 80, "quantity": 15},
    {"name": "яйца", "price": 120, "quantity": 30},
    {"name": "сыр", "price": 300, "quantity": 8},
    {"name": "масло", "price": 200, "quantity": 12}
]

print("Список товаров:")
for product in products:
    name = product["name"]
    price = product["price"]
    quantity = product["quantity"]
    total_value = price * quantity

    print(f"{name}: {price} руб × {quantity} шт = {total_value} руб")

print()

# Поиск дорогих товаров
print("Дорогие товары (цена > 100 руб):")
for product in products:
    if product["price"] > 100:
        print(f"- {product['name']}: {product['price']} руб")

print()

# Подсчет общей стоимости
total_cost = 0
for product in products:
    total_cost += product["price"] * product["quantity"]

print(f"Общая стоимость товаров: {total_cost} руб")

# Поиск самого дешевого товара
cheapest_product = products[0]
for product in products:
    if product["price"] < cheapest_product["price"]:
        cheapest_product = product

print(f"Самый дешевый товар: {cheapest_product['name']} - {cheapest_product['price']} руб")