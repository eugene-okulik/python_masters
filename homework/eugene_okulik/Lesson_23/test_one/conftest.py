import pytest


@pytest.fixture()
def one():
    print('\nOne start')
    yield
    print('\nOne finish')
