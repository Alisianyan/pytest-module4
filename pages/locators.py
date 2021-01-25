from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_field = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWD_field = (By.CSS_SELECTOR, "#id_login-password")
    
    SIGN_UP_email_field = (By.CSS_SELECTOR, "#id_registration-email")
    SIGN_UP_PASSWD_field = (By.CSS_SELECTOR, "#id_registration-password1")
    SIGN_UP_repiet_passwd_field = (By.CSS_SELECTOR, "#id_registration-password2")
    
class ProductLocators():
    CART_button = (By.CSS_SELECTOR, ".btn-add-to-basket")