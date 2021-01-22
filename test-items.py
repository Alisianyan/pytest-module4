from selenium import webdriver

##тестируем наличие кнопки на страницах на разных языках
def test_cart_button_diff_languages(language, browser): ##браузер и язык передаются как параметр
    ##формируем ссылку, подставляя язык в URL. Язык указывается как параметр при старте теста
    language=str(language)
    link=f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    
    ##находим элемент кнопки добавления в корзину
    button_add_to_cart=browser.find_element_by_css_selector(".btn-add-to-basket")
    ##отображается ли кнопка на странице, is_enabled - встроенный метод Selenium
    is_button_add_to_cart_enabled=button_add_to_cart.is_enabled()
    
    ##падаем с ассертом, если кнопки нет. Ассерт ЕСТЬ!
    assert is_button_add_to_cart_enabled, "add-to-cart-button not present on the page"