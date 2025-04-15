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
        self.__options = self.__get_options()
        self.driver = self.__init_driver()
        self.driver.set_window_size(1920, 1080)
        self.base_url = 'https://www.saucedemo.com/'

    def __get_options(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        return options

    def __init_driver(self):
        return webdriver.Chrome(options=self.__options, service=ChromeService(ChromeDriverManager().install()))

    def open_browser(self):
        self.driver.get(self.base_url)


begin_test = Testing()  # Создаем экземпляр класса
begin_test.open_browser() # Вызываем метод класса