import pytest
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import MainPageLocators, LoginPageLocators, BasketLocators

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) #инициализируем Page object, передаём в конструктор экземпляр драйвера и юрл
    page.open()
    page.should_be_login_link() ##см mainPage
    #page.should_be_login_url() ##см mainPage
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
@pytest.mark.new    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) #инициализируем Page object, передаём в конструктор экземпляр драйвера и юрл
    page.open()
    page.go_to_basket()
    objBasketPage=BasketPage(page.browser, page.url)
    objBasketPage.basket_empty_msg()
    objBasketPage.should_be_empty()