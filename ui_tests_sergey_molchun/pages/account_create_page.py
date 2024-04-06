from pages.base_page import BasePage
from data.locators import Locators


class AccountCreatePage(BasePage):
    page_url = Locators.create_account_url
    title = 'Create New Customer Account'
