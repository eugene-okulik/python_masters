from ui_tests_sergey_molchun.pages.base_page import BasePage
from ui_tests_sergey_molchun.data.data import Data


class SalePage(BasePage):
    page_url = Data.sale_url
    title = 'Sale'
