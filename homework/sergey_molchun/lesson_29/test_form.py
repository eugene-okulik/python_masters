from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#
# Напишите тест, который заходит на страницу
# https://www.qa-practice.com/elements/select/single_select,
# выбирает какой-нибудь вариант из Choose language,
# кликает Submit и проверяет,
# что в окошке с результатом отображается тот вариант, который был выбран.

URL1 = 'https://www.qa-practice.com/elements/select/single_select'


def test_select(select_text):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome()  # options=chrome_options
    driver.get(URL1)
    driver.maximize_window()

    # time.sleep(2)
    select = driver.find_element(By.CSS_SELECTOR, 'select#id_choose_language[class="form-select"]')
    button_submit = driver.find_element(By.CSS_SELECTOR, 'input#submit-id-submit[name="submit"]')
    dropdown = Select(select)
    dropdown.select_by_visible_text(select_text)
    button_submit.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p#result-text.result-text')))
    result_form = driver.find_element(By.CSS_SELECTOR, 'p#result-text[class="result-text"]')
    assert result_form.text == select_text


# TODO Напишите тест, который зайдет на страницу https://the-internet.herokuapp.com/dynamic_loading/2,
#  нажмет Start, и проверит, что на странице появляется текст "Hello World!"

URL2 = 'https://the-internet.herokuapp.com/dynamic_loading/2'


def test_text(text):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome()  # options=chrome_options
    driver.get(URL2)
    driver.maximize_window()

    button_start = driver.find_element(By.CSS_SELECTOR, '#start > button:first-child')
    button_start.click()
    finish_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']//h4[text()='Hello World!']")))
    assert finish_element.text == text


test_select("Python")
test_text("Hello World!")
