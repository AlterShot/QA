import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(1920, 1080)
base_url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(base_url)

# Ищем первую кнопку, нажимаем и принимаем alert
alert_button = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
alert_button.click()
driver.switch_to.alert.accept()
alert_field_area = driver.find_element(By.XPATH, "//*[@id='result']")
alert_field_text = alert_field_area.text
time.sleep(2)

# Проверяем правильность принятия alert
print(alert_field_text)
assert alert_field_text == "You successfully clicked an alert", "alert gone wrong"
print("alert fine")
time.sleep(2)

# Ищем вторую кнопку, нажимаем
confirm_button = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
confirm_button.click()
time.sleep(2)

# Принимаем alert и проверяем правильность
driver.switch_to.alert.accept()
confirm_field_area = driver.find_element(By.XPATH, "//*[@id='result']")
confirm_field_text = confirm_field_area.text
assert confirm_field_text == "You clicked: Ok", "confirm accept gone wrong"
print("confirm accept fine")
time.sleep(2)

# Снова нажимаем на кнопку, отклоняем и проверяем
confirm_button.click()
driver.switch_to.alert.dismiss()
confirm_field_text = confirm_field_area.text
assert confirm_field_text == "You clicked: Cancel", "confirm decline gone wrong"
print("confirm decline fine")
time.sleep(2)

# Ищем третью кнопку, создаем переменную с текстом и нажимаем на кнопку
prompt_button = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
text = "Big bad wolf"
prompt_button.click()

time.sleep(2)

# Вводим подготовленный текст в поле, принимаем и проверяем правильность
driver.switch_to.alert.send_keys(text)
driver.switch_to.alert.accept()
prompt_field_area = driver.find_element(By.XPATH, "//*[@id='result']")
prompt_field_text = prompt_field_area.text
assert prompt_field_text == "You entered: " + text, "prompt info gone wrong"
print("prompt info fine")
time.sleep(2)

# Снова нажимаем кнопку, отклоняем alert и проверяем правильность
prompt_button.click()
driver.switch_to.alert.dismiss()
prompt_field_text = prompt_field_area.text
assert prompt_field_text == "You entered: null", "prompt dismiss gone wrong"
print("prompt dismiss fine")