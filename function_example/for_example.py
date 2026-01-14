#Функции - наши собственные методы

#Пример
    #def имя_функции():
    #Код функции
    #print("Функция выполняется")

#Вызов функции
#имя_функции()

    # def приветствие(имя):
    #     print(f"Здаров, {имя}")
    # приветствие("Анна")

    #def сложить(a,b)
    # результат = a +b
    # return результат

# Использовангие резульата
# сумма = сложить(5,3)


def check_user(age, email):
    if age>= 20 and email and "@" in email:
        print(f"Пользователь {email} валиден")
        return True
    else:
        print(f"Пользователь {email} не валиден")
        return False

is_valid = check_user(22,"alex@email.com")
is_valid2 =check_user(2,"alex@email.yo")
is_valid3 =check_user(12,"alex@email.ru")
is_valid4 =check_user(32,"alex@email.rus")

# Простые функции без параметров
print("=== Простые функции ===")

def say_hello():
    """Приветствует пользователя"""
    print("Привет! Добро пожаловать в нашу программу!")

def show_menu():
    """Показывает меню программы"""
    print("\nМеню:")
    print("1. Посмотреть фильмы")
    print("2. Добавить фильм")
    print("3. Выйти")

def say_goodbye():
    """Прощается с пользователем"""
    print("До свидания! Увидимся позже!")

def show_loading():
    """Показывает загрузку"""
    print("Загружаем данные...")
    print("██████████ 100%")
    print("Готово!")

# Используем функции
say_hello()
show_loading()
show_menu()
say_goodbye()
