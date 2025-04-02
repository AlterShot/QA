import time
import datetime
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

now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S") # Добавляем переменную с датой
screenshot_name = 'screen' + now_date + '.png' # Добавляем переменную с именем

time.sleep(3) #Ждем, пока страница прогрузится

# Делаем скриншот браузера и сохраняем в папку
driver.save_screenshot('C:\\Programming\\PycharmProjects\\QA\\screenshots\\' + screenshot_name)