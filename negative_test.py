import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless") # Проводим тесты без открытия браузера

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url: str = "https://www.saucedemo.com/"
driver.get(base_url)
driver.set_window_size(1920, 1080)

user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys("performance_glitch_user")
print("Логин введен")

password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys("secret")
print("Пароль введен")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("Кнопка нажата")

# Негативный тест
warning_text = driver.find_element(By.XPATH, "//h3[@data-test = 'error']")
warning_text_value = warning_text.text
assert warning_text_value == "Epic sadface: Username and password do not match any user in this service"
print("Сообщение об ошибке отображается корректно")

# Закрытие сообщения об ошибке
error_button = driver.find_element(By.XPATH, "//button[@class = 'error-button']")
error_button.click()
print("Сообщение об ошибке закрыто")
