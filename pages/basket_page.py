from .base_page import BasePage
from .product_page import ProductPage
from selenium.webdriver.common.by import By
from pages.locators import BasketLocators
from selenium.common.exceptions import NoAlertPresentException

class BasketPage(BasePage):
    def basket_empty_msg(self):
        basket_msg = self.browser.find_element(*BasketLocators.BASKET_MESSAGE).text
        assert basket_msg == "Ваша корзина пуста Продолжить покупки", basket_msg
    
    def should_be_empty(self):
        assert self.is_element_not_present(*BasketLocators.PRODUCT_BASKET_SELECTOR), "Basket not empty, but should"
        