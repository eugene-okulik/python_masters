from selenium import webdriver
import pytest


@pytest.fixture
def driver():
    my_driver = webdriver.Chrome()
    my_driver.maximize_window()
    my_driver.implicitly_wait(10)
    return my_driver
