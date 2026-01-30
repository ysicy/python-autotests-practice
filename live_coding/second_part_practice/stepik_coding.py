# На вход программе подается строка текста
# Программа должна вывести измененный список, разделяя его элементы одним пробелом.
def reverse_ints(text):
    lst = [int(i) for i in text.split()]
    for i in range(0,len(lst)-1,2):
        lst[i], lst[i+1] = lst[i+1], lst[i]
    print(*lst)

reverse_ints('1 2 4 5')

# На вход программе подается строка текста
# Программа должна вывести элементы измененного списка с циклическим сдвигом
def reverse_list(text):
    lst = [int(i) for i in  text.split()]
    print(*lst[-1:] + lst[:-1])
reverse_list('1 2 4 5')

# На вход программе подается строка текста, содержащая натуральные числа
# вывести одно число – количество различных элементов списка.

def count_ints(text):
    lst = [int(i) for i in text.split()]
    unique =set(lst)
    print(len(unique))

count_ints('1 2 4 5')

# В первой строке подается натуральное число
# n(1<n<1000) – количество чисел в наборе. В последующих
# n строках вводятся целые числа, составляющие набор (могут повторяться).
# Затем следует целое число, которое является или не является произведением двух каких-то чисел из набора.
# Формат выходных данных
# Программа должна вывести ДА или НЕТ в соответствии с условием задачи.

# def bim_bim_bam_bam():
#     n = int(input())
#     lst =[]
#     for i in range(n):
#         ints = int(input())
#         lst.append(ints)
#     b = int(input())
#     no = "НЕТ"
#     for j in range(len(lst)):
#         for k in range(len(lst)):
#             if j != k and lst[j] * lst[k] == b:
#                 no = "ДА"
#     print(no)
#
# bim_bim_bam_bam()

# Формат входных данных
# На вход программе подаются две строки текста, содержащие слова "камень", "ножницы" или "бумага".
# На первой строке записан выбор Тимура, на второй – выбор Руслана.
# Формат выходных данных
# Программа должна вывести результат жеребьевки, то есть кто победит: Тимур, Руслан или же они сыграют вничью.

# def kamen_noj_paper():
#     choose_timur = input()
#     choose_ruslan = input()
#     if choose_timur == 'камень' and choose_ruslan == 'бумага':
#         print('Руслан')
#     if choose_timur == 'бумага' and choose_ruslan == 'ножницы':
#         print('Руслан')
#     if choose_timur == 'ножницы' and choose_ruslan == 'камень':
#         print('Руслан')
#     if choose_timur == 'камень' and choose_ruslan == 'ножницы':
#         print('Тимур')
#     if choose_timur == 'ножницы' and choose_ruslan == 'бумага':
#         print('Тимур')
#     if choose_timur == 'бумага' and choose_ruslan == 'камень':
#         print('Тимур')
#     if choose_timur == choose_ruslan:
#         print('ничья')
# kamen_noj_paper()

# гениальное решение,забрал себе
# def genius():
#     x, y = input(), input()
#     var = ['камень', 'ножницы', 'бумага']
#     ans = ['ничья', 'Руслан', 'Тимур']
#     print(ans[var.index(x) - var.index(y)])


#На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
# Программа должна вывести наибольшее количество подряд выпавших Решек.
# def  check_count_symbols():
#     text = input().split('О')
#     print(len(max(text)))
#
# check_count_symbols()

def find_anton():
    n = int(input())
    word = 'anton'
    result = []
    for i in range(1,n+1):
        text = input()
        index = 0
        for j in text:
            if j == word[index]:
                index+=1
            if index == len(word):
                result.append(i)
                break
    print(*result)
find_anton()

def  check_symbols():
    b = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
         'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


