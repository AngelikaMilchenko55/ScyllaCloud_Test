import string
from Scylla_Cloud import conftest
import pytest
from pages.signUp import SignUp
from pages.signIn import SignIn
from browser import Browser
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSignUpPage:

    def test_signup(self, browser, user_test):
        browser.go_to_site(SignUp.path) # вызываем метод для перехода на страницу, склеивается baseurl из browser  с частью url path из __init__
        browser.driver.implicitly_wait(5)
        page = SignUp(browser)
        page.signup(user=user_test)
        print("email:", page.email.get_text(), "пароль:",page.password.get_text())
        time.sleep(2)
        #assert browser.current_url == base_url + "/"

class TestSignInPage:

    def test_signin(self, browser, user_test):
        browser.go_to_site(SignIn.path)
        browser.driver.implicitly_wait(5)
        page = SignIn(browser)
        page.signin(user=user_test)
        print("email:", page.email.get_text(), "пароль:", page.password.get_text())
        time.sleep(3)

    def test_link(self, browser):# пока не получается реализовать открытие одной ссылки, возвращение назад и открытие следующей ссылки
        browser.go_to_site(SignIn.path)
        browser.driver.implicitly_wait(5)
        page = SignIn(browser)
        time.sleep(2)
        page.signin_link()
        time.sleep(2)
        browser.back_page()
        time.sleep(2)







