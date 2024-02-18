import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
URL = "https://secure-retreat-92358.herokuapp.com/"
driver.get(URL)

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Sergey")
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Molchun")
email = driver.find_element(By.NAME, "email")
email.send_keys("email@email.com")
submit_button = driver.find_element(By.CSS_SELECTOR, "form button")
time.sleep(2)
submit_button.click()
