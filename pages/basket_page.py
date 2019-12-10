from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Empty message is not present"

    def should_not_be_item(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), "Item is presented, but should not be"
