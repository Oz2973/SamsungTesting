from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver, product_title):
        self.driver = driver
        self.product_title = product_title
        self.search_icon_element = "nv00-gnb__utility-btn.gnb__search-btn-js"
        self.search_submit_element = "gnb-search__input-btn--search"
        self.search_bar_element = "gnb-search__input"

    def search_function(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.search_icon_element)))
        except TimeoutException:
            raise TimeoutException("Error! Failed to locate the Search icon in time")
        search_icon = self.driver.find_element(By.CLASS_NAME, self.search_icon_element)
        search_submit = self.driver.find_element(By.CLASS_NAME, self.search_submit_element)
        search_icon.click()
        search_bar = self.driver.find_element(By.CLASS_NAME, self.search_bar_element)
        search_bar.send_keys(self.product_title)
        search_submit.click()
