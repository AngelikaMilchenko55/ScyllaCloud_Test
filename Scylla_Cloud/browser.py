from selenium import webdriver

class Browser:
    def __init__(self, base_url="https://cloud.scylladb.com"): #описываем какю ссылку используем
        self.driver = webdriver.Chrome() #описываем какой браузер используем
        self.base_url = base_url

    def go_to_site(self, url):
        curl_url = self.base_url + url #"клеем" url для перехода на нужную страницу
        return self.driver.get(curl_url)

    def get_driver(self): #обращение к браузеру извне
        return self.driver

    def back_page(self):
        return self.driver.back()

    def close_browser(self):
        return self.driver.quit()