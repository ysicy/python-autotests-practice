#Цикл for
from lists.lists_basics import grades, subjects
from variable.real_life_example import average_grade

#for элемент in коллекция:
     #Код выполняется дял каждого элемента
     #print(элемент)



fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Мне нравится: '{fruit}'")

print("\nРассмотрим цикл со списком")
user = {
    "name": "Alex",
    "age": 32,
    "email": "alex@examle.com"
}
for key in user:
    print(f"У пользователя:'{key}'")

for value in user.values():
    print(f"{value}")

for k,v in user.items():
    print(f"{k} : {v}")


#range - используется для того чтобы цикл выполнился определенное количество раз
for i in range(2,7):
    print(i)

print(f"Щас че то будет")
numbers = [50,60,100]
result = 0
for number in numbers:
    result = result + number
print(result)


grades = [4,3,5,5,4]
subjects = ["Математика", "Физика", "Химия", "История", "Литература"]
for i in range(len(grades)):
    grade = grades[i]
    subject = subjects[i]
    if grade == 5:
        status = "Отлично"
    elif grade == 4:
        status = "Хорошо"
    else:
        status = "Удовлетворительно"
    print(f"Студент получил оценку {grade} за предмет '{subject}' и статус его успеваемости: {status}")

#Подсчет статистики
excellent_count = 0
good_count = 0
satisfactory_count = 0
for grade in grades:
    if grade == 5:
        excellent_count += 1
    elif grade == 4:
        good_count += 1
    else:
        satisfactory_count += 1
total_subjects = len(grades)
average_grade = sum(grades) / total_subjects
print(f"\nСтатистика успеваемости")
print(f"Всего предметов: {total_subjects}")
print(f"Отличных оценок: {excellent_count}")
print(f"Хороших оценок: {good_count}")
print(f"Удовлетворительных оценок: {satisfactory_count}")
print(f"Средняя оценка: {average_grade:.1f}")
