# headless mode
from selenium import webdriver
from selenium3_OOP import LoginPage
import time
from Selenium1 import make_screenshot

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.w3schools.com/')
time.sleep(2)
accept = driver.find_element('id', 'accept-choices')
accept.click()
time.sleep(2)
menu = driver.find_element('id', 'navbtn_tutorials')
HTMLtutorial = driver.find_element('xpath', '/html/body/div[2]/div[2]/div/nav[1]/div[1]/div/div[2]/div[1]/div[1]/a[2]')



webdriver.ActionChains(driver).move_to_element(menu).click().move_to_element(HTMLtutorial).click().perform()
time.sleep(2)

HTML_form_attributes = driver.find_element('xpath','//*[@id="leftmenuinnerinner"]/a[40]')
HTML_form_attributes.click()
tryityourself = driver.find_element('xpath', '//*[@id="main"]/div[3]/a')
tryityourself.click()
print(driver.title)
# przejść do drugiej karty