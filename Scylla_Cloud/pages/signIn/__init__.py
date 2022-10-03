import locators
from Scylla_Cloud.browser import Browser

class Element:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator  # (By.ID, "id")
        self.element = self.driver.find_element(self.locator[0], self.locator[1])

    def click_element(self):
        self.element.click()

class InputElement(Element):

    def enter_text(self, text):
        self.click_element()
        self.element.send_keys(text)

    def get_text(self):
        return self.element.get_attribute("value")

class LinkElement(Element):
    pass

class ButtonElement(Element):
    pass

class SignIn:

    def __init__(self, base_url, Browser):
        self.path = "/user/signin"
        self.url = base_url + self.path
        self.email = InputElement(Browser.driver, locators.email_locator)
        self.password = InputElement(Browser.driver, locators.password_locator)
        self.signin_button = ButtonElement(Browser.driver, locators.signin_button_locator)
        self.signup_link = LinkElement(Browser.driver, locators.signup_link_locator)
        self.forgot_password_link =LinkElement(Browser.driver, locators.forgot_password_link_locator)
        self.open_ticket_link = LinkElement(Browser.driver, locators.open_ticket_link_locator)


    def signin(self):
        pass