from playwright.sync_api import BrowserContext, Playwright
import pytest
from ui_tests_eokulik_pw.pages.whats_new_page import WhatsNew


@pytest.fixture()
def page(context: BrowserContext, playwright: Playwright):
    # playwright.selectors.set_test_id_attribute('id')
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    yield page


# @pytest.fixture()
# def page(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
#     context = browser.new_context(no_viewport=True)
#     context = browser.new_context(viewport={'width': 300, 'height': 300})
#     page = context.new_page()
#     yield page


# @pytest.fixture
# def page(context: BrowserContext):
#     page = context.new_page()
#     yield page


@pytest.fixture()
def whats_new_page(page):
    return WhatsNew(page)
