import glob
import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# Создаем новый путь для скачивания
download_path = 'C:\\Programming\\PycharmProjects\\QA\\download_files\\'
prefs = {'download.default_directory' : download_path}

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.set_window_size(1920, 1080)
base_url = 'https://www.lambdatest.com/selenium-playground/download-file-demo'
driver.get(base_url)

# Ищем и нажимаем кнопку скачивания файла
download_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Download File')]")
download_button.click()

# Даем файлу скачаться и проверяем, есть ли он в папке
time.sleep(5)
file_name = "LambdaTest.pdf"
file_path = download_path + file_name
assert os.access(file_path, os.F_OK) == True, "no file found"
print("file found")

# Проверяем, не пустой ли файл
files = glob.glob(os.path.join(download_path, '*.*'))
for file in files:
    size = os.path.getsize(file)
    if size > 10:
        print("file fine")
    else:
        print("file empty")

# Удаляем скачанный файл
files = glob.glob(os.path.join(download_path, '*.*'))
for file in files:
    os.remove(file)