from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from all_web_locators.alllocators import *

class TestStellarBurgersProfileForm:

    def test_click_profile_button_open_profile_form(self, login): # личный кабинет - открыть
        driver = login

        driver.find_element(*MainPage.m_n_prof_button).click()
        WebDriverWait(driver, 9).until(EC.presence_of_element_located(LKProfl.l_k_info_message))
        profile = driver.find_element(*LKProfl.l_k_histry_shop_button)
        assert "https://stellarburgers.nomoreparties.site/account/profile" == driver.current_url and profile.text == 'История заказов'

    def test_click_constructor_button_show_constructor_form(self, login): # переход из лк в конструктор по кнопке
        driver = login

        driver.find_element(*MainPage.m_n_prof_button).click()
        WebDriverWait(driver, 9).until(EC.presence_of_element_located(LKProfl.l_k_info_message))
        driver.find_element(*MainPage.m_n_constr_button).click()

        h1_tag = driver.find_elements(By.XPATH, ".//h1")
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'

    def test_click_logo_button_show_constructor_form(self, login): # переход из лк в конструктор по лого
        driver = login

        driver.find_element(*MainPage.m_n_prof_button).click()
        WebDriverWait(driver, 9).until(EC.presence_of_element_located(LKProfl.l_k_info_message))
        driver.find_element(*MainPage.m_n_logo).click()

        h1_tag = driver.find_elements(By.XPATH, ".//h1")
        assert len(h1_tag) > 0 and h1_tag[0].text == 'Соберите бургер'

    def test_click_logout_button_in_lk_open_login_form(self, login): # выход из аккаунта
        driver = login

        driver.find_element(*MainPage.m_n_prof_button).click()
        WebDriverWait(driver, 9).until(EC.presence_of_element_located(LKProfl.l_k_info_message))
        driver.find_element(*LKProfl.l_k_logout_button).click()
        WebDriverWait(driver, 9).until(EC.presence_of_element_located(AuthLogining.a_l_login_button_form))

        login_button = driver.find_element(*AuthLogining.a_l_element_login_text)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login" and login_button.text == 'Вход'
