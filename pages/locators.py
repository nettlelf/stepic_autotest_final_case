from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#registration_link')

class LoginPageLocators():
    EMAIL = (By.ID, 'id_login-username')
    PASSWORD = (By.ID, 'id_login-password')
    I_FORGOT_PASSWORD_LINK = (By.LINK_TEXT, 'Я забыл пароль')
    SIGN_IN = (By.NAME, 'login_submit')

    REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD = (By.ID, 'id_registration-password1')
    REGISTRATION_PASSWORD_REPEAT = (By.ID, 'id_registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')

class ProductPageLocators():
    BUTTON_ADD_TO_BUSKET = (By.CLASS_NAME, 'btn-add-to-basket')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')

    ALERT_NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.alert-success:nth-child(1) strong')
    ALERT_PRICE_IN_BUSKET = (By.CSS_SELECTOR, '.alert-info strong')

