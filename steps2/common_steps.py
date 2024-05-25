# steps/common_steps.py

from behave import *
from page_objects.login_page import LoginPage


@given('I am on the login page')
def login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when('I enter username "{username}" and password "{password}"')
def enter_credentials(context, username, password):
    context.login_page.enter_credentials(username, password)


@when('I click the login button')
def click_login_btn(context):
    context.login_page.click_login_button()


@then('I should be redirected to the dashboard page')
def verify_dashboard(context):
    assert context.driver.current_url == "dashboard_url"
