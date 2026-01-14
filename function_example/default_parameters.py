# Функции с параметрами по умолчанию
print("=== Функции с параметрами по умолчанию ===")


def make_coffee(size="средний", milk=False, sugar=False):
    """Готовит кофе с настройками по умолчанию"""
    print(f"☕ Готовим кофе:")
    print(f"   Размер: {size}")

    if milk:
        print("   С молоком")
    else:
        print("   Без молока")

    if sugar:
        print("   С сахаром")
    else:
        print("   Без сахара")

    print("   Готово!\n")


def send_message(text, sender="Система", urgent=False):
    """Отправляет сообщение"""
    if urgent:
        print("🚨 СРОЧНО!")

    print(f"📧 От: {sender}")
    print(f"📝 Сообщение: {text}")
    print("✅ Отправлено\n")


def calculate_price(base_price, discount=0, delivery=50):
    """Рассчитывает итоговую цену"""
    price_with_discount = base_price - discount
    total_price = price_with_discount + delivery

    print(f"💰 Расчет цены:")
    print(f"   Базовая цена: {base_price} руб")
    print(f"   Скидка: {discount} руб")
    print(f"   Доставка: {delivery} руб")
    print(f"   Итого: {total_price} руб\n")

    return total_price


# Используем функции с разными параметрами

# Кофе с настройками по умолчанию
make_coffee()

# Кофе с молоком
make_coffee(milk=True)

# Большой кофе с молоком и сахаром
make_coffee("большой", True, True)

# Маленький кофе только с сахаром
make_coffee(size="маленький", sugar=True)

# Сообщения
send_message("Добро пожаловать!")
send_message("Ваш заказ готов", sender="Магазин")
send_message("Система будет недоступна", urgent=True)

# Расчет цен
calculate_price(1000)  # Только базовая цена
calculate_price(1000, discount=100)  # Со скидкой
calculate_price(1000, delivery=0)  # Без доставки
calculate_price(1000, discount=200, delivery=100)  # Все параметры

