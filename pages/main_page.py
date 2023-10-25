from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

class MainPage(Page):
    CURRENT_PAGE = (By.XPATH, "//div[@wized = 'currentPageProperties']")
    TOTAL_PAGES = (By.XPATH, "//div[@wized = 'totalPageProperties']")
    PAGINATION_BTN_NEXT = (By.XPATH, "//a[@wized = 'nextPageProperties']")
    PAGINATION_BTN_PREVIOUS = (By.XPATH, "//a[@wized = 'previousPageProperties']")

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
        # current_page = self.find_current_page()
        total_pages = self.find_total_page()
        sleep(3)
        for x in range(0, len(total_pages)):
            if x < total_pages:
                self.click(*self.PAGINATION_BTN_NEXT)
                x += 1
            sleep(3)
        # print(current_page)
        # print(total_pages)
