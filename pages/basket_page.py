from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        self.is_basket_has_no_product()
        self.is_basket_has_empty_message()


    def is_basket_has_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Empty message is not present"

    def is_basket_has_no_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BACKET_ITEMS), "Items in basket are present"