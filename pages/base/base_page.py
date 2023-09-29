from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

from .locators import TimeOut, BaseLocator


class BasePage:
    """
    Base page to contain common functionality for pages
    """
    URL = None

    def __init__(self, driver=None):
        self.driver = driver or webdriver.Chrome()
        self.locators = BaseLocator()
        self.driver.get(self.URL)

    def find_element(self, locator, time_out: int = TimeOut.TWO_SECONDS):
        message = f"{locator} not found"
        return WebDriverWait(self.driver, time_out).until(
            EC.visibility_of_element_located(locator), message
        )

    @staticmethod
    def click(element):
        element.click()

    @staticmethod
    def enter_text(element, text):
        return element.send_keys(text)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
