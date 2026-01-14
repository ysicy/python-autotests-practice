def check_promo_code(code):
    if code == "WELCOME10":
        return 10
    elif code == "SALE20":
        return 20
    elif code == "VIP30":
        return 30
    else:
        return 0

def calculate_discount(price,discount_percent):
    price_with_discount = price - (price * discount_percent / 100)
    return price_with_discount

discount = check_promo_code("SALE20")
print(f"Ваша скидка:{discount}%")

final_price = calculate_discount(333, discount)
print(f"Итоговая цена:{final_price} рублей")


