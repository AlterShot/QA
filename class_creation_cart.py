from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceCart():
    def __init__(self, driver):
        self.driver = driver

    def cart_page_test(self, expected_name, expected_price):
        # Переходим в корзину
        cart_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-test='shopping-cart-link']")))
        cart_button.click()
        print("cart button clicked")

        # Создаем переменную названия сумки в корзине и сравниваем
        cart_backpack = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='item_4_title_link']")))
        cart_backpack_name = cart_backpack.text
        print(cart_backpack_name)
        assert cart_backpack_name == expected_name, "wrong bag name"
        print("right bag added")

        # Создаем переменную цены сумки в корзине и сравниваем
        cart_backpack_price = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='inventory_item_price']")))
        cart_backpack_price_value = float(cart_backpack_price.text.replace("$", ""))
        print(cart_backpack_price_value)
        assert cart_backpack_price_value == expected_price, "bag price wrong"
        print("bag price ok")

        # Проверяем правильность заголовка на странице корзины
        cart_success_check = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='title']")))
        cart_success_text = cart_success_check.text
        assert cart_success_text == "Your Cart", "wrong page"
        print("cart page ok")