#Сохранение списка покупок

def save_shopping_list(items, filename="shopping_list.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("=== СПИСОК ПОКУПОК ===\n")
            for i, item in enumerate(items, 1):
                file.write(f"{i}. {item}\n")
        print(f"Список сохранён в файл {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

def load_shopping_list(filename="shopping_list.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            print("Ваш список покупок:")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("Список покупок не найден!")
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")

# Использование
shopping_items = ["Молоко", "Хлеб", "Яйца", "Сыр", "Яблоки"]
save_shopping_list(shopping_items)
load_shopping_list()

def save_list_to_file(items, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for item in items:
                file.write(str(item) + "\n")
                print(f"Файл сохранен в: {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")