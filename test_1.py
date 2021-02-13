import pytest
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import MainPageLocators, LoginPageLocators, BasketLocators

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) #инициализируем Page object, передаём в конструктор экземпляр драйвера и юрл
    page.open()
    page.go_to_basket()
    objProductPage = ProductPage(page.browser, page.url)
    objProductPage.should_not_be_success_message()
    objBasketPage = BasketPage(page.browser, page.url)
    objBasketPage.basket_empty_msg()
    objBasketPage.should_be_empty()