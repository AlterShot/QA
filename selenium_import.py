# Импорт вебдрайвера
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Создание переменных
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Оставляем браузер открытым
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# Ввод базового url для использования
base_url: str = "https://www.saucedemo.com/"  # Адрес сайта для тестирования

# Команда драйверу открыть ссылку
driver.get(base_url)

# Команда драйверу отрыть браузер в определенном разрешении
driver.set_window_size(1920, 1080)
