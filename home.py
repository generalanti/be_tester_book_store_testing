from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

path_to_extension = r'C:\Users\gener\AppData\Local\Google\Chrome\User Data\Profile 1\Extensions\bgnkhhnnamicmpeenaelnjfhikgbkllg\4.1.55_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(options=chrome_options)
driver.create_options()
time.sleep(10)
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(first_browser_tab)
driver.maximize_window()

''' Home: добавление комментария'''
# Откройте https://practice.automationtesting.in/
driver.get('https://practice.automationtesting.in/')

# Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)

# Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
driver.find_element(By.CSS_SELECTOR, '.products li:first-child a:nth-child(2)[href*="ruby"]').click()

# Нажмите на вкладку "REVIEWS"
driver.find_element(By.CSS_SELECTOR, 'a[href="#tab-reviews"]').click()
driver.execute_script("window.scrollBy(0, 400);")

# Поставьте 5 звёзд
driver.find_element(By.CSS_SELECTOR, '.stars a:nth-child(5)').click()

# Заполните поле "Review" сообщением: "Nice book!"
driver.find_element(By.CSS_SELECTOR, '#comment').send_keys("Nice book!")

# Заполните поле "Name"
driver.find_element(By.CSS_SELECTOR, '#author').send_keys("Gosha")

# Заполните "Email"
driver.find_element(By.CSS_SELECTOR, '#email').send_keys('gosha2000@mail.ru')

# Нажмите на кнопку "SUBMIT"
driver.find_element(By.CSS_SELECTOR, '#submit').click()

driver.quit()
