#Словари

student = {
    "name": "Алексей",
    "age": 32,
    "speciality": "Информатика"
}

print(student)

book = {
    "title": "Война и мир",
    "author": "Толстой",
    "year": 1969,
    "pages": 1300
}
print(book)

user = {
    "name": "Анна",
    "age": 32
}

user_name = user["name"]
print(user_name)

year = user.get("year", "Не задан год")
print(year)

user["name"] = "Alex"
print(user)

#Вложенный словарь

api_response = {
    "data": {
        "user_id": 12345,
        "username": "Alex",
        "email": "test@example.com",
        "profile": {
            "first_name": "Test",
            "last_name": "Пользователь",
            "age": 25,
            "preferences": ["python", "testing", "automation"]
        }
    },
    "metadata": {
        "timestamp": "2024-01-15T10:30:00Z",
        "version": "1.0",
        "request_id": "req_abc123"
    }
}

nested_last_name = api_response["data"]["profile"]["last_name"]
print(nested_last_name)