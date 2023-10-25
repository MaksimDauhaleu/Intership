from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

email = "maksimdauhaleu@gmail.com"
password = "waxdiz-4Vikho-neszan"


EMAIL_LOC = (By.ID, "email-2")
PASSWORD_LOC = (By.ID, "field")
LOGIN_BTN = (By.XPATH, "//a[@wized ='loginButton']")


@then('Log in to the page')
def log_in(context):
    context.app.base_page.input_text(email, *EMAIL_LOC)
    context.app.base_page.input_text(password, *PASSWORD_LOC)
    context.app.base_page.click(*LOGIN_BTN)
    sleep(10)