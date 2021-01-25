from pages.product_page import ProductPage
from pages.locators import ProductLocators
from selenium import webdriver

def test_can_add_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()