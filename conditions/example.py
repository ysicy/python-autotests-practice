#if,elif,else

student_age = 15
print(f"Возраст студента: {student_age}")

if student_age >= 18:
    print("Можно получить водительские права")
    print("Доступ к курсам вождения разрешен")

print("Проверка завершена")

#Проверка пустой строки
empty_name = ""
print(f"\nПустое имя: '{empty_name}'")

if empty_name:
    print(f" Студент: '{empty_name}'")
else:
    print("Имя студента пустое")



#elif

score = 85
if score >= 90:
    print("super")
elif score >= 70:
    print("good")
elif score >= 50:
    print("not bad")
else:
    print("so bad")
