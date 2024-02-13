import requests
import allure
from data import posts
from endpoints.endpoint import Endpoints


class CreatePublication(Endpoints):
    post_id = None

    @allure.step('Send request to create new post')
    def create_new_post(self, payload=posts.default_post_data, headers=posts.default_headers):
        self.response = requests.post(
            self.base_url,
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()
        self.post_id = self.response_json['id']

    @allure.step('Check that title is correct')
    def check_title(self, title=posts.default_post_data['title']):
        assert self.response_json['title'] == title, 'title is incorrect'
