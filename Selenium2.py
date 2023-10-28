from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as excon
from Selenium1 import make_screenshot

def czekaj_na_id(element_id):
    timeout = 5
    timeout_mesage = (f'Element o ID {element_id} nie pojawil sie w czasie {timeout} sekund')
    lokalizator = (By.ID, element_id)
    znaleziono = excon.visibility_of_element_located(lokalizator)   #sprawdzamy, czy element widoczny
    oczekiwator = WebDriverWait(driver, timeout)   #jak długo czekać i gdzie
    return oczekiwator.until(znaleziono, timeout_mesage)  #zwrotka



driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com')

#login_button = driver.find_element('id', 'login-button')

try:
    login_button = czekaj_na_id('login-buttonn')
except:
    print('Nie znaleziono')
    raise
else:
    print('znaleziono')
finally:
    print('i koniec')
    make_screenshot(driver)
    driver.quit()