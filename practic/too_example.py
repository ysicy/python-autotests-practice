# Запрос к API, который возвращает JSON
import requests

response = requests.get('https://jsonplaceholder.typicode.com/users/1')
print(response.text)

# Проверяем успешность запроса
if response.status_code == 200:
    # Автоматически парсим JSON
    user_data = response.json()

    print(f"Имя пользователя: {user_data['name']}")
    print(f"Email: {user_data['email']}")
    print(f"Город: {user_data['address']['city']}")
else:
    print(f"Ошибка: {response.status_code}")


import json

# Запись в файл с расширением .txt
data = {'name': 'Ivan', 'age': 30}

with open('data.txt', 'w') as f:
    json.dump(data, f)  # Запишет JSON в файл data.txt

# Чтение из файла с расширением .txt
with open('data.txt', 'r') as f:
    data_loaded = json.load(f)  # Прочитает JSON из файла data.txt

print(data_loaded)