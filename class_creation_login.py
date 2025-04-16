from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceLogin():
    def __init__(self, driver):
        self.driver = driver

    def login_page_test(self, login_name, login_password):
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='user-name']")))
        user_name.send_keys(login_name)
        print("login entered")

        # Вводим пароль
        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']")))
        password.send_keys(login_password)
        print("password entered")

        # Нажимаем на кнопку авторизации
        login_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
        print("login button clicked")

        # Проверяем правильность url
        get_url = self.driver.current_url
        print(get_url)
        shop_url = "https://www.saucedemo.com/inventory.html"
        assert shop_url == get_url, "Ошибка: url не совпадает"
        print("URL корректен")

        # Проверяем правильность заголовка на странице
        text_products = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class = 'title']")))
        print(text_products.text)
        text_products_value = text_products.text
        assert text_products_value == "Products", "Ошибка: неверный заголовок"
        print("Заголовок верен")