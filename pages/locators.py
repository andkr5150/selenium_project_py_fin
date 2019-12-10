from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_ADDED_IN_CART = (By.XPATH, "//div[@class='alertinner '][contains(.,'Your basket total is now')]")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_ADDED_IN_CART = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    ADD_TO_CART_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > :nth-child(1)")

