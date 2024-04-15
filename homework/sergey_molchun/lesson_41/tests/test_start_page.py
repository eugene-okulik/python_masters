import os

print("Current working directory:", os.getcwd())

from playwright.sync_api import Page
from data import Data
from start_page import StartPage
import allure
import pytest


@pytest.mark.smoke
@pytest.mark.startpage
@allure.testcase(Data.base_url, 'Test start page')
def test_start_page(page: Page):
    page = StartPage(page)
    page.open()
    page.check_url(Data.base_url)
    page.check_title(page.title)
    page.check_header_h1('Home Page')
