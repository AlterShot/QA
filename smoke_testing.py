import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url: str = "https://www.saucedemo.com/"
driver.get(base_url)
driver.set_window_size(1920, 1080)

user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys("performance_glitch_user")
print("Логин введен")

password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys("secret_sauce")
print("Пароль введен")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
print("Кнопка нажата")

get_url = driver.current_url
print(get_url)
shop_url = "https://www.saucedemo.com/inventory.html"
assert shop_url == get_url, "Ошибка: url не совпадает"
print("URL корректен")

text_products = driver.find_element(By.XPATH, "//span[@class = 'title']")
print(text_products.text)
text_products_value = text_products.text
assert text_products_value == "Products", "Ошибка: неверный заголовок"
print("Заголовок верен")

# Добавляем переменную названия сумки в магазине
backpack = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
backpack_name = backpack.text
print(backpack_name)

# Добавляем переменную цены сумки в магазине
backpack_price = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
backpack_price_value = float(backpack_price.text.replace("$", ""))
print(backpack_price_value)

# Добавляем переменную названия фонаря в магазине
light = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']")
light_name = light.text
print(light_name)

# Добавляем переменную цены фонаря в магазине
light_price = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div")
light_price_value = float(light_price.text.replace("$", ""))
print(light_price_value)

# Добавляем сумку в корзину
backpack_add_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
backpack_add_button.click()
print("Сумка в корзине")

# Добавляем фонарь в корзину
light_add_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
light_add_button.click()
print("Фонарь в корзине")

# Переходим в корзину
cart_button = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
cart_button.click()
print("Переход в корзину")

# Создаем переменную названия сумки в корзине и сравниваем
cart_backpack = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
cart_backpack_name = cart_backpack.text
print(cart_backpack_name)
assert cart_backpack_name == backpack_name, "Ошибка, названия сумки не совпадают"
print("Добавлена правильная сумка")

# Создаем переменную цены сумки в корзине и сравниваем
cart_backpack_price = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
cart_backpack_price_value = float(cart_backpack_price.text.replace("$", ""))
print(cart_backpack_price_value)
assert cart_backpack_price_value == backpack_price_value, "Ошибка, цена сумки не совпадает"
print("Цена сумки указана верно")

# Создаем переменную названия фонаря в корзине и сравниваем
cart_light = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']")
cart_light_name = cart_light.text
print(cart_light_name)
assert cart_light_name == light_name, "Ошибка, названия фонаря не совпадают"
print("Добавлен правильный фонарь")

# Создаем переменную цены фонаря в корзине и сравниваем
cart_light_price = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
cart_light_price_value = float(cart_light_price.text.replace("$", ""))
print(cart_light_price_value)
assert cart_light_price_value == light_price_value, "Ошибка, цена фонаря не совпадает"
print("Цена фонаря указана верно")

# Переходим на следующую страницу
checkout_button = driver.find_element(By.XPATH, "//*[@id='checkout']")
checkout_button.click()
print("Переход в подтверждение заказа")

# Вводим имя
first_name_field = driver.find_element(By.XPATH, "//*[@id='first-name']")
first_name_field.send_keys('FirstName')
print("Имя введено")

# Вводим фамилию
last_name_field = driver.find_element(By.XPATH, "//*[@id='last-name']")
last_name_field.send_keys('LastName')
print("Фамилия введена")

# Вводим почтовый индекс
zip_field = driver.find_element(By.XPATH, "//*[@id='postal-code']")
zip_field.send_keys(12345)
print("Почтовый индекс введен")

# Переходим дальше
continue_button = driver.find_element(By.XPATH, "//*[@id='continue']")
continue_button.click()
print("Переход на следующий этап")

# Создаем переменную названия сумки в итоге и сравниваем
checkout_backpack = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']")
checkout_backpack_name = checkout_backpack.text
print(checkout_backpack_name)
assert checkout_backpack_name == backpack_name, "Ошибка, сумка не та"
print("Правильная сумка в итоге")

# Создаем переменную цены сумки в корзине и сравниваем
checkout_backpack_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
checkout_backpack_price_value = float(checkout_backpack_price.text.replace("$", ""))
print(checkout_backpack_price_value)
assert checkout_backpack_price_value == backpack_price_value, "Ошибка, цена сумки не та"
print("Правильная цена сумки в итоге")

# Создаем переменную названия фонаря в корзине и сравниваем
checkout_light = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div")
checkout_light_name = checkout_light.text
print(checkout_light_name)
assert checkout_light_name == light_name, "Ошибка, фонарь не тот"
print("Правильный фонарь в итоге")

# Создаем переменную цены фонаря в корзине и сравниваем
checkout_light_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
checkout_light_price_value = float(checkout_light_price.text.replace("$", ""))
print(checkout_light_price_value)
assert checkout_light_price_value == light_price_value, "Ошибка, цена фонаря не та"
print("Правильная цена фонаря в итоге")

# Создаем переменную общей цены в итоге и сравниваем
site_price_total = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
site_price_total_value = site_price_total.text
site_price_total_value = site_price_total_value.replace("Item total: ", "").strip()
print(site_price_total_value)
purchased_items_total = checkout_backpack_price_value + checkout_light_price_value
print(purchased_items_total)
assert purchased_items_total == purchased_items_total, "Ошибка, итоговая цена не совпадает"
print("Итоговая цена гуд")

# Завершаем покупку, нажав кнопку "завершить"
finish_button = driver.find_element(By.XPATH, "//*[@id='finish']")
finish_button.click()
print("Покупка завершена")

# Проверяем корректность отображения последней страницы
final_page = driver.find_element(By.XPATH, "//*[contains(text(), 'Thank you for your order!')]")
final_page_text = final_page.text
print(final_page_text)
assert final_page_text == 'Thank you for your order!', "Ошибка, текст не совпадает"
print("Успех")

# Нажимаем на кнопку возвращения в главное меню
back_button = driver.find_element(By.XPATH, "//*[@id='back-to-products']")
back_button.click()
print("Кнопка возвращения назад нажата")

# Открываем скрытое меню
hidden_menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
hidden_menu_button.click()
print("Скрытое меню открыто")

time.sleep(1) # Даем меню прогрузиться

# Нажимаем на кнопку выхода в скрытом меню
logout_button = driver.find_element(By.ID, 'logout_sidebar_link')
logout_button.click()
print("Выход из аккаунта")

# Проверяем корректность выхода
get_url = driver.current_url
print(get_url)
login_page_url = "https://www.saucedemo.com/"
assert login_page_url == get_url, "Ошибка: URL не совпадает"
print("URL корректен, выход совершен")
