import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(1920, 1080)
base_url: str = "https://demoqa.com/radio-button"
driver.get(base_url)

yes_radio = driver.find_element(By.XPATH, "(//label[@class='custom-control-label'])[1]")
yes_radio.click()
assert not yes_radio.is_selected(), "yes not chosen"
print("yes chosen")

time.sleep(3)

impressive_radio = driver.find_element(By.XPATH, "(//label[@class='custom-control-label'])[2]")
impressive_radio.click()
text = driver.find_element(By.XPATH, "//span[@class='text-success']")
check = text.text
assert check == "Impressive", "Wrong text"
print("impressive chosen")
