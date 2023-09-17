from unittest import TestCase
from pages.home_screen.google_search import HomePage


class TestGoogleSearch(TestCase):
    def setUp(self) -> None:
        self.page = HomePage()

    def test_search_google(self):
        search_bar = self.page.get_search_bar()
        self.page.enter_text(search_bar, "Nusrat Fateh Ali Khan")
        search_icon = self.page.get_search_icon()
        self.page.click(search_icon)
        numbers = self.page.find_element(self.page.locators.search_numbers)
        self.assertIsNotNone(numbers)

