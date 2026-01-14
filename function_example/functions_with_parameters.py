# Функции с параметрами
print("=== Функции с параметрами ===")

def greet_person(name):
    """Приветствует человека по имени"""
    print(f"Привет, {name}!")

def add_numbers(a, b):
    """Складывает два числа"""
    result = a + b
    print(f"{a} + {b} = {result}")

def check_password(password):
    """Проверяет пароль"""
    if len(password) < 6:
        print("❌ Пароль слишком короткий")
    else:
        print("✅ Пароль подходит")

def make_sandwich(bread, filling, sauce):
    """Делает сэндвич"""
    print(f"🥪 Готовим сэндвич:")
    print(f"   Хлеб: {bread}")
    print(f"   Начинка: {filling}")
    print(f"   Соус: {sauce}")
    print("   Готово!")

# Используем функции
greet_person("Анна")
greet_person("Петр")

add_numbers(5, 3)
add_numbers(10, 7)

check_password("123")
check_password("mypassword123")

make_sandwich("белый", "курица", "майонез")
make_sandwich("черный", "сыр", "горчица")
