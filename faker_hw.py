from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(1920, 1080)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)

faker = Faker("en_US")
input_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
random_name = faker.first_name()
input_name.send_keys(random_name)
print("name entered")