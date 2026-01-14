# Методы для работы со списками
print("=== Методы списков ===")

# Начальный список покупок
shopping_list = ["хлеб", "молоко"]
print(f"Исходный список: {shopping_list}")

# Метод .append() - добавляет элемент в конец
shopping_list.append("яйца")
print(f"После append('яйца'): {shopping_list}")

shopping_list.append("сыр")
print(f"После append('сыр'): {shopping_list}")

# Метод .insert() - вставляет элемент в определенную позицию
shopping_list.insert(1, "масло")  # Вставляем на позицию 1
print(f"После insert(1, 'масло'): {shopping_list}")

# Метод .remove() - удаляет первое вхождение элемента
shopping_list.remove("молоко")
print(f"После remove('молоко'): {shopping_list}")

# Метод .pop() - удаляет и возвращает элемент
removed_item = shopping_list.pop()  # Удаляет последний элемент
print(f"После pop(): {shopping_list}")
print(f"Удаленный товар: {removed_item}")

# .pop() с индексом - удаляет элемент по индексу
first_item = shopping_list.pop(0)  # Удаляет первый элемент
print(f"После pop(0): {shopping_list}")
print(f"Удаленный первый товар: {first_item}")

# Метод .clear() - очищает весь список
backup_list = shopping_list.copy()  # Создаем копию перед очисткой
shopping_list.clear()
print(f"После clear(): {shopping_list}")
print(f"Резервная копия: {backup_list}")

# Метод .extend() - добавляет все элементы из другого списка
new_items = ["мясо", "овощи"]
backup_list.extend(new_items)
print(f"После extend({new_items}): {backup_list}")