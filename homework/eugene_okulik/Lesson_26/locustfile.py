from locust import task, HttpUser
import random


class PostsUser(HttpUser):
    post_id = None
    token = None

    def on_start(self):
        response = self.client.post('/authorize', json={'login': 'admin', 'password': 'mypass'})
        self.token = response['token']
        payload = {
            "title": "My tile",
            "body": "my body",
            "userId": 1
        }
        response = self.client.post('/posts', json=payload)
        self.post_id = response['post_id'] - 1

    @task(26)
    def get_one_post(self):
        self.client.get(f'/posts/{random.randrange(1, 102)}', headers={'Authorization': self.token})

    @task(1)
    def create_post(self):
        payload = {
            "title": "My tile",
            "body": "my body",
            "userId": 1
        }
        self.client.post('/posts', json=payload)

    @task(5)
    def get_created_post(self):
        self.client.get(f'/posts/{self.post_id}')


class CommentsUser(HttpUser):

    @task
    def get_one_comment(self):
        self.client.get(f'/comments/{random.randrange(1, 502)}')
