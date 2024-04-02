from playwright.sync_api import Page, expect, Locator
import allure
from ui_tests_eokulik_pw.pages.locators import BaseLoc as loc


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open the page')
    def open(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Can\'t open this page using URL')

    @allure.step('Find element')
    def find(self, locator) -> Locator:
        return self.page.locator(locator)

    @allure.step('Check title is correct')
    def check_header_is_correct(self, header):
        expect(self.find(loc.page_header)).to_have_text(header)

    @allure.step('Check url is correct')
    def check_url_is_correct(self, url):
        expect(self.page).to_have_url(url)
