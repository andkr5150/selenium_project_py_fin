import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import BasePage
from .pages.main_page import MainPage
import random
import string

LOGIN_LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
LINK_PRODUCT_CODERS_AT_WORK = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
LINK_PRODUCT_THE_CITY_AND_THE_STARS = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    # link ="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    product_name = browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    product_price = browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    page.press_add_to_cart_button()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.product_name_in_message_check(product_name)
    page.product_price_in_message_check(product_price)


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    product_name = browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    product_price = browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    page.press_add_to_cart_button()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.product_name_in_message_check(product_name)
    page.product_price_in_message_check(product_price)


@pytest.mark.need_review
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.put_item_to_basket()
    page.test_guest_cant_see_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_cant_see_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.put_item_to_basket()
    page.test_message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_not_be_item()
    page.should_be_empty_message()


@pytest.mark.user_authorization
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        random_email = ''.join([random.choice(string.ascii_letters) for _ in range(10)]) + "@example.com"
        random_pass = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(16)])
        login_page = LoginPage(browser, LOGIN_LINK)
        login_page.open()
        login_page.register_new_user(random_email, random_pass, random_pass)
        login_page.should_display_success_message()
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_page = ProductPage(browser, LINK_PRODUCT_CODERS_AT_WORK + "?promo=newYear2019")
        product_page.open()
        product_page.add_item_to_basket()
        product_page.should_be_product_added_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, LINK_PRODUCT_CODERS_AT_WORK + "?promo=newYear2019")
        product_page.open()
        product_page.add_item_to_basket()
        product_page.should_be_product_added_message()
        product_page.should_be_product_price_message()

