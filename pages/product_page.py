from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_to_basket(self):
        price = self.return_text_value(*ProductPageLocators.PRICE)
        name = self.return_text_value(*ProductPageLocators.NAME_OF_PRODUCT)
        self.click_on_element(*ProductPageLocators.BUTTON_ADD_TO_BUSKET)
        self.solve_quiz_and_get_code()
        alert_price = self.return_text_value(*ProductPageLocators.ALERT_PRICE_IN_BUSKET)
        alert_name = self.return_text_value(*ProductPageLocators.ALERT_NAME_OF_PRODUCT)
        assert price == alert_price and name ==alert_name, f'price != alertprice, {price}, {alert_price}'