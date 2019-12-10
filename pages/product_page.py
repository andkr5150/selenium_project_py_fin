from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math


class ProductPage(BasePage):
    def press_add_to_cart_button(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        cart_button.click()

    def product_name_in_message_check(self, text):
        print(text)
        print(self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED_IN_CART).text)
        assert text == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED_IN_CART).text

    def product_price_in_message_check(self, price):
        print(price)
        print(self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ADDED_IN_CART).text)
        assert price in self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ADDED_IN_CART).text

    def put_item_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        basket_btn.click()

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_CART_SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_CART_SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_CART_SUCCESS_MESSAGE), "Success message is presented, but should be disappeared"

    def add_item_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        button.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_product_name_message(self):
        product_name_message = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_MESSAGE)
        return product_name_message.text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def get_product_price_message(self):
        product_price_message = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_MESSAGE)
        return product_price_message.text

    def should_be_product_added_message(self):
        assert self.get_product_name() in self.get_product_name_message()

    def should_be_product_price_message(self):
        assert self.get_product_price() in self.get_product_price_message()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

