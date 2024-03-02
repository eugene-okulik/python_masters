from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

URL = 'https://demoqa.com/automation-practice-form'


# Напишите программу, которая зайдет на страницу
# https://demoqa.com/automation-practice-form и полностью заполнит форму (кроме загрузки файла) и нажмет Submit.
#
# Небольшая особенность
# Страничка эта немного кривая, иногда реклама перекрывает элементы и по ним невозможно кликнуть
# (но сейчас, смотрю, вообще реклама пропала). Если бы это было приложение, которое мы тестируем, это был бы баг.
# Но работаем с тем, что есть. И для нас это даже плюс, нужно найти как выкрутиться.
# Обойти это можно уменьшив размер экрана браузера - тогда элементы перераспределяются и становятся доступны.
# Но если реклама так и не появится, то ничего на странице не мешает.
#
# После отправки вам будет отображено окошко с тем что вы ввели.
# Получите со страницы содержимое этого окошка и распечатайте (выведите на экран).


def test_fill_the_form(fn: str, ln: str, eml: str, gndr: int, tel: int, bd: str, subj: str, hbby: int,
                       addr: str, stv: str, ctyv: str):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome()  # options=chrome_options
    driver.get(URL)
    driver.maximize_window()

    # time.sleep(2)
    fname = driver.find_element(By.CSS_SELECTOR, 'input#firstName[placeholder="First Name"]')
    lname = driver.find_element(By.CSS_SELECTOR, 'input#lastName[placeholder="Last Name"]')
    email = driver.find_element(By.CSS_SELECTOR, 'input#userEmail[placeholder="name@example.com"]')
    gender = driver.find_element(By.CSS_SELECTOR, f'input#gender-radio-{gndr}')
    mobile = driver.find_element(By.CSS_SELECTOR, 'input#userNumber[placeholder="Mobile Number"]')
    # Impossible to clear the date field. the form became blank!!!
    dob = driver.find_element(By.CSS_SELECTOR, 'input#dateOfBirthInput')
    subject = driver.find_element(By.CSS_SELECTOR, 'input#subjectsInput')
    hobbie = driver.find_element(By.CSS_SELECTOR, f'input#hobbies-checkbox-{hbby}[value="{hbby}"]')
    address = driver.find_element(By.CSS_SELECTOR, 'textarea#currentAddress[placeholder="Current Address"]')

    state_dropdown = driver.find_element(By.CSS_SELECTOR, '#stateCity-wrapper #state')
    city_dropdown = driver.find_element(By.CSS_SELECTOR, '#stateCity-wrapper #city')
    submit = driver.find_element(By.CSS_SELECTOR, 'button#submit[class="btn btn-primary"]')

    fname.send_keys(fn)
    lname.send_keys(ln)
    email.send_keys(eml)
    driver.execute_script("arguments[0].click();", gender)
    mobile.send_keys(tel)

    # Impossible to clear the date field. the form became blank!!!
    print(dob)
    # dob.click()
    # dob.send_keys(Keys.CONTROL + 'a')
    # dob.send_keys(Keys.DELETE)
    # dob.send_keys(bd)

    driver.execute_script("arguments[0].scrollIntoView();", subject)

    # Subject field erases value after inserting string!!!
    subject.send_keys(subj)
    driver.execute_script("arguments[0].click();", hobbie)
    address.send_keys(addr)
    ActionChains(driver).move_to_element(state_dropdown).click().perform()
    state_option = driver.find_element(By.XPATH,
                                       '//div[@id="stateCity-wrapper"]//div[@id="state"]//div[text()="NCR"]')
    driver.execute_script("arguments[0].scrollIntoView();", state_option)
    state_option.click()
    ActionChains(driver).move_to_element(city_dropdown).click().perform()
    city_option = driver.find_element(By.XPATH,
                                      '//div[@id="stateCity-wrapper"]//div[@id="city"]//div[text()="Noida"]')
    city_option.click()
    submit.click()

    modal_content = driver.find_element(By.CLASS_NAME, "modal-content")
    print(modal_content.text)
    driver.find_element(By.ID, "closeLargeModal").click()


test_fill_the_form("Serge", "Moseratti", "moseratti@gmail.com", 1, 381611492416,
                   "15.10.1999", "Serge's message subject", 3, "Belgrad", "NCR", "Noida")
