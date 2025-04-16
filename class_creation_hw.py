# Импортируем библиотеки
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создаем класс
class SauceDemoTesting():
    def __init__(self):
        self.base_url = 'https://www.saucedemo.com/'
        self.driver = None
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

    # Создаем метод авторизации
    def login(self):
        # Выводим начало теста
        print("test start")

        # Вводим имя пользователя
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='user-name']")))
        user_name.send_keys("performance_glitch_user")
        print("login entered")

        # Вводим пароль
        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']")))
        password.send_keys("secret_sauce")
        print("password entered")

        # Нажимаем на кнопку авторизации
        login_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
        print("login button clicked")

        # Проверяем правильность url
        get_url = self.driver.current_url
        print(get_url)
        shop_url = "https://www.saucedemo.com/inventory.html"
        assert shop_url == get_url, "Ошибка: url не совпадает"
        print("URL корректен")

        # Проверяем правильность заголовка на странице
        text_products = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[@class = 'title']")))
        print(text_products.text)
        text_products_value = text_products.text
        assert text_products_value == "Products", "Ошибка: неверный заголовок"
        print("Заголовок верен")

    # Создаем метод добавления товара в корзину
    def buy_backpack(self):
        # Добавляем переменную названия сумки в магазине
        backpack = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='item_4_title_link']")))
        self.backpack_name = backpack.text
        print(self.backpack_name)

        # Добавляем переменную цены сумки в магазине
        backpack_price = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")))
        self.backpack_price_value = float(backpack_price.text.replace("$", ""))
        print(self.backpack_price_value)

        # Добавляем сумку в корзину
        backpack_add_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        backpack_add_button.click()
        print("bag added")

    # Создаем метод перехода в корзину и проверки корректности перехода
    def go_to_cart(self):
        # Переходим в корзину
        cart_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-test='shopping-cart-link']")))
        cart_button.click()
        print("cart button clicked")

        # Создаем переменную названия сумки в корзине и сравниваем
        cart_backpack = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='item_4_title_link']")))
        cart_backpack_name = cart_backpack.text
        print(cart_backpack_name)
        assert cart_backpack_name == self.backpack_name, "wrong bag name"
        print("right bag added")

        # Создаем переменную цены сумки в корзине и сравниваем
        cart_backpack_price = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='inventory_item_price']")))
        cart_backpack_price_value = float(cart_backpack_price.text.replace("$", ""))
        print(cart_backpack_price_value)
        assert cart_backpack_price_value == self.backpack_price_value, "bag price wrong"
        print("bag price ok")

        # Проверяем правильность заголовка на странице корзины
        cart_success_check = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[@class='title']")))
        cart_success_text = cart_success_check.text
        assert cart_success_text == "Your Cart", "wrong page"
        print("cart page ok")

        # Обозначаем завершение теста
        print("test finished")

# Создаем экземпляр класса
test = SauceDemoTesting()

# Вызываем методы класса
test.open_browser()
test.login()
test.buy_backpack()
test.go_to_cart()

# Закрываем браузер
test.driver.close()