"""Tests for navbar."""
import unittest
from tests.base_test import BaseTest


class TestNavBar(BaseTest):
    """Main test class for testing my navbar."""
    def test_get_home_url(self):
        """Test if the get_home_url function retrieves the correct URL."""
        expected_url = "https://uzuran.pythonanywhere.com/"
        actual_url = self.base_page.get_home_url()
        self.assertEqual(actual_url, expected_url,
                         f"Expected home URL '{expected_url}' but got '{actual_url}'.")

    def test_get_title_text(self):
        """Test if the get_title_text function retrieves the correct text."""
        expected_title = "Černopaščenko"  # Adjust this to the expected text
        actual_text = self.base_page.get_title_text()
        self.assertEqual(actual_text, expected_title, f"Expected logo text '{expected_title}'"
                                                      f" but got '{actual_text}'.")

    def test_get_logo_text(self):
        """Test if the get_logo_text function retrieves the correct text."""
        expected_text = "Černopaščenko"  # Adjust this to the expected text
        actual_text = self.page_navbar.get_logo_text()
        self.assertEqual(actual_text, expected_text, f"Expected logo text '{expected_text}'"
                                                     f" but got '{actual_text}'.")

    def test_get_home_text(self):
        """Test if the get_home_text function retrieves the correct text."""
        expected_text = "Home"
        actual_text = self.page_navbar.get_home_text()
        self.assertEqual(actual_text, expected_text, f"Expected home text '{expected_text}'"
                                                     f" but got '{actual_text}'.")


if __name__ == "__main__":
    unittest.main()
