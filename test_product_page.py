from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import MainPageLocators, LoginPageLocators
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = ProductPage(browser, link)
    page.open()
    book_name, product_amount = page.add_to_cart()
    page.solve_quiz_and_get_code()
    cart_page = ProductPage(browser, browser.current_url)
    cart_page.look_for_asserts(book_name, product_amount)
    time.sleep(10)
