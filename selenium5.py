import pytest
from selenium import webdriver
from selenium3_OOP import LoginPage
import time
from Selenium1 import make_screenshot


@pytest.mark.parametrize('username, url',
                         [('standard_user', 'https://www.saucedemo.com/inventory.html'),
                          ('lock_out_user', 'https://www.saucedemo.com/')])
def test_login_page(username, url):
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    page.enter_username(username)
    page.enter_password('secret_sauce')
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