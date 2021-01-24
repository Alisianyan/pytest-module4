##наследуются все остальные классы. Тут вспомогательные методы для работы с браузером
class BasePage():
    def __init__(self, browser, url, timeout=10): ##конструктор
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def open(self): ##метод, открывающий страницу в браузере
        self.browser.get(self.url)
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
