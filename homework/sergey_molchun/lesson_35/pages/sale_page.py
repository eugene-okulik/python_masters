from pages.base_page import BasePage
from data.locators import Data


class SalePage(BasePage):
    page_url = Data.sale_url
    title = 'Sale'
