# Задание 1
# Напишите тест, который заходит на страницу
# https://www.qa-practice.com/elements/alert/confirm,
# кликает на кнопку, чтобы появился алерт, жмет Ok
# и проверяет, что на страние в секции "You selected" написано "Ok"

from playwright.sync_api import Page, expect, Dialog
import allure


@allure.testcase('https://www.qa-practice.com/elements/alert/confirm', 'Test Alert accept.')
def test_allert(page: Page, timeout=5000):
    def alert_accept(alert: Dialog):
        alert.accept()

    page.on('dialog', alert_accept)
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.locator('.a-button').click()

    expect(page.locator('#result-text')).to_have_text('Ok')
