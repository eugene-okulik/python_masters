from pages.base_page import BasePage
from data.locators import Locators


class EcoFriendlyPage(BasePage):
    page_url = Locators.eco_friendly_url
    title = 'Eco Friendly'
