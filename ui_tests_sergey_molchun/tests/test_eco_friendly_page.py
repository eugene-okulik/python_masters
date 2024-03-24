from data.data import driver
from data.locators import Locators
from pages.eco_friendly_page import EcoFriendlyPage
import allure


@allure.testcase(Locators.eco_friendly_url, 'Test eco-friendly page')
def test_eco_friendly_page(driver):
    page = EcoFriendlyPage(driver)
    page.open()
    page.check_url(f'{Locators.base_url}{Locators.eco_friendly_url}')
    page.check_title(page.title)
    page.check_element_by_text(Locators.goods_titles, Locators.page1_item1)
    page.check_element_by_text(Locators.goods_titles, Locators.page1_item2)
    page.check_element_by_text(Locators.goods_titles, Locators.page1_item3)
    page.check_elements(Locators.next_page)[1].click()
    page.check_element_by_text(Locators.goods_titles, Locators.page2_item1)
    page.check_element_by_text(Locators.goods_titles, 'Bruno Compete Hoodie')
