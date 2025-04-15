# Импортируем библиотеки
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создаем класс
class Testing():
    def __init__(self):
        self.base_url = 'https://www.saucedemo.com/'
        self._get_options()
        self.driver = None
        self._init_driver()

    def _get_options(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument("--start-maximized")

    def _init_driver(self):
        self.driver = webdriver.Chrome(options=self.options, service=ChromeService(ChromeDriverManager().install()))

    def open_browser(self):
        self.driver.get(self.base_url)


begin_test = Testing()  # Создаем экземпляр класса
begin_test.open_browser() # Вызываем метод класса