import pytest


@pytest.fixture()
def start():
    print('\nStarting a test')
    yield
    print('\nFinishing a test')
