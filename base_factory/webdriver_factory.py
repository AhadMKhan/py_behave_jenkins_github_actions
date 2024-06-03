from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from Util_Factory.property_reader import PropertyReader


class WebDriverFactory:
    browser = PropertyReader.get_configuration_property("env_config", "browser.type")
    headless = PropertyReader.get_configuration_property(
        "env_config", "browser.headless"
    )
    incognito = PropertyReader.get_configuration_property(
        "env_config", "browser.incognito"
    )
    print(browser + " --headless " + str(headless) + " --incognito " + str(incognito))

    @staticmethod
    def get_common_options(options, headless):
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--disable-extensions")
        # options.set_capability("acceptInsecureCerts", True)
        options.add_argument("--start-maximized")

        if headless:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-setuid-sandbox")
            options.add_argument("--hide-scrollbars")
        return options

    @staticmethod
    def get_chrome_options(headless, incognito):
        options = ChromeOptions()
        prefs = {"credentials_enable_service": False, "password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        if incognito:
            options.add_argument("--incognito")
        options = WebDriverFactory.get_common_options(options, headless)
        return options

    @staticmethod
    def get_firefox_options(headless, incognito):
        options = FirefoxOptions()
        options.set_preference("signon.rememberSignons", False)
        options.set_preference("network.proxy.type", 0)
        if incognito:
            options.add_argument("--private")
        options = WebDriverFactory.get_common_options(options, headless)
        return options

    @staticmethod
    def get_edge_options(headless, incognito):
        options = EdgeOptions()
        options.use_chromium = True
        if incognito:
            options.add_argument("--inprivate")
        options = WebDriverFactory.get_common_options(options, headless)
        return options

    # pylint: disable=R1705
    @staticmethod
    def get_browser_options(browser_name, headless, incognito):
        if browser_name.lower() == "chrome":
            return WebDriverFactory.get_chrome_options(headless, incognito)
        elif browser_name.lower() == "firefox":
            return WebDriverFactory.get_firefox_options(headless, incognito)
        elif browser_name.lower() == "edge":
            return WebDriverFactory.get_edge_options(headless, incognito)
        else:
            raise ValueError("Unsupported browser")

    # pylint: disable=R1705
    @classmethod
    def get_driver(cls):
        options = WebDriverFactory.get_browser_options(
            cls.browser, cls.headless, cls.incognito
        )
        if cls.browser.lower() == "chrome":
            return webdriver.Chrome(options=options)
        elif cls.browser.lower() == "firefox":
            return webdriver.Firefox(options=options)
        elif cls.browser.lower() == "edge":
            return webdriver.Edge(options=options)
        else:
            raise ValueError("Unsupported browser")

    @staticmethod
    def quit_driver(driver):
        driver.quit()
