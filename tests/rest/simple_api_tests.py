import requests



def test_simple_login_and_get_users():
    test_data = {
        "username": "AlexTest",
        "password": "Alex2301"
    }

    response = requests.post("http://localhost:8080/api/auth/login", json=test_data)
    assert response.status_code == 200

    response_data = response.json()
    token = response_data['token']

    headers = {"Authorization": f"Bearer {token}"}


    response2 = requests.get("http://localhost:8080/api/users/all", headers=headers)

    print(f"Status code: {response2.status_code}")
    print(f"Response headers: {response2.headers}")
    print(f"Response body: {response2.text}")

    assert response2.status_code == 200
    users = response2.json()
    assert users

def test_get_user_by_id():
    test_data = {
        "username": "AlexTest",
        "password": "Alex2301"
    }

    response = requests.post("http://localhost:8080/api/auth/login", json=test_data)
    assert response.status_code == 200

    response_data = response.json()
    token = response_data['token']

    headers = {"Authorization": f"Bearer {token}"}

    response2 = requests.get("http://localhost:8080/api/users/1", headers=headers)
    admin = response2.json()
    print(admin)


def test_put_created_user(my_admin_login,create_user):
    user_id = create_user["id"]
    update_data = {
        "username": "PutAlex",
        "email": "bimbim@bambam",
        "password": "qwerty123",
        "role": "SELLER"
    }
    response = requests.put(f"http://localhost:8080/api/users/{user_id}", json=update_data, headers=my_admin_login)
    assert response.status_code == 200

    updated_user = response.json()

    assert updated_user["id"] == user_id
    assert "username" in updated_user
    assert "email" in updated_user
    assert "role" in updated_user
    assert updated_user["username"] == "PutAlex"
    assert updated_user["email"] == "bimbim@bambam"

def test_check_pagination(my_admin_login):
    pages_numbers = [i for i in range(0, 1)]
    for page in pages_numbers:
        params = {
            "pages":page,
            "size": 10,
            "sortBy": "createdAt",
            "sortDirection": "asc"
        }
        response = requests.get("http://localhost:8080/api/users", params=params, headers=my_admin_login)
        assert response.status_code == 200

        data = response.json()
        for k, v in data.items():
            print(f'{k}: {v}')

        assert 'content' in data
        users = data["content"]
        for user in users:
            assert "id" in user
            assert "username" in user
            assert "email" in user
            assert "role" in user

        assert 'pages' in data
        assert 'size' in data
        assert 'totalElements' in data
        assert 'totalPages' in data
        assert 'first' in data
        assert 'last' in data
        assert 'hasNext' in data
        assert 'hasPrevious' in data


def test_get_all_users(my_admin_login):
    response = requests.get("http://localhost:8080/api/users/all", headers=my_admin_login)
    assert response.status_code == 200
    data = response.json()
    assert data is not None
    assert isinstance(data, list)
    assert len(data) > 0

    for user in data:
        assert "id" in user
        assert "username" in user
        assert "email" in user
        assert "role" in user

def test_negative_updates(my_admin_login,create_user):
    user_id = create_user["id"]
    update_data = {
        "username": "PutAlex",
        "email": "bimbim@bambam",
        "password": "qwerty123",
        "role": "SELLER"
    }
    response = requests.put(f"http://localhost:8080/api/users/{user_id}", json=update_data)
    print(response.json())
    assert response.status_code == 403

def test_create_ingredients(my_admin_login):
    ingredient = {
        "name": "BimBi1m11121 21",
        "quantity": 10,
    }
    response = requests.post("http://localhost:8080/api/ingredients", json=ingredient,headers=my_admin_login)
    assert response.status_code == 200
    ingredients = response.json()
    print(ingredients)

    id_ingredient = ingredients["id"]
    response2 = requests.delete(f"http://localhost:8080/api/ingredients/{id_ingredient}", headers=my_admin_login)
    assert response2.status_code == 204
    print(f"✅ Успешно удален ингредиент id: {id_ingredient}")

def test_get_created_ingredients_by_id(my_admin_login):
    ingredient = {
        "name": "B1mB1m",
        "quantity": 5,
    }
    response = requests.post("http://localhost:8080/api/ingredients", json=ingredient, headers=my_admin_login)
    assert response.status_code == 200
    created_ingredients = response.json()
    id_ingredient = created_ingredients["id"]

    response2 = requests.get(f"http://localhost:8080/api/ingredients/{id_ingredient}", headers=my_admin_login)
    assert response2.status_code == 200
    print(response2.json())
    assert response2.json() is not None
    print(f"Айди ингредиента: {id_ingredient} получаем по ссылке /get")

def test_check_available_ingredients(my_admin_login):
    response = requests.get("http://localhost:8080/api/ingredients/available", headers=my_admin_login)
    assert response.status_code == 200

    data = response.json()
    for ingredients in data:
        assert "id" in ingredients
        assert "name" in ingredients
        assert "quantity" in ingredients





