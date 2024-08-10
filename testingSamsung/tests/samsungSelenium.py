from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class SamsungSelenium:
    def selenium_start(self, url):
        print("Test start")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    def selenium_end(self, driver):
        driver.close()
        print("Test end")
