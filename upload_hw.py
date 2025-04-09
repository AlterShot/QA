from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(1920, 1080)
base_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'
driver.get(base_url)

file_to_upload = "C:\\Programming\\PycharmProjects\\QA\\screenshots\\screen2025.04.02-18.18.14.png"
file_name = "screen2025.04.02-18.18.14.png"

upload_button = driver.find_element(By.XPATH, "//input[@id='file']")
upload_button.send_keys(file_to_upload)

success = driver.find_element(By.XPATH, "//*[@id='error']")
success_text = success.text
assert success_text == "File Successfully Uploaded", "upload gone wrong"
print("upload fine")

uploaded_file_name = upload_button.get_attribute("value").split("\\")[-1]
assert uploaded_file_name == file_name, "name gone wrong"
print("name fine")
