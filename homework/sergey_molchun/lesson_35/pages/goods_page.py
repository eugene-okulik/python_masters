from data.locators import Locators
from pages.start_page import StartPage
import allure


@allure.step("Change number of the elements at the page")
class GoodsPage(StartPage):
    def change_page_items_number(self, preset_value, timeout=10000):
        self.page.wait_for_selector(Locators.page_limiter, state="attached")
        self.page.locator(Locators.page_limiter).last.select_option(preset_value)
        self.page.wait_for_load_state("networkidle")
