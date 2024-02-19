from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


options = Options()
# options.add_argument('start-maximized')
# options.add_argument('--window-size=500,500')
driver = webdriver.Chrome(options=options)
sleep(3)
driver.maximize_window()
# driver.set_window_size(500, 500)
driver.get('https://www.google.com')
print(driver.title)
print(driver.current_url)

input_field = driver.find_element(By.NAME, 'q')
sleep(1)
input_field.send_keys('dog')
sleep(1)
input_field.submit()
assert driver.title.startswith('dog')

sleep(1)

driver.quit()
# driver.close()
