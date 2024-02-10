import pytest
import functions


@pytest.fixture(scope='session', autouse=True)
def global_test():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture(scope='function')
def entity_id():
    entity_id = functions.create_new_entity().json()['id']
    yield entity_id
    functions.delete_the_entity(entity_id)
