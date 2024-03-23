from playwright.sync_api import Page, expect
from data.locators import Data
from pages.eco_friendly_page import EcoFriendlyPage
import allure


@allure.testcase(Data.eco_friendly_url, 'Test eco-friendly page')
def test_eco_friendly_page(page: Page):
    page = EcoFriendlyPage(page)
    page.open()
    page.check_url(f'{Data.base_url}{Data.eco_friendly_url}')
    page.check_title(page.title)
    # page.change_page_items_number('36')
    # page.check_element(Data.page_limiter).last.select_option("36")

    page.check_elements(Data.goods_titles, Data.page1_item1)
    page.check_elements(Data.goods_titles, Data.page1_item2)
    page.check_elements(Data.goods_titles, Data.page1_item3)
    page.check_element(Data.next_page).last.click()
    page.check_elements(Data.goods_titles, Data.page2_item1)
    page.check_elements(Data.goods_titles, 'Bruno Compete Hoodie')
