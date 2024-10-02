import time
from all_web_locators.alllocators import *

class TestStellarBurgersConstructorForm:

    def test_constructor_go_to_bylk_scroll_to_bylk(self, login): # тест перехода к булкам
        driver = login
        driver.find_element(*MainPage.m_n_constr_button).click()
        driver.find_element(*MainPage.m_n_fill_button).click()
        driver.find_element(*MainPage.m_n_bylk_button).click()
        h_bylk = driver.find_element(*MainPage.m_n_h_bylk)
        time.sleep(2)
        assert h_bylk.text == 'Булки'

    def test_constructor_go_to_sauces_scroll_to_sauces(self, login): # тест перехода к соусам
        driver = login
        driver.find_element(*MainPage.m_n_constr_button).click()
        driver.find_element(*MainPage.m_n_scs_button).click()
        h_sauce = driver.find_element(*MainPage.m_n_h_scs)
        time.sleep(2)
        assert h_sauce.text == 'Соусы'

    def test_constructor_go_to_fill_scroll_to_fill(self, login): # тест перехода к начинкам
        driver = login
        driver.find_element(*MainPage.m_n_constr_button).click()
        driver.find_element(*MainPage.m_n_fill_button).click()
        h_fill = driver.find_element(*MainPage.m_n_h_fill)
        time.sleep(2)
        assert h_fill.text == 'Начинки'

