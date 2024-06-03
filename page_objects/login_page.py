from selenium.webdriver.common.by import By
from base_factory.element_factory import ElementFactory


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.element_factory = ElementFactory(self.driver)  # Instantiate ElementFactory

    def enter_credentials(self, username, password):
        self.element_factory.find_element("id", "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, "login-button").click()
