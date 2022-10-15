from Scylla_Cloud.pages.signIn import locators
from Scylla_Cloud.browser import Browser
from Scylla_Cloud.conftest import User
from Scylla_Cloud.pages.signIn.element import Element, InputElement, ButtonElement, LinkElement

class SignIn:
    path = "/user/signin"
    def __init__(self, browser):
        self.email = InputElement(driver=browser.get_driver(), locator= locators.email_locator)
        self.password = InputElement(driver = browser.get_driver(), locator= locators.password_locator)
        self.signin_button = ButtonElement(driver= browser.get_driver(), locator= locators.signin_button_locator)
        self.signup_link = LinkElement(driver= browser.get_driver(),locator= locators.signup_link_locator)
        self.forgot_password_link =LinkElement(driver= browser.get_driver(), locator= locators.forgot_password_link_locator)
        self.open_ticket_link = LinkElement(driver= browser.get_driver(), locator= locators.open_ticket_link_locator)

    def signin(self, user: User):
        self.email.enter_text(user.email)
        self.password.enter_text(user.password())
        self.signin_button.click_element()

    def signin_link(self): # пока не получается реализовать открытие одной ссылки, возвращение назад и открытие следующей ссылки
        self.forgot_password_link.click_link()
        # self.signup_link.click_link()
        # self.open_ticket_link.click_link()
