from .base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url, 'login is not in url'

    def should_be_login_form(self):
        email = self.browser(*LoginPageLocators.EMAIL)
        password = self.browser(*LoginPageLocators.PASSWORD)
        sign_in_button = self.browser(*LoginPageLocators.SIGN_IN)
        assert email and password and sign_in_button, 'page is broken, this id no login form'

    def should_be_register_form(self):
        email = self.browser(*LoginPageLocators.REGISTRATION_EMAIL)
        password = self.browser(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_repeat = self.browser(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT)
        registration_button = self.browser(*LoginPageLocators.REGISTRATION_BUTTON)
        assert email and password and registration_button and password_repeat, 'page is broken, this id no login form'

