import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(1920, 1080)
base_url: str = "https://demoqa.com/buttons"
driver.get(base_url)


action = ActionChains(driver)

# Делаем двойной клик
double = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double).perform()
print("double done")
time.sleep(5)
# Ищем соответствующий текст на странице
d_mes = driver.find_element(By.ID, "doubleClickMessage")
double_message = d_mes.text
# Проверяем корректность сообщения
assert double_message == "You have done a double click", "double gone wrong"
print("double correct")

# Делаем правый клик
right = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(right).perform()
print("right done")
time.sleep(5)
# Ищем соответствующий текст на странице
r_mes = driver.find_element(By.XPATH, "//p[@id='rightClickMessage']")
right_message = r_mes.text
# Проверяем корректность сообщения
assert right_message == "You have done a right click", "right gone wrong"
print("right correct")