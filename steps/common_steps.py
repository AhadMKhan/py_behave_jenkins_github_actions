# steps/common_steps.py

from behave import given, when  # pylint: disable=no-name-in-module

from Util_Factory.property_reader import PropertyReader
from Util_Factory.utility_factory import UtilityFactory
from base_factory.common_actions import CommonActions


@given('I am on the "{web_url}" login page')
def open_url(context, web_url):
    web_url = UtilityFactory.make_property_name(web_url)
    web_url = PropertyReader.get_configuration_property("run_config", web_url)
    context.common_actions = CommonActions(context.driver)
    context.common_actions.navigate_to_url(web_url)


@when(
    'User Enter "{test_data}" on "{locator_value}" using "{locator_type}" on "{page_name}" Page'
)
def enter_text_on_page(context, test_data, locator_value, locator_type, page_name):
    test_data = PropertyReader.get_test_data_property(test_data, page_name)
    locator_value = PropertyReader.get_locator_property(locator_value, page_name)

    context.common_actions.enter_text(test_data, locator_value, locator_type)


@when('User Click on "{locator_value}" using "{locator_type}" on "{page_name}" Page')
def click_button_on_page(context, locator_value, locator_type, page_name):
    locator_value = PropertyReader.get_locator_property(locator_value, page_name)
    context.common_actions.click_button(locator_value, locator_type)


@when(
    'User Assert "{test_data}" on "{locator_value}" using "{locator_type}" on "{page_name}" Page'
)
def assert_text_on_page(context, test_data, locator_value, locator_type, page_name):
    test_data = PropertyReader.get_test_data_property(test_data, page_name)
    locator_value = PropertyReader.get_locator_property(locator_value, page_name)

    context.common_actions.assert_text(test_data, locator_value, locator_type)


# enter_text_on_page("context", "Username", "Username", "id", "Login Page")
