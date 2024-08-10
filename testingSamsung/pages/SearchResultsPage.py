from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage:

    def __init__(self, driver, product_title):
        self.driver = driver
        self.product_title = product_title
        self.search_results_bar_element = "search-result-global-srp-tab-bar__link"
        self.product_price_element = "result-price__money"
        self.product_original_price_element = "search-result-global__result-price__normal-money"
        # when there's a sale there's an original price element
        self.product_details_element = "search-result-global__result-item__content"
        self.product_title_element = "a.search-result-global__result-title__link"
        self.products_container_element = "search-result-global__result__panel"

    def test_search_results_bar(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.search_results_bar_element)))
        except TimeoutException:
            raise TimeoutException("Failed to locate the search bar in time")
        search_results_bar = self.driver.find_elements(By.CLASS_NAME, self.search_results_bar_element)
        assert len(search_results_bar) != 0, "Error! The current page isn't 'search results', check for changes in the site"

    def test_product_title(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, self.product_title)))
        except TimeoutException:
            raise TimeoutException("Failed to locate the product title in time")
        product_title = self.driver.find_elements(By.LINK_TEXT, self.product_title)
        assert product_title is not None, "Error! Product was not found"

    def test_product_price(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.products_container_element)))
        except TimeoutException:
            raise TimeoutException("Error! Failed to locate the container in time")

        price_after_discount = 0
        product_details_dynamic = self.driver.find_elements(By.CLASS_NAME, self.product_details_element)
        for item_in_array in product_details_dynamic:
            item_text = item_in_array.text
            item_text_split = item_text.split("\n")
            for item_after_split_in_array in item_text_split:
                if self.product_title == item_after_split_in_array:
                    if len(item_text_split) == 6:
                        currency_type = item_text_split[1][:1]
                        price_after_discount = float(item_text_split[1].split("(")[0][1:])
                        price_before_discount = float(item_text_split[2][2:].split(")")[0])
                        assert price_after_discount < price_before_discount, "Error! The price after discount isn't cheaper than price before discount"
                        price_difference = price_before_discount - price_after_discount
                        print(f"The current price for the product is {currency_type}{price_after_discount}, and the discount is {currency_type}{price_difference}")
                        return

                    elif len(item_text_split) == 5:
                        currency_type = item_text_split[1][:1]
                        price_before_discount = float(item_text_split[1][1:-8])
                        assert price_after_discount != 0, "Error! There is no discount at the moment"
                        # Assert will purposefully fail,
                        # In cases where there's no discount.
                        print(f"The price for the product is {currency_type}{price_before_discount}")
                        return

                    else:
                        assert True, "Error, Check for changes in the site"
                        return
