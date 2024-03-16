from playwright.async_api import async_playwright, Page, Locator, expect
import pytest


# pip install pytest-asynci


# Задание 1
# get_by_role
# Напишите тест, который заходит на страницу
# https://the-internet.herokuapp.com/,
# кликает по ссылке Form Authentication,
# заполняет логин и пароль, кликает кнопку Login
#
# Все элементы должны быть найдены с помощью локатора get_by_role
#
class Urls:
    initial_webpage = "https://the-internet.herokuapp.com/"


@pytest.mark.asyncio
async def test_login_page():  # Просто через (page: Page) у меня не работает почему-то !?!?!?
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, timeout=2000, slow_mo=500)
        context = await browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = await context.new_page()

        await page.goto(Urls.initial_webpage)
        await page.get_by_role('link', name='Form Authentication').click()
        await page.get_by_role('textbox', name="Username").fill("tomsmith")
        await page.get_by_role('textbox', name="Password").fill("SuperSecretPassword!")
        await page.get_by_role('button', name='Login').click()

        secret_area = await page.get_by_role('heading', name="Secure Area").first.text_content()
        assert secret_area == ' Secure Area', 'Wrong Header after login'
        expect(page).to_have_url('https://the-internet.herokuapp.com/secure')


# Задание 2
# Напишите программу, которая зайдет на страницу
# https://demoqa.com/automation-practice-form и полностью
# заполнит форму (кроме загрузки файла) и нажмет Submit.
#
# Какие локаторы использовать - выбирайте сами.

class Urls2:
    form_webpage = 'https://demoqa.com/automation-practice-form'


class Locators2:
    first_name_field = '#firstName'
    last_name_field = '#lastName'
    email_field = '#userEmail'
    gender_m = '.custom-control.custom-radio.custom-control-inline'  # '#gender-radio-1'
    phone_field = '#userNumber'

    dob_field = '#dateOfBirthInput'
    month_selector = '.react-datepicker__month-select'
    year_selector = '.react-datepicker__year-select'
    date_selector = '.react-datepicker__day.react-datepicker__day--015'

    subject_field = '#subjectsInput'
    hobbies_sports = 'label[for="hobbies-checkbox-1"]'
    address_field = '#currentAddress'
    state_field = '#react-select-3-input'
    city_field = '#react-select-4-input'
    button_submit = '#submit'

    confirmation_page = '.modal-title.h4'


@pytest.mark.asyncio
async def test_fill_the_form():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, timeout=2000, slow_mo=500)
        context = await browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = await context.new_page()

        await page.goto(Urls2.form_webpage)

        await page.fill(Locators2.first_name_field, "Sergey")
        await page.fill(Locators2.last_name_field, "Moser")
        await page.fill(Locators2.email_field, "moser@gmail.com")
        await page.locator(Locators2.gender_m).first.click()
        await page.fill(Locators2.phone_field, "0611492416")

        await page.click(Locators2.dob_field)
        await page.locator(Locators2.month_selector).select_option("October")
        await page.locator(Locators2.year_selector).select_option("1999")
        await page.locator(Locators2.date_selector).click()

        subject_field = page.locator(Locators2.subject_field)
        await subject_field.fill("Homework Lesson 32")

        await page.locator(Locators2.hobbies_sports).check()
        await page.fill(Locators2.address_field, "Serbia, Belgrade")

        state_field = page.locator(Locators2.state_field)
        await state_field.fill("NCR")
        await state_field.press("Enter")

        city_filed = page.locator(Locators2.city_field)
        await city_filed.fill("Noida")
        await city_filed.press("Enter")

        await page.click(Locators2.button_submit)

        confirmation = await page.locator(Locators2.confirmation_page).text_content()
        assert confirmation == 'Thanks for submitting the form'
