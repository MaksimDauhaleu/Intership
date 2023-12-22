from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver

OFF_PLAN_BTN = (By.ID, "w-node-_455f4786-676e-1311-ab71-82d622b51c3b-9b22b68b")
PAGE_TITLE = (By.XPATH, "//div[@class='page-title']")
CURRENT_PAGE = (By.XPATH, "//div[@wized = 'currentPageProperties']")
TOTAL_PAGES = (By.XPATH, "//div[@wized = 'totalPageProperties']")
PAGINATION_BTN_NEXT = (By.XPATH, "//a[@wized = 'nextPageProperties']")
PAGINATION_BTN_PREVIOUS = (By.XPATH, "//a[@wized = 'previousPageProperties']")
CONNECT_BUTTON = (By.XPATH, "//a[@href='/book-presentation']")

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
    context.app.main_page.loop_to_end()
    sleep(5)


@then('Go back to the first page using the pagination button')
def loop_back(context):
    context.app.main_page.loop_back()

@then('Click on “Connect the company”')
def click_connect(context):
    context.app.base_page.click(*CONNECT_BUTTON)

@given('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)

@then('Switch the new tab')
def switch_new_tab(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows = context.driver.window_handles
    context.driver.switch_to.window(all_windows[1])

@then('Verify the right tab opens')
def verify_tab_switched(context):
    context.driver.wait.until(EC.url_contains("https://soft.reelly.io/book-presentation"))
