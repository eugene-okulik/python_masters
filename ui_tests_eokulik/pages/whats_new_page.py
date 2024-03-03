import allure
from selenium.webdriver.common.by import By
from ui_tests_eokulik.pages.base_page import BasePage


YOGA_BUTTON = (By.CSS_SELECTOR, '.more.button')
PAGE_HEADER = (By.TAG_NAME, 'h1')


class WhatsNew(BasePage):
    page_url = '/what-is-new.html'

    @allure.step('Click yoga button')
    def click_yoga_button(self):
        self.find(YOGA_BUTTON).click()
