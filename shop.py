from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

email = 'gosha2000@mail.ru'
password = 'ITMBZHr7m2wk3UDXDbK0'

path_to_extension = r'C:\Users\gener\AppData\Local\Google\Chrome\User Data\Profile 1\Extensions\bgnkhhnnamicmpeenaelnjfhikgbkllg\4.1.55_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(options=chrome_options)
driver.create_options()
time.sleep(10)
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(first_browser_tab)
driver.maximize_window()

''' Shop: отображение страницы товара'''
# Откройте https://practice.automationtesting.in/
driver.get('https://practice.automationtesting.in/')

# Залогиньтесь
driver.find_element(By.CSS_SELECTOR, 'a[href*="my-account"]').click()
driver.find_element(By.CSS_SELECTOR, '#username').send_keys(email)
driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
driver.find_element(By.CSS_SELECTOR, 'input[name="login"]').click()

# Нажмите на вкладку "Shop"
driver.find_element(By.CSS_SELECTOR, '#menu-item-40').click()

# Откройте книгу "HTML 5 Forms"
driver.find_element(By.CSS_SELECTOR, '.products.masonry-done a[href*="html5-forms"]:nth-child(2)').click()

# Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'h1[itemprop="name"]'), 'HTML5 Forms'))

''' Shop: количество товаров в категории'''
# Откройте https://practice.automationtesting.in/
driver.get('https://practice.automationtesting.in/')

# Залогиньтесь
driver.find_element(By.CSS_SELECTOR, 'a[href*="my-account"]').click()
driver.find_element(By.CSS_SELECTOR, '#username').send_keys(email)
driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
driver.find_element(By.CSS_SELECTOR, 'input[name="login"]').click()

# Нажмите на вкладку "Shop"
driver.find_element(By.CSS_SELECTOR, '#menu-item-40').click()

# Откройте категорию "HTML"
driver.find_element(By.CSS_SELECTOR, '.product-categories .cat-item-19 a').click()

# Добавьте тест, что отображается три товара
three_el = driver.find_elements(By.CSS_SELECTOR, 'ul li.product')
assert len(three_el) == 3

''' Shop: сортировка товаров'''
# Откройте https://practice.automationtesting.in/
driver.get('https://practice.automationtesting.in/')

# Залогиньтесь
driver.find_element(By.CSS_SELECTOR, 'a[href*="my-account"]').click()
driver.find_element(By.CSS_SELECTOR, '#username').send_keys(email)
driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
driver.find_element(By.CSS_SELECTOR, 'input[name="login"]').click()

# Нажмите на вкладку "Shop"
driver.find_element(By.CSS_SELECTOR, '#menu-item-40').click()

# Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# • Используйте проверку по value
default_sorting_selected = driver.find_element(By.CSS_SELECTOR, 'option[value="menu_order"]').get_attribute('selected')
assert default_sorting_selected is not None

# Отсортируйте товары по цене от большей к меньшей
# • в селекторах используйте класс Select
select = Select(driver.find_element(By.CSS_SELECTOR, '.orderby'))
select.select_by_value('price-desc')

# Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
# order_selector = driver.find_element(By.CSS_SELECTOR, '.orderby')

# Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# • Используйте проверку по value
price_desc_sorting_selected = driver.find_element(By.CSS_SELECTOR, 'option[value="price-desc"]').get_attribute(
    'selected')
assert price_desc_sorting_selected is not None
'''

'''
Shop: отображение, скидка
товара
# Откройте https://practice.automationtesting.in/
driver.get('https://practice.automationtesting.in/')

# Залогиньтесь
driver.find_element(By.CSS_SELECTOR, 'a[href*="my-account"]').click()
driver.find_element(By.CSS_SELECTOR, '#username').send_keys(email)
driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
driver.find_element(By.CSS_SELECTOR, 'input[name="login"]').click()

# Нажмите на вкладку "Shop"
driver.find_element(By.CSS_SELECTOR, '#menu-item-40').click()

# Откройте книгу "Android Quick Start Guide"
driver.find_element(By.CSS_SELECTOR, '.products.masonry-done a[href*="android-quick-start-guide"]:nth-child(2)').click()

# Добавьте тест, что содержимое старой цены = "₹600.00"
old_price_text = driver.find_element(By.CSS_SELECTOR, 'del .woocommerce-Price-amount').text
assert old_price_text == '₹600.00'

# Добавьте тест, что содержимое новой цены = "₹450.00"
new_price_text = driver.find_element(By.CSS_SELECTOR, 'ins .woocommerce-Price-amount').text
assert new_price_text == '₹450.00'

# Добавьте явное ожидание и нажмите на обложку книги
# • Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
driver.find_element(By.CSS_SELECTOR, '.zoom img').click()

# Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
close_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.pp_close')))
close_button.click()

''' Shop: проверка цены в корзине'''
# Откройте https://practice.automationtesting.in/ # в этом тесте логиниться не нужно
driver.get('https://practice.automationtesting.in/')

# Нажмите на вкладку "Shop"
driver.find_element(By.CSS_SELECTOR, '#menu-item-40').click()

# Добавьте в корзину книгу "HTML5 WebApp Development"
# если эта книга будет out of stock - тогда вместо неё добавьте книгу HTML5 Forms и выполните тесты по аналогии
# если все книги будут out of stock - тогда пропустите это и следующие два задания
# Добавил книгу Mastering JavaScript, это единственная доступная и я не хочу пропускать задания
driver.find_element(By.CSS_SELECTOR, '.product_tag-javascript.product_tag-mastering a:nth-child(2)').click()
time.sleep(2)

# Добавьте тест, что возле корзины(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# Для книги Mastering JavaScript = "₹350.00"
# • Используйте для проверки assert
amount_in_cart = driver.find_element(By.CSS_SELECTOR, '.cartcontents').text
assert amount_in_cart == '1 Item'
price_in_cart = driver.find_element(By.CSS_SELECTOR, '.cartcontents + .amount').text
assert price_in_cart == '₹350.00'

# Перейдите в корзину
driver.find_element(By.CSS_SELECTOR, '.wpmenucart-contents').click()

# Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'td[data-title="Subtotal"] > span')))

# Используя явное ожидание, проверьте что в Total отобразилась стоимость
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'td[data-title="Total"] > span')))

''' Shop: работа в корзине'''
# Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента, этот сценарий один из таких, используйте time.sleep()
# Откройте https://practice.automationtesting.in/ # в этом тесте логиниться не нужно
driver.get('https://practice.automationtesting.in/')

# Нажмите на вкладку "Shop"
driver.find_element(By.CSS_SELECTOR, '#menu-item-40').click()

# Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# Добавил книгу Mastering JavaScript, это единственная доступная и я не хочу пропускать задания
# • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# • После добавления 1-й книги добавьте sleep
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element(By.CSS_SELECTOR, '.product_tag-javascript.product_tag-mastering a:nth-child(2)').click()
time.sleep(2)

# Перейдите в корзину
driver.find_element(By.CSS_SELECTOR, '.wpmenucart-contents').click()

# Удалите первую книгу
# • Перед удалением добавьте sleep
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '.remove').click()

# Нажмите на Undo (отмена удаления)
undo = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href*="undo"]')))
undo.click()

# В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# Сделал для Mastering JavaScript
# • Предварительно очистите поле с помощью локатор_поля.clear()
quantity = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[title="Qty"]')))
quantity.clear()
quantity.send_keys(3)

# Нажмите на кнопку "UPDATE BASKET"
driver.find_element(By.CSS_SELECTOR, 'input[name="update_cart"]').click()

# Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
# Сделал для Mastering JavaScript
assert quantity.get_attribute('value') == '3'

# Нажмите на кнопку "APPLY COUPON"
# • Перед нажатимем добавьте sleep
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, 'input[name="apply_coupon"]').click()

# Добавьте тест, что возникло сообщение: "Please enter a coupon code."
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-error li'), 'Please enter a coupon code'))

''' Shop: покупка товара'''
# Откройте https://practice.automationtesting.in/ # в этом тесте логиниться не нужно
driver.get('https://practice.automationtesting.in/')

# Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
driver.find_element(By.CSS_SELECTOR, '#menu-item-40').click()
driver.execute_script("window.scrollBy(0, 300);")

# Добавьте в корзину книгу "HTML5 WebApp Development"
# Добавил книгу Mastering JavaScript, это единственная доступная и я не хочу пропускать задания
driver.find_element(By.CSS_SELECTOR, '.product_tag-javascript.product_tag-mastering a:nth-child(2)').click()

# Перейдите в корзину
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '.wpmenucart-contents').click()

# Нажмите "PROCEED TO CHECKOUT"
# • Перед нажатием, добавьте явное ожидание
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.checkout-button'))).click()

# Заполните все обязательные поля
# • Перед заполнением first name, добавьте явное ожидание
# • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#billing_first_name'))).send_keys('Gosha')
driver.find_element(By.CSS_SELECTOR, '#billing_last_name').send_keys('Kucenko')
driver.find_element(By.CSS_SELECTOR, '#billing_email').send_keys('gosha.kucenko@gmail.com')
driver.find_element(By.CSS_SELECTOR, '#billing_phone').send_keys('+1 (326) 837-8031')
driver.find_element(By.CSS_SELECTOR, '#select2-chosen-1').click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#s2id_autogen1_search'))).send_keys('Kaz')
driver.find_element(By.CSS_SELECTOR, '#select2-results-1 li:first-child').click()
driver.find_element(By.CSS_SELECTOR, '#billing_address_1').send_keys('Bahchelievlerevaya 5')
driver.find_element(By.CSS_SELECTOR, '#billing_city').send_keys('Astana')
driver.find_element(By.CSS_SELECTOR, '#billing_state').send_keys('Aqmola')
driver.find_element(By.CSS_SELECTOR, '#billing_postcode').send_keys('15577')

# Выберите способ оплаты "Check Payments"
# • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#payment_method_cheque').click()

# Нажмите PLACE ORDER
driver.find_element(By.CSS_SELECTOR, '#place_order').click()

# Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-thankyou-order-received'),
                                            'Thank you. Your order has been received.'))

# Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.method strong'), 'Check Payments'))
