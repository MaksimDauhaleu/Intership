from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Page):
    CURRENT_PAGE = (By.XPATH, "//div[@wized = 'currentPageProperties']")
    TOTAL_PAGES = (By.XPATH, "//div[@wized = 'totalPageProperties']")
    PAGINATION_BTN_NEXT = (By.XPATH, "//a[@wized = 'nextPageProperties']")
    PAGINATION_BTN_PREVIOUS = (By.XPATH, "//div[@wized = 'previousPageProperties']")

    def open_main_page(self):
        self.open_url('https://soft.reelly.io')
        sleep(10)

    def find_current_page(self):
        current_page = self.find_element(*self.CURRENT_PAGE)
        # print(current_page.text)
        return current_page.text

    def find_total_page(self):
        total_page = self.find_element(*self.TOTAL_PAGES)
        # print(total_page.text)
        return total_page.text

    def loop_to_end(self):
        sleep(3)
        total_pages = self.find_total_page()
        sleep(3)
        for x in range(0, int(total_pages)):
            if x < int(total_pages):
                self.click(*self.PAGINATION_BTN_NEXT)
                x += 1
                sleep(2)

    def loop_back(self):
        current_page = self.find_current_page()
        sleep(3)
        while int(current_page) > 1:
            self.click(*self.PAGINATION_BTN_PREVIOUS)
            sleep(2)
            current_page = self.find_current_page()