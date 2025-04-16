from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceItem():
    def __init__(self, driver):
        self.driver = driver
        self.backpack_name = None
        self.backpack_price_value = None

    def item_page_test(self):
        # Добавляем переменную названия сумки в магазине
        backpack = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='item_4_title_link']")))
        self.backpack_name = backpack.text
        print(self.backpack_name)

        # Добавляем переменную цены сумки в магазине
        backpack_price = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")))
        self.backpack_price_value = float(backpack_price.text.replace("$", ""))
        print(self.backpack_price_value)

        # Добавляем сумку в корзину
        backpack_add_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        backpack_add_button.click()
        print("bag added")

        return self.backpack_name, self.backpack_price_value