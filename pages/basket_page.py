from .base_page import BasePage
from .locators import BusketLocators

class BusketPage(BasePage):

    def should_be_busket_empty(self):
        message = self.browser.find_element(*BusketLocators.BUSKET_IS_EMPTY)
        message = message.text
        assert message == 'Ваша корзина пуста Продолжить покупки', f'{message}, There is no empty busket message'

    def should_be_no_products(self):
        assert self.is_not_element_present(*BusketLocators.PRODUCTS),'there is products in busket'