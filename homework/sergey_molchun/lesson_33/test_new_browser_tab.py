# Задание 2
# Напишите тест, который зайдет на страницу
# https://www.qa-practice.com/elements/new_tab/button,
# нажмет на кнопку Click, в открывшемся табе проверит,
# что в результате написано "I am a new page in a new tab"
# и проверит, что на изначальной вкладке кнопка Click - активна (enabled)

from playwright.sync_api import Page, expect, BrowserContext
import allure


@allure.testcase('https://www.qa-practice.com/elements/new_tab/button', 'Test new browser tab.')
def test_new_browser_tab(page: Page, context: BrowserContext, timeout=5000):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')

    with context.expect_page() as page_event:
        page.locator('#new-page-button').click()
        new_page = page_event.value

    result_text = new_page.locator('#result-text')
    expect(result_text).to_have_text('I am a new page in a new tab')

    expect(page.locator('#new-page-button')).to_be_enabled()
