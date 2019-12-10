from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.browser.current_url, "url - login is NOT correct"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login FORM is NOT correct"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register FORM is NOT correct"

    def register_new_user(self, email, password, confirm_password):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        reg_email.send_keys(email)

        reg_pass = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        reg_pass.send_keys(password)

        reg_conf_pass = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD)
        reg_conf_pass.send_keys(confirm_password)

        reg_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        reg_button.click()

    def should_display_success_message(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESS_MESSAGE), "Registration success message is not displayed"
