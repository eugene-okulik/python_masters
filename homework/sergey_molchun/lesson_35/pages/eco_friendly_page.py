from pages.base_page import BasePage
from data.locators import Data


class EcoFriendlyPage(BasePage):
    page_url = Data.eco_friendly_url
    title = 'Eco Friendly'
