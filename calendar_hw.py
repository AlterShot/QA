from datetime import datetime, timedelta
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(1920, 1080)
base_url: str = "https://demoqa.com/date-picker"
driver.get(base_url)

date_input = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
date_input.send_keys(Keys.CONTROL + 'a')
date_input.send_keys(Keys.BACKSPACE)

today = datetime.now()
future = (today + timedelta(days=10)).strftime("%m-%d-%Y")
date_input.send_keys(future)
print("date entered")
