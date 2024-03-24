from data.locators import Locators
from pages.base_page import BasePage
import allure


@allure.testcase(Locators.base_url, 'Test start page')
def test_start_page(driver):
    page = BasePage(driver)
    page.open()
    page.check_url(Locators.base_url)
    page.check_title(driver.title)
    page.check_header_h1('Home Page')
