my_tuple_first = ((1, 2, 3, 'Alex', 'Python'),
            (6, 4, 7, 'MaLEX', 'gO'),
            (8, 9, True, 'Alik', 'Java'),)
print(my_tuple_first)

second_tuple_nested = my_tuple_first[1]
print(second_tuple_nested)

nested_tuple_to_list = list(second_tuple_nested)
print(nested_tuple_to_list)

nested_tuple_to_list.insert(0, 'new word')
print(nested_tuple_to_list)
nested_tuple_to_list.append('в конец')
print(nested_tuple_to_list)
nested_tuple_to_list.remove('new word')
print(nested_tuple_to_list)
nested = tuple(nested_tuple_to_list)
print(nested)
temp_list = list(my_tuple_first)
temp_list[1] = nested
my_tuple_first = tuple(temp_list)
print(my_tuple_first)
for item in my_tuple_first:
    print(*item)
    print(len(my_tuple_first[1]))
