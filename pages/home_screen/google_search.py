
from pages.base.base_page import BasePage

from .locators import BaseLocator


class HomePage(BasePage):
    """
    Home page objects
    """
    URL = "https://google.com/"

    def __init__(self):
        super().__init__()
        self.locators = BaseLocator()

    def get_search_bar(self):
        return self.find_element(self.locators.google_search_bar)

    def get_search_icon(self):
        return self.find_element(self.locators.google_search_icon)
