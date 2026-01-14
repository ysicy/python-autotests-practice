# Пример 2: Простой блокнот
def add_note():
    note = input("Введите заметку: ")
    timestamp = input("Введите дату (или нажмите Enter для пропуска): ")

    try:
        with open("notes.txt", "a", encoding="utf-8") as file:
            if timestamp:
                file.write(f"[{timestamp}] {note}\n")
            else:
                file.write(f"{note}\n")
        print("Заметка добавлена!")
    except Exception as e:
        print(f"Ошибка при сохранении заметки: {e}")


def show_notes():
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            notes = file.read()
            if notes:
                print("=== ВАШИ ЗАМЕТКИ ===")
                print(notes)
            else:
                print("Заметок пока нет.")
    except FileNotFoundError:
        print("Файл с заметками не найден. Добавьте первую заметку!")
    except Exception as e:
        print(f"Ошибка при чтении заметок: {e}")


# Простое меню
def notebook():
    while True:
        print("\n=== БЛОКНОТ ===")
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Выход")

        choice = input("Выберите действие (1-3): ")

        if choice == "1":
            add_note()
        elif choice == "2":
            show_notes()
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")

# Запуск блокнота
notebook()  # Раскомментируйте для запуска