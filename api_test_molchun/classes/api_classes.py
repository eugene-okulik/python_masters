from data.data_file import URL, headers
import requests
import json
import allure


class Base:
    URL = URL
    REQUEST_HEADERS = headers
    ENTITY_ID = None
    response = None
    response_json = None

    @allure.step('Check response code is 200')
    def check_response_code(self):
        # print(f"Response code: {self.response.status_code}")
        assert self.response.status_code == 200, "Response status code is not 200 OK"


class GetEntity(Base):
    entity_id = None

    @allure.step('Get all entities')
    def get_all(self, url=URL, headers=Base.REQUEST_HEADERS):
        self.response = requests.get(url, headers=headers)
        self.response_json = self.response.json()

    @allure.step('Get entity by ID')
    def get_by_id(self, entity_id, url=URL, headers=Base.REQUEST_HEADERS):
        requestUrl = f"{url}/{entity_id}"
        self.response = requests.get(requestUrl, headers=headers)
        self.response_json = self.response.json()


class CreateEntity(Base):
    entity_id = None

    @allure.step('Create an entity')
    def create_entity(self, name='Apple iPhone 16/5', color='Plasma', generation='1.2', price=15975,
                      url=URL, headers=Base.REQUEST_HEADERS):
        self.name = name
        self.color = color
        self.generation = generation
        self.price = price

        payload = json.dumps(
            {"name": name,
             "data": {
                 "color": color,
                 "generation": generation,
                 "price": price}
             }
        )

        self.response = requests.post(url, data=payload, headers=headers)
        # print(f"Response text: {self.response.text}")
        self.response_json = self.response.json()
        self.entity_id = self.response_json['id']
        # print(f"entity_id: {self.entity_id}")

    @allure.step('Check response code for entity creation is 200')
    def check_response_code(self):
        assert self.response.status_code == 200, "Response status code is not 200 OK"

    @allure.step('Check entity name')
    def check_entity_name(self):
        assert self.response_json['name'] == self.name, "Entity name is not correct"

    @allure.step('Check entity color')
    def check_entity_color(self):
        assert self.response_json['data']['color'] == self.color, "Entity color is not correct"

    @allure.step('Check entity generation')
    def check_entity_generation(self):
        assert self.response_json['data']['generation'] == self.generation, "Entity generation is not correct"

    @allure.step('Check entity price')
    def check_entity_price(self):
        assert self.response_json['data']['price'] == self.price, "Entity price is not correct"


class ReplaceEntity(Base):
    @allure.step('Replace entire entity')
    def replace_entity(self, entity_id=None, name='Apple iPhone 16/5', color='Plasma', generation='1.2', price=15975,
                       url=URL, headers=Base.REQUEST_HEADERS):
        requestUrl = f"{url}/{entity_id}"
        payload = json.dumps(
            {"name": name,
             "data": {
                 "color": color,
                 "generation": generation,
                 "price": price}
             }
        )
        self.response = requests.put(requestUrl, data=payload, headers=headers)
        self.response_json = self.response.json()

    @allure.step('Check entity name')
    def check_replaced_entity_name(self, name):
        # print(f"response: {self.response_json['name']}, argument: {name}")
        assert self.response_json['name'] == name, "Entity name is not correct"

    @allure.step('Check entity color')
    def check_replaced_entity_color(self, color):
        # print(f"response: {self.response_json['data']['color']}, argument: {color}")
        assert self.response_json['data']['color'] == color, "Entity color is not correct"

    @allure.step('Check entity generation')
    def check_replaced_entity_generation(self, generation):
        # print(f"response: {self.response_json['data']['generation']}, argument: {generation}")
        assert self.response_json['data']['generation'] == generation, "Entity generation is not correct"

    @allure.step('Check entity price')
    def check_replaced_entity_price(self, price):
        # print(f"response: {self.response_json['data']['price']}, argument: {price}")
        assert self.response_json['data']['price'] == price, "Entity price is not correct"


class UpdateEntity(Base):
    entity_id = None
    name = None

    @allure.step('Update entity partialy')
    def update_entity(self, entity_id, name, url=URL, headers=Base.REQUEST_HEADERS):
        payload = {"name": name}
        requestUrl = f"{url}/{entity_id}"
        self.response = requests.patch(requestUrl, json=payload, headers=headers)
        # print(f"Update response: {self.response.status_code}")
        self.response_json = self.response.json()

    @allure.step('Check entity name')
    def check_update_entity_name(self, name):
        # print(f"Check name response: {self.response_json['name']}, argument: {name}")
        assert self.response_json['name'] == name, "Entity name is not correct"


class DeleteEntity(Base):
    entity_id = None

    @allure.step('Delete entity')
    def delete_entity(self, entity_id, url=URL, headers=Base.REQUEST_HEADERS):
        requestUrl = f"{url}/{entity_id}"
        self.response = requests.delete(requestUrl, headers=headers)

    @allure.step('Check entity is not found')
    def check_entity_is_deleted(self, entity_id, url=URL, headers=Base.REQUEST_HEADERS):
        requestUrl = f"{url}/{entity_id}"
        self.response = requests.get(requestUrl, headers=headers)
        self.response_json = self.response.json()
        # print(f"Status code: {self.response.status_code}")
        # print(f"Response text: {self.response.text}")
        assert self.response.status_code == 404
        assert self.response_json['error'] == f"Oject with id={entity_id} was not found."
