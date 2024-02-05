import pytest


@pytest.fixture()
def experiment():
    print('\nexperiment')
    yield
    print('\nexperiment END')
