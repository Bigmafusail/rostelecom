import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://b2c.passport.rt.ru/'

        super().__init__(web_driver, url)

    # Таб "Телефон"
    phone_tab = WebElement(id='t-btn-tab-phone')

    # Таб "Email"
    em_tab = WebElement(id='t-btn-tab-mail')

    # Таб "Login"
    l_tab = WebElement(id='t-btn-tab-login')

    # Таб "Лицевой счет"
    ls_tab = WebElement(id='t-btn-tab-ls')

    # Поле ввода Logina
    login = WebElement(id='username')

    # Поле ввода "Пароль"
    password = WebElement(id='password')

    # Кнопка "Войти"
    btn = WebElement(id='kc-login')

    # Кнопка личный кабинет
    btn_l = WebElement(id='lk-btn')

    # Неверный логин или пароль
    error = WebElement(id='form-error-message')

    # Ссылка на страницу регистрации
    link_reg = WebElement(id='kc-register')

    # Поле ввода "Имя"
    first_name = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]')

    # Поле ввода "Фамилия"
    last_name = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]')

    # Поле ввода "Номер или Почта"
    address = WebElement(id='address')

    # Поле ввода "Пароль" при регистрации
    password_reg = WebElement(id='password')

    # Поле ввода "Подтверждение пароля" при регистрации
    password_reg_confirm = WebElement(id='password-confirm')

    # Ссылка на Пользовательское соглашение
    agreement_link = WebElement(id='rt-auth-agreement-link')

    # Неверный формат телефона
    phone_error = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div[2]/form/div[1]/div[2]/span')

    # Кнопка "Зарегистрироваться"
    btn_reg = WebElement(xpath='//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span')

    #Неверный формат логина
    login_error = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]')
