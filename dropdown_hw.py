import time

from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(1920, 1080)
base_url: str = "https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo"
driver.get(base_url)

select = Select(driver.find_element(By.XPATH, "//select[@id='country']"))
select.select_by_value("India")

time.sleep(1)

state = driver.find_element(By.XPATH, "//input[@class='select2-search__field']")
state.click()
state.send_keys("Arizona")
state.send_keys(Keys.RETURN)

time.sleep(1)

state.click()
new_state = driver.find_element(By.XPATH, "(//li[@class='select2-results__option'])[8]")
new_state.click()