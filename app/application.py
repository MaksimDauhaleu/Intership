from pages.main_page import MainPage
from pages.base_page import Page
from pages.log_in_page import LogInPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = Page(self.driver)
        self.main_page = MainPage(self.driver)
        self.log_in_page = LogInPage(self.driver)


