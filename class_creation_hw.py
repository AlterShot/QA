# Импортируем библиотеки
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


# Создаем класс
class Testing():
    def __init__(self):
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        self.driver.set_window_size(1920, 1080)
        self.base_url = 'https://www.saucedemo.com/'

    def open_browser(self):
        self.driver.get(self.base_url)


begin_test = Testing() # Создаем экземпляр класса
begin_test.open_browser() # Вызываем метод класса