import pytest
import datetime
from functions import *


@pytest.fixture(scope='session', autouse=True)
def global_test():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture(scope='function')
def created_entity():
    entity_id = create_new_entity().json()['id']
    yield entity_id
    delete_the_entity(entity_id)


@pytest.mark.medium
def test_get_request():
    r = get_request()
    assert r.status_code == 200, 'Status code is incorrect'


@pytest.mark.critical
def test_create_new_entity_post():
    r = create_new_entity()
    assert r.status_code == 200, 'Status code is incorrect'
    assert r.json()['name'] == "Apple iPhone 16/5", 'Name value is incorrect'
    assert r.json()['data']['color'] == "Plasma", 'Color value is incorrect'
    assert r.json()['data']['generation'] == "1.2", 'Generation value is incorrect'
    assert r.json()['data']['price'] == 15975, 'Price value is incorrect'


@pytest.mark.critical
@pytest.mark.parametrize("name, color, generation, price", [
    ("Apple Vision", "white", "2nd", 3499),
    ("Apple Vision Pro", "black", "3rd", 3999),
    ("Apple Vision Plus", "silver", "4th", 4499)
])
def test_replace_entire_entity_put(global_test, created_entity, name, color, generation, price):
    entity_id = created_entity
    payload = json.dumps({"name": name, "data": {"color": color, "generation": generation, "price": price}})
    r = replace_entire_entity(entity_id, payload)
    day_today = str(datetime.datetime.now()).split()[0]
    assert r.status_code == 200, 'Status code is incorrect'
    update_date = str(r.json()['updatedAt']).split('T')[0]
    assert update_date == day_today, 'Update date is incorrect'
    assert r.json()['name'] == name, 'Name value is incorrect'
    assert r.json()['data']['color'] == color, 'Color value is incorrect'
    assert r.json()['data']['generation'] == generation, 'Generation value is incorrect'
    assert r.json()['data']['price'] == price, 'Price value is incorrect'


@pytest.mark.critical
def test_update_entity_partialy(created_entity):
    entity_id = created_entity
    r_name = update_entity_name(entity_id)
    assert r_name.status_code == 200, 'Status code is incorrect'
    assert r_name.json()['name'] == "Apple Vision Pro", 'Name value is incorrect'


@pytest.mark.critical
def test_delete_the_entity():
    entity_id = create_new_entity().json()['id']
    r = delete_the_entity(entity_id)
    assert r.status_code == 200, 'Status code is incorrect'
    assert r.json()['message'] == f"Object with id = {entity_id} has been deleted."
