from .base_page import BasePage
from .locators import BusketLocators

class BusketPage(BasePage):

    def should_be_busket_empty(self):
        assert self.is_element_present(*BusketLocators.BUSKET_IS_EMPTY), 'message busket is empty isnt exist'

    def should_be_no_products(self):
        assert self.is_not_element_present(*BusketLocators.PRODUCTS),'there is products in busket'