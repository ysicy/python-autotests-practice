# Работа с файлами позволяет:
#
# Сохранять данные между запусками программы
# Читать конфигурации и настройки
# Обрабатывать большие объёмы данных
# Создавать отчёты и логи
# Импортировать и экспортировать информацию

# file = open("example.txt","режим работы с файлом")
# #работа с файлом
# file.close() #ВАЖНО.Всегда закрывать файл

# Режимы открытия файлов:
# "r" - чтение (read) - файл должен существовать
# "w" - запись (write) - создаёт новый файл или перезаписывает существующий
# "a" - добавление (append) - добавляет в конец файла
# "r+" - чтение и запись
# "w+" (write and read) — открыть файл для записи и чтения. Если файл существует — очищается, если нет — создаётся новый.
# "a+" (append and read) — открыть файл для добавления и чтения. Если файла нет — создаётся новый.

file = open("example.txt", "w",encoding="utf-8")
file.write("Hello World, это моя первая запись\nНовая строка")
file.close()

file = open("example.txt", "r",encoding="utf-8")
for line in file:
    print(f"Строка: {line.strip()}") # strip() убирает символы переноса
file.close()

#РЕКОМЕНДУМАЫЙ СПОСОБ! Можно в конце не писать file.close(), используя вот такую конструкцию:
with open("example.txt", "r",encoding="utf-8") as file:
    for line in file:
        print(f"Строка: {line.strip()}") # strip() убирает символы переноса

file = open("example.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()

print(f"Всего строк: {len(lines)}")
for i, line in enumerate(lines):
    print(f"Строка {i+1}: {line.strip()}")

#Запись файла
file = open("output.txt", "w", encoding="utf-8")
file.write("Это новый файл!\n")
file.write("Вторая строка.\n")
file.close()

print("Файл создан!")

file = open("output.txt", "a", encoding="utf-8")
file.write("Эта строка добавлена в конец.\n")
file.write("И ещё одна строка.\n")
file.close()

print("Текст добавлен!")