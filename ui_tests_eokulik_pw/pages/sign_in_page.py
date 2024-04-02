from playwright.sync_api import expect
import allure
from ui_tests_eokulik_pw.pages.base_page import BasePage
from ui_tests_eokulik_pw.pages.locators import SignIn as loc


class SignIn(BasePage):
    page_url = '/customer/account/login'

    @allure.step('Enter email')
    def enter_email(self, email):
        email_field = self.page.get_by_test_id('email')
        # email_field = self.find(loc.email)
        email_field.fill(email)

    @allure.step('Enter password')
    def enter_password(self, passw):
        password = self.find(loc.password)
        password.fill(passw)

    @allure.step('Click sign in button')
    def click_sign_in(self):
        self.find(loc.sign_in_button).click()

    @allure.step('login user')
    def login_user(self, email, passw):
        self.enter_email(email)
        self.enter_password(passw)
        self.click_sign_in()

    @allure.step('Check message is correct')
    def alert_message_is_correct(self, message):
        alert = self.find(loc.alert)
        expect(alert).to_have_text(message)
