import allure
import pytest


@pytest.mark.regression
@allure.feature('One')
def test_yoga_button(whats_new_page):
    whats_new_page.open()
    whats_new_page.click_yoga_button()
    whats_new_page.check_url_is_correct('https://magento.softwaretestingboard.com/collections/yoga-new.html')
    whats_new_page.check_header_is_correct('New Luma Yoga Collection')
