from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
import pytest


@pytest.fixture()
def driver():
    my_driver = webdriver.Chrome()
    my_driver.implicitly_wait(10)
    sleep(3)  # Нужен для перетаскивания браузера в видимый экран (на занятии)
    my_driver.maximize_window()
    return my_driver


def test_cookies(driver):
    driver.get('https://demoblaze.com/')
    driver.find_element(By.ID, 'signin2').click()
    sleep(1)
    driver.add_cookie(
        {
            'domain': 'demoblaze.com',
            'httpOnly': False,
            'name': 'test',
            'path': '/',
            'sameSite': 'Lax',
            'secure': False,
            'value': 'test_value'
        }
    )
    cookies = driver.get_cookies()
    # driver.get_cookie('user')
    print(cookies)


def test_same_elements(driver):
    driver.get('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
    # welcome = driver.find_element(By.XPATH, '(//*[@class="greet welcome"])[1]')
    WebDriverWait(
        driver,
        5
    ).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, '(//*[@class="greet welcome"])[1]'),
            'Click “Write for us” link in the footer to submit a guest post'
        )
    )
    products = driver.find_elements(By.CSS_SELECTOR, '.product-item-info')
    product: WebElement = random.choice(products)
    product_price = product.find_element(By.CSS_SELECTOR, 'span.price-wrapper')
    # products[-1].click()
    print(product_price.text)
    products = sorted(products, key=lambda x: x.find_element(By.CSS_SELECTOR, 'span.price-wrapper').text)
    for prod in products:
        print(prod.find_element(By.CSS_SELECTOR, '.product-item-link').text)
    sleep(3)


def test_tabs(driver):
    driver.get('https://www.qa-practice.com/elements/new_tab/link')
    driver.find_element(By.ID, 'new-page-link').click()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    assert driver.find_element(By.ID, 'result-text').text == 'I am a new page in a new tab'
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.LINK_TEXT, 'New tab button').click()


def test_stale(driver):
    driver.get('https://www.qa-practice.com/elements/checkbox/single_checkbox')
    checkbox = driver.find_element(By.ID, 'id_checkbox_0')
    print(checkbox.id)
    checkbox.click()
    driver.find_element(By.ID, 'submit-id-submit').click()
    # checkbox = driver.find_element(By.ID, 'id_checkbox_0')
    checkbox.click()


def test_iframe(driver):
    driver.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    driver.find_element(By.CSS_SELECTOR, '.navbar-toggler-icon').click()
    driver.switch_to.default_content()
    driver.find_element(By.LINK_TEXT, 'Iframe').click()


def test_hover(driver):
    driver.get('https://magento.softwaretestingboard.com/')
    men = driver.find_element(By.ID, 'ui-id-5')
    tops = driver.find_element(By.ID, 'ui-id-17')
    jackets = driver.find_element(By.ID, 'ui-id-19')
    # ActionChains(driver).move_to_element(men).move_to_element(tops).click(jackets).perform()
    actions = ActionChains(driver)
    actions.move_to_element(men)
    actions.move_to_element(tops)
    actions.click(jackets)
    actions.perform()
    sleep(3)


def test_d_n_d(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    first = driver.find_element(By.ID, 'rect-draggable')
    second = driver.find_element(By.ID, 'rect-droppable')
    # ActionChains(driver).drag_and_drop(first, second).perform()
    actions = ActionChains(driver)
    actions.click_and_hold(first)
    actions.move_to_element(second)
    actions.release()
    actions.perform()
    sleep(3)


def test_in_new_tab(driver):
    driver.get('https://www.qa-practice.com/')
    home = driver.find_element(By.LINK_TEXT, 'Homepage')
    ActionChains(driver).key_down(Keys.CONTROL).click(home).key_down(Keys.CONTROL).perform()
    sleep(3)


def test_alert(driver):
    driver.get('https://www.qa-practice.com/elements/alert/alert')
    driver.find_element(By.LINK_TEXT, 'Click').click()
    alert = Alert(driver)
    print(alert.text)
    alert.accept()
    sleep(3)


def test_file_upload(driver):
    driver.get('https://the-internet.herokuapp.com/upload')
    driver.find_element(By.ID, 'file-upload').send_keys('/home/eugene/Downloads/hearts.png')
    sleep(3)
