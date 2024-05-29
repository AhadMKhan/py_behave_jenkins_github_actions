from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from readers import get_yaml_property

environment_file_path = "./configuration/environment_config.yaml"
browser = get_yaml_property(environment_file_path, "browser")
headless = get_yaml_property(environment_file_path, "headless")
print(browser+" --headless "+str(headless))


class WebDriverFactory:

    @staticmethod
    def get_browser_options(browser_name, headless):
        if browser_name.lower() == 'chrome':
            options = ChromeOptions()
        elif browser_name.lower() == 'firefox':
            options = FirefoxOptions()
        elif browser_name.lower() == 'edge':
            options = EdgeOptions()
            # Add Edge specific options if needed
        else:
            raise ValueError("Unsupported browser")

        if headless:
            options.add_argument("--headless")  # Example: running in headless mode
        return options

    @staticmethod
    def get_driver(browser_name=browser):
        options = WebDriverFactory.get_browser_options(browser_name, headless)
        if browser_name.lower() == 'chrome':
            return webdriver.Chrome(options=options)
        elif browser_name.lower() == 'firefox':
            return webdriver.Firefox(options=options)
        elif browser_name.lower() == 'edge':
            return webdriver.Edge(options=options)
        else:
            raise ValueError("Unsupported browser")

    @staticmethod
    def quit_driver(driver):
        driver.quit()
