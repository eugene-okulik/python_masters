import requests
import json

URL = 'https://api.restful-api.dev/objects'
headers = {"content-type": "application/json"}


def get_request():
    r = requests.get(URL, headers=headers)
    return r


def get_particular_entity(entity_id):
    requestUrl = f"{URL}/{entity_id}"
    r = requests.get(requestUrl, headers=headers)
    return r


def create_new_entity():
    payload = json.dumps(
        {"name": "Apple iPhone 16/5", "data": {"color": "Plasma", "generation": "1.2", "price": 15975}})
    r = requests.post(URL, data=payload, headers=headers)
    return r


def replace_entire_entity(entity_id, payload):
    requestUrl = f"{URL}/{entity_id}"
    r = requests.put(requestUrl, data=payload, headers=headers)
    return r


def update_entity_name(entity_id):
    payload_name = {"name": "Apple Vision Pro"}
    requestUrl = f"{URL}/{entity_id}"
    r_name = requests.patch(requestUrl, json=payload_name, headers=headers)
    return r_name


def delete_the_entity(entity_id):
    requestUrl = f"{URL}/{entity_id}"
    r = requests.delete(requestUrl, headers=headers)
    return r
