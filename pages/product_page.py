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

