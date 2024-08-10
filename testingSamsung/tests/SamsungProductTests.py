import unittest

from testingSamsung.pages.HomePage import HomePage
from testingSamsung.tests.globalSamsung import urlSamsung, product_title
from testingSamsung.tests.samsungSelenium import SamsungSelenium
from testingSamsung.pages.SearchResultsPage import SearchResultsPage


class SamsungProductTests(unittest.TestCase):

    def setUp(self):
        base = SamsungSelenium()
        self.driver = base.selenium_start(urlSamsung)
        self.product_title = product_title
        home_page = HomePage(self.driver, self.product_title)
        home_page.search_function()
        self.search_results = SearchResultsPage(self.driver, self.product_title)
        self.test_product_successful_search()
        self.test_product_name()

    def test_product_successful_search(self):
        self.search_results.test_search_results_bar()

    def test_product_name(self):
        self.search_results.test_product_title()

    def test_product_price(self):
        self.search_results.test_product_price()

    def tearDown(self):
        print("Test tear down")
        self.base = SamsungSelenium()
        self.base.selenium_end(self.driver)

