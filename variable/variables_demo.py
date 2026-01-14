#Через штрих этот пишутся комменты, запоминаем



#str
student_name = "Alex"
favorite_book = "Python"

#int
student_age = 32
books_read = 1

#float
book_rating = 4.8
reading_hours = 17

#bool (True or False)
likes_reading = True
has_library_card = False

print("=== Информация о студенте ===")
print(student_name)
print(favorite_book)
print(student_age)
print(books_read)

#Функция type().
# Короче, добавляя в конец строки функцию type()
# после выполнения программы в консоль тебе напишется
# тип данных, которая хранится в переменной

print("\n=== Типы данных ===")
print("Тип student_name:", type(student_name))
print("Тип student_age:", type(student_age))
print("Тип book_rating:", type(book_rating))
print("Тип likes_reading:", type(likes_reading))

#Изменение значения переменных
print("\n=== Изменение переменных ===")
print("Возраст до изменения: ", student_age)

student_age = 33
print("Возраст после изменения: ", student_age)