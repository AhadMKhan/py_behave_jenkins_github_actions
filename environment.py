# steps/environment.py

from base_factory.webdriver_factory import WebDriverFactory


def before_all(context):
    context.driver = WebDriverFactory.get_driver()


def after_all(context):
    WebDriverFactory.quit_driver(context.driver)
