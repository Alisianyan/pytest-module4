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
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    CART_button = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_AMOUNT = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]")
    CART_added_product = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/strong")
    CART_sum = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")