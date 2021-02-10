from pages.product_page import ProductPage
from pages.locators import ProductLocators
from selenium import webdriver
import time, pytest

def test_message_disappeared_after_adding_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    book_name, product_amount = page.add_to_cart()
    page.should_hidden_success_message_after_timeout()