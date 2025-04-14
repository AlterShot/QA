from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


faker = Faker("en_US")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.set_window_size(1920, 1080)
driver.get(base_url)

user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys("performance_glitch_user")
print("Логин введен")

password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys("secret_sauce")
print("Пароль введен")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("Кнопка нажата")

text_products = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[@class = 'title']")))
print(text_products.text)
text_products_value = text_products.text
assert text_products_value == "Products", "Ошибка: неверный заголовок"
print("Заголовок верен")

# Создаем список товаров
products_full_list = [
    {"name_xpath": "//*[@id='item_4_title_link']",
     "price_xpath": "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div",
     "add_button_xpath": "//button[@id='add-to-cart-sauce-labs-backpack']",
     "text_name": "Sauce Labs Backpack"},
    {"name_xpath": "//*[@id='item_0_title_link']",
     "price_xpath": "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div",
     "add_button_xpath": "//button[@id='add-to-cart-sauce-labs-bike-light']",
     "text_name": "Sauce Labs Bike Light"},
    {"name_xpath": "//*[@id='item_1_title_link']",
     "price_xpath": "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div",
     "add_button_xpath": "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']",
     "text_name": "Sauce Labs Bolt T-Shirt"},
    {"name_xpath": "//*[@id='item_5_title_link']",
     "price_xpath": "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div",
     "add_button_xpath": "//button[@id='add-to-cart-sauce-labs-fleece-jacket']",
     "text_name": "Sauce Labs Fleece Jacket"},
    {"name_xpath": "//*[@id='item_2_title_link']",
     "price_xpath": "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div",
     "add_button_xpath": "//button[@id='add-to-cart-sauce-labs-onesie']",
     "text_name": "Sauce Labs Onesie"},
    {"name_xpath": "//*[@id='item_3_title_link']",
     "price_xpath": "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div",
     "add_button_xpath": "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']",
     "text_name": "Test.allTheThings() T-Shirt (Red)"}
]

# Выводим приветственное сообщение
print("Приветствую тебя в нашем интернет - магазине")

print("Выбери один из следующих товаров и укажи его номер: 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light, "
        "3 - Sauce Labs Bolt T-Shirt, 4 - Sauce Labs Fleece Jacket, 5 - Sauce Labs Onesie, 6 - Test.allTheThings() T-Shirt (Red)")

# Создаем переменную, чтобы проверить выбранный товар
product = None
# Просим пользователя выбрать товар и выводим, что он выбрал
try:
    selected = int(input("Выбери товар (1-6): ")) - 1
    product = products_full_list[selected]
    print(f"you chose {product['text_name']}")
except ValueError:
    print("Ввод должен быть числовым")
except IndexError:
    print("Вы выбрали неверный товар")

# Начинаем выполнение программы, если товар выбран правильно
if product:
    # Создаем переменные для конкретного товара
    product_name = driver.find_element(By.XPATH, product["name_xpath"]).text
    product_price = driver.find_element(By.XPATH, product["price_xpath"])
    product_price_value = float(product_price.text.replace("$", ""))

    # Добавляем товар в корзину
    product_add_button = driver.find_element(By.XPATH, product["add_button_xpath"])
    product_add_button.click()

    # Переходим в корзину
    cart_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-test='shopping-cart-link']")))
    cart_button.click()
    print("moving to cart")

    # Сравниваем название в корзине с изначальным
    cart_product_name = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='inventory_item_name']"))).text
    assert cart_product_name == product_name, "cart name bad"
    print("cart name good")

    # Сравниваем цену в корзине с изначальной
    cart_price = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
    cart_price_value = float(cart_price.text.replace("$", ""))
    assert cart_price_value == product_price_value, "cart price bad"
    print("cart price good")

    # Переходим на следующую страницу
    checkout_button = driver.find_element(By.XPATH, "//*[@id='checkout']")
    checkout_button.click()
    print("moving to checkout")

    # Вводим случайное имя
    first_name_field = driver.find_element(By.XPATH, "//*[@id='first-name']")
    first_name_field.send_keys(faker.first_name())
    print("name entered")

    # Вводим случайную фамилию
    last_name_field = driver.find_element(By.XPATH, "//*[@id='last-name']")
    last_name_field.send_keys(faker.last_name())
    print("last name entered")

    # Вводим случайный почтовый индекс
    zip_field = driver.find_element(By.XPATH, "//*[@id='postal-code']")
    zip_field.send_keys(faker.zipcode())
    print("zipcode entered")

    # Переходим дальше
    continue_button = driver.find_element(By.XPATH, "//*[@id='continue']")
    continue_button.click()
    print("moving to final stage")

    # Сравниваем название в итоге с изначальным
    overview_product_name = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='inventory_item_name']"))).text
    assert overview_product_name == product_name, "final product name bad"
    print("final product name good")

    # Сравниваем цену в итоге с изначальной
    overview_product_price = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
    overview_product_price_value = float(overview_product_price.text.replace("$", ""))
    assert overview_product_price_value == product_price_value, "final product price bad"
    print("final product price good")

    # Завершаем этот процесс
    finish_button = driver.find_element(By.XPATH, "//*[@id='finish']")
    finish_button.click()
    print("shopping done")

    # Проверяем корректность отображения последней страницы
    final_page = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Thank you for your order!')]")))
    final_page_text = final_page.text
    print(final_page_text)
    assert final_page_text == 'Thank you for your order!', "Ошибка, текст не совпадает"
    print("success")

    # Нажимаем на кнопку возвращения в главное меню
    back_button = driver.find_element(By.XPATH, "//*[@id='back-to-products']")
    back_button.click()
    print("going back")

    # Открываем скрытое меню
    hidden_menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
    hidden_menu_button.click()
    print("hidden menu opened")

    # Нажимаем на кнопку выхода в скрытом меню
    logout_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'logout_sidebar_link')))
    logout_button.click()
    print("log out")

    # Проверяем корректность выхода
    get_url = driver.current_url
    print(get_url)
    login_page_url = "https://www.saucedemo.com/"
    assert login_page_url == get_url, "wrong url"
    print("logout complete")

    # Закрываем браузер
    driver.close()
else:
    print("Товар не выбран")
