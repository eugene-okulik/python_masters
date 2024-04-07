import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ui_tests_eokulik.pages.whats_new_page import WhatsNew
from time import sleep


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome = webdriver.Chrome(options=options)
    chrome.implicitly_wait(5)
    sleep(3)  # Чтобы перетягивать окошко
    chrome.maximize_window()
    return chrome


@pytest.fixture()
def whats_new_page(driver):
    return WhatsNew(driver)
