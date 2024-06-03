from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    ElementClickInterceptedException,
    InvalidElementStateException,
)

from Util_Factory.property_reader import PropertyReader
from Util_Factory.utility_factory import UtilityFactory

global_timeout = PropertyReader.get_configuration_property(
    "env_config", "timeout.global"
)
element_timeout = PropertyReader.get_configuration_property(
    "env_config", "timeout.element"
)
element_retries = PropertyReader.get_configuration_property(
    "env_config", "retries.element"
)
element_polling_interval = PropertyReader.get_configuration_property(
    "env_config", "retries.polling_interval"
)


# pylint: disable=R0903
class ElementFactory:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator_value, locator_type):
        return self._find_element(locator_value, locator_type)

    # pylint: disable=W0718
    def _find_element(self, locator_value, locator_type):
        by = self._get_by(locator_type)
        for attempt in range(1, element_retries + 1):
            try:
                element = WebDriverWait(
                    self.driver, element_timeout, element_polling_interval
                ).until(EC.presence_of_element_located((by, locator_value)))
                return element
            except TimeoutException as e:
                self._handle_exception(attempt, "Timed out", by, locator_value, e)
            except NoSuchElementException as e:
                self._handle_exception(
                    attempt, "Element not found", by, locator_value, e
                )
            except StaleElementReferenceException as e:
                self._handle_exception(
                    attempt, "Stale element encountered", by, locator_value, e
                )
            except ElementNotInteractableException as e:
                self._handle_exception(
                    attempt, "Element not interactable", by, locator_value, e
                )
            except ElementClickInterceptedException as e:
                self._handle_exception(
                    attempt, "Element click intercepted", by, locator_value, e
                )
            except InvalidElementStateException as e:
                self._handle_exception(
                    attempt, "Invalid element state encountered", by, locator_value, e
                )
            except Exception as e:
                self._handle_exception(
                    attempt, "An unexpected error occurred", by, locator_value, e
                )
        return None

    @staticmethod
    def _get_by(locator_type):
        locator_type = locator_type.replace(" ", "").lower()
        locator_type = UtilityFactory.remove_spaces(locator_type)

        locator_map = {
            "id": By.ID,
            "xpath": By.XPATH,
            "css selector": By.CSS_SELECTOR,
            "class name": By.CLASS_NAME,
            "name": By.NAME,
            "tag": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
        }

        if locator_type in locator_map:
            return locator_map[locator_type]

        raise ValueError(f"Invalid locator type: {locator_type}")

    @staticmethod
    def _handle_exception(attempt, message, by, locator_value, exception):
        print(f"Attempt {attempt}: {message} with {by}: {locator_value}")
        print(exception)
