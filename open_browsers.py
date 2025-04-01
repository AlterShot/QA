# Импорт отсчета времени
import time
# Импорт вебдрайвера
from selenium import webdriver
# Импорт хрома
from selenium.webdriver.chrome.service import Service as ChromeService
# Импорт эджа
from selenium.webdriver.edge.service import Service as EdgeService
# Импорт мозилы
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Работа с хромом
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

# Настраиваем время работы на 10 секунд
time.sleep(10)

# Автоматически закрываем браузер
driver.close()

# Работа с мозилой
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Ввод базового url для использования
base_url: str = "https://www.saucedemo.com/"  # Адрес сайта для тестирования

# Команда драйверу открыть ссылку
driver.get(base_url)

# Команда драйверу отрыть браузер в определенном разрешении
driver.set_window_size(1920, 1080)

# Настраиваем время работы на 10 секунд
time.sleep(10)

# Автоматически закрываем браузер
driver.close()

# Работа с эджем
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)  # Оставляем браузер открытым
driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))

# Ввод базового url для использования
base_url: str = "https://www.saucedemo.com/"  # Адрес сайта для тестирования

# Команда драйверу открыть ссылку
driver.get(base_url)

# Команда драйверу отрыть браузер в определенном разрешении
driver.set_window_size(1920, 1080)

# Настраиваем время работы на 10 секунд
time.sleep(10)

# Автоматически закрываем браузер
driver.close()
