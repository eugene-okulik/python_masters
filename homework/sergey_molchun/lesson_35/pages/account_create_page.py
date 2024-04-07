from pages.start_page import StartPage
from data.data import Data
import allure


class AccountCreatePage(StartPage):
    page_url = Data.create_account_url

    @allure.step("Check element is editable")
    def element_is_editable(self, element_locator, timeout=5000):
        page_element = self.page.locator(element_locator).is_editable()
        if page_element:
            return True
        else:
            return False

    @allure.step("Check element is enabled")
    def element_is_enabled(self, element_locator, timeout=5000):
        page_element = self.page.locator(element_locator).is_enabled()
        if page_element:
            return True
        else:
            return False
