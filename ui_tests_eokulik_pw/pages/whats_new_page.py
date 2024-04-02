import allure
from ui_tests_eokulik_pw.pages.base_page import BasePage


YOGA_BUTTON = '.more.button'
PAGE_HEADER = 'h1'


class WhatsNew(BasePage):
    page_url = '/what-is-new.html'

    @allure.step('Click yoga button')
    def click_yoga_button(self):
        self.find(YOGA_BUTTON).click()
