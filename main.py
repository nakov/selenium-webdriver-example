import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_search_in_python_org_positive(self):
        driver = self.driver
        driver.get("https://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_search_in_python_org_negative(self):
        driver = self.driver
        driver.get("https://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("missingkeyword")
        elem.send_keys(Keys.RETURN)
        assert "No results found." in driver.page_source

    def tearDown(self):
        #self.driver.quit()
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)
