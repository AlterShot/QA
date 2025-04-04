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

password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys("secret_sauce")
print("Пароль введен")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("Кнопка нажата")

backpack_add_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
backpack_add_button.click()
print("Сумка в корзине")

cart_button = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
cart_button.click()
print("Переход в корзину")

# Даем странице прогрузиться и возвращаемся в каталог
time.sleep(1)
driver.back()
print("Возвращение в каталог")

# Даем странице прогрузиться и возвращаемся в корзину
time.sleep(1)
driver.forward()
print("Возвращение в корзину")