# Напишите тест, который заходит на страницу
# https://www.apple.com/shop/buy-iphone,
# кликает по iPhone 15 Pro & iPhone 15 Pro Max,
# открывшемся попапе проверяет заголовок.
#
# Но не всё так просто. ))) Перед открытием страницы включите отлавливание запроса
# https://www.apple.com/shop/api/digital-mat?path=library/step0_iphone/digitalmat
# и измените ответ так так, чтобы iPhone 15 Pro в попапе назывался "яблокофон 15 про"
#
# Попробуйте самостоятельно поискать где что нужно подменить в ответе на этот запрос.
# Вам в помощь всякие онлайн отображатели json, чтобы было проще разобраться в структуре ответа.
# Я обычно пользуюсь https://jsoneditoronline.org/
#
# Если совсем не получится разобраться, пишите мне в личку,
# одскажу какой кусок нужно изменить.
#
# Ну и при проверке заголовка в попапе проверяйте,
# что заголовок = тому, на что вы заменили название телефона.

from playwright.sync_api import Page, Route, BrowserContext, expect
import pytest
import json


@pytest.fixture(scope='session')
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 3000,
    }


@pytest.fixture(scope='session')
def context(browser):
    context = browser.new_context(viewport={'width': 1920, 'height': 1080}, screen={'width': 1920, 'height': 1080})
    yield context
    context.close()


apple_url = "https://www.apple.com/shop/buy-iphone"
catch_url = 'https://www.apple.com/shop/api/digital-mat?path=library/step0_iphone/digitalmat'


def test_replace_text(page: Page):
    def on_route(route: Route):
        response = route.fetch()
        body = response.json()
        # print(json.dumps(body, indent=4))
        item_name = body['body']['digitalMat'][0]['familyTypes'][0]
        item_name["productName"] = "Jablokofon 15 P"
        body = json.dumps(body)
        # print(json.dumps(body, indent=4))

        route.fulfill(
            response=response,
            body=body
        )

    page.route(catch_url, on_route)
    page.goto(apple_url)
    link = page.locator("div.rf-hcard-content.tile.as-util-relatedlink").first
    link.click()

    title = page.locator("h2.rf-digitalmat-overlay-header.typography-manifesto").first

    expect(title).to_have_text("Jablokofon 15 P")
