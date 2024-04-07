from playwright.sync_api import Page, expect
from data.locators import Locators
from data.data import Data
from pages.base_page import BasePage
import allure


class StartPage(BasePage):
    page_url = None
    title = 'Home Page'

    @allure.step("Open the page")
    def open(self, timeout=5000):
        if self.page_url:
            self.page.goto(f'{self.root_url}{self.page_url}')
        else:
            self.page.goto(self.root_url)

    @allure.step("Check page title")
    def check_title(self, title: str, timeout=5000):
        expect(self.page).to_have_title(title)

    @allure.step("Check page-url is correct")
    def check_url(self, url: str, timeout=5000):
        expect(self.page).to_have_url(url)

    @allure.step("Check page header")
    def check_header_h1(self, header: str, timeout=5000):
        page_header = self.page.locator(Locators.header_h1).text_content().strip()
        assert page_header == header

    @allure.step("Check and return the element")
    def check_element_is_present(self, element_locator, timeout=5000):
        page_element = self.page.locator(element_locator)
        return page_element

    @allure.step("Check element is visible")
    def element_is_visible(self, element_locator, timeout=5000):
        page_element = self.page.locator(element_locator).is_visible()
        if page_element:
            return True
        else:
            return False

    @allure.step("Open next page")
    def open_next_page(self, element_locator, timeout=5000):
        next_page = self.page.locator(element_locator)
        return next_page

    @allure.step("Check if element is present")
    def check_element_text(self, element_locator, product_text, timeout=5000):
        page_elements = self.page.locator(element_locator)
        element_texts = page_elements.all_text_contents()
        element_is_found = False
        for element in element_texts:
            item = element.strip()
            if item == product_text:
                # print(item)
                element_is_found = True
                assert item == product_text

        if element_is_found is False:
            raise Exception(f"No such element found: {product_text}")

    @allure.step("Change number of the elements at the page")
    def change_page_items_number(self, preset_value, timeout=10000):
        # self.page.locator(element_locator)
        self.page.wait_for_selector(Locators.page_limiter, state="attached")
        self.page.locator(Locators.page_limiter).last.select_option(preset_value)
        # time.sleep(15)
        self.page.wait_for_load_state("networkidle")
