from selenium.webdriver.common.by import By


class Locators:
    # URLs
    base_url = 'https://magento.softwaretestingboard.com/'
    create_account_url = 'customer/account/create/'
    eco_friendly_url = 'collections/eco-friendly.html'
    sale_url = 'sale.html'

    # LOCATORS
    # BASE PAGE LOCATORS
    linkWhatsNew = (By.ID, "ui-id-3")
    linkSales = (By.ID, 'ui-id-8')
    linkCreateAccount = (By.LINK_TEXT, "Account")
    header_h1 = (By.TAG_NAME, "h1")

    # CREATE ACCOUNT PAGE LOCATORS
    field_first_name = (By.ID, "firstname")
    field_last_name = (By.ID, "lastname")
    field_email = (By.ID, "email_address")
    field_password = (By.ID, "password")
    field_password_confirm = (By.ID, "password-confirmation")
    button_submit = (By.CSS_SELECTOR, "button[title=\'Create an Account\']")

    # ECO FRIENDLY PAGE LOCATORS
    goods_titles = (By.CSS_SELECTOR, "a.product-item-link")
    page_limiter = (By.ID, "limiter")
    next_page = (By.CSS_SELECTOR, "a.action.next")
    next_page_locator = "a.action.next"
    page1_item1 = "Ana Running Short"
    page1_item2 = "Tiffany Fitness Tee"
    page1_item3 = "Atlas Fitness Tank"
    page2_item1 = "Chaz Kangeroo Hoodie"

    # SALES PAGE LOCATORS
    dealsWomen = (By.CSS_SELECTOR, 'span.more.button')
    dealsMen = (By.XPATH, "//strong[contains(@class, 'title') and contains(text(), 'Men’s Bargains')]")
    dealsLuma = (By.XPATH, "//strong[contains(@class, 'title') and contains(text(), 'Luma Gear Steals')]")
    discont20Percent = (By.XPATH, "//strong[contains(@class, 'title') and contains(text(), '20% OFF')]")
    discont50Uds = (By.XPATH, "//strong[contains(@class, 'title') and contains(text(), 'Spend $50 or more')]")
    dealsTees = (By.XPATH, "//strong[contains(@class, 'title') and contains(text(), 'You can\'t have too many tees')]")
