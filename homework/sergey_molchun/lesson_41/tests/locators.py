class Locators:
    # LOCATORS
    # BASE PAGE LOCATORS
    linkWhatsNew = "page.locator('#ui-id-3')"
    linkSales = "page.locator('#ui-id-8')"
    linkCreateAccount = "page.get_by_role('link','Account')"
    header_h1 = "h1"

    # CREATE ACCOUNT PAGE LOCATORS
    # field_first_name = "self.page.locator('#firstname')"
    field_first_name = "#firstname"
    field_last_name = "#lastname"
    field_email = "#email_address"
    field_password = "#password"
    field_password_confirm = "#password-confirmation"
    button_submit = "button[title=\'Create an Account\']"

    # ECO FRIENDLY PAGE LOCATORS
    goods_titles = "a.product-item-link"
    page_limiter = "#limiter"
    next_page = "a.action.next"
    page1_item1 = "Ana Running Short"
    page1_item2 = "Tiffany Fitness Tee"
    page1_item3 = "Atlas Fitness Tank"
    page2_item1 = "Chaz Kangeroo Hoodie"
    page2_item2 = "Bruno Compete Hoodie"

    # SALES PAGE LOCATORS
    dealsWomen = 'span.more.button'
    dealsMen = "//strong[contains(@class, 'title') and contains(text(), 'Men’s Bargains')]"
    dealsLuma = "//strong[contains(@class, 'title') and contains(text(), 'Luma Gear Steals')]"
    discont20Percent = "//strong[contains(@class, 'title') and contains(text(), '20% OFF')]"
    discont50Uds = "//strong[contains(@class, 'title') and contains(text(), 'Spend $50 or more')]"
    dealsTees = "//strong[contains(@class, 'title') and contains(text(), 'You can\'t have too many tees')]"
