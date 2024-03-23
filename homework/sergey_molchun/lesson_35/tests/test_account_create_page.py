from playwright.sync_api import Page, expect
# from data.data import Data
# from data.data import Data
from data.locators import Data
from pages.account_create_page import AccountCreatePage
import allure


@allure.testcase(Data.create_account_url, 'Test create account page')
def test_create_account_page(page: Page):
    page = AccountCreatePage(page)
    page.open()
    page.check_url(f'{Data.base_url}{Data.create_account_url}')
    page.check_title(page.title)

    page.check_element(Data.field_first_name).is_editable()
    page.check_element(Data.field_last_name).is_editable()
    page.check_element(Data.field_email).is_editable()
    page.check_element(Data.field_password).is_editable()
    page.check_element(Data.field_password_confirm).is_editable()
    page.check_element(Data.button_submit).is_enabled()
