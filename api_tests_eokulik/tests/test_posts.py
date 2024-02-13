import allure
from data import posts
from endpoints.create_post import CreatePublication


@allure.feature('Creation')
@allure.story('Create one')
@allure.severity('critical')
@allure.title('Создание одного поста')
@allure.description('Этот тест что-то проверяет')
def test_post_create():
    new_pub_endpoint = CreatePublication()
    new_pub_endpoint.create_new_post()
    new_pub_endpoint.check_response_is_201()
    new_pub_endpoint.check_title()


@allure.feature('Creation')
@allure.story('Create one')
@allure.severity('minor')
def test_post_create_negative(new_pub_endpoint):
    new_pub_endpoint.create_new_post(
        payload=posts.wrong_types_data
    )
    new_pub_endpoint.check_response_is_201()
    new_pub_endpoint.check_title(posts.wrong_types_data['title'])


@allure.feature('Get existing')
@allure.story('Get Many')
def test_get_all(get_posts_endp):
    get_posts_endp.get_all_posts()
    get_posts_endp.check_response_is_200()
    get_posts_endp.check_all_posts_returned()


@allure.severity('blocker')
@allure.feature('Get existing')
@allure.story('Get one')
def test_get_one(post_id, get_posts_endp):
    get_posts_endp.get_post_by_id(post_id)
    get_posts_endp.check_post_id_is_correct(post_id)
