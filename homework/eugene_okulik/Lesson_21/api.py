import requests


def get_all():
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100, 'Posts quantity is not correct'


def get_one():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/42').json()
    print(response['title'])


def create_post():
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
    print(response)


def put_post():
    data = {
        "title": "woeiurwejhrksjdf-UPD",
        "body": "iwueiuwkjsdfnbvkskjahdsfkjahsdf-UPD",
        "userId": 1
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.put(
        'https://jsonplaceholder.typicode.com/posts/42',
        json=data,
        headers=headers
    ).json()
    print(response)


def patch_post():
    data = {
        "title": "woeiurwejhrksjdf-UPD"
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.patch(
        'https://jsonplaceholder.typicode.com/posts/42',
        json=data,
        headers=headers
    ).json()
    print(response)


def delete_post():
    post_id = 101
    response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert response.status_code == 200, 'Status code incorrect'
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert response.status_code == 404, 'post is not deleted'
