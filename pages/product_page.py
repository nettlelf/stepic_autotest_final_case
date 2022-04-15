from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        price = self.return_value(*ProductPageLocators.PRICE)
        price = price.text
        name = self.return_value(*ProductPageLocators.NAME_OF_PRODUCT)
        name = name.text
        self.click_on_element(*ProductPageLocators.BUTTON_ADD_TO_BUSKET)
        self.solve_quiz_and_get_code()
        alert_price = self.return_value(*ProductPageLocators.ALERT_PRICE_IN_BUSKET)
        alert_price = alert_price.text
        alert_name = self.return_value(*ProductPageLocators.ALERT_NAME_OF_PRODUCT)
        alert_name = alert_name.text
        self.should_price_alert_price_be_equal(price, alert_price)
        self.should_name_alert_name_be_equal(name, alert_name)

    def should_price_alert_price_be_equal(self, price, alert_price):
        assert price == alert_price, f'price != alertprice, {price}, {alert_price}'

    def should_name_alert_name_be_equal(self, name, alert_name):
        assert name == alert_name, f'price != alertprice, {name}, {alert_name}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),  "Success message is presented, but should not be"

    def should_dissapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"



