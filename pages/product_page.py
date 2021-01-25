from .base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import ProductLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math

class ProductPage(BasePage):
    def add_to_cart(self):
        book_name = self.browser.find_element(*ProductLocators.BOOK_NAME).text
        product_amount = self.browser.find_element(*ProductLocators.PRODUCT_AMOUNT).text
        button = self.browser.find_element(*ProductLocators.CART_button)
        button.click()
        return book_name, product_amount
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
            
    def look_for_asserts(self, book_name, product_amount):
        print("sdfdsg")
        cart_added_product = self.browser.find_element(*ProductLocators.CART_added_product).text
        cart_sum = self.browser.find_element(*ProductLocators.CART_sum).text
        assert book_name == cart_added_product, "не тот продукт!"
        assert product_amount == cart_sum, "не совпадает стоимость"
        