from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(1920, 1080)
base_url = 'https://www.lambdatest.com/selenium-playground/simple-form-demo'
driver.get(base_url)

# Ищем поле ввода и вписываем информацию
user_input = driver.find_element(By.XPATH, "//input[@id='user-message']")
message = 'Big Bad Wolf'
user_input.send_keys(message)

# Нажимаем на кнопку подтверждения
message_button = driver.find_element(By.XPATH, "//button[@id='showInput']")
message_button.click()

# Сравниваем результат с изначальным текстом
answer_message = driver.find_element(By.XPATH, "//p[@id='message']")
answer_to_check = answer_message.text
assert answer_to_check == message, "wrong text"
print("message fine")

# Создаем переменные с числами и проверяем их сумму
num_one = 100
num_two = 256
initial_result = num_one + num_two

# Ищем поля ввода и вводим числа
user_input_sum_one = driver.find_element(By.XPATH, "//input[@id='sum1']")
user_input_sum_one.send_keys(num_one)
user_input_sum_two = driver.find_element(By.XPATH, "//input[@id='sum2']")
user_input_sum_two.send_keys(num_two)

# Нажимаем на кнопку подтверждения
sum_button = driver.find_element(By.XPATH, "//*[@id='gettotal']/button")
sum_button.click()

# Сравниваем полученный результат с изначальной суммой
sum_answer = driver.find_element(By.XPATH, "//p[@id='addmessage']")
check_sum_answer = sum_answer.text
assert check_sum_answer == str(initial_result), "wrong number"
print("sum fine")


