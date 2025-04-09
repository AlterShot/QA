import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(1920, 1080)
base_url = 'https://demoqa.com/browser-windows'
driver.get(base_url)

# Нажимаем на кнопку новой вкладки и переключаемся на нее
new_tab = driver.find_element(By.XPATH, "//button[@id='tabButton']")
new_tab.click()
driver.switch_to.window(driver.window_handles[1])

# Проверяем содержимое новой вкладки и правильность перехода
page_one_sample = driver.find_element(By.XPATH, "//*[@id='sampleHeading']")
page_one_sample_text = page_one_sample.text
assert page_one_sample_text == "This is a sample page", "wrong text"
print("tab fine")

# Ждем, закрываем вторую вкладку и возвращаемся на первую вкладку
time.sleep(2)
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)

# Нажимаем на кнопку нового окна и переключаемся на него
new_window = driver.find_element(By.XPATH, "//button[@id='windowButton']")
new_window.click()
driver.switch_to.window(driver.window_handles[1])

# Проверяем содержимое нового окна и правильность перехода
page_two_sample = driver.find_element(By.XPATH, "//*[@id='sampleHeading']")
page_two_sample_text = page_two_sample.text
assert page_two_sample_text == "This is a sample page", "wrong text"
print("window fine")

# Ждем, закрываем второе окно и возвращаемся на первую вкладку
time.sleep(2)
driver.close()
driver.switch_to.window(driver.window_handles[0])
