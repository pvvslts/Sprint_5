from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from all_web_locators.alllocators import *
from info_data_script.generate import MyInfo

class TestStellarBurgersLoginLogoutForm:

    def test_login_correct_email_and_password_sh_main_page(self, login): # данные корректны, переход на главную страницу
        driver = login

        order_button = driver.find_element(*MainPage.m_n_order_button)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/" and order_button.text == 'Оформить заказ'

    def test_login_sign_in_button_show_login_page(self, driver): # войти в аккаунт по кнопке
        driver.find_element(*MainPage.m_n_auth).click()
        WebDriverWait(driver, 9).until(EC.presence_of_element_located(AuthLogining.a_l_login_text))

        driver.find_element(*AuthLogining.a_l_email_field).send_keys(MyInfo.login)
        driver.find_element(*AuthLogining.a_l_pass_field).send_keys(MyInfo.password)

        driver.find_element(*AuthLogining.a_l_login_button_form).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(MainPage.m_n_order_button))

        order_button = driver.find_element(*MainPage.m_n_order_button)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/" and order_button.text == 'Оформить заказ'

    def test_login_personal_account_button_show_login_page(self, driver): # проверка личного кабинета
        driver.find_element(*MainPage.m_n_prof_button).click()
        WebDriverWait(driver, 9).until(EC.presence_of_element_located(AuthLogining.a_l_login_text))

        driver.find_element(*AuthLogining.a_l_email_field).send_keys(MyInfo.login)
        driver.find_element(*AuthLogining.a_l_pass_field).send_keys(MyInfo.password)

        driver.find_element(*AuthLogining.a_l_login_button_form).click()
        WebDriverWait(driver, 9).until(EC.presence_of_element_located(MainPage.m_n_order_button))

        order_button = driver.find_element(*MainPage.m_n_order_button)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/" and order_button.text == 'Оформить заказ'

    def test_login_registration_form_sign_in_button(self, driver): # войти в регистрации
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*AuthLogining.a_l_login_text_w_href).click()
        WebDriverWait(driver, 9).until(EC.presence_of_element_located(AuthLogining.a_l_login_text))

        driver.find_element(*AuthLogining.a_l_email_field).send_keys(MyInfo.login)
        driver.find_element(*AuthLogining.a_l_pass_field).send_keys(MyInfo.password)

        driver.find_element(*AuthLogining.a_l_login_button_form).click()
        WebDriverWait(driver, 9).until(EC.presence_of_element_located(MainPage.m_n_order_button))

        order_button = driver.find_element(*MainPage.m_n_order_button)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/" and order_button.text == 'Оформить заказ'

    def test_login_forgot_password_form_sign_in_button(self, driver): # войти через страницу забытый пароль
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        driver.find_element(*AuthPass.a_p_login_text_href).click()
        WebDriverWait(driver, 9).until(EC.presence_of_element_located(AuthLogining.a_l_login_text))

        driver.find_element(*AuthLogining.a_l_email_field).send_keys(MyInfo.login)
        driver.find_element(*AuthLogining.a_l_pass_field).send_keys(MyInfo.password)

        driver.find_element(*AuthLogining.a_l_login_button_form).click()
        WebDriverWait(driver, 9).until(EC.presence_of_element_located(MainPage.m_n_order_button))

        order_button = driver.find_element(*MainPage.m_n_order_button)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/" and order_button.text == 'Оформить заказ'
