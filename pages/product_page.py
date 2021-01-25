from .base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import ProductLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductLocators.CART_button)
        button.click()
        