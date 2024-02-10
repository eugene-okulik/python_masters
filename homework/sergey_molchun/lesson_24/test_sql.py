import pytest
import functions
import allure


@allure.epic('Website API')
@allure.feature('Get all items')
@allure.severity('blocker')
@pytest.mark.medium
def test_get_request():
    r = functions.get_request()
    assert r.status_code == 200, 'Status code is incorrect'


@allure.epic('Website API')
@allure.feature('Create a new item')
@allure.severity('critical')
@pytest.mark.critical
def test_create_new_entity_post(entity_id):
    r = functions.get_particular_entity(entity_id)
    assert r.status_code == 200, 'Status code is incorrect'
    assert r.json()['name'] == "Apple iPhone 16/5", 'Name value is incorrect'
    assert r.json()['data']['color'] == "Plasma", 'Color value is incorrect'
    assert r.json()['data']['generation'] == "1.2", 'Generation value is incorrect'
    assert r.json()['data']['price'] == 15975, 'Price value is incorrect'


@allure.epic('Website API')
@allure.feature('Update existing item with PUT')
@allure.severity('critical')
@pytest.mark.critical
@pytest.mark.parametrize("name, color, generation, price", [
    ("Apple Vision", "white", "2nd", 3499),
    ("Apple Vision Pro", "black", "3rd", 3999),
    ("Apple Vision Plus", "silver", "4th", 4499)
])
def test_replace_entire_entity_put(entity_id, name, color, generation, price):
    payload = functions.json.dumps({"name": name, "data": {"color": color, "generation": generation, "price": price}})
    r = functions.replace_entire_entity(entity_id, payload)
    assert r.status_code == 200, 'Status code is incorrect'
    assert r.json()['name'] == name, 'Name value is incorrect'
    assert r.json()['data']['color'] == color, 'Color value is incorrect'
    assert r.json()['data']['generation'] == generation, 'Generation value is incorrect'
    assert r.json()['data']['price'] == price, 'Price value is incorrect'


@allure.epic('Website API')
@allure.feature('Update existing item with PATCH')
@allure.severity('critical')
@pytest.mark.critical
def test_update_entity(entity_id):
    payload = {"name": "Apple Vision Pro"}
    r = functions.update_entity(entity_id, payload)
    assert r.status_code == 200, 'Status code is incorrect'
    assert r.json()['name'] == "Apple Vision Pro", 'Name value is incorrect'


@allure.epic('Website API')
@allure.feature('Delete existing item')
@allure.severity('critical')
@pytest.mark.critical
def test_delete_the_entity(entity_id):
    r = functions.delete_the_entity(entity_id)
    assert r.status_code == 200, 'Status code is incorrect'
    check = functions.get_particular_entity(entity_id)
    assert check.json()['error'] == f"Oject with id={entity_id} was not found."
