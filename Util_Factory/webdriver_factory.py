from selenium import webdriver


class WebDriverFactory:
    @staticmethod
    def get_driver(browser_name='chrome'):
        if browser_name.lower() == 'chrome':
            return webdriver.Chrome()
        elif browser_name.lower() == 'firefox':
            return webdriver.Firefox()
        else:
            raise ValueError("Unsupported browser")

    @staticmethod
    def quit_driver(driver):
        driver.quit()
