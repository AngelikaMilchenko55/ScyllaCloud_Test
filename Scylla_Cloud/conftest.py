import pytest
import random
import string
import datetime

from Scylla_Cloud.browser import Browser

class User: #отвечает за создание полей и генерацию пароля
    def __init__(self, first_name, last_name, email, company, country, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self._password = ""
        self._invalid_password = ""
        self.company = company
        self.country = country

    @staticmethod #генерация пароля
    def generate_password(count_special_chars, count_letters, count_numbers):
        special_chars = random.sample(string.punctuation, count_special_chars)
        letters = random.sample(string.ascii_letters, count_letters)
        numbers = random.sample(string.digits, count_numbers)
        password = special_chars + letters + numbers
        return password

    def password(self):
        """ 8 characters minimum
            One special character
            One letter
            One number
        """
        self._password = self.generate_password(count_special_chars=1, count_letters=5, count_numbers=2)
        return self._password

    def invalid_password(self):
        """ 8 characters minimum
            Zero special character
            One letter
            One number"""
        self._invalid_password = self.generate_password(count_special_chars=0, count_letters=5, count_numbers=3)
        return self._invalid_password


@pytest.fixture(scope="session")#создает уникальный email для каждой сессии
def id_test():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")#возвращает сегодняшнюю дату в дополнение к указанному email для его уникальности
@pytest.fixture()
def browser():
    return Browser()

@pytest.fixture() #параметры для регистрации пользователя
def user_test(id_test):
    return User(first_name="Ivan",
    last_name="Ivanov",
    email=f"angmi57a+{id_test}@gmail.com",#id_test делает email уникальным
    company="Step It",
    country="Russia",
    phone="+79331234455")








