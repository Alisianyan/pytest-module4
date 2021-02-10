from pages.product_page import ProductPage
from pages.locators import ProductLocators
from selenium import webdriver
import time, pytest

def test_guest_cant_see_success_message(browser):
    link=" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()