# pip install pytest-playwright
# playwright install


from playwright.sync_api import Page, expect
import re
from time import sleep


def test_first_test(page: Page):
    sleep(3)
    page.goto('https://www.google.com/')
    search_field = page.get_by_role('combobox')
    search_field.fill('cat')
    search_field.press('Enter')
    # assert page.title().startswith('cat')
    expect(page).to_have_title(re.compile('^cat'))


def test_by_role(page: Page):
    sleep(3)
    page.goto('https://magento.softwaretestingboard.com/')
    whats_new = page.get_by_role('menuitem', name="What's New")
    sleep(1)
    whats_new.click()
    # search_terms = page.get_by_role('link', name='Search Terms')
    search_terms = page.get_by_text('Search Terms')
    sleep(1)
    search_terms.click()
    sleep(2)


def test_by_label(page: Page):
    sleep(3)
    page.goto('https://www.qa-practice.com/elements/input/simple')
    # input_field = page.get_by_label('Text string')
    input_field = page.get_by_placeholder('Submit me')
    input_field.fill('skjdfksjdhfkjh')
    sleep(3)


def test_by_alt_text(page: Page):
    sleep(3)
    page.goto('https://epam.com')
    pict = page.get_by_alt_text('The Next Evolution of Software Engineering')
    pict.click()
    sleep(3)


def test_by_title(page: Page):
    sleep(3)
    page.goto('https://google.com')
    page.get_by_title('Шукаць').fill('dog')
    sleep(3)


def test_by_test_id(page):
    sleep(3)
    page.goto('https://www.airbnb.com/')
    sleep(2)
    page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()
    sleep(3)


def test_locator(page: Page):
    sleep(3)
    page.goto('https://magento.softwaretestingboard.com/')
    # basket = page.locator('.action.showcart')
    basket = page.locator('//*[@class="action showcart"]')
    basket.click()
    sleep(3)
