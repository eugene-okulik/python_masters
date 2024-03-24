from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import StaleElementReferenceException
from data.locators import Locators
from conftest import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    root_url = Locators.base_url
    page_url = None
    title = 'Home Page'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Open the page")
    def open(self, timeout=5000):
        if self.page_url:
            self.driver.get(f'{self.root_url}{self.page_url}')
        else:
            self.driver.get(self.root_url)

    @allure.step("Check page title")
    def check_title(self, title: str, timeout=5000):
        assert self.driver.title == title

    @allure.step("Check page-url is correct")
    def check_url(self, url: str, timeout=5000):
        # print(self.driver.current_url)
        assert self.driver.current_url == url

    @allure.step("Check page header")
    def check_header_h1(self, header: str, timeout=5000):
        page_header = self.driver.find_element(*Locators.header_h1).text.strip()
        assert page_header == header

    @allure.step("Check and return the element")
    def check_element(self, element_locator: tuple, timeout=5000):
        element = self.driver.find_element(*element_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        attempts = 3
        for attempt in range(attempts):
            try:
                page_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element_locator))
                # page_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(*element_locator))
                # page_element = self.driver.find_element(*element_locator)
                return page_element
            except StaleElementReferenceException:
                if attempt == attempts - 1:  # If this was the last attempt, raise the exception
                    raise

    @allure.step("Check and return the element")
    def check_elements(self, element_locator: tuple, timeout=5000):
        page_elements = self.driver.find_elements(*element_locator)
        return page_elements

    @allure.step("Check if element is present")
    def check_element_by_text(self, element_locator: tuple, product_text, timeout=5000):
        page_elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(element_locator))
        element_is_found = False
        for element in page_elements:

            item = element.text.strip()
            if item == product_text:
                element_is_found = True
                assert item == product_text

        if element_is_found is False:
            raise Exception(f"No such element found: {product_text}")
