from selenium.webdriver.support.ui import Select
from base_factory.element_factory import ElementFactory


class CommonActions:
    def __init__(self, driver):
        self.driver = driver
        self.element_factory = ElementFactory(self.driver)  # Instantiate ElementFactory

    def navigate_to_url(self, web_url):
        return self.driver.get(web_url)

    def click_button(self, locator_value, locator_type):
        return self.element_factory.find_element(locator_value, locator_type).click()

    def enter_text(self, text_to_enter, locator_value, locator_type):
        return self.element_factory.find_element(locator_value, locator_type).send_keys(
            text_to_enter
        )

    def select_dropdown_by_text(self, option_text, locator_value, locator_type):
        dropdown_element = self.element_factory.find_element(
            locator_value, locator_type
        )
        select = Select(dropdown_element)
        return select.select_by_visible_text(option_text)

    def select_dropdown_by_value(self, option_value, locator_value, locator_type):
        dropdown_element = self.element_factory.find_element(
            locator_value, locator_type
        )
        select = Select(dropdown_element)
        return select.select_by_value(option_value)

    def select_dropdown_by_index(self, option_index, locator_value, locator_type):
        dropdown_element = self.element_factory.find_element(
            locator_value, locator_type
        )
        select = Select(dropdown_element)
        return select.select_by_index(option_index)

    def assert_text(self, expected_text, locator_value, locator_type):
        element = self.element_factory.find_element(locator_value, locator_type)
        actual_text = element.text
        assert (
            actual_text == expected_text
        ), f"Expected text '{expected_text}' but got '{actual_text}'"

    def assert_attribute_value(
        self, attribute, expected_value, locator_value, locator_type
    ):
        element = self.element_factory.find_element(locator_value, locator_type)
        actual_value = element.get_attribute(attribute)
        assert (
            actual_value == expected_value
        ), f"Expected attribute '{attribute}' to be '{expected_value}' but got '{actual_value}'"

    def assert_element_present(self, locator_value, locator_type):
        element = self.element_factory.find_element(locator_value, locator_type)
        assert (
            element is not None
        ), f"Element with {locator_type}='{locator_value}' should be present"
