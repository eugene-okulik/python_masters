import allure
from time import sleep

import pytest

from ui_tests_eokulik.pages.sign_in_page import SignIn
from ui_tests_eokulik.data import users


@pytest.mark.smoke
@allure.feature('login')
@allure.story('Validations')
def test_incorrect_login(driver):
    sign_in_page = SignIn(driver)
    sign_in_page.open()
    sign_in_page.login_user(
        users.incorrect_user['email'],
        users.incorrect_user['password']
    )
    sleep(3)
    sign_in_page.alert_message_is_correct(
        'The account sign-in was incorrect or your account is disabled temporarily. '
        + 'Please wait and try again later.'
    )
