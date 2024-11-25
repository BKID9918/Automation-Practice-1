from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep

@given('Open Nike main page')
def open_Nike_page(context):
    sleep(3)
    context.app.jordan_colors.open_main_page()

@when('Find Jordan')
def find_jordan(context):
    context.app.jordan_colors.find_jordan_elements()
    sleep(4)
# @when('Find Jordan')
# def wait_for_Jordan_be_clickable_click(context):
#     sleep(4)
#     context.app.jordan_colors.wait_for_Jordan_to_be_clickable()

@when('Hover over Jordan')
def hover_over_jordan_name(context):
    context.app.jordan_colors.hover_over_jordan_element()
    sleep(4)
#
@when('Click Jordan Name')
def click_Jordan_name(context):
    context.app.jordan_colors.wait_for_Jordan_be_clickable_click()
    sleep (4)
#
@when('Click on New Releases')
def click_new_releases(context):
    context.app.jordan_colors.click_new_releases()
    sleep (4)