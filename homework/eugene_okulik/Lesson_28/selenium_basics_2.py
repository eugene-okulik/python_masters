from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture()
def driver():
    my_driver = webdriver.Chrome()
    sleep(3)  # Нужен для перетаскивания браузера в видимый экран (на занятии)
    my_driver.maximize_window()
    return my_driver


def test_one(driver):
    driver.get('https://magento.softwaretestingboard.com/sale.html')
    header = driver.find_element(By.TAG_NAME, 'h1')
    # header = driver.find_element(By.CSS_SELECTOR, 'h1')
    print(header.text)
    # bags = driver.find_element(By.LINK_TEXT, 'Bags')
    bags = driver.find_element(By.PARTIAL_LINK_TEXT, 'Bag')
    bags.click()
    sleep(2)


def test_two(driver):
    driver.get('https://www.qa-practice.com/elements/button/simple')
    # button = driver.find_element(By.ID, 'submit-id-submit')
    button = driver.find_element(By.NAME, 'submit')
    button.click()
    sleep(2)


def test_three(driver):
    driver.get('https://magento.softwaretestingboard.com/sale.html')
    button = driver.find_element(By.CLASS_NAME, 'button')
    button.click()
    sleep(2)


def test_four(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    # cart = driver.find_element(By.CSS_SELECTOR, '''a[data-bind="scope: 'minicart_content'"]''')
    cart = driver.find_element(By.XPATH, '''//a[@data-bind="scope: 'minicart_content'"]''')
    cart.click()
    sleep(2)
