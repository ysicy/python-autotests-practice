numbers = [1,2,3,4,5]
numbers.append(6)  ##добавили в конец
print(f"В конец добавили {numbers}")
numbers.insert(2,8)
print(f"Новый список {numbers}") #до 3 вставили 8
numbers.insert(0, -1)
print(numbers)
numbers.remove(8) #удаляешь именно число
print(numbers)
numbers.reverse()
print(numbers)
new_numbers = numbers[::-1]
print(numbers)
numbers2 = [2,4,6,8,1,3,2,4,5,2]
numbers2.sort()
print(numbers2)
count_list = len(numbers)
print(count_list)
count_symbol = numbers2.count(2)
print(count_symbol)

# reversed_list = list(reversed(numbers))
# print(reversed_list)
string_num = str(numbers)
print(string_num)
tuple_num = tuple(numbers)
print(tuple_num)

words = ['python', 'programming', 'len4ik', 'chat', 'bot']
print(words)

words.reverse()
print(words)
words2 = words[::-1]
print(words2)
words.append('telecom')
print(words)
words.insert(0,'trenya')
print(words)
words.pop(0)
print(words)
words.remove('telecom')
print(words)

print(words[-2:])

new_words = ['lenya', 'learning', 'python', '4weeks', 'okay']
print(new_words[:-4])
new_new_words = ['я учусь!'] + new_words
print(new_new_words)
new_new_words.insert(0, 'учусь')
print(new_new_words)
new_new_words.append('в конец')
print(new_new_words)
len_counts = len(new_new_words)
print(len_counts)

dany_massiv = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [True, False],
    ['lenya', 'learning', 'python', '4weeks', 'okay']
]
print(dany_massiv[0])
print(dany_massiv[0][1])
print(dany_massiv[1][1])
print(dany_massiv[2][1])
summa = sum(dany_massiv[1])
print(summa)
summa2 = sum(dany_massiv[3])
print(summa2)
count_list = sum(len(word) for word in dany_massiv[4])
print(count_list)
count = len(dany_massiv[4])
print(count)

massiv = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    (1,2,3)
]
list = list(massiv[3])
print(list)
list.insert(0,'len4ik')
print(list)
tuple = tuple(list)
print(tuple)
massiv[3]= tuple
print(massiv)

assert massiv[3] == tuple

Person = {
    "name": "Alex",
    "age": 22,
    "gender": "male",
    "profile": {
            "first_name": "Test",
            "last_name": "Пользователь",
            "age": 25,
            "preferences": ["python", "testing", "automation"]
        }
}
named = Person["name"]
print(named)

profile = Person["profile"]
print(profile)
last_name = Person["profile"]["last_name"]
print(last_name)



