from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(1920, 1080)
base_url = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'
driver.get(base_url)

# Добавляем и переключаемся на iFrame
iframe = driver.find_element(By.XPATH, "//iframe[@id='iFrame1']")
driver.switch_to.frame(iframe)

# Задаем текст для ввода
initial_input_text = "Big bad wolf"

# Находим поле и смотрим, что там изначально
text_field = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]")
start_text = text_field.text
print(start_text)

# Удаляем изначальный текст, вводим новый и проверяем, что получилось
text_field.send_keys(Keys.CONTROL + 'a')
text_field.send_keys(Keys.BACKSPACE)
text_field.send_keys(initial_input_text)
new_text = text_field.text
print(new_text)

# Снова выделяем текст
text_field.send_keys(Keys.CONTROL + 'a')

# Добавляем жирный шрифт
bold_button = driver.find_element(By.XPATH, "//button[@title='Bold']")
bold_button.click()
print("text is now bold")

# Добавляем курсив
italics_button = driver.find_element(By.XPATH, "//button[@title='Italic']")
italics_button.click()
print("text is also italic")

# Сравниваем получившийся текст с изначальным
processed_text = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/b/i")
final_text = processed_text.text
assert final_text == initial_input_text, "texts do not match"
print("success")