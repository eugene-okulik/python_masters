import unittest
import requests
import sys


class TestPostAPI(unittest.TestCase):
    post_id = None

    def setUp(self):
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
        # self.post_id = response['id']
        self.post_id = response['id'] - 1  # демонстрационный костыль

    def tearDown(self):
        requests.delete(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}')

    @unittest.skipIf(sys.platform == 'linux', 'Not for linux')
    def test_get_one(self):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{self.post_id}').json()
        self.assertEqual(response['id'], self.post_id)


class TestPostAPINoSetUp(unittest.TestCase):
    def test_create_post(self):
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
        self.assertEqual(response['title'], data['title'])

    def test_get_all(self):
        response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts').json()
        self.assertEqual(len(response), 100)


'''
assertEqual(a, b) — a == b
assertNotEqual(a, b) — a != b
assertTrue(x) — bool(x) is True
assertFalse(x) — bool(x) is False
assertIs(a, b) — a is b
assertIsNot(a, b) — a is not b
assertIsNone(x) — x is None
assertIsNotNone(x) — x is not None
assertIn(a, b) — a in b
assertNotIn(a, b) — a not in b
assertIsInstance(a, b) — isinstance(a, b)
assertNotIsInstance(a, b) — not isinstance(a, b)
assertGreater(a, b) — a > b
assertGreaterEqual(a, b) — a >= b
assertLess(a, b) — a < b
assertLessEqual(a, b) — a <= b
'''
