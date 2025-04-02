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

user_name = driver.find_element(By.XPATH, "//*[@id='user-name']") # Заменили id на xpath

user_name.send_keys("performance_glitch_user")

password = driver.find_element(By.XPATH, "//*[@id='password']") # Заменили id на xpath

password.send_keys("secret_sauce")

time.sleep(10)

driver.close()