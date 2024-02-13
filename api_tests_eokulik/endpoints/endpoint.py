import allure


class Endpoints:
    response = None
    response_json = None
    base_url = 'https://jsonplaceholder.typicode.com/posts'

    @allure.step('Check that response is 200')
    def check_response_is_200(self):
        assert self.response.status_code == 200, 'Code is not 200'

    @allure.step('Check that response is 201')
    def check_response_is_201(self):
        assert self.response.status_code == 201, 'Code is not 201'
