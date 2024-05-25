# import threading
# from behave import *
# from selenium import *
# from page_objects.login_page import LoginPage
# from Util_Factory.webdriver_factory import WebDriverFactory
#
#
# # Define a before_all hook to set up the driver
# def before_all(context):
#     context.driver = WebDriverFactory.get_driver()
#
#
# # Define an after_all hook to quit the driver
# def after_all(context):
#     WebDriverFactory.quit_driver(context.driver)
#
#
# # Define a cleanup step to quit the driver after each scenario
# def after_scenario(context, scenario):
#     print("Closing browser")
#     context.driver.quit()
#
#
# # Define a hook to execute before each scenario
# # For example, you can use this hook to log information about the scenario being executed
# def before_scenario(context, scenario):
#     print(f"Executing scenario: {scenario.name}")
#
#
# # Define a hook to execute before each step
# # For example, you can use this hook to log information about the step being executed
# def before_step(context, step):
#     step_name = step.name
#     print(f"Executing step: {step_name}")
#
#
# # Define a hook to execute after each step
# # For example, you can use this hook to capture screenshots after each step
# def after_step(context, step):
#     if step.status == "failed":
#         # Capture screenshot on failure
#         context.driver.save_screenshot(f"failure_screenshot_{step.name}.png")
#
#     elif step.status == "passed":
#         # Capture screenshot on failure
#         context.driver.save_screenshot(f"passed_screenshot_{step.name}.png")
#
# # Define other hooks as needed
