from data.locators import Locators
from pages.sale_page import SalePage
import allure


@allure.testcase(Locators.sale_url, 'Test sale page')
def test_sales_page(driver):
    page = SalePage(driver)

    page.open()
    page.check_url(f"{Locators.base_url}{Locators.sale_url}")
    page.check_title(page.title)
    page.check_element(Locators.dealsWomen).is_displayed()
    page.check_element(Locators.dealsMen).is_displayed()
    page.check_element(Locators.dealsLuma).is_displayed()
    page.check_element(Locators.discont20Percent).is_displayed()
    page.check_element(Locators.discont50Uds).is_displayed()
