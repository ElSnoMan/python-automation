from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expect


class HomePage:
    def __init__(self, driver, wait):
        self._driver = driver
        self._wait = wait
        self.map = HomePageMap(driver)

    def goto(self):
        self.map.home_tab.click()
        self.wait_for_page_load()

    def wait_for_page_load(self):
        self._wait.until(expect.visibility_of(self.map.home_tab))


class HomePageMap:
    def __init__(self, driver):
        self._driver = driver

    @property
    def home_tab(self):
        return self._driver.find_element(By.XPATH, "//*[@class='main-nav-menu']/li/a[1]")
