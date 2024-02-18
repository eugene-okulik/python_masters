import time
import threading
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, \
    TimeoutException
from selenium.webdriver.common.by import By


URL = "http://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(URL)
time.sleep(2)

cookies_count = None



def check_prices_periodically():
    while True:
        try:
            print(f"0.{cookies_count}")
            cursor_price_tag = driver.find_element(By.CSS_SELECTOR, "#buyCursor b")
            cursor_price = int(cursor_price_tag.text.strip().replace(",", "").split("-")[1])
            print(f"1.{cursor_price}")
            grandma_price_tag = driver.find_element(By.CSS_SELECTOR, "#buyGrandma b")
            grandma_price = int(grandma_price_tag.text.strip().replace(",", "").split("-")[1])
            print(f"2.{grandma_price}")
            factory_price_tag = driver.find_element(By.CSS_SELECTOR, "#buyFactory b")
            factory_price = int(factory_price_tag.text.strip().replace(",", "").split("-")[1])
            print(f"3.{factory_price}")
            mine_price_tag = driver.find_element(By.CSS_SELECTOR, "#buyMine b")
            mine_price = int(mine_price_tag.text.strip().replace(",", "").split("-")[1])
            print(f"4.{mine_price}")
            shipment_price_tag = driver.find_element(By.CSS_SELECTOR, "#buyShipment b")
            shipment_price = int(shipment_price_tag.text.strip().replace(",", "").split("-")[1])
            print(f"5.{shipment_price}")
            alchemy_price_tag = driver.find_element(By.CSS_SELECTOR, "#buyAlchemy\\ lab b")
            alchemy_price = int(alchemy_price_tag.text.strip().replace(",", "").split("-")[1])
            print(f"6.{alchemy_price}")
            portal_price_tag = driver.find_element(By.CSS_SELECTOR, "#buyPortal b")
            portal_price = int(portal_price_tag.text.strip().replace(",", "").split("-")[1])
            print(f"7.{portal_price}")
            time_machine_price_tag = driver.find_element(By.CSS_SELECTOR, "#buyTime\\ machine b")
            time_machine_price = int(time_machine_price_tag.text.strip().replace(",", "").split("-")[1])
            print(f"8.{time_machine_price}")
            # elder_price_tag = driver.find_element(By.CSS_SELECTOR, "#buyElder\\ Pledge b")
            # elder_price = int(elder_price_tag.text.strip().replace(",", "").split("-")[0])
            # print(f"9.{elder_price}")
            time.sleep(10)

            if cookies_count >= time_machine_price:
                time_machine_price_tag.click()
            elif cookies_count >= portal_price:
                portal_price_tag.click()
            elif cookies_count >= alchemy_price:
                alchemy_price_tag.click()
            elif cookies_count >= shipment_price:
                shipment_price_tag.click()
            elif cookies_count >= mine_price:
                mine_price_tag.click()
            elif cookies_count >= factory_price:
                factory_price_tag.click()
            elif cookies_count >= grandma_price:
                grandma_price_tag.click()
            elif cookies_count >= cursor_price:
                cursor_price_tag.click()

        except:
            print("Something wrong with items buying.")
#
prices_check_thread = threading.Thread(target=check_prices_periodically)
prices_check_thread.start()

def run_game():
    global cookies_count

    try:
        while True:
            cookie = driver.find_element(By.ID, "cookie")
            cookie.click()
            cookies_number = driver.find_element(By.ID, "money")
            cookies_count = int(cookies_number.text.replace(",", ""))
            print(cookies_count)
            # time.sleep(0.01)

    except NoSuchElementException as ex:
        print(ex)

    except StaleElementReferenceException as ex:
        print(ex)

    except ElementNotInteractableException as ex:
        print(ex)

    except TimeoutException as ex:
        print(ex)

    finally:
        print("Retrying continue the game.")
        run_game()
run_game()
