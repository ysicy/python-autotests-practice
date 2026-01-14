from typing import Any

import requests

def test_get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    users_data = response.json()
    assert response.status_code == 200
    assert "email" in users_data
    assert "name" in users_data
    assert "id" in users_data
    assert users_data["address"]["street"] == 'Kulas Light'
    assert users_data["address"]["city"] == 'Gwenborough'
    assert users_data["address"]["zipcode"] == '92998-3874'
    assert users_data["company"]["catchPhrase"] == 'Multi-layered client-server neural-net'
    assert users_data["company"]["bs"] == 'harness real-time e-markets'

def test_get_user_all():

    response = requests.get("https://jsonplaceholder.typicode.com/users")
    users_list = response.json()

    user = users_list[2]
    assert response.status_code == 200
    assert user["id"] == 3
    assert user["company"]["name"] == 'Romaguera-Jacobson'

def test_get_photos():
    parametrs = {
        "albumId": 32
    }
    response = requests.get("https://jsonplaceholder.typicode.com/photos", params=parametrs)

    assert response.status_code == 200
    photo_albums = response.json()
    photo_album = photo_albums[0]
    assert photo_album["id"] == 1551
    assert photo_album["title"] == "nemo labore earum est atque voluptatem inventore quae et"
    assert "url" in photo_album
    assert "thumbnailUrl" in photo_album

def test_get_todos():

    user_data = {
        "userId": 2,
        "completed": "false"
    }

    response = requests.get("https://jsonplaceholder.typicode.com/todos",params=user_data)
    assert response.status_code == 200
    todos = response.json()
    one_todos = todos[4]
    assert one_todos["userId"] == 2
    assert one_todos["completed"] == False
    assert one_todos["id"] == 29
    assert one_todos["title"] == "laborum aut in quam"

def test_get_one_todos():

    response = requests.get("https://jsonplaceholder.typicode.com/todos/45")
    assert response.status_code == 200
    one_todos = response.json()
    assert one_todos["userId"] == 3
    assert one_todos["completed"] == False
    assert one_todos["id"] == 45
    assert one_todos["title"] == "velit soluta adipisci molestias reiciendis harum"

def test_post_comments():
    comment = {
        "userId": 10,
        "name": "Alex",
        "email": "lenya@autotester",
        "body": "Hello! It's my first POST endpoint!"
    }
    response = requests.post("https://jsonplaceholder.typicode.com/comments", json=comment)
    assert response.status_code == 201
    message = response.json()
    assert message["body"] == "Hello! It's my first POST endpoint!"
    assert message["userId"] == 10
    assert message["email"] == "lenya@autotester"
    assert message["id"] == 501

def test_post_posts():
    my_post = {
        "userId": 100500,
        "id": 101,
        "title": "Alex",
        "body": "Hello! It's my second POST endpoint!"
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=my_post)
    assert response.status_code == 201
    message = response.json()
    assert message["body"] == "Hello! It's my second POST endpoint!"
    assert message["id"] == 101
    assert message["title"] == "Alex"
    assert "userId" in message

def test_patch_posts():
    my_patch = {
        "title": "My first PATCH endpoint"
    }
    response = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json=my_patch)
    assert response.status_code == 200
    message = response.json()
    assert response.json()["title"] == "My first PATCH endpoint"
    assert "userId" in message
    assert "body" in message

def test_put_posts():
    my_put = {
        "title": "My first PUT endpoint",
        "body": "Hello! It's my second PUT endpoint!",
        "userId": 101
    }
    response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=my_put)
    assert response.status_code == 200
    message = response.json()
    assert message["title"] == "My first PUT endpoint"
    assert "userId" in message
    assert message["body"] == "Hello! It's my second PUT endpoint!"
    assert "userId" in message

def test_delete_posts():

    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    message = response.json()
    assert message == {} #просто попробовал

def test_create_user():

    new_user = {
        "name": "Alex autotester",
        "email": "testimpost@mail.co",
        "username": "Bimbim BamBam"
    }
    response = requests.post("https://jsonplaceholder.typicode.com/users", json=new_user)
    assert response.status_code == 201
    user = response.json()
    assert "id" in user
    assert "name" in user
    assert "email" in user
    assert "username" in user



#ОЛЕГОВСКИЕ РУЧКИ

def test_get_users_oleg():

    response = requests.get("http://localhost:8080/api/users/all")
    otvet = response.json()
    print(otvet)


def post_json(url: str, data: dict[str, Any]) -> requests.Response:
    return requests.post(url, json=data)

post_json(
    "https://jsonplaceholder.typicode.com/posts", {
        "name": "Alex autotester",
        "email": "testimpost@mail.co",
        "username": "Bimbim BamBam"
    })







