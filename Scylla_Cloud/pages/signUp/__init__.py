import time
from selenium import webdriver
from Scylla_Cloud.pages.signUp import locators
from Scylla_Cloud.browser import Browser
from Scylla_Cloud.conftest import User
from Scylla_Cloud.pages.signUp.element import Element, InputElement, CheckBoxElement, \
    ButtonElement  # указываем какие элементы взяли из файла element


class SignUp():  # класс описывает саму страницу
    path = "/user/signup"

    def __init__(self, browser):
        self.first_name = InputElement(driver=browser.get_driver(), locator=locators.first_name_locator)
        self.last_name = InputElement(driver=browser.get_driver(), locator=locators.last_name_locator)
        self.email = InputElement(driver=browser.get_driver(), locator=locators.email_locator)
        self.password = InputElement(driver=browser.get_driver(), locator=locators.password_locator)
        self.company = InputElement(driver=browser.get_driver(), locator=locators.company_locator)
        self.country = InputElement(driver=browser.driver, locator=locators.country_locator)
        self.phone = InputElement(driver=browser.get_driver(), locator=locators.phone_locator)
        self.agreement_check_box = CheckBoxElement(driver=browser.get_driver(),
                                                   locator=locators.agreement_check_box_locator)
        self.signup_button = ButtonElement(driver=browser.get_driver(), locator=locators.signup_button_locator)

    def signup(self, user: User):  # метод для регистрации пользователя, с данными из conftest
        self.first_name.enter_text(user.first_name)
        self.last_name.enter_text(user.last_name)
        self.email.enter_text(user.email)
        self.password.enter_text(user.password())
        self.company.enter_text(user.company)
        self.country.enter_text(user.country)
        self.country.key_code()  # начинаем вводить страну в предыдущей строчке и подтверждаем ее выбор нажатием на enter
        self.phone.enter_text(user.phone)
        self.agreement_check_box.click_element()
        print(self.agreement_check_box.state())
    # time.sleep(2)
    # self.signup_button.click_element()
