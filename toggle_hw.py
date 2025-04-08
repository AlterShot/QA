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
base_url: str = "https://html5css.ru/howto/howto_js_rangeslider.php"
driver.get(base_url)

action = ActionChains(driver)

# Добавляем значение value в переменную
start_value = driver.find_element(By.XPATH, "//span[@id='f']")
initial_value = int(start_value.text)
print(initial_value)

# Находим ползунок и задаем перемещение
toggle = driver.find_element(By.XPATH, "//input[@class='slider-square']")
left_right = 500

# Двигаем ползунок
action.click_and_hold(toggle).move_by_offset(left_right, 0).release().perform()

# Вычисляем, насколько изменилось значение value и соотношение value/пиксель
new_value = int(start_value.text)
print(new_value)
value_change = new_value - initial_value
movement = value_change / left_right

# Добавляем переменную ожидаемого результата и проверяем на соответствие
result = initial_value + (left_right * movement)
print(result)
assert new_value == result, "smth gone wrong"
print("correct")