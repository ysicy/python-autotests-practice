def safe_calculator():
    try:
        a = float(input("Введите первое число: "))
        operation = input("Введите операцию (+, -, *, /): ")
        b = float(input("Введите второе число: "))

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            result = a / b
        else:
            print("Неизвестная операция!")
            return

        print(f"Результат: {result}")

    except ValueError:
        print("Ошибка: введите корректное число!")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно!")
    except:
        print("Произошла неожиданная ошибка!")


# Вызов функции
safe_calculator()


# Основные типы ошибок в Python
# ValueError - неправильное значение (например, int("abc"))
# TypeError - неправильный тип данных
# IndexError - индекс вне диапазона списка
# KeyError - ключ не найден в словаре
# ZeroDivisionError - деление на ноль
# FileNotFoundError - файл не найден
# AttributeError - атрибут не найден у объекта