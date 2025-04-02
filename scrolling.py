import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
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

# Добавляем товары в корзину
add_button_backpack = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
add_button_light = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
add_button_bolt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
add_button_jacket = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
add_button_onesie = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()
add_button_red = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()

# Переходим в корзину с добавленными товарами
cart_button = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()

time.sleep(2)

# Скроллим до последнего элемента в корзине
action = ActionChains(driver)
element = driver.find_element(By.ID, "item_3_title_link")
action.move_to_element(element).perform()