import datetime
import requests
import json

URL = 'https://api.restful-api.dev/objects'
headers = {"content-type": "application/json"}
entity_id = None


# TODO: Задание
# Для тестирования возьмем небольшое тестовое API: https://restful-api.dev
# Нужно протестировать все перечисленные в спецификации функции, а именно:
#


# Выполняйте всё задание так же, как я делал на занятии, - каждый запрос в отдельной функции.
# Каждая функция должна заканчиваться проверкой того, что запрос отработал правильно.


def get_request():
    r = requests.get(URL, headers=headers)
    assert r.status_code == 200, 'Status code is incorrect'


# Создание объекта
def create_new_entity_post():
    global entity_id
    payload = json.dumps(
        {"name": "Apple iPhone 16/5", "data": {"color": "Plasma", "generation": "1.2", "price": 15975}})
    r = requests.post(URL, data=payload, headers=headers)
    entity_id = r.json()['id']
    print(entity_id)

    assert r.status_code == 200, 'Status code is incorrect'
    assert r.json()['name'] == "Apple iPhone 16/5", 'Name value is incorrect'
    assert r.json()['data']['color'] == "Plasma", 'Color value is incorrect'
    assert r.json()['data']['generation'] == "1.2", 'Generation value is incorrect'
    assert r.json()['data']['price'] == 15975, 'Price value is incorrect'


# Изменение объекта с помощью метода PUT
def replace_entire_entity_put():
    payload = json.dumps({"name": "Apple Vision", "data": {"color": "white", "generation": "2nd", "price": 3499}})
    requestUrl = f"{URL}/{entity_id}"
    r = requests.put(requestUrl, data=payload, headers=headers)

    day_today = str(datetime.datetime.now()).split()[0]
    assert r.status_code == 200, 'Status code is incorrect'
    update_date = str(r.json()['updatedAt']).split('T')[0]

    assert update_date == day_today, 'Update date is incorrect'
    assert r.json()['name'] == "Apple Vision", 'Name value is incorrect'
    assert r.json()['data']['color'] == "white", 'Color value is incorrect'
    assert r.json()['data']['generation'] == "2nd", 'Generation value is incorrect'
    assert r.json()['data']['price'] == 3499, 'Price value is incorrect'


# Изменение объекта с помощью метода PATCH
def update_entity_partialy():
    payload_name = {"name": "Apple Vision Pro"}
    payload_data_color = {"data": {"color": "White"}}
    payload_data_price = {"data": {"price": 4099}}
    # payload_data = json.dumps({"name": "Apple Vision Pro", "data": {"color": "White", "price": 4099}})
    requestUrl = f"{URL}/{entity_id}"
    r_name = requests.patch(requestUrl, json=payload_name, headers=headers)
    print(r_name.json())
    r_color = requests.patch(requestUrl, json=payload_data_color, headers=headers)
    print(r_color.json())
    r_price = requests.patch(requestUrl, json=payload_data_price, headers=headers)
    print(r_price.json())
    r = requests.get(requestUrl, headers=headers)
    print(r.json())

    assert r.status_code == 200, 'Status code is incorrect'
    assert r.json()['name'] == "Apple Vision Pro", 'Name value is incorrect - Это неправильный PATCH сервера!'
    assert r.json()['data']['color'] == "White", 'Color value is incorrect - Это неправильный PATCH сервера!'
    assert r.json()['data']['generation'] == "2nd", 'Generation value is incorrect - Это неправильный PATCH сервера!'
    assert r.json()['data']['price'] == 4099, 'Price value is incorrect - Это неправильный PATCH сервера!'


# Удаление объекта
def delete_the_entiry():
    requestUrl = f"{URL}/{entity_id}"
    r = requests.delete(requestUrl, headers=headers)

    assert r.status_code == 200, 'Status code is incorrect'
    assert r.json()['message'] == f"Object with id = {entity_id} has been deleted."

    r_check = requests.get(requestUrl, headers=headers)
    print(r_check.text)


get_request()
create_new_entity_post()
replace_entire_entity_put()
update_entity_partialy()
delete_the_entiry()
