from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(1920, 1080)
base_url: str = "https://demoqa.com/checkbox"
driver.get(base_url)

home_box = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
home_box.click()
assert home_box.is_selected(), "wrong choice"
print("home chosen correctly")