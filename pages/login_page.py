from .base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = str(self.browser.current_url)
        if 'login' in current_url:
            assert True, "login page exist"

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_field)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWD_field)
        assert True

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.SIGN_UP_email_field)
        self.browser.find_element(*LoginPageLocators.SIGN_UP_PASSWD_field)
        self.browser.find_element(*LoginPageLocators.SIGN_UP_PASSWD_field)       

        