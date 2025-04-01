# Импорт вебдрайвера
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
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

# Создание переменной для поля имени пользователя
user_name = driver.find_element(By.ID, "user-name")

# Ввод информации в поле имени пользователя
user_name.send_keys("performance_glitch_user")

# Создание переменной для поля пароля
password = driver.find_element(By.ID, "password")

# Ввод информации в поле пароля
password.send_keys("secret_sauce")