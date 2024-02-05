import pytest


@pytest.fixture()
def start():
    print('\nStarting a test - UPD')
    yield
    print('\nFinishing a test - UPD')
