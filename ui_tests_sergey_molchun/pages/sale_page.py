from pages.base_page import BasePage
from data.locators import Locators


class SalePage(BasePage):
    page_url = Locators.sale_url
    title = 'Sale'
