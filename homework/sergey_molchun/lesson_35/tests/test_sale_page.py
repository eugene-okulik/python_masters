from playwright.sync_api import Page, expect
from data.data import Data
from data.locators import Locators
from pages.sale_page import SalePage
import allure


@allure.testcase(Data.sale_url, 'Test sale page')
def test_sales_page(page: Page):
    page = SalePage(page)

    page.open()
    page.check_url(f"{Data.base_url}{Data.sale_url}")
    page.check_title(page.title)

    assert page.element_is_visible(Locators.dealsWomen)
    assert page.element_is_visible(Locators.dealsMen)
    assert page.element_is_visible(Locators.dealsLuma)
    assert page.element_is_visible(Locators.discont20Percent)
    assert page.element_is_visible(Locators.discont50Uds)
