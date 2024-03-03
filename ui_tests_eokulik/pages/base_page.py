from selenium.webdriver.remote.webdriver import WebDriver
import allure
from ui_tests_eokulik.pages.locators import BaseLoc as loc


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Open the page')
    def open(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Can\'t open this page using URL')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    @allure.step('Check title is correct')
    def check_header_is_correct(self, header):
        assert self.find(loc.page_header).text == header

    @allure.step('Check url is correct')
    def check_url_is_correct(self, url):
        assert self.driver.current_url == url
