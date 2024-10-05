import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from all_web_locators.alllocators import *
from info_data_script.generate import Generate
from site_url.url import Url

class TestStellarBurgersRegistration:

    def test_registration_correct_email_a_pass_successful_registration(self, driver): # при регистрации на страницу входа
        driver.get(Url.url_register)

        driver.find_element(*AuthRegistr.a_r_name_field).send_keys(Generate.user_name)
        driver.find_element(*AuthRegistr.a_r_email_field).send_keys(Generate.login)
        driver.find_element(*AuthRegistr.a_r_password_field).send_keys(Generate.password)

        driver.find_element(*AuthRegistr.a_r_register_button).click()
        WebDriverWait(driver, 9).until(EC.presence_of_element_located((AuthLogining.a_l_element_login_text)))

        login_button = driver.find_element(*AuthLogining.a_l_element_login_text)
        assert driver.current_url == Url.url_login and login_button.text == 'Вход'

    def test_registration_empty_name_nothing_happens(self, driver): # пустое имя без ошибки, но входа нет
        driver.get(Url.url_register)

        driver.find_element(*AuthRegistr.a_r_email_field).send_keys("login99888888@ya.ru")
        driver.find_element(*AuthRegistr.a_r_password_field).send_keys("1234567890")

        driver.find_element(*AuthRegistr.a_r_register_button).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(AuthRegistr.a_r_register_button))
        time.sleep(2)
        errors_messages = driver.find_elements(*AuthRegistr.a_r_error_message)

        assert driver.current_url == Url.url_register and len(errors_messages) == 0

    @pytest.mark.parametrize('email_list', ['qwerty@yannn', 'test2y.ru', 'te st1998@yan.ru', 'test4@yaaa n.ru',
                                            '@yaandex.ru', 'test235@.ru', 'test34634@yandex.'])

    def test_registration_incorrect_email_show_error(self, driver, email_list): # проверка существующего пользователя
        driver.get(Url.url_register)

        driver.find_element(*AuthRegistr.a_r_name_field).send_keys("Pavel Pavel")
        driver.find_element(*AuthRegistr.a_r_email_field).send_keys(email_list)
        driver.find_element(*AuthRegistr.a_r_password_field).send_keys("1234567890")

        driver.find_element(*AuthRegistr.a_r_register_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(AuthRegistr.a_r_error_message_2))
        error_message = driver.find_element(*AuthRegistr.a_r_error_message_2)

        assert error_message.text == 'Такой пользователь уже существует'

    @pytest.mark.parametrize('password_list', ['0', '000'])
    def test_login_incorrect_password_less_six_symbols_show_error(self, driver, password_list): # некорректный пароль
        driver.get(Url.url_register)

        driver.find_element(*AuthRegistr.a_r_name_field).send_keys("Pavel Pavel")
        driver.find_element(*AuthRegistr.a_r_email_field).send_keys("pvvasile_13_998@ya.ru")
        driver.find_element(*AuthRegistr.a_r_password_field).send_keys(password_list)

        driver.find_element(*AuthRegistr.a_r_register_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(AuthRegistr.a_r_error_message))
        error_message = driver.find_element(*AuthRegistr.a_r_error_message)

        assert error_message.text == 'Некорректный пароль'