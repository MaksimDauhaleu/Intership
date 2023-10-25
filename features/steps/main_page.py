from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

OFF_PLAN_BTN = (By.ID, "w-node-_455f4786-676e-1311-ab71-82d622b51c3b-9b22b68b")
PAGE_TITLE = (By.XPATH, "//div[@class='page-title']")
CURRENT_PAGE = (By.XPATH, "//div[@wized = 'currentPageProperties']")
TOTAL_PAGES = (By.XPATH, "//div[@wized = 'totalPageProperties']")
PAGINATION_BTN_NEXT = (By.XPATH, "//a[@wized = 'nextPageProperties']")
PAGINATION_BTN_PREVIOUS = (By.XPATH, "//a[@wized = 'previousPageProperties']")


@given('Open main page')
def open_main_page(context):
    context.app.main_page.open_main_page()
    EC.url_contains("https://soft.reelly.io/sign-in")


@then('Click on off plan option at the left side menu')
def click_off_plan(context):
    context.app.base_page.click(*OFF_PLAN_BTN)


@then('Verify the right page opens')
def verify_page(context):
    context.app.base_page.verify_element_text("Total projects", *PAGE_TITLE)


@when('Go to the final page using the pagination button')
def loop_to_end(context):
    # context.app.base_page.click(*PAGINATION_BTN_NEXT)
    # sleep(3)

    context.app.main_page.loop_to_end()
    # while current_page < total_page:
    #     context.app.base_page.click(*PAGINATION_BTN_NEXT)
    # print(total_page.text)
    sleep(5)
