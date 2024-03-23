from playwright.sync_api import Page, expect
from data.locators import Data
from pages.sale_page import SalePage
import allure


@allure.testcase(Data.sale_url, 'Test sale page')
def test_sales_page(page: Page):
    page = SalePage(page)

    page.open()
    page.check_url(f"{Data.base_url}{Data.sale_url}")
    page.check_title(page.title)

    page.check_element(Data.dealsWomen).is_visible()
    page.check_element(Data.dealsMen).is_visible()
    page.check_element(Data.dealsLuma).is_visible()
    page.check_element(Data.discont20Percent).is_visible()
    page.check_element(Data.discont50Uds).is_visible()
