import time
from allure_commons.types import AttachmentType
import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By

def setup_function():
    global driver
    hub_url = "http://192.168.56.1:4444/wd/hub"
    options = webdriver.FirefoxOptions()
    driver = webdriver.Remote(command_executor=hub_url, options=options)
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()

def teardown_function():
    driver.quit()

def cred():
    return [
        ('ali','1234'),
        ('noman','1234'),
        ('zobair','5253')
    ]
@pytest.mark.parametrize("username,password",cred())
def test_login(username, password):
    print("my pytest login")
    driver.find_element(By.ID,'user-name').send_keys(username)
    time.sleep(10)
    driver.find_element(By.ID,'password').send_keys(password)
    time.sleep(10)
