#try:
#    Код, который может вызвать ошибку
#    опасная_операция()
#except:
#    Код, который выполнится, если произошла ошибка
#    print("Произошла ошибка")

try:
    result = 10/0
    print(result)
except:
    print("Ошибка, чел")
    result = 0

print(f"Программа работает. Результат арифметической функции:{result}")

print("\nНа новой строке")
user_input = "abc"

try:
    number = int(user_input)
    print(f"Вы ввели число: {number}")
except:
    print("Ошибка чел, это не число")
    number = 0

print(f"Работает с числом: {number}")

print("\nЕще новая")
my_list = [1, 2, 3]

try:
    print(my_list[12]) #Пытаемся достать элемент которого нет в списке
except:
    print("Ошибка чел, ТАКОГО ЭЛЕМЕНТА НЕТ В СПИСКЕ")


print("\nFINALLY")

try:
    file = open("file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Файл не найден чел")
finally:
    print("Блок финали всегда будет выполняться чел")
    #Здесь обычно закрывают файлы или освобождают ресурсы