# Операции изменения словарей
print("=== Изменение словарей ===")

# Исходный словарь с информацией о книге
book_info = {
    "title": "Война и мир",
    "author": "Толстой",
    "year": 1869
}

print(f"Исходная информация: {book_info}")

# Добавление новых элементов
book_info["pages"] = 1300
book_info["genre"] = "Роман"
book_info["languages"] = ["русский"]

print(f"После добавления полей: {book_info}")

# Изменение существующих элементов
book_info["genre"] = "Исторический роман"
book_info["languages"].append("английский")

print(f"После изменения жанра: {book_info}")

# Удаление элементов
# Способ 1: del
del book_info["languages"]
print(f"После удаления languages: {book_info}")

# Способ 2: .pop() - удаляет и возвращает значение
pages = book_info.pop("pages")
print(f"Удаленное количество страниц: {pages}")
print(f"После pop('pages'): {book_info}")

# Способ 3: .pop() с значением по умолчанию
isbn = book_info.pop("isbn", "ISBN не указан")
print(f"ISBN: {isbn}")

# Обновление словаря другим словарем
additional_info = {
    "publisher": "Русский вестник",
    "country": "Россия",
    "rating": 4.8
}

book_info.update(additional_info)
print(f"После update(): {book_info}")

# Очистка словаря
backup = book_info.copy()  # Создаем копию
book_info.clear()
print(f"После clear(): {book_info}")
print(f"Резервная копия: {backup}")