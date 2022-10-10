from selenium import webdriver
from selenium.webdriver import Keys #модуль для имитации нажатия на клавиатуре кнопок типа enter
from Scylla_Cloud.pages.signUp.locators import is_checked_locator

class Element:#базовый элемент
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator  # (By.ID, "id")
        self.element = self.driver.find_element(self.locator[0], self.locator[1])#параметр в котором хранится ссылка на найденный элемент на странице

    def click_element(self):#метод для клика по элементам
        self.element.click()

class InputElement(Element):

    def enter_text(self, text):
        self.click_element()
        self.element.send_keys(text)

    def get_text(self):
        return self.element.get_attribute("value")

    def key_code(self):
        return self.element.send_keys(Keys.ENTER)#имитация нажатие на enter на клавиатуре

class CheckBoxElement(Element):#проверяем в каком состоянии находится элемент(стоит галочка или нет)
    is_checked = False #указываем, что изначально пока галочки нет у нас передается False

    def checked(self):#метод ставит галочку и возвращает True
        self.element.click_element()
        self.is_checked = True
        return self.is_checked

    def unchecked(self):#метод снимает галочку и возвращает False
        self.element.click_element()
        self.is_checked = False
        return self.is_checked

    def state(self):#доп. проверка
        """return when checkBox is checked or not"""
        if self.is_checked and self.driver.find_element(is_checked_locator[0],is_checked_locator[1]):
            return True
        else:
            return False

class ButtonElement(Element):

    def key_code(self):
        return self.element.send_keys(Keys.ENTER)