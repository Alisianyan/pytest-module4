import pytest
from pages.product_page import ProductPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import MainPageLocators, LoginPageLocators,BasketLocators
import time

@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    book_name, product_amount = page.add_to_cart()
    page.solve_quiz_and_get_code()
    cart_page = ProductPage(browser, browser.current_url)
    cart_page.look_for_asserts(book_name, product_amount)
    time.sleep(10)

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    objBasketPage = BasketPage(page.browser, page.url)
    objBasketPage.basket_empty_msg()
    objBasketPage.should_be_empty()