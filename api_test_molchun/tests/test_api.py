import classes.api_classes as api
import pytest
import allure


@allure.epic('Website API')
@allure.feature('Get all items')
@allure.severity('blocker')
@pytest.mark.medium
def test_get_request():
    new_test = api.GetEntity()
    new_test.get_all()
    new_test.check_response_code()


@allure.epic('Website API')
@allure.feature('Create a new item')
@allure.severity('critical')
@pytest.mark.critical
def test_create_new_entity(entity_id):
    name = 'Apple iPhone 16/5'
    color = 'Plasma'
    generation = '1.2'
    price = 15975
    new_test = api.CreateEntity()
    new_test.create_entity(name, color, generation, price)
    new_test.check_response_code()
    new_test.check_entity_name(name)
    new_test.check_entity_color(color)
    new_test.check_entity_generation(generation)
    new_test.check_entity_price(price)


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
    # print(entity_id, name, color, generation, price)
    replace_entity = api.ReplaceEntity()
    replace_entity.replace_entity(entity_id, name=name, color=color, generation=generation, price=price)
    replace_entity.check_response_code()
    replace_entity.check_entity_name(name)
    replace_entity.check_entity_color(color)
    replace_entity.check_entity_generation(generation)
    replace_entity.check_entity_price(price)


@allure.epic('Website API')
@allure.feature('Update existing item with PATCH')
@allure.severity('critical')
@pytest.mark.critical
def test_update_entity(entity_id):
    update_entity = api.UpdateEntity()
    update_entity.update_entity(entity_id, "Apple Vision Pro")
    update_entity.check_response_code()
    update_entity.check_entity_name("Apple Vision Pro")


@allure.epic('Website API')
@allure.feature('Delete existing item')
@allure.severity('critical')
@pytest.mark.critical
def test_delete_the_entity(entity_id):
    delete_entity = api.DeleteEntity()
    delete_entity.delete_entity(entity_id)
    delete_entity.check_response_code()
    delete_entity.check_entity_is_deleted(entity_id)
