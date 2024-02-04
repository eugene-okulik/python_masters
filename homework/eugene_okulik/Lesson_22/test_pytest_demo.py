import requests
import pytest
import sys


@pytest.fixture()
def post_id():
    data = {
        "title": "woeiurwejhrksjdf",
        "body": "iwueiuwkjsdfnbvkskjahdsfkjahsdf",
        "userId": 2
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=data,
        headers=headers
    ).json()
    yield response['id'] - 1
    requests.delete(f'https://jsonplaceholder.typicode.com/posts{response["id"] - 1}')


@pytest.fixture(scope='function')
def start_end():
    print('\nStart test')
    yield
    print('\nend test')


@pytest.fixture(scope='session')
def start_end_testing():
    print('\nTesting started....')
    yield
    print('\n....Tesing finished')


@pytest.mark.skipif(sys.platform == 'darwin', reason='Bug #456')
def test_get_all(start_end):
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100, 'Posts quantity is not correct'


@pytest.mark.huge
def test_get_one(post_id, start_end, start_end_testing):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    assert response['id'] == post_id


@pytest.mark.parametrize('data', [1, 2, 3])
@pytest.mark.tiny
def test_one(data):
    assert data == 1
