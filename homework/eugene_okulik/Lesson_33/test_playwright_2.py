from playwright.sync_api import Page, expect, Playwright
from time import sleep


def test_input(page: Page):
    sleep(3)
    page.goto('https://magento.softwaretestingboard.com/customer/account/create/')
    input_field = page.locator('#password')
    # input_field.fill('sldkfjsldkjflskdfj')
    input_field.press_sequentially('qwertyusdf', delay=100)
    sleep(1)
    input_field.press('Control+a')
    sleep(1)
    input_field.press('Backspace')
    sleep(3)


def test_visible(page: Page):
    sleep(3)
    page.goto('https://www.qa-practice.com/elements/input/simple')
    reqs = page.locator('#req_text')
    expect(reqs).not_to_be_visible()
    page.locator('#req_header').click()
    expect(reqs).to_be_visible()
    page.locator('#req_header').click()
    expect(reqs).not_to_be_visible()
    sleep(3)


def test_enabled_and_select(page: Page):
    sleep(3)
    page.goto('https://www.qa-practice.com/elements/button/disabled')
    button = page.locator('#submit-id-submit')
    expect(button).to_be_disabled()
    page.locator('#id_select_state').select_option('enabled')
    expect(button).to_be_enabled()
    expect(button).to_have_text('Submit')
    expect(button).to_contain_text('ubm')
    sleep(3)


def test_value(page: Page):
    text = 'qwert'
    sleep(3)
    page.goto('https://www.qa-practice.com/elements/input/simple')
    input_field = page.locator('#id_text_string')
    input_field.fill(text)
    expect(input_field, f'input value is not {text}').to_have_value('skjdhksdjh')
    sleep(3)


def test_sort_and_waits(page: Page):
    sleep(3)
    page.goto('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
    greet = page.locator('.greet').first
    expect(greet).not_to_be_empty()
    first_man = page.locator('.product-item-link').first
    print(first_man.inner_text())
    page.locator('#sorter').first.select_option('Price')
    print(first_man.inner_text())
    sleep(1)


def test_focused(page):
    page.goto('https://www.google.com')
    field = page.locator('[name="q"]')
    sleep(3)
    expect(field).to_be_focused()


def test_hover(page: Page):
    sleep(3)
    page.goto('https://magento.softwaretestingboard.com/')
    men = page.locator('#ui-id-5')
    tops = page.locator('#ui-id-17')
    jackets = page.locator('#ui-id-19')
    men.hover()
    tops.hover()
    jackets.click()
    sleep(3)


def test_d_n_d(page: Page):
    sleep(3)
    page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
    drag_me = page.locator('#rect-draggable')
    drop_here = page.locator('#rect-droppable')
    drag_me.drag_to(drop_here)
