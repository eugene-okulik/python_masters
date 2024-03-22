from playwright.sync_api import Page, expect
from ui_tests_sergey_molchun.data.data import Data
from ui_tests_sergey_molchun.pages.base_page import BasePage
import allure


@allure.testcase(Data.base_url, 'Test start page')
def test_start_page(page: Page):
    page = BasePage(page)
    page.open()
    page.check_url(Data.base_url)
    page.check_title(page.title)
    page.check_header_h1('Home Page')
