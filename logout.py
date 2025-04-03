import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url: str = "https://www.saucedemo.com/"
driver.get(base_url)
driver.set_window_size(1920, 1080)

user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys("performance_glitch_user")
print("Логин введен")

password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys("secret_sauce")
print("Пароль введен")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("Кнопка нажата")

# Открываем скрытое меню
hidden_menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
hidden_menu_button.click()
print("Скрытое меню открыто")

time.sleep(1) # Даем меню прогрузиться

# Нажимаем на кнопку выхода в скрытом меню
logout_button = driver.find_element(By.ID, 'logout_sidebar_link')
logout_button.click()
print("Выход из аккаунта")

# Проверяем корректность выхода
get_url = driver.current_url
print(get_url)
login_page_url = "https://www.saucedemo.com/"
assert login_page_url == get_url, "Ошибка: URL не совпадает"
print("URL корректен")
