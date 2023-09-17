from selenium.webdriver.common.by import By


class BaseLocator:
    google_search_bar = (By.CLASS_NAME, "gLFyf")
    google_search_icon = (By.ID, "jZ2SBf")
    search_numbers = (By.CLASS_NAME, "REySof")
