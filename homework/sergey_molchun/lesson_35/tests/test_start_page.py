from playwright.sync_api import Page, expect
from data.data import Data
from data.locators import Locators
from pages.start_page import StartPage
import allure


@allure.testcase(Data.base_url, 'Test start page')
def test_start_page(page: Page):
    page = StartPage(page)
    page.open()
    page.check_url(Data.base_url)
    page.check_title(page.title)
    page.check_header_h1('Home Page')
