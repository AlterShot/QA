import time
from selenium.webdriver.common.keys import Keys
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

time.sleep(2)

# Выделяем все поле логина и удаляем
user_name.send_keys(Keys.CONTROL + 'a')
user_name.send_keys(Keys.BACKSPACE)
print("Поле логина очищено")

time.sleep(2)

password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys("secret")
print("Пароль введен")

time.sleep(2)

#Выделяем все поле пароля и удаляем
password.send_keys(Keys.CONTROL + 'a')
password.send_keys(Keys.BACKSPACE)
print("Поле пароля очищено")

time.sleep(2)

# Нажимаем на кнопку авторизации
password.send_keys(Keys.ENTER)