from project import app
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

class AllTests(unittest.TestCase):
    def setUp(self):
        self.options = Options()
        self.options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=self.options)
        self.app = app.test_client()

    def test_form_showing(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        self.assertIn("Python3", driver.title)
        assert "No results found." not in driver.page_source

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    unittest.main()

