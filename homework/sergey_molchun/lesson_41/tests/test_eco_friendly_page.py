from playwright.sync_api import Page
from data import Data
from locators import Locators
from eco_friendly_page import EcoFriendlyPage
import allure
import pytest


@pytest.mark.regression
@pytest.mark.ecofriendly
@allure.testcase(Data.eco_friendly_url, 'Test eco-friendly page')
def test_eco_friendly_page(page: Page):
    page = EcoFriendlyPage(page)
    page.open()
    page.check_url(f'{Data.base_url}{Data.eco_friendly_url}')
    page.check_title(page.title)
    # page.change_page_items_number('36')
    # page.check_element(Data.page_limiter).last.select_option("36")

    page.check_element_text(Locators.goods_titles, Locators.page1_item1)
    page.check_element_text(Locators.goods_titles, Locators.page1_item2)
    page.check_element_text(Locators.goods_titles, Locators.page1_item3)
    page.open_next_page(Locators.next_page).last.click()
    page.check_element_text(Locators.goods_titles, Locators.page2_item1)
    page.check_element_text(Locators.goods_titles, Locators.page2_item2)
