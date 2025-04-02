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
password.send_keys("secret_sauce")
print("Пароль введен")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("Кнопка нажата")

get_url = driver.current_url
print(get_url)
shop_url = "https://www.saucedemo.com/inventory.html"
assert shop_url == get_url
print("URL корректен")

text_products = driver.find_element(By.XPATH, "//span[@class = 'title']")
print(text_products.text)
text_products_value = text_products.text
assert text_products_value == "Products"
print("Заголовок верен")