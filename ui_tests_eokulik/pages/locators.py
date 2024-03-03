from selenium.webdriver.common.by import By


class BaseLoc:
    page_header = (By.TAG_NAME, 'h1')


class SignIn(BaseLoc):
    email = (By.ID, 'email')
    password = (By.ID, 'pass')
    sign_in_button = (By.ID, 'send2')
    alert = (By.CSS_SELECTOR, '[role="alert"]')


class WhatsNew(BaseLoc):
    button = ''
