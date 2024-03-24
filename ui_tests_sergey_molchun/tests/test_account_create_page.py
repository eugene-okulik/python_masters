from data.data import driver
from data.locators import Locators
from pages.account_create_page import AccountCreatePage
from selenium.webdriver.remote.webdriver import WebDriver
import allure


@allure.testcase(Locators.create_account_url, 'Test create account page')
def test_create_account_page(driver: WebDriver):
    page = AccountCreatePage(driver)
    page.open()
    page.check_url(f'{Locators.base_url}{Locators.create_account_url}')
    page.check_title(page.title)

    page.check_element(Locators.field_first_name)
    page.check_element(Locators.field_last_name)
    page.check_element(Locators.field_email)
    page.check_element(Locators.field_password)
    page.check_element(Locators.field_password_confirm)
    page.check_element(Locators.button_submit)
