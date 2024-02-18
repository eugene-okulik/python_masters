import pytest
from classes.api_classes import CreateEntity, DeleteEntity


@pytest.fixture()
def create_entity_fixture():
    return CreateEntity()


@pytest.fixture()
def entity_id(create_entity_fixture):
    print("CreateEntityFixture =", create_entity_fixture)
    create_entity_fixture.create_entity(name='Apple iPhone 16/5', color='Plasma', generation='1.2', price=15975)
    print(f"Returned entity_id: {create_entity_fixture.entity_id}")
    yield create_entity_fixture.entity_id
    delete_item = DeleteEntity()
    delete_item.delete_entity(create_entity_fixture.entity_id)
