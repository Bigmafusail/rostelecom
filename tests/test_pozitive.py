from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.rostelekom import AuthPage


def test_registration(web_browser):
    """1) Тест на возможность перейти к странице регистрации """
    page = AuthPage(web_browser)
    # Нажимаем на ссылку "Зарегистрироваться"
    page.link_reg.click()
    # Ожидаем
    WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div['
                                                                                   '1]/h1[1]')))
    # Проверяем что на странице присутствует обязательное поле "Имя"
    assert page.btn_reg.is_presented()


def test_registration_mandatory_first_name(web_browser):
    """2) Тест на наличие обязательного поля при регистрации (Имя) """
    page = AuthPage(web_browser)
    # Нажимаем на ссылку "Зарегистрироваться"
    page.link_reg.click()
    # Ожидаем
    WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div['
                                                                                   '1]/h1[1]')))
    # Проверяем что на странице присутствует обязательное поле "Имя"
    assert page.first_name.is_presented()


def test_registration_mandatory_last_name(web_browser):
    """3) Тест на наличие обязательного поля при регистрации (Фамилия) """
    page = AuthPage(web_browser)
    # Нажимаем на ссылку "Зарегистрироваться"
    page.link_reg.click()
    # Ожидаем
    WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div['
                                                                                   '1]/h1[1]')))
    # Проверяем что на странице присутствует обязательное поле "Фамилия"
    assert page.last_name.is_presented()


def test_registration_mandatory_address(web_browser):
    """4) Тест на наличие обязательного поля при регистрации (Почта или номер) """
    page = AuthPage(web_browser)
    # Нажимаем на ссылку "Зарегистрироваться"
    page.link_reg.click()
    # Ожидаем
    WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div['
                                                                                   '1]/h1[1]')))
    # Проверяем что на странице присутствует обязательное поле "Email или номер телефона"
    assert page.address.is_presented()


def test_registration_mandatory_password_reg(web_browser):
    """5) Тест на наличие обязательного поля при регистрации (Пароль) """
    page = AuthPage(web_browser)
    # Нажимаем на ссылку "Зарегистрироваться"
    page.link_reg.click()
    # Ожидаем
    WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div['
                                                                                   '1]/h1[1]')))
    # Проверяем что на странице присутствует обязательное поле "Пароль"
    assert page.password_reg.is_presented()


def test_registration_mandatory_password_reg_confirm(web_browser):
    """6) Тест на наличие обязательного поля при регистрации (Подтверждение пароля) """
    page = AuthPage(web_browser)
    # Нажимаем на ссылку "Зарегистрироваться"
    page.link_reg.click()
    # Ожидаем
    WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div['
                                                                                   '1]/h1[1]')))
    # Проверяем что на странице присутствует обязательное поле "Подтверждение пароля"
    assert page.password_reg_confirm.is_presented()


def test_registration_agreement_link(web_browser):
    """7) Тест на наличие ссылки на политику конфиденциальности и пользовательское соглашение """
    page = AuthPage(web_browser)
    # Нажимаем на ссылку "Зарегистрироваться"
    page.link_reg.click()
    # Ожидаем
    WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div['
                                                                                   '1]/h1[1]')))
    # Проверяем что на странице присутствует ссылка на Пользовательское соглашение
    assert page.agreement_link.is_presented()


def test_registration_btn(web_browser):
    """8) Тест на наличие Кнопки "Продолжить" в форме Регистрации  """
    page = AuthPage(web_browser)
    # Нажимаем на ссылку "Зарегистрироваться"
    page.link_reg.click()
    # Ожидаем
    WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div[1]/div['
                                                                                   '1]/h1[1]')))
    # Проверяем что на странице присутствует кнопка "Продолжить"
    assert page.btn_reg.is_presented()


def test_authorisation_valid_phone(web_browser):
    """9) Тест на авторизацию по номеру телефона с валидными данными"""
    page = AuthPage(web_browser)
    # Нажимаем на таб "Телефон"
    page.phone_tab.click()
    # Вводим валидный номер телефона
    page.login.send_keys('9276208189')
    # Вводим валидный пароль
    page.password.send_keys("12345Test")
    # Нажимаем на кнопку "Войти"
    page.btn.click()
    # Нажимаем на кнопку "Личный кабинет"
    page.btn_l.click()
    # Ожидание
    WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"root"]'
                                                                    '/div/div/div[2]/div/div/div[2]/div[3]')))
    # Проверяем что мы оказались по указанному адресу.
    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


def test_authorisation_valid_email(web_browser):
    """10) Тест на авторизацию по почте с валидными данными"""
    page = AuthPage(web_browser)
    # Нажимаем на таб "Почта"
    page.em_tab.click()
    # Вводим валидный адрес почты
    page.login.send_keys('rudov.dmitriy@gmail.com')
    # Вводим валидный пароль
    page.password.send_keys("12345Test")
    # Нажимаем на кнопку "Войти"
    page.btn.click()
    # Нажимаем на кнопку "Личный кабинет"
    page.btn_l.click()
    # Ожидание
    WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"root"]'
                                                                                   '/div/div/div[2]/div/div/div[2]/div[3]')))
    # Проверяем что мы оказались по указанному адресу.
    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'


def test_authorisation_valid_login(web_browser):
    """11) Тест на авторизацию по логину с валидными данными"""
    page = AuthPage(web_browser)
    # Нажимаем на таб "Логин"
    page.l_tab.click()
    # Вводим валидный логин
    page.login.send_keys('rtkid_1704366111521')
    # Вводим валидный пароль
    page.password.send_keys("12345Test")
    # Нажимаем на кнопку "Войти"
    page.btn.click()
    # Нажимаем на кнопку "Личный кабинет"
    page.btn_l.click()
    # Ожидание
    WebDriverWait(web_browser, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id=\"root"]'
                                                                                   '/div/div/div[2]/div/div/div[2]/div[3]')))
    # Проверяем что мы оказались по указанному адресу.
    assert page.get_current_url() == 'https://start.rt.ru/?tab=main'







