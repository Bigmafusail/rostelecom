from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from pages.rostelekom import AuthPage


def test_authorisation_incorrect_phone(web_browser):
    """11)Негативный тест с вводом неверного номера телефона"""
    page = AuthPage(web_browser)
    # Нажимаем на таб "Телефон"
    page.phone_tab.click()
    # Вводим невалидный номер телефона
    page.login.send_keys('9276200000')
    # Вводим валидный пароль
    page.password.send_keys("12345Test")
    # Нажимаем на кнопку "Войти"
    page.btn.click()
    # Проверяем на странице наличие сообщения "Неверный логин или пароль"
    assert page.error.is_presented()


def test_authorisation_incorrect_email(web_browser):
    """12)Негативный тест с вводом неверного email"""
    page = AuthPage(web_browser)
    # Нажимаем на таб "Email"
    page.em_tab.click()
    # Вводим невалидный email
    page.login.send_keys('testtesttest@gmail.com')
    # Вводим валидный пароль
    page.password.send_keys("12345Test")
    # Нажимаем на кнопку "Войти"
    page.btn.click()
    # Проверяем на странице наличие сообщения "Неверный логин или пароль"
    assert page.error.is_presented()


def test_authorisation_incorrect_login(web_browser):
    """13)Негативный тест с вводом неверного логина"""
    page = AuthPage(web_browser)
    # Нажимаем на таб "Логин"
    page.l_tab.click()
    # Вводим невалидный логин
    page.login.send_keys('rtkid_0000000000000')
    # Вводим валидный пароль
    page.password.send_keys("12345Test")
    # Нажимаем на кнопку "Войти"
    page.btn.click()
    # Проверяем на странице наличие сообщения "Неверный логин или пароль"
    assert page.error.is_presented()


def test_authorisation_incorrect_password(web_browser):
    """14)Негативный тест с вводом неверного пароля"""
    page = AuthPage(web_browser)
    # Нажимаем на таб "Телефон"
    page.phone_tab.click()
    # Вводим валидный номер телефона
    page.login.send_keys('9276208189')
    # Вводим невалидный пароль
    page.password.send_keys("12345Testttt")
    # Нажимаем на кнопку "Войти"
    page.btn.click()
    # Проверяем на странице наличие сообщения "Неверный логин или пароль"
    assert page.error.is_presented()


def test_authorisation_incorrect_ls(web_browser):
    """15)Негативный тест с вводом неверного лицевого счета"""
    page = AuthPage(web_browser)
    # Нажимаем на таб "Лицевой счет"
    page.ls_tab.click()
    # Вводим невалидный лицевой счет
    page.login.send_keys('888888888888')
    # Вводим валидный пароль
    page.password.send_keys("12345Test")
    # Нажимаем на кнопку "Войти"
    page.btn.click()
    # Проверяем на странице наличие сообщения "Неверный логин или пароль"
    assert page.error.is_presented()


def test_authorisation_wrong_format_phone(web_browser):
    """16)Негативный тест с вводом невалидного номера телефона (1 символ)"""
    page = AuthPage(web_browser)
    # Нажимаем на таб "Телефон"
    page.phone_tab.click()
    # Вводим невалидный номер телефона
    page.login.send_keys('7')
    # Вводим валидный пароль
    page.password.send_keys("12345Test")
    # Проверяем на странице наличие сообщения "Неверный формат телефона"
    error_message = page.phone_error
    assert error_message.is_displayed()


def test_authorisation_incorrect_login_one_simvol(web_browser):
    """17)Негативный тест с вводом невалидного логина, 1 символ """
    page = AuthPage(web_browser)
    # Нажимаем на таб "Логин"
    page.l_tab.click()
    # Вводим невалидный логин
    page.login.send_keys('1')
    # Вводим валидный пароль
    page.password.send_keys("12345Test")
    # Нажимаем на кнопку "Войти"
    page.btn.click()
    # Проверяем на странице наличие сообщения "Неверный логин или пароль"
    assert page.error.is_presented()



def test_authorisation_incorrect_ls_one_simvol(web_browser):
    """18)Негативный тест с вводом невалидного ЛС, один символ """
    page = AuthPage(web_browser)
    # Нажимаем на таб "Логин"
    page.ls_tab.click()
    # Вводим невалидный лицевой счет
    page.login.send_keys('1')
    # Вводим валидный пароль
    page.password.send_keys("12345Test")
    # Нажимаем на кнопку "Войти"
    page.btn.click()
    # Проверяем на странице наличие сообщения "Неверный логин или пароль"
    assert page.error.is_presented()


def test_authorisation_incorrect_(web_browser):
    """19)Негативный тест авторизация незаполненными полями ввода """
    page = AuthPage(web_browser)
    # Нажимаем на таб "Логин"
    page.ls_tab.click()
    # Вводим невалидный лицевой счет
    page.login.send_keys('')
    # Вводим валидный пароль
    page.password.send_keys("")
    # Нажимаем на кнопку "Войти"
    page.btn.click()
    # Проверяем на странице наличие сообщения "Введите логин указанный при регистрации"
    error_login = page.login_error
    assert error_login.is_displayed()


def test_authorisation_incorrect_password_empty(web_browser):
    """20)Негативный тест с пустым поля ввода "Пароль" """
    page = AuthPage(web_browser)
    # Нажимаем на таб "Телефон"
    page.phone_tab.click()
    # Вводим валидный номер телефона
    page.login.send_keys('9276208189')
    # Вводим невалидный пароль
    page.password.send_keys("")
    # Нажимаем на кнопку "Войти"
    page.btn.click()
    # Проверяем на странице наличие сообщения "Неверный логин или пароль"
    assert page.error.is_presented()





