import allure
import requests
from endpoints.endpoint import Endpoints


class GetPosts(Endpoints):

    @allure.step('Get all posts')
    def get_all_posts(self):
        self.response = requests.request('GET', self.base_url)
        self.response_json = self.response.json()

    @allure.step('Check that 100 results returned')
    def check_all_posts_returned(self):
        assert len(self.response_json) == 100, 'Response len incorrect'

    @allure.step('Get post by id')
    def get_post_by_id(self, post_id):
        self.response = requests.get(f'{self.base_url}/{post_id}')
        self.response_json = self.response.json()

    @allure.step('Check that post id is correct')
    def check_post_id_is_correct(self, post_id):
        assert self.response_json['id'] == post_id, 'post id is incorrect'
