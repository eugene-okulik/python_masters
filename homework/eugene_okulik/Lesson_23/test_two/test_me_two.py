import pytest
import random


@pytest.fixture(autouse=True)
def start():
    print('\nStarting a test - In File')
    yield '5'
    print('\nFinishing a test - In File')


def test_5(experiment):
    # sleep(3)
    assert 1 == 1


def help_calc(x):
    # sleep(3)
    return x * 2


def test_6(start):
    # sleep(3)
    print(start)
    assert 1 == random.randrange(3)
