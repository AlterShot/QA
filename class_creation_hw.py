# Импортируем библиотеки
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Импортируем классы
from class_creation_cart import SauceCart
from class_creation_item import SauceItem
from class_creation_login import SauceLogin


# Создаем класс
class SauceDemoTesting():
    def __init__(self):
        self.base_url = 'https://www.saucedemo.com/'
        self.driver = None
        self.product_name = None
        self.product_price_value = None
        self._get_options()
        self._init_driver()

    def _get_options(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--disable-notifications")
        self.options.add_argument("--disable-features=PasswordCheck")
        self.options.add_argument("--incognito")

    def _init_driver(self):
        self.driver = webdriver.Chrome(options=self.options, service=ChromeService(ChromeDriverManager().install()))

    def open_browser(self):
        self.driver.get(self.base_url)

    # Обращаемся к модулю авторизации
    def login_test(self):
        login = SauceLogin(self.driver)
        login.login_page_test(login_name="performance_glitch_user", login_password="secret_sauce")

    # Обращаемся к модулю покупки
    def item_test(self):
        item = SauceItem(self.driver)
        self.product_name, self.product_price_value = item.item_page_test()

    # Обращаемся к модулю корзины
    def cart_test(self):
        cart = SauceCart(self.driver)
        cart.cart_page_test(self.product_name, self.product_price_value)

# Создаем экземпляр класса
test = SauceDemoTesting()

# Вызываем методы класса
test.open_browser()
test.login_test()
test.item_test()
test.cart_test()

# Закрываем браузер
test.driver.close()