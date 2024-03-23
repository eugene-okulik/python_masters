# Задание 3
# Напишите тест, который зайдет на страницу
# https://demoqa.com/dynamic-properties,
# нажмет на кнопку Color change только после того как она станет красной.


from playwright.sync_api import Page, expect, BrowserContext
import allure


@allure.testcase('https://demoqa.com/dynamic-properties', 'Test press a button when it\'s RED.')
def test_click_tbe_button_when_its_red(page: Page, timeout=10000):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator('.mt-4.text-danger.btn.btn-primary')
    button.click()
