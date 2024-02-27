from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pytest


@pytest.fixture()
def driver():
    my_driver = webdriver.Chrome()
    my_driver.implicitly_wait(10)
    sleep(3)  # Нужен для перетаскивания браузера в видимый экран (на занятии)
    my_driver.maximize_window()
    return my_driver


def test_one(driver):
    driver.get('https://magento.softwaretestingboard.com/sale.html')
    header = driver.find_element(By.TAG_NAME, 'h1')
    print(header.text)
    print(header.get_attribute('innerText'))
    print(header.get_attribute('class'))
    print(header.value_of_css_property('font-size'))
    print(header.tag_name)
    assert header.value_of_css_property('font-size') == '40px'


def test_clear(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    input_field = driver.find_element(By.ID, 'id_text_string')
    input_field.send_keys('wiewuyeuwiwi')
    sleep(1)
    # input_field.clear()
    # field_len = len(input_field.get_attribute('value'))
    # for _ in range(field_len):
    #     input_field.send_keys(Keys.BACKSPACE)
    input_field.send_keys(Keys.CONTROL + 'a')
    sleep(1)
    input_field.send_keys(Keys.BACKSPACE)
    sleep(2)


def test_select_and_enabled(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    select = driver.find_element(By.ID, 'id_select_state')
    button = driver.find_element(By.ID, 'submit-id-submit')
    sleep(1)
    # button.click()
    assert not button.is_enabled()
    dropdown = Select(select)
    dropdown.select_by_value('enabled')
    sleep(1)
    # dropdown.select_by_visible_text('Enabled')
    assert button.is_enabled()


def test_visible(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    req_header = driver.find_element(By.ID, 'req_header')
    req_body = driver.find_element(By.ID, 'req_text')
    sleep(1)
    assert not req_body.is_displayed()
    req_header.click()
    sleep(1)
    assert req_body.is_displayed()


def test_implicit(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    men = driver.find_element(By.ID, 'ui-id-5')
    men.click()


def test_implicit2(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    after = driver.find_element(By.ID, 'visibleAfter')
    after.click()


def test_explicit(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    disabled = driver.find_element(By.ID, 'enableAfter')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(disabled))
    assert disabled.is_enabled()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'enableAfter')))


def test_explicit2(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    after = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'visibleAfter')))
    # after = driver.find_element(By.ID, 'visibleAfter')
    after.click()


def test_av_dropdown(driver):
    driver.get('https://av.by/')
    driver.find_element(By.XPATH, '//*[@class="button button--primary button--block button--large"]').click()
    driver.find_element(By.ID, 'p-10-price_currency').click()
    sleep(5)
    options = driver.find_elements(By.CSS_SELECTOR, '#p-10-price_currency > div > div > ul > li')
    # print(options.text)
    print(len(options))
    for option in options:
        print(option.find_element(By.TAG_NAME, 'button').text)
