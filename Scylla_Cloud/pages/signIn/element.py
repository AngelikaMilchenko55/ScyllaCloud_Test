from selenium import webdriver
from selenium.webdriver import Keys

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

    def key_code(self):
        return self.element.send_keys(Keys.ENTER)

class LinkElement(Element):

    def click_link(self):
        self.click_element()

class ButtonElement(Element):

    def key_code(self):
        return self.element.send_keys(Keys.ENTER)