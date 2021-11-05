import time

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_busket(self):
        add_button = self.browser.find_element(*ProductPageLocators.BUSKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.ACCEPT_MESSAGE).text , "Bookname added is not the same"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE).text, "Price is not the same"



