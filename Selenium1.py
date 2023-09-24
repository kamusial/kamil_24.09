from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def make_screenshot(driver):
    today = datetime.datetime.today()
    short_date = today.strftime('_stamp%H%M%S')
    screen_name = 'screen' + short_date + '.png'
    driver.get_screenshot_as_file(screen_name)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

username_field = driver.find_element('id', 'user-name')
username_field.send_keys('standard_user')

#driver.find_element('id', 'user-name').send_keys('standard_user')

password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
password_field.send_keys('secret_sauce')

login_button = driver.find_element('name', 'login-button')
login_button.click()
time.sleep(2)

make_screenshot(driver)

driver.quit()