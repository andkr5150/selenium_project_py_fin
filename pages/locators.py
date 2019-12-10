from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span a.btn-default")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    FIND_INPUT = (By.CSS_SELECTOR, "#id_q")
    FIND_BUTTON = (By.CSS_SELECTOR, "input[type = 'submit']")


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_ADDED_IN_CART = (By.XPATH, "//div[@class='alertinner '][contains(.,'Your basket total is now')]")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_ADDED_IN_CART = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    ADD_TO_CART_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > :nth-child(1)")
    ITEM_ADDED_MESSAGE = (By.XPATH, "(//div[@class='alertinner '])[1]")
    ITEM_PRICE_MESSAGE = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    ITEM_PRODUCT = (By.CSS_SELECTOR, "#id_sort_by")
    ITEM_PRODUCTS = (By.CSS_SELECTOR, ".product_pod")


class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.XPATH, "//p[contains(text(), 'пуста')]")
    ITEM_IN_BASKET = (By.CSS_SELECTOR, "[class='basket-items']")
    BASKET_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-default']")

