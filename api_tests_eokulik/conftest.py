from endpoints.create_post import CreatePublication
from endpoints.get_posts import GetPosts
import pytest
import requests


@pytest.fixture()
def new_pub_endpoint():
    return CreatePublication()


@pytest.fixture()
def get_posts_endp():
    return GetPosts()


@pytest.fixture()
def post_id(new_pub_endpoint):
    new_pub_endpoint.create_new_post()
    yield new_pub_endpoint.post_id - 1
    requests.delete(f'https://jsonplaceholder.typicode.com/posts{new_pub_endpoint.post_id - 1}')
