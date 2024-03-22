import json
import re

from playwright.sync_api import Page, BrowserContext, expect, Dialog, Request, Response, Route
from time import sleep


def test_new_tab(page: Page, context: BrowserContext):
    sleep(3)
    page.goto('https://www.qa-practice.com/elements/new_tab/link')
    sleep(1)
    with context.expect_page() as new_page_event:
        page.locator('#new-page-link').click()
        page2 = new_page_event.value

    result = page2.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    sleep(2)
    page.locator('#new-page-link').click()
    sleep(3)


def fill_and_accept(alert: Dialog, message=None):
    alert.accept('some text')


def fill_indirect(text):

    def fill_accept(alert: Dialog):
        alert.accept(text)

    return fill_accept


def test_alert(page: Page):
    sleep(3)

    def cancel_alert(alert: Dialog):
        print(alert.type)
        print(alert.message)
        alert.dismiss()

    page.on('dialog', fill_indirect('indirect text'))
    # page.on('dialog', lambda alert: alert.accept('some text'))
    page.goto('https://www.qa-practice.com/elements/alert/prompt')
    page.get_by_role('link', name='Click').click()
    sleep(3)


def test_listen(page: Page):

    def print_request(request: Request):
        print('REQUEST:', request.post_data, request.url)

    page.on('request', print_request)
    page.on('response', lambda response: print('RESPONSE:', response.url, response.status))
    page.goto('https://www.qa-practice.com/')


def test_catch_response(page: Page):
    sleep(3)
    page.goto('https://www.airbnb.ru/')
    with page.expect_response(re.compile('/autosuggestions')) as response_event:
        page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()
        response = response_event.value

    print(response.json())
    assert response.json()['show_nearby'] is False


def test_pogoda(page: Page):
    sleep(3)

    def change_response(route: Route):
        response = route.fetch()
        body = response.json()
        body['icon'] = 'A2'
        body['temperature'] = '+28'
        print(body)
        body = json.dumps(body)
        route.fulfill(response=response, body=body)

    page.route('**/pogoda/**', change_response)
    page.goto('https://www.onliner.by/')
    page.locator('[name="query"]').click()
    sleep(5)


def test_resp(page: Page):
    sleep(3)

    def change_resp(route: Route):
        response = route.fetch()
        data = response.body().decode('utf-8')
        data = data.replace('Galaxy Z Fold5', 'AAAAAAAAAAAAAAAAAAAAAAAAAA')
        data = data.encode('ascii')
        route.fulfill(response=response, body=data)

    page.route(re.compile('/product/finder'), change_resp)
    page.goto('https://www.samsung.com/au/smartphones/galaxy-z')
    sleep(1)
    page.locator('[for="checkbox-series09z01"]').click()
    sleep(3)
