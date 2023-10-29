import pytest
from selenium import webdriver
from selenium3_OOP import LoginPage
import time
from Selenium1 import make_screenshot


test_data = [
    ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html')
]

@pytest.mark.parametrize('username, password, url', test_data)
def test_login_page(username, password, url):
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    page.enter_username(username)
    page.enter_password(password)
    page.click_login()
    time.sleep(1)

    try:
        assert driver.current_url == url, make_screenshot(driver)
    except AssertionError:
        print('Błąd, adres url się nie zgadza')
        raise
    else:
        print('ok')
    finally:
        driver.quit()