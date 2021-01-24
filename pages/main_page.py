from .base_page import BasePage ##импортируем конструктор(browser, url) и метод open
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
import sys

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element_by_css_selector("#login_link")
        login_link.click()
        
    def should_be_login_link(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login link not presented"