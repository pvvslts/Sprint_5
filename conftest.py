import pytest
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from all_web_locators.alllocators import *
from info_data_script.generate import MyInfo

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):

    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(*AuthLogining.a_l_email_field).send_keys(MyInfo.login)
    driver.find_element(*AuthLogining.a_l_pass_field).send_keys(MyInfo.password)
    driver.find_element(*AuthLogining.a_l_login_button_form).click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located(MainPage.m_n_order_button))
    return driver