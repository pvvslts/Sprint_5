from selenium.webdriver.common.by import By
class AuthRegistr:
    a_r_name_field = (By.XPATH, ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")
    a_r_email_field = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    a_r_password_field = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    a_r_register_button = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    a_r_error_message = (By.XPATH, ".//p[contains(@class, 'input__error')]")
    a_r_error_message_2 = (By.XPATH, ".//div[@class='Auth_login__3hAey']/p[@class='input__error text_type_main-default']")
    a_r_login_button = (By.CLASS_NAME, "Auth_link__1fOlj")
class AuthLogining:
    a_l_login_text = (By.XPATH, ".//h2[text()='Вход']")
    a_l_login_button_form = (By.XPATH, ".//button[text()='Войти']")
    a_l_login_text_w_href = (By.XPATH, ".//a[text()='Войти']")
    a_l_login_button = (By.CLASS_NAME, "Auth_link__1fOlj")
    a_l_email_field = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    a_l_pass_field = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    a_l_element_login_text = (By.XPATH, ".//*[text() = 'Вход']")
class MainPage:
    m_n_prof_button = (By.XPATH, ".//p[text()='Личный Кабинет']")
    m_n_auth = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    m_n_order_button = (By.XPATH, ".//button[text()='Оформить заказ']")
    m_n_constr_button = (By.XPATH, ".//p[text()='Конструктор']")
    m_n_logo = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")
    m_n_scs_button = (By.XPATH, ".//span[text()='Соусы']/parent::*")
    m_n_h_scs = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']"
    m_n_bylk_button = (By.XPATH, ".//span[text()='Булки']/parent::*")
    m_n_h_bylk = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']"
    m_n_fill_button = (By.XPATH, ".//span[text()='Начинки']/parent::*")
    m_n_h_fill = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']"
class LKProfl:
    l_k_logout_button = (By.XPATH, ".//button[text()='Выход']")
    l_k_info_message = (By.XPATH, ".//p[contains(text(),'персональные данные')]")
    l_k_histry_shop_button = (By.XPATH, ".//li[@class='Account_listItem__35dAP']/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")
    l_k_h1_tag = (By.XPATH, ".//h1")
class AuthPass:
    a_p_login_text_href = (By.XPATH, ".//a[text()='Войти']")