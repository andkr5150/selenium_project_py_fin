from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
from selenium.webdriver.support.ui import Select
from .locators import ProductPageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"

    def go_to_basket(self):
        basket = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket.click()

    def find_button(self):
        assert self.browser.find_element(*BasePageLocators.FIND_BUTTON), "Find button is not presented"

    def find_item(self):
        find_input = self.browser.find_element(*BasePageLocators.FIND_INPUT)
        find_input.send_keys("Hack")
        find = self.browser.find_element(*BasePageLocators.FIND_BUTTON)
        find.click()

    def view_product_page(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_PRODUCT), "It is not product page"

    def view_product_page_count(self):
        assert len(self.browser.find_elements(*ProductPageLocators.ITEM_PRODUCTS)) >= 3, "It is not product page"
