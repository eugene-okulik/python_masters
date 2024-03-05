from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time


# Первый тест
# https://www.demoblaze.com/index.html
# откройте товар в новой вкладке
# Перейдите на вкладку с товаром
# Добавьте товар в корзину
# Закройте вкладку с товаром
# На начальной вкладке откройте корзину
# Убедитесь, что в корзине тот товар, который вы добавляли

@pytest.fixture
def driver():
    my_driver = webdriver.Chrome()
    my_driver.implicitly_wait(5)
    my_driver.maximize_window()
    return my_driver


@pytest.mark.busket_check
def test_busket(driver):
    driver.get('https://www.demoblaze.com/index.html')
    driver.find_element(By.CSS_SELECTOR, 'a#itemc[onclick="byCat(\'notebook\')"]').click()
    macbookpro = driver.find_element(By.CSS_SELECTOR, 'a[href*="prod.html?idp_=15"].hrefch')
    ActionChains(driver).key_down(Keys.CONTROL).click(macbookpro).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    product_name = driver.find_element(By.TAG_NAME, 'h2').text
    product_price_text = driver.find_element(By.TAG_NAME, 'h3').text

    number = ''
    for char in product_price_text:
        if char.isdigit():
            number += char
    product_price = int(number)

    add_to_cart = driver.find_element(By.CSS_SELECTOR, "a[class='btn btn-success btn-lg']")
    add_to_cart.click()

    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())

    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    cart = driver.find_element(By.CSS_SELECTOR, "a#cartur")
    cart.click()
    product_row = driver.find_element(By.CSS_SELECTOR, '#tbodyid tr')
    product_name_cart = product_row.find_element(By.CSS_SELECTOR, 'td:nth-of-type(2)').text
    product_price_cart = int(product_row.find_element(By.CSS_SELECTOR, 'td:nth-of-type(3)').text)

    assert product_name == product_name_cart
    assert product_price == product_price_cart


# Второй тест
# https://magento.softwaretestingboard.com/gear/bags.html
# Навести мышку на первый товар ->
# кликнуть внизу карточки товара на кнопку Add to compare ->
# Проверить, что товар появился слева на этой же странице в секции Compare Products
@pytest.mark.busket_check
def test_compare(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    first_product = driver.find_element(By.XPATH, "(//*[@class='item product product-item'])[1]")

    ActionChains(driver).move_to_element(first_product).perform()
    first_product_name = driver.find_element(By.XPATH, '(//*[@class="product-item-link"])[1]').text

    add_to_compare_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//*[@class='action tocompare'])[1]")))
    (ActionChains(driver).move_to_element(first_product).move_to_element(add_to_compare_button).
     click(add_to_compare_button).perform())

    check_comparable_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@class='product-item-name']")))

    assert first_product_name == check_comparable_item.text
