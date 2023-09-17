from selenium.webdriver.common.by import By


class BaseLocator:
    google_search_bar = (By.CLASS_NAME, "gLFyf")
    google_search_com = (By.CLASS_NAME, "CcAdNb")


class TimeOut:
    TWO_SECONDS = 2
    FIVE_SECONDS = 5
    TEN_SECONDS = 10
    FIFTEEN_SECONDS = 15
    THIRTY_SECONDS = 30
    ONE_MINUTE = 60
