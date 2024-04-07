from pages.start_page import StartPage
from data.data import Data


class SalePage(StartPage):
    page_url = Data.sale_url
    title = 'Sale'
