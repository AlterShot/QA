# Импортируем библиотеки
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


# Создаем класс
class Testing():
    def open_browser(self):
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        driver.set_window_size(1920, 1080)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)


begin_test = Testing() # Создаем экземпляр класса
begin_test.open_browser() # Вызываем метод класса