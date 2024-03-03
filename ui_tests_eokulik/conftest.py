import pytest
from selenium import webdriver
from ui_tests_eokulik.pages.whats_new_page import WhatsNew
from time import sleep


@pytest.fixture()
def driver():
    chrome = webdriver.Chrome()
    chrome.implicitly_wait(5)
    sleep(3)  # Чтобы перетягивать окошко
    chrome.maximize_window()
    return chrome


@pytest.fixture()
def whats_new_page(driver):
    return WhatsNew(driver)
