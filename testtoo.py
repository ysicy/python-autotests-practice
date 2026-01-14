firs_name = "Иван"
last_name = "Петров"
full_name = firs_name + " " + last_name
print(full_name)

name = "Анна"
age = 30
message = f"Привет, {name}, тебе реально {age}?"
print(message)

result = f"{name} {age}"
print(result)

print(name.upper())
print(name.lower())

name2 = " хз кто это "
print(name2)
print(name2.strip())

students = ["Саша", "Катя", "Серега"]
prices = [10, 20, 5, 4]
mixed = [True, "BMV", 20.99, 1]

fruits = ["apple", "banana", "orange"]
apple = fruits[-1]
print(apple)


fruits[0] = "арбуз"
print(fruits)

fruits.append("мандарин")
print(fruits)

fruits.remove("banana")
print(fruits)

size = len(fruits)
print(size)

has_watermelon = "арбуз" in fruits
print(has_watermelon)