import requests
import pytest
import allure


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


@allure.feature('Creation')
@allure.story('Create one')
@allure.severity('critical')
@allure.title('Создание одного поста')
def test_post_create():
    with allure.step('Prepare data'):
        data = {
            "title": "woeiurwejhrksjdf",
            "body": "iwueiuwkjsdfnbvkskjahdsfkjahsdf",
            "userId": 2
        }
        headers = {
            'Content-Type': 'application/json'
        }
    with allure.step(f'Send request with data {data}'):
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=data,
            headers=headers
        ).json()
    with allure.step('Check response'):
        assert response['title'] == data['title']


@allure.feature('Creation')
@allure.story('Create one')
@allure.severity('minor')
def test_post_create_negative():
    with allure.step('Prepare data'):
        data = {
            "title": [],
            "body": {},
            "userId": 2
        }
        headers = {
            'Content-Type': 'application/json'
        }
    with allure.step(f'Send request with data {data}'):
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=data,
            headers=headers
        ).json()
    with allure.step('Check response'):
        assert response['title'] == data['title']


@allure.feature('Get existing')
@allure.story('Get Many')
def test_get_all(start_end):
    with allure.step('run request'):
        response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts').json()
    with allure.step('Check response'):
        assert len(response) == 100, 'Posts quantity is not correct'


@allure.severity('blocker')
@allure.feature('Get existing')
@allure.story('Get one')
@pytest.mark.huge
def test_get_one(post_id, start_end, start_end_testing):
    with allure.step('run request'):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}').json()
    with allure.step('Check response'):
        assert response['id'] == post_id


@allure.severity('trivial')
@allure.feature('example')
@pytest.mark.parametrize('data', [1, 2, 3])
@pytest.mark.tiny
def test_one(data):
    assert data == data
