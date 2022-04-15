from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url, 'login is not in url'

    def should_be_login_form(self):
        email = self.is_element_present(*LoginPageLocators.EMAIL)
        password = self.is_element_present(*LoginPageLocators.PASSWORD)
        sign_in_button = self.is_element_present(*LoginPageLocators.SIGN_IN)
        self.should_element_exist(email)
        self.should_element_exist(password)
        self.should_element_exist(sign_in_button)

    def should_be_register_form(self):
        email = self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL)
        password = self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_repeat = self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT)
        registration_button = self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON)
        self.should_element_exist(email)
        self.should_element_exist(password)
        self.should_element_exist(password_repeat)
        self.should_element_exist(registration_button)

    def should_element_exist(self, element):
        assert element, f'element not exist, {element}'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

