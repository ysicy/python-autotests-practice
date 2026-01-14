
import requests
import pytest




# Тест получения списка пользователей
def test_get_users_list():

    response = requests.get("https://jsonplaceholder.typicode.com/users")
    user_data = response.json()
    first_user = user_data[0]

    assert response.status_code == 200
    assert user_data
    assert "name" in first_user
    assert "email" in first_user
    assert first_user["username"] == "Bret"
    assert first_user["address"]["zipcode"] == "92998-3874"


# Тест получение информации об пользователе
def test_get_user_details():

    base_url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(f"{base_url}")
    user_data = response.json()
    ten_user = user_data[9]

    assert response.status_code == 200
    assert ten_user["username"] == "Moriah.Stanton"
    assert ten_user["company"]["name"] == "Hoeger LLC"
    assert ten_user["address"]["geo"]["lat"] == "-38.2386"
    assert ten_user["address"]["geo"]["lng"] == "57.2232"

# Тест создания поста(Я НЕ ПРАВИЛЛЬНО РЕАЛИЗОВАЛ!!!)
def test_create_post():

    base_url = 'https://jsonplaceholder.typicode.com/posts'

    new_post = {
        'title': "Test Post",
        'body': "Test Content",
        "user_id": 1,
    }

    create_response = requests.post(f'{base_url}', json=new_post)
    print(create_response.text)
    assert create_response.status_code == 201
    assert create_response.json()["title"] == "Test Post"
    assert create_response.json()["body"] == "Test Content"
    assert create_response.json()["user_id"] == 1
    assert create_response.json()["id"] == 101


#пРАВИЛЬНО!!!
def test_create_post2():

    base_url = 'https://jsonplaceholder.typicode.com/posts'

    new_post = {
        'title': "Test Post",
        'body': "Test Content",
        "user_id": 1,
    }

    create_response = requests.post(f'{base_url}', json=new_post)
    print(create_response.text)
    assert create_response.status_code == 201

    created_post = create_response.json()
    assert created_post["title"] == "Test Post"
    assert created_post["body"] == "Test Content"
    assert created_post["user_id"] == 1
    assert created_post["id"] == 101


# Тест с параметрами
def test_get_posts_by_user():

     params = {
        'userId': 1,
     }
     response = requests.get('https://jsonplaceholder.typicode.com/posts',params=params)
     posts = response.json()
     assert response.status_code == 200
     assert posts
     for post in posts:
         assert post.get("userId") == 1




# Тест обработки ошибки
def test_get_nonexistent_user():

    user_id = 999999
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    assert response.status_code == 404