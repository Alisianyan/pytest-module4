from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import MainPageLocators, LoginPageLocators

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) #инициализируем Page object, передаём в конструктор экземпляр драйвера и юрл
    page.open()
    page.should_be_login_link() ##см mainPage
    #page.should_be_login_url() ##см mainPage
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    