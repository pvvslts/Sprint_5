import time
from all_web_locators.alllocators import *

class TestStellarBurgersConstructorForm:

    def test_constructor_go_to_bylk_scroll_to_bylk(self, driver): # тест перехода к булкам
        driver.find_element(*MainPage.m_n_constr_button).click()
        driver.find_element(*MainPage.m_n_fill_button).click()
        driver.find_element(*MainPage.m_n_bylk_button).click()
        h_bylk = driver.find_element(*MainPage.m_n_h_bylk)
        assert h_bylk.text == 'Булки'

    def test_constructor_go_to_sauces_scroll_to_sauces(self, driver): # тест перехода к соусам
        driver.find_element(*MainPage.m_n_constr_button).click()
        driver.find_element(*MainPage.m_n_scs_button).click()
        h_sauce = driver.find_element(*MainPage.m_n_h_scs)
        assert h_sauce.text == 'Соусы'

    def test_constructor_go_to_fill_scroll_to_fill(self, driver): # тест перехода к начинкам
        driver.find_element(*MainPage.m_n_constr_button).click()
        driver.find_element(*MainPage.m_n_fill_button).click()
        h_fill = driver.find_element(*MainPage.m_n_h_fill)
        assert h_fill.text == 'Начинки'

