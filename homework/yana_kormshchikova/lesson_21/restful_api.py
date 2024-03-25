import json

import requests

# Для тестирования возьмем небольшое тестовое API: https://restful-api.dev
# Нужно протестировать все перечисленные в спецификации функции, а именно:
#
# Создание объекта
# Изменение объекта с помощью метода PUT
# Изменение объекта с помощью метода PATCH
# Удаление объекта
# Выполняйте всё задание так же, как я делал на занятии, - каждый запрос в отдельной функции.
# Каждая функция должна заканчиваться проверкой того, что запрос отработал правильно.

BASE_URL = 'https://api.restful-api.dev/objects'
headers = {"content-type": "application/json"}


def create_object():
    global object_id
    payload = json.dumps({
        "name": "Apple Iphone 8 Plus",
        "data": {
            "year": 2017,
            "color": "Space Grey",
            "price": 599.98,
            "memory size": "256 GB"
        }
    })
    response = requests.post(f'{BASE_URL}', data=payload, headers=headers)

    object_id = response.json()['id']
    print(object_id)

    assert response.status_code == 200, 'Incorrect status code'
    assert response.json()['name'] == 'Apple Iphone 8 Plus', 'Incorrect name value'
    assert response.json()['data']['year'] == 2017, 'Incorrect year value'
    assert response.json()['data']['color'] == 'Space Grey', 'Incorrect color value'
    assert response.json()['data']['price'] == 599.98, 'Incorrect price value'
    assert response.json()['data']['memory size'] == '256 GB', 'Incorrect memory size value'


def update_object():
    payload = json.dumps({
        "name": "Apple Iphone 15 Pro Max",
        "data": {
            "year": 2023,
            "color": "Green",
            "price": 1599,
            "memory size": "1 TB"
        }
    })
    response = requests.put(f'{BASE_URL}/{object_id}', data=payload, headers=headers)

    assert response.status_code == 200, 'Incorrect status code'
    assert response.json()['name'] == 'Apple Iphone 15 Pro Max', 'Incorrect name value'
    assert response.json()['data']['year'] == 2023, 'Incorrect year value'
    assert response.json()['data']['color'] == 'Green', 'Incorrect color value'
    assert response.json()['data']['price'] == 1599, 'Incorrect price value'
    assert response.json()['data']['memory size'] == '1 TB', 'Incorrect memory size value'


def partially_update_object():
    payload_updated_name = {"name": "Samsung S20 Ultra"}

    requests.patch(f'{BASE_URL}/{object_id}', json=payload_updated_name, headers=headers)

    response = requests.get(f'{BASE_URL}/{object_id}', headers=headers)

    assert response.status_code == 200, 'Incorrect status code'
    assert response.json()['name'] == 'Samsung S20 Ultra', 'Incorrect name value'


def delete_object():
    response = requests.delete(f'{BASE_URL}/{object_id}', headers=headers)

    assert response.status_code == 200, 'Incorrect status code'
    assert response.json()['message'] == f"Object with id = {object_id} has been deleted."


create_object()
update_object()
partially_update_object()
delete_object()
