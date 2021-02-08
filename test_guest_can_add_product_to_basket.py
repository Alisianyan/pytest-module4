from pages.product_page import ProductPage
from pages.locators import ProductLocators
from selenium import webdriver
import time, pytest

array_link = [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" for i in range(10)]
@pytest.mark.parametrize('link', array_link)
def test_can_add_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    book_name, product_amount = page.add_to_cart()
    page.solve_quiz_and_get_code()
    cart_page = ProductPage(browser, browser.current_url)
    cart_page.look_for_asserts(book_name, product_amount)
    time.sleep(10)