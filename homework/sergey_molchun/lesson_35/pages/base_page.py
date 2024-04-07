from playwright.sync_api import Page
from data.data import Data


class BasePage:
    root_url = Data.base_url
    page_url = None

    def __init__(self, page: Page):
        self.page = page
