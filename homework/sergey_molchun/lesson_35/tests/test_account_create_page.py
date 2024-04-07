from playwright.sync_api import Page, expect
import data.test_data
from data.data import Data
from data.locators import Locators
from pages.account_create_page import AccountCreatePage
import allure


@allure.testcase(Data.create_account_url, 'Test create account page')
def test_create_account_page(page: Page):
    page = AccountCreatePage(page)
    page.open()
    page.check_url(f'{Data.base_url}{Data.create_account_url}')
    page.check_title(data.test_data.title)

    assert page.element_is_editable(Locators.field_first_name)
    assert page.element_is_editable(Locators.field_last_name)
    assert page.element_is_editable(Locators.field_email)
    assert page.element_is_editable(Locators.field_password)
    assert page.element_is_editable(Locators.field_password_confirm)
    assert page.element_is_enabled(Locators.button_submit)
