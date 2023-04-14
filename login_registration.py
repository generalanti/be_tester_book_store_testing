from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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



''' Registration_login: регистрация аккаунта'''
# Откройте https://practice.automationtesting.in/
driver.get('https://practice.automationtesting.in/')

# Нажмите на вкладку "My Account"
driver.find_element(By.CSS_SELECTOR, 'a[href*="my-account"]').click()

# В разделе "Register", введите email для регистрации
driver.find_element(By.CSS_SELECTOR, '#reg_email').send_keys(email)

# В разделе "Register", введите пароль для регистрации
# • составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# • почту и пароль сохраните, потребуюутся в дальнейшем
driver.find_element(By.CSS_SELECTOR, '#reg_password').send_keys(password)

# Нажмите на кнопку "Register"
driver.find_element(By.CSS_SELECTOR, 'input[name="register"]').click()

''' Registration_login: логин в систему'''
# Откройте https://practice.automationtesting.in/
driver.get("https://practice.automationtesting.in/")

# Нажмите на вкладку "My Account"
driver.find_element(By.CSS_SELECTOR, 'a[href*="my-account"]').click()

# В разделе "Login", введите email для логина
driver.find_element(By.CSS_SELECTOR, '#username').send_keys(email)

# В разделе "Login", введите пароль для логина
driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)

# Нажмите на кнопку "Login"
driver.find_element(By.CSS_SELECTOR, 'input[name="login"]').click()

# Добавьте проверку, что на странице есть элемент "Logout"
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.woocommerce-MyAccount-navigation a[href*="logout"]')))
