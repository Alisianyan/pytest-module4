from pages.product_page import ProductPage
from pages.locators import ProductLocators
from selenium import webdriver
import time, pytest

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    book_name, product_amount = page.add_to_cart()
    page.solve_quiz_and_get_code()
    should_not_be_success_message()