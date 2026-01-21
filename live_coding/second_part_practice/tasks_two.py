# Python / структуры / логика
#
# 1.
#
# [1,2,3,4,5,6], k=3 → [[1,2,3],[4,5,6]]
# Разбить список на чанки.
def chunk_list(lst,k):
    result = []
    for i in range(0, len(lst), k):
        result.append(lst[i:i+k])
    return result

print(chunk_list([1,2,3,4,5,6],3))
#
# 2.
# Сдвинуть список вправо на k.
# [1,2,3,4,5], k=2 → [4,5,1,2,3]
def check_list(lst,k):
    return lst[-k:] + lst[:-k]

print(check_list([1,2,3,4,5],2))
print(check_list([1,2,3,4,5],4))

#
# 3.
# Найти число, которое встречается нечётное количество раз.
def ckeck_ne_chetnoe(lst):
    result = 0
    for num in lst:
        result ^= num
    return result

print(ckeck_ne_chetnoe([1,2,1,2,5]))

# 4.
# Вернуть True, если элементы идут строго возрастающе без дублей.
def is_strictly_increasing(lst):
    for i in range(len(lst) - 1):
        if lst[i + 1] > lst[i]:
            continue
        else:
            return False
    return True
print(is_strictly_increasing([1,2,1,2,5]))
print(is_strictly_increasing([1,2,3,5,7]))
# 5.
# Найти все пары чисел, сумма которых = target.
def find_all_pairs(nums, target):
    pairs = []
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))
    return pairs

print(find_all_pairs([1,2,3,4,5],5))
print(find_all_pairs([2,2,2,4,9],6))
print(find_all_pairs([1,2,3,4,5,0],5))
# 6.
# Слить два отсортированных списка без sort().
#
# 7.
# Найти «провал»:
#
# [1,2,3,7,8] → 4,5,6
#
#
# 8.
# Удалить из списка всё, что встречается более одного раза.
#
# Строки / парсинг
#
# 9.
#
# "aabbccdd" → "abcd"
#
#
# но в порядке первого появления.
#
# 10.
# Сжать строку:
#
# "aaabbcccc" → "a3b2c4"
#
#
# 11.
# Проверить, что строка — анаграмма другой.
#
# 12.
# Извлечь числа из строки:
#
# "ab12cd34" → [12,34]
#
# Dict / JSON
#
# 13.
# Проверить, что 2 словаря «глубоко равны» (nested).
#
# 14.
# Отсортировать словарь по значениям.
#
# 15.
# Проверить, что JSON:
#
# валиден
#
# все ключи — строки
#
# нет None
#
# Алгоритмическое мышление
#
# 16.
# Найти подмассив с максимальной суммой.
#
# 17.
# Найти самый частый элемент без Counter.
#
# 18.
# Найти первую непрерывную последовательность длиной ≥ k.
#
# QA мышление
#
# 19.
# Функция:
#
# def process(user):
#     return user["profile"]["email"]
#
#
# Какие edge cases?
#
# 20.
# API возвращает 200 и пустой body.
# Что это значит? Какие гипотезы?