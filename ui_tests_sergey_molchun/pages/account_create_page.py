from ui_tests_sergey_molchun.pages.base_page import BasePage
from ui_tests_sergey_molchun.data.data import Data


class AccountCreatePage(BasePage):
    page_url = Data.create_account_url
    title = 'Create New Customer Account'
